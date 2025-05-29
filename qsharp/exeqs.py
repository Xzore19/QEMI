import qsharp
from collections import Counter
from scipy.stats import chi2_contingency
import time

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

def perform_chi_square_test(dist1: Counter, dist2: Counter, name1="A", name2="B"):
    all_keys = sorted(set(dist1) | set(dist2))
    obs = [
        [dist1.get(k, 0) for k in all_keys],
        [dist2.get(k, 0) for k in all_keys]
    ]
    chi2, p, _, _ = chi2_contingency(obs)
    print(f"Chi-square test p-value: {p:.4f}")
    if p < 0.05:
        print(f"❌ 分布之间存在统计显著差异 (p < 0.05)")
    else:
        print(f"✅ 无统计显著差异，分布一致 (p >= 0.05)")
    print()

# 参数
SHOTS = 1

# 收集主程序分布及耗时
main_dist, main_time = collect_distribution("Main.TestCircuit", shots=SHOTS)
fuzz_dist, fuzz_time = collect_distribution("Main_fuzzing.TestCircuit", shots=SHOTS)

# 打印分布与时间
pretty_print(main_dist, "Main", main_time)
pretty_print(fuzz_dist, "Main_fuzzing", fuzz_time)

# 执行卡方分析
perform_chi_square_test(main_dist, fuzz_dist)
