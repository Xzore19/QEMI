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
parser.add_argument("--samples", type=int, default=1000, help="Number of iterations (default: 1000)")
parser.add_argument("--shots", type=int, default=8192, help="Number of measurement shots per circuit")
args = parser.parse_args()

ITERATIONS = args.samples
EXEQS_SHOTS = args.shots
MAX_SHOTS = 12800
HELLINGER_THRESHOLD = 0.1

LOG_FILE = "stress_test_log.txt"
BUGGY_DIR = "buggy_program"
QSHARP_FILES = ["src/Main.qs", "src/Fuzzing_Main.qs"]

from math import sqrt

def hellinger_distance(p: Counter, q: Counter) -> float:
    """计算两个概率分布之间的 Hellinger 距离"""
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

def save_buggy_program(reason: str, qs_contents: dict, extra_info: str = None):
    buggy_id = get_next_buggy_id()
    dir_path = os.path.join(BUGGY_DIR, f"{buggy_id:04d}")
    os.makedirs(dir_path, exist_ok=True)
    print(f"[保存出错程序] -> {dir_path}")

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

def try_exeqs_until_converge(qs_contents: dict, initial_shots=8192, max_shots=400, threshold=0.01):
    total_main = Counter()
    total_fuzz = Counter()
    total_shots = 0
    step = initial_shots
    extra_info_lines = []

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
            return None, None, True

        log(f"[exeqs.py SUCCESS @ step={step}]")

        # 提取这次的 Main 和 Main_fuzzing 分布
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

        # 累积统计
        total_main += current_main
        total_fuzz += current_fuzz
        total_shots += step

        # 计算 h
        h = hellinger_distance(total_main, total_fuzz)
        log(f"[Cumulative Hellinger] shots={total_shots}, h={h:.4f}")

        if h <= threshold:
            return h, "\n".join(extra_info_lines), False
        
        log(f"[Hellinger above threshold] h={h:.4f} > {threshold}, total_shots={total_shots}, next_step={step}")
        step *= 2  # 增加下一轮 shots

    # 如果超过 max_shots 仍然没通过
    reason = f"[Hellinger distance FAIL after {total_shots} shots: {h:.4f}]"
    save_buggy_program(reason, qs_contents, "\n".join(extra_info_lines))
    return h, "\n".join(extra_info_lines), False

for i in tqdm(range(1, ITERATIONS + 1), desc="Stress Test Progress", unit="iter"):
    log(f"\n=== Iteration {i} ===")
    qs_contents = {}

    try:
        start_time = time.time()

        result_gen = subprocess.run(
            ["python", "base_gen.py"], capture_output=True, text=True
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

        h, extra_info, errored = try_exeqs_until_converge(
            qs_contents, initial_shots=EXEQS_SHOTS,
            max_shots=MAX_SHOTS, threshold=HELLINGER_THRESHOLD
        )

        if errored:
            continue

        elapsed = time.time() - start_time
        log(f"[Time elapsed: {elapsed:.2f} seconds]")

    except Exception:
        err_msg = traceback.format_exc()
        log("[EXCEPTION]")
        log(err_msg)
        save_buggy_program(f"[EXCEPTION]\n{err_msg}", qs_contents)
