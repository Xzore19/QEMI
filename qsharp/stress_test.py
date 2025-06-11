import subprocess
import traceback
import time
import os
import shutil
from tqdm import tqdm
import argparse

# ==== 参数解析 ====
parser = argparse.ArgumentParser(description="Quantum circuit fuzz test runner")
parser.add_argument("--samples", type=int, default=1000, help="Number of iterations (default: 1000)")
parser.add_argument("--shots", type=int, default=8192, help="Number of measurement shots per circuit")
args = parser.parse_args()

ITERATIONS = args.samples
EXEQS_SHOTS = args.shots

LOG_FILE = "stress_test_log.txt"
# ITERATIONS = 1000
BUGGY_DIR = "buggy_program"

# Q# 文件的真实路径（位于 src/ 下）
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

def save_buggy_program(reason: str, qs_contents: dict):
    buggy_id = get_next_buggy_id()
    dir_path = os.path.join(BUGGY_DIR, f"{buggy_id:04d}")
    os.makedirs(dir_path, exist_ok=True)

    print(f"[保存出错程序] -> {dir_path}")

    # 保存所有 Q# 文件内容（只保留文件名）
    for fullpath in QSHARP_FILES:
        fname = os.path.basename(fullpath)
        content = qs_contents.get(fullpath, "// [Missing or empty]")
        with open(os.path.join(dir_path, fname), "w", encoding="utf-8") as f:
            f.write(content)

    # 保存错误信息
    with open(os.path.join(dir_path, "error.txt"), "w", encoding="utf-8") as f:
        f.write(reason)

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

# 主循环 + tqdm 进度条
for i in tqdm(range(1, ITERATIONS + 1), desc="Stress Test Progress", unit="iter"):
    log(f"\n=== Iteration {i} ===")
    qs_contents = {}

    try:
        start_time = time.time()

        # Step 1: 运行 base_gen.py
        result_gen = subprocess.run(
            ["python", "base_gen.py"],
            capture_output=True, text=True
        )
        if result_gen.returncode != 0:
            log("[base_gen.py ERROR]")
            log(result_gen.stderr.strip())
            save_buggy_program(f"[base_gen.py ERROR]\n{result_gen.stderr.strip()}", qs_contents)
            continue
        log("[base_gen.py SUCCESS]")

        # Step 2: 缓存 src/ 下的 Q# 文件内容
        for fullpath in QSHARP_FILES:
            if os.path.exists(fullpath):
                try:
                    with open(fullpath, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read().strip()
                        if content:
                            qs_contents[fullpath] = content
                        else:
                            qs_contents[fullpath] = "// [Empty file]"
                except Exception as e:
                    qs_contents[fullpath] = f"// [Failed to read: {e}]"
            else:
                qs_contents[fullpath] = "// [Not found]"

        # Step 3: 运行 exeqs.py
        result_exec = subprocess.run(
            ["python", "exeqs.py", "--shots", str(EXEQS_SHOTS)],
            capture_output=True, text=True
        )
        if result_exec.returncode != 0:
            log("[exeqs.py ERROR]")
            log(result_exec.stderr.strip())
            save_buggy_program(f"[exeqs.py ERROR]\n{result_exec.stderr.strip()}", qs_contents)
        else:
            log("[exeqs.py SUCCESS]")
            hellinger_value = None

            for line in result_exec.stdout.splitlines():
                if not is_redundant_output(line):
                    log(line.strip())

                if "Hellinger distance between" in line:
                    try:
                        # 示例: Hellinger distance between Main and Main_fuzzing: 0.2875
                        parts = line.strip().split(":")
                        if len(parts) == 2:
                            hellinger_value = float(parts[1].strip())
                    except Exception:
                        hellinger_value = None  # 忽略提取失败

                if "[FAIL]" in line:
                    reason = f"[Hellinger distance FAIL: {hellinger_value:.4f}]\n{line.strip()}" if hellinger_value is not None else line.strip()
                    save_buggy_program(reason, qs_contents)

        elapsed = time.time() - start_time
        log(f"[Time elapsed: {elapsed:.2f} seconds]")

    except Exception:
        err_msg = traceback.format_exc()
        log("[EXCEPTION]")
        log(err_msg)
        save_buggy_program(f"[EXCEPTION]\n{err_msg}", qs_contents)
