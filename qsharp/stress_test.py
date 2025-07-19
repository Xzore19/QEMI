import subprocess
import traceback
import time
import os
import argparse
import json
import re
from collections import Counter
from tqdm import tqdm

parser = argparse.ArgumentParser(description="Quantum circuit fuzz test runner")
parser.add_argument("--iter", type=int, default=1000, help="Number of iterations (default: 1000)")
parser.add_argument("--delta", type=float, default=0.1, help="Threshold of Hellinger distance")
parser.add_argument("--qubits", type=int, default=8, help="Number of qubits per circuit")
parser.add_argument("--test-mode", action="store_true", help="Enable test mode (force full measurement)")
args = parser.parse_args()

ITERATIONS = args.iter
HELLINGER_THRESHOLD = args.delta
NUM_QUBITS = args.qubits
TEST_MODE = args.test_mode

LOG_FILE = "stress_test_log.txt"
BUGGY_DIR = "buggy_program"
QSHARP_FILES = ["src/Main.qs", "src/Fuzzing_Main.qs"]

from math import sqrt, ceil

def compute_S(delta: float, N: float) -> int:
    val1 = N ** (2/3) / (delta ** (8/3))
    val2 = N ** (3/4) / (delta ** 2)
    return ceil(min(val1, val2))

def hellinger_distance(p: Counter, q: Counter) -> float:
    all_keys = set(p) | set(q)
    p_total = sum(p.values())
    q_total = sum(q.values())
    return sqrt(0.5 * sum(
        (sqrt(p.get(k, 0) / p_total) - sqrt(q.get(k, 0) / q_total)) ** 2
        for k in all_keys
    ))

def log(message):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(message + "\n")

def get_next_buggy_id():
    os.makedirs(BUGGY_DIR, exist_ok=True)
    existing = [
        int(name) for name in os.listdir(BUGGY_DIR)
        if os.path.isdir(os.path.join(BUGGY_DIR, name)) and name.isdigit()
    ]
    return max(existing, default=0) + 1

def get_next_test_id():
    base_dir = "test_record"
    os.makedirs(base_dir, exist_ok=True)
    existing = [
        int(name) for name in os.listdir(base_dir)
        if os.path.isdir(os.path.join(base_dir, name)) and name.isdigit()
    ]
    return max(existing, default=0) + 1

def save_buggy_program(reason: str, qs_contents: dict, extra_info: str = None):
    buggy_id = get_next_buggy_id()
    dir_path = os.path.join(BUGGY_DIR, f"{buggy_id:04d}")
    os.makedirs(dir_path, exist_ok=True)
    print(f"[buggy program] -> {dir_path}")

    for fullpath in QSHARP_FILES:
        fname = os.path.basename(fullpath)
        content = qs_contents.get(fullpath, "// [Missing or empty]")
        with open(os.path.join(dir_path, fname), "w", encoding="utf-8") as f:
            f.write(content)

    with open(os.path.join(dir_path, "error.txt"), "w", encoding="utf-8") as f:
        f.write(reason)
        if extra_info:
            f.write("\n\n=== Distributions ===\n")
            f.write(extra_info)

def is_redundant_output(line: str) -> bool:
    skip_keywords = [
        "Distribution (collected",
        "Chi-square test p-value",
        "[PASS]",
        "[FAIL]",
        ":"
    ]
    return any(
        line.strip().startswith(prefix) or
        (":" in line and line.strip().split(":")[0].strip().isalnum() and "%" in line)
        for prefix in skip_keywords
    )

def save_test_record(qs_contents: dict, early_info: tuple, standard_s: int, max_s: int,
                     final_h: float, h_history: list):
    test_id = get_next_test_id()  
    dir_path = os.path.join("test_record", f"{test_id:04d}")
    os.makedirs(dir_path, exist_ok=True)

    for fullpath in QSHARP_FILES:
        fname = os.path.basename(fullpath)
        content = qs_contents.get(fullpath, "// [Missing or empty]")
        with open(os.path.join(dir_path, fname), "w", encoding="utf-8") as f:
            f.write(content)

    stats = {
        "early_stop_shots": early_info[0] if early_info else None,
        "early_stop_h": round(early_info[1], 6) if early_info else None,
        "standard_S": standard_s,
        "max_shots": max_s,
        "final_h": round(final_h, 6),
        "h_history": h_history
    }
    with open(os.path.join(dir_path, "stats.json"), "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2)

def try_exeqs_until_converge(qs_contents: dict, n_qubits: int, delta: float, test_mode: bool):
    N = 2 ** n_qubits
    N_sqrt = 2 ** (n_qubits / 2)
    h_history = [] 

    initial_shots = compute_S(delta, N_sqrt)
    max_shots = 2 * compute_S(delta, N)

    total_main = Counter()
    total_fuzz = Counter()
    total_shots = 0
    step = initial_shots
    extra_info_lines = []

    confirm_once = False
    early_stop_info = None

    while total_shots + step <= max_shots:
        result_exec = subprocess.run(
            ["python", "exeqs.py", "--shots", str(step)],
            capture_output=True, text=True
        )
        stdout = result_exec.stdout

        if result_exec.returncode != 0:
            log("[exeqs.py ERROR]")
            log(result_exec.stderr.strip())
            save_buggy_program(f"[exeqs.py ERROR]\n{result_exec.stderr.strip()}", qs_contents)
            return None, None, True, None, None, None

        log(f"[exeqs.py SUCCESS @ step={step}]")

        current_main = Counter()
        current_fuzz = Counter()
        current_section = None

        for line in stdout.splitlines():
            line = line.strip()
            if not line:
                continue
            if line.startswith("Main Distribution"):
                current_section = "main"
                extra_info_lines.append(line)
                continue
            elif line.startswith("Main_fuzzing Distribution"):
                current_section = "fuzz"
                extra_info_lines.append(line)
                continue
            elif line.startswith("Hellinger distance"):
                extra_info_lines.append(line)
                continue
            elif re.match(r"^[01]+: \d+ \(\d+\.\d+%\)", line):
                extra_info_lines.append("  " + line)
                bitstring, count = line.split(":")[0], int(line.split(":")[1].split("(")[0].strip())
                if current_section == "main":
                    current_main[bitstring] += count
                elif current_section == "fuzz":
                    current_fuzz[bitstring] += count

        total_main += current_main
        total_fuzz += current_fuzz
        total_shots += step

        h = hellinger_distance(total_main, total_fuzz)
        log(f"[Cumulative Hellinger] shots={total_shots}, h={h:.4f}")
        h_history.append({
            "shots": total_shots,
            "h": round(h, 6)
        })

        if h <= delta:
            if not test_mode:
                if confirm_once:
                    early_stop_info = (total_shots, h)
                    if early_stop_info is None: 
                        log(f"[Confirmed convergence after confirmation round: h={h:.4f} ≤ δ={delta}]")
                    return h, "\n".join(extra_info_lines), False, early_stop_info, total_shots, h, h_history
                else:
                    log(f"[Hellinger below threshold: h={h:.4f} ≤ δ={delta}, waiting for confirmation round]")
                    confirm_once = True
                    continue
            else:
                if not confirm_once:
                    if early_stop_info is None: 
                        log(f"[Test mode: h={h:.4f} ≤ δ={delta}, waiting for confirmation round]")
                    confirm_once = True
                    continue
                else:
                    if early_stop_info is None:  
                        early_stop_info = (total_shots, h)
                        log(f"[Test mode: confirmed h={h:.4f}, continuing to max shots]")
                    confirm_once = False

    reason = f"[Hellinger distance FAIL after {total_shots} shots: {h:.4f}]"
    if not test_mode:
        save_buggy_program(reason, qs_contents, "\n".join(extra_info_lines))
    return h, "\n".join(extra_info_lines), False, early_stop_info, total_shots, h, h_history



for i in tqdm(range(1, ITERATIONS + 1), desc="Stress Test Progress", unit="iter"):
    log(f"\n=== Iteration {i} ===")
    qs_contents = {}

    try:
        start_time = time.time()
        qubit_num = NUM_QUBITS
        result_gen = subprocess.run(
            ["python", "base_gen.py", "--qubit_num", str(qubit_num)],
            capture_output=True,
            text=True
        )
        if result_gen.returncode != 0:
            log("[base_gen.py ERROR]")
            log(result_gen.stderr.strip())
            save_buggy_program(f"[base_gen.py ERROR]\n{result_gen.stderr.strip()}", qs_contents)
            continue
        log("[base_gen.py SUCCESS]")

        for fullpath in QSHARP_FILES:
            if os.path.exists(fullpath):
                try:
                    with open(fullpath, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read().strip()
                        qs_contents[fullpath] = content or "// [Empty file]"
                except Exception as e:
                    qs_contents[fullpath] = f"// [Failed to read: {e}]"
            else:
                qs_contents[fullpath] = "// [Not found]"

        standard_S = compute_S(HELLINGER_THRESHOLD, 2 ** NUM_QUBITS)
        max_S = 2 * compute_S(HELLINGER_THRESHOLD, 2 ** NUM_QUBITS)

        h, extra_info, errored, early_info, final_shots, final_h, h_history = try_exeqs_until_converge(
            qs_contents, n_qubits=NUM_QUBITS, delta=HELLINGER_THRESHOLD, test_mode=TEST_MODE
        )

        if errored:
            continue

        if TEST_MODE:
            save_test_record(
                qs_contents,
                early_info,
                standard_S,
                max_S,
                final_h,
                h_history
            )

        elapsed = time.time() - start_time
        log(f"[Time elapsed: {elapsed:.2f} seconds]")

    except Exception:
        err_msg = traceback.format_exc()
        log("[EXCEPTION]")
        log(err_msg)
        save_buggy_program(f"[EXCEPTION]\n{err_msg}", qs_contents)