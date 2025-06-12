import subprocess
import traceback
import time
import os
import shutil
from tqdm import tqdm
import argparse
import json
import re
from collections import Counter

parser = argparse.ArgumentParser(description="Quantum circuit fuzz test runner")
parser.add_argument("--samples", type=int, default=1000, help="Number of iterations (default: 1000)")
parser.add_argument("--shots", type=int, default=8192, help="Number of measurement shots per circuit")
args = parser.parse_args()

ITERATIONS = args.samples
EXEQS_SHOTS = args.shots

LOG_FILE = "stress_test_log.txt"
BUGGY_DIR = "buggy_program"
QSHARP_FILES = ["src/Main.qs", "src/Fuzzing_Main.qs"]

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
    print(f"[\u4fdd\u5b58\u51fa\u9519\u7a0b\u5e8f] -> {dir_path}")

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

        result_exec = subprocess.run(
            ["python", "exeqs.py", "--shots", str(EXEQS_SHOTS)], capture_output=True, text=True
        )
        stdout = result_exec.stdout

        if result_exec.returncode != 0:
            log("[exeqs.py ERROR]")
            log(result_exec.stderr.strip())
            save_buggy_program(f"[exeqs.py ERROR]\n{result_exec.stderr.strip()}", qs_contents)
        else:
            log("[exeqs.py SUCCESS]")
            extra_info = ""
            for line in stdout.splitlines():
                if not is_redundant_output(line):
                    log(line.strip())
                if "Distribution (collected" in line or line.strip().startswith("  "):
                    extra_info += line + "\n"

            match = re.search(r"Hellinger distance between .*?: ([0-9.]+)", stdout)
            h = float(match.group(1)) if match else None
            if "[FAIL]" in stdout:
                reason = f"[Hellinger distance FAIL: {h:.4f}]" if h else "[FAIL]"
                save_buggy_program(reason, qs_contents, extra_info)

        elapsed = time.time() - start_time
        log(f"[Time elapsed: {elapsed:.2f} seconds]")

    except Exception:
        err_msg = traceback.format_exc()
        log("[EXCEPTION]")
        log(err_msg)
        save_buggy_program(f"[EXCEPTION]\n{err_msg}", qs_contents)