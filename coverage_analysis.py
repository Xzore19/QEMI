from remove_import import remove_import
import subprocess
import sys
from tqdm import tqdm

coverage = [0]
def coverage_analysis(filename):
    remove_import(filename)
    truth_result = subprocess.run([sys.executable, filename], capture_output=True, text=True, timeout=600)
    for line in truth_result.stdout.split("\n"):
        if "TOTAL" in line:
            a,_ = line.split("%")
            coverage.append(eval(a[-3:]))


if __name__ == "__main__":
    for i in tqdm(range(10), desc="Processing"):
        filename = f"code_coverage/origin_{i}.py"
        coverage_analysis(filename)

    print(coverage)