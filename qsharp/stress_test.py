import subprocess
import traceback
import time

LOG_FILE = "stress_test_log.txt"
ITERATIONS = 1000

def log(message):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(message + "\n")

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
            log(result_gen.stderr)
            continue  # Skip exeqs if generation fails
        else:
            log("[base_gen.py SUCCESS]")

        # Step 2: Execute Q# file
        result_exec = subprocess.run(
            ["python", "exeqs.py"],
            capture_output=True, text=True, timeout=30
        )
        if result_exec.returncode != 0:
            log("[exeqs.py ERROR]")
            log(result_exec.stderr)
        else:
            log("[exeqs.py SUCCESS]")

        elapsed = time.time() - start_time
        log(f"[Time elapsed: {elapsed:.2f} seconds]")

    except Exception as e:
        log("[EXCEPTION]")
        log(traceback.format_exc())
