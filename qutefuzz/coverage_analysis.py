from remove_import import remove_import
import subprocess
import sys
from tqdm import tqdm

coverage = [0]
def coverage_analysis(filename, savefile):
    remove_import(filename, savefile)
    truth_result = subprocess.run([sys.executable, savefile], capture_output=True, text=True, timeout=600)
    for line in truth_result.stdout.split("\n"):
        if "TOTAL" in line:
            a,_ = line.split("%")
            coverage.append(eval(a[-3:]))


if __name__ == "__main__":
    for i in tqdm(range(100), desc="Processing"):
        filename = f"code_coverage/circuit{i+1}.py"
        savefile = f"coverage/circuit{i+1}.py"
        coverage_analysis(savefile, savefile)

    print(coverage)