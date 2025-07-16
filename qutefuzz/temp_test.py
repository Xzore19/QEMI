import subprocess
import sys
from tqdm import tqdm
def run(filename):
    truth_result = subprocess.run([sys.executable, filename], capture_output=True, text=True)
    return truth_result.stdout

def check_wrong(strings):
    if "np.float64(0.0" in strings or "KS value: 0.0" in strings:
        return True
    return False

if __name__ == "__main__":
    index = []
    new_wrong = []
    with open("qiskit_result/need_check.txt", "r") as file:
        for line in file:
            line = line.replace("\n","")
            index.append(line)
    for i in tqdm(index, desc="Processing"):
        filename = "qiskit_result/quantum_circuits/circuit"+i+".py"
        strings = run(filename)
        if check_wrong(strings):
            new_wrong.append(i)

    with open("new_check.txt", "w") as file:
        for i in new_wrong:
            file.write(str(i)+"\n")