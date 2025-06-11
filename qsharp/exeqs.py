import qsharp
from collections import Counter
from math import sqrt
import time
import argparse

# ==== 解析命令行参数 ====
parser = argparse.ArgumentParser(description="Compare Q# circuit outputs via Hellinger distance")
parser.add_argument("--shots", type=int, default=8192, help="Number of measurement shots (default: 8192)")
args = parser.parse_args()

SHOTS = args.shots

qsharp.init(project_root=".")

def collect_distribution(op_name: str, shots: int = 1000) -> (Counter, float):
    counter = Counter()
    start_time = time.time()
    for _ in range(shots):
        result = qsharp.eval(f"{op_name}()")
        bitstring = ''.join(['1' if r == 1 else '0' for r in result])
        counter[bitstring] += 1
    duration = time.time() - start_time
    return counter, duration

def pretty_print(counter: Counter, name: str, duration: float):
    print(f"{name} Distribution (collected in {duration:.2f}s):")
    total = sum(counter.values())
    for outcome, count in sorted(counter.items()):
        percent = (count / total) * 100
        print(f"  {outcome}: {count} ({percent:.2f}%)")
    print()

def hellinger_distance(p: Counter, q: Counter) -> float:
    all_keys = set(p) | set(q)
    p_total = sum(p.values())
    q_total = sum(q.values())
    return sqrt(0.5 * sum(
        (sqrt(p.get(k, 0) / p_total) - sqrt(q.get(k, 0) / q_total)) ** 2
        for k in all_keys
    ))

def compare_distributions_with_hellinger(dist1: Counter, dist2: Counter, name1="A", name2="B", threshold=0.25):
    h = hellinger_distance(dist1, dist2)
    print(f"Hellinger distance between {name1} and {name2}: {h:.4f}")
    if h > threshold:
        print(f"[FAIL] (Hellinger distance {h:.4f} > {threshold})")
    else:
        print(f"[PASS] (Hellinger distance {h:.4f} ≤ {threshold})")
    print()

# ==== 主逻辑 ====

main_dist, main_time = collect_distribution("Main.TestCircuit", shots=SHOTS)
fuzz_dist, fuzz_time = collect_distribution("Main_fuzzing.TestCircuit", shots=SHOTS)

pretty_print(main_dist, "Main", main_time)
pretty_print(fuzz_dist, "Main_fuzzing", fuzz_time)

compare_distributions_with_hellinger(main_dist, fuzz_dist, "Main", "Main_fuzzing")
