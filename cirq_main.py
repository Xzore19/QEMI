from code_fuzzer.cirq_gen import CirqGenerator
from tqdm import tqdm
import gc

if __name__ == "__main__":
    for i in tqdm(range(10000), desc="Processing"):
        a = CirqGenerator(5, 1)
        a.run()

        del a
        gc.collect()