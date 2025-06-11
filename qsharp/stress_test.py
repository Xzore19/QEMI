import subprocess
import traceback
import time

LOG_FILE = "stress_test_log.txt"
ITERATIONS = 1000

def log(message):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(message + "\n")

def is_redundant_output(line: str) -> bool:
    skip_keywords = [
        "Distribution (collected",
        "Chi-square test p-value",
        "[PASS]",
        "[FAIL]",
        ":",  # like 000000000000: 1 (100.00%)
    ]
    return any(
        line.strip().startswith(prefix) or
        (":" in line and line.strip().split(":")[0].strip().isalnum() and "%" in line)
        for prefix in skip_keywords
    )

for i in range(1, ITERATIONS + 1):
    log(f"\n=== Iteration {i} ===")
    try:
        start_time = time.time()

        # Step 1: Generate Q# file
        result_gen = subprocess.run(
            ["python", "base_gen.py"],
            capture_output=True, text=True, timeout=30
        )
        if result_gen.returncode != 0:
            log("[base_gen.py ERROR]")
            log(result_gen.stderr.strip())
            continue
        else:
            log("[base_gen.py SUCCESS]")

        # Step 2: Execute Q# file
        result_exec = subprocess.run(
            ["python", "exeqs.py"],
            capture_output=True, text=True, timeout=30
        )
        if result_exec.returncode != 0:
            log("[exeqs.py ERROR]")
            log(result_exec.stderr.strip())
        else:
            log("[exeqs.py SUCCESS]")
            for line in result_exec.stdout.splitlines():
                if not is_redundant_output(line):
                    log(line.strip())

        elapsed = time.time() - start_time
        log(f"[Time elapsed: {elapsed:.2f} seconds]")

    except Exception:
        log("[EXCEPTION]")
        log(traceback.format_exc())
