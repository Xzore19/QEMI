from code_fuzzer.cirq_gen import CirqGenerator
from tqdm import tqdm
import gc
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Qiskit fuzzing tester")
    parser.add_argument("--qubits", type=int, default=4, help="Number of qubits for each generated circuit")
    args = parser.parse_args()
    for i in tqdm(range(1000), desc="Processing"):
        a = CirqGenerator(args.qubits, 1)
        a.run()

        del a
        gc.collect()