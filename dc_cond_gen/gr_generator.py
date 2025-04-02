import random
from math import pi, sqrt, floor, asin, log, ceil, sin
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.circuit.library import MCXGate
from qiskit_aer import Aer
from collections import Counter


def generate_grover_subcircuit(num_qubits=4, target_bitstring=None):
    if target_bitstring is None:
        target_bitstring = "".join(random.choice(["0", "1"]) for _ in range(num_qubits))
    target_bitstring_reversed = target_bitstring[::-1]  # Qiskit 小端顺序

    # === Step 1: 理论成功率与重复次数计算 ===
    N = 2 ** num_qubits
    r = floor(pi / 4 * sqrt(N))
    theta = asin(1 / sqrt(N))
    p_success = sin((2 * r + 1) * theta) ** 2

    confidence = 0.9995
    if p_success >= 1.0:
        n_repeat = 1
    else:
        n_repeat = ceil(log(1 - confidence) / log(1 - p_success))

    backend = Aer.get_backend("aer_simulator")
    results = []

    for _ in range(n_repeat):
        qreg = QuantumRegister(num_qubits)
        creg = ClassicalRegister(num_qubits)
        qc = QuantumCircuit(qreg, creg)

        # 初始 Hadamard 叠加
        qc.h(qreg)

        # 构建 oracle 子电路
        oracle = QuantumCircuit(num_qubits, name="Oracle")
        for i in range(num_qubits):
            if target_bitstring_reversed[i] == '0':
                oracle.x(i)
        oracle.h(num_qubits - 1)
        oracle.append(MCXGate(num_qubits - 1), qargs=list(range(num_qubits)))
        oracle.h(num_qubits - 1)
        for i in range(num_qubits):
            if target_bitstring_reversed[i] == '0':
                oracle.x(i)
        oracle_gate = oracle.to_gate(label="Oracle")

        # 构建 diffuser 子电路
        diffuser = QuantumCircuit(num_qubits, name="Diffuser")
        diffuser.h(range(num_qubits))
        diffuser.x(range(num_qubits))
        diffuser.h(num_qubits - 1)
        diffuser.append(MCXGate(num_qubits - 1), qargs=list(range(num_qubits)))
        diffuser.h(num_qubits - 1)
        diffuser.x(range(num_qubits))
        diffuser.h(range(num_qubits))
        diffuser_gate = diffuser.to_gate(label="Diffuser")

        # Grover 迭代
        for _ in range(r):
            qc.append(oracle_gate, qargs=qreg)
            qc.append(diffuser_gate, qargs=qreg)

        # 测量
        qc.measure(qreg, creg)

        # 执行
        compiled = transpile(qc, backend)
        job = backend.run(compiled, shots=1)
        result = job.result().get_counts()
        measured = list(result.keys())[0]
        results.append((measured, qc, creg))

    # === Step 2: 统计最频繁的测量结果 ===
    bit_counter = Counter(bitstring for bitstring, _, _ in results)
    most_common_bitstring = bit_counter.most_common(1)[0][0]

    # 返回匹配这个结果的那一个电路 + 寄存器
    for bitstring, qc, creg in results:
        if bitstring == most_common_bitstring:
            return qc, creg, target_bitstring  # 返回人类可读顺序的目标态


################################################################################
# 构造 Oracle 子电路
def create_grover_oracle(num_qubits, target):
    qreg = QuantumRegister(num_qubits)
    oracle = QuantumCircuit(qreg, name="Oracle")

    # 对目标中为 '0' 的 qubit 施加 X 门
    for i in range(num_qubits):
        if target[i] == '0':
            oracle.x(qreg[i])

    # 多控制 Z：H + MCX + H
    oracle.h(qreg[num_qubits - 1])
    oracle.mcx(list(range(num_qubits - 1)), qreg[num_qubits - 1])
    oracle.h(qreg[num_qubits - 1])

    # 恢复 X 门
    for i in range(num_qubits):
        if target[i] == '0':
            oracle.x(qreg[i])

    return oracle.to_gate(label="Oracle")

################################################################################
# 构造 Diffuser 子电路
def create_diffuser(num_qubits):
    qreg = QuantumRegister(num_qubits)
    diffuser = QuantumCircuit(qreg, name="Diffuser")

    diffuser.h(range(num_qubits))
    diffuser.x(range(num_qubits))
    diffuser.h(qreg[num_qubits - 1])
    diffuser.mcx(list(range(num_qubits - 1)), qreg[num_qubits - 1])
    diffuser.h(qreg[num_qubits - 1])
    diffuser.x(range(num_qubits))
    diffuser.h(range(num_qubits))

    return diffuser.to_gate(label="Diffuser")

################################################################################
# 生成 Grover 算法完整代码
def generate_grover_code(num_qubits=4, cir_name="qc", qreg_name="qreg", creg_name="creg"):
    target = "".join(random.choice(["0", "1"]) for _ in range(num_qubits))
    target = target[::-1]  # Qiskit 小端顺序

    # 理论成功率 & 最优迭代次数
    N = 2 ** num_qubits
    r = math.floor(math.pi / 4 * math.sqrt(N))
    theta = math.asin(1 / math.sqrt(N))
    p_success = math.sin((2 * r + 1) * theta) ** 2

    # 计算重复次数以满足置信度 ≥ 99.95%
    confidence = 0.9995
    n_repeat = math.ceil(math.log(1 - confidence) / math.log(1 - p_success))

    # 注释部分
    theory_comment = f"# 理论单次查询成功率（n={num_qubits}, r={r}）: {p_success:.4f}"
    repeat_comment = f"# 为达到 99.95% 置信度，需重复运行 Grover 电路 {n_repeat} 次（每次 shots=1）"

    header = [
        "from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile",
        "from qiskit_aer import Aer",
        "from collections import Counter",
        "",
        f"# Grover 算法 - 量子位数: {num_qubits}",
        f"# Grover 迭代次数（最优）: {r}",
        theory_comment,
        repeat_comment,
        "",
        f"# 目标状态（小端顺序）: '{target}'",
        ""
    ]

    body = []

    body.append("# 构造 Oracle 子电路")
    body.append(f"def create_oracle(qreg):")
    body.append(f"    oracle = QuantumCircuit(qreg, name='Oracle')")
    for i in range(num_qubits):
        if target[i] == '0':
            body.append(f"    oracle.x(qreg[{i}])")
    body.append(f"    oracle.h(qreg[{num_qubits - 1}])")
    body.append(f"    oracle.mcx([{', '.join(f'qreg[{i}]' for i in range(num_qubits - 1))}], qreg[{num_qubits - 1}])")
    body.append(f"    oracle.h(qreg[{num_qubits - 1}])")
    for i in range(num_qubits):
        if target[i] == '0':
            body.append(f"    oracle.x(qreg[{i}])")
    body.append(f"    return oracle.to_gate(label='Oracle')")
    body.append("")

    body.append("# 构造 Diffuser 子电路")
    body.append(f"def create_diffuser(qreg):")
    body.append(f"    diffuser = QuantumCircuit(qreg, name='Diffuser')")
    body.append(f"    diffuser.h(qreg)")
    body.append(f"    diffuser.x(qreg)")
    body.append(f"    diffuser.h(qreg[{num_qubits - 1}])")
    body.append(f"    diffuser.mcx([{', '.join(f'qreg[{i}]' for i in range(num_qubits - 1))}], qreg[{num_qubits - 1}])")
    body.append(f"    diffuser.h(qreg[{num_qubits - 1}])")
    body.append(f"    diffuser.x(qreg)")
    body.append(f"    diffuser.h(qreg)")
    body.append(f"    return diffuser.to_gate(label='Diffuser')")
    body.append("")

    body.append("# 模拟执行")
    body.append("backend = Aer.get_backend('aer_simulator')")
    body.append("oracle_gate = create_oracle(QuantumRegister({}))".format(num_qubits))
    body.append("diffuser_gate = create_diffuser(QuantumRegister({}))".format(num_qubits))
    body.append("results = []")
    body.append(f"for _ in range({n_repeat}):")
    body.append(f"    qreg = QuantumRegister({num_qubits})")
    body.append(f"    creg = ClassicalRegister({num_qubits})")
    body.append(f"    qc = QuantumCircuit(qreg, creg)")
    body.append(f"    qc.h(qreg)")
    body.append(f"    for _ in range({r}):")
    body.append(f"        qc.append(oracle_gate, qargs=qreg)")
    body.append(f"        qc.append(diffuser_gate, qargs=qreg)")
    body.append(f"    qc.measure(qreg, creg)")
    body.append(f"    compiled = transpile(qc, backend)")
    body.append(f"    job = backend.run(compiled, shots=1)")
    body.append(f"    result = job.result().get_counts()")
    body.append(f"    results.append(list(result.keys())[0])")
    body.append("")

    body.append("# 统计出现最多的测量结果")
    body.append("freq = Counter(results)")
    body.append("most_common = freq.most_common(1)[0]")
    body.append(f"human_target = '{target[::-1]}'")
    body.append("print('测量结果统计:', freq)")
    body.append("print(f'出现次数最多的测量结果: {most_common[0]}，共出现 {most_common[1]} 次')")
    body.append("print(f'目标状态: {human_target}')")
    body.append("print(f'是否命中目标: {most_common[0] == human_target}')")

    return "\n".join(header + body)


################################################################################
def write_grover_code_to_file(filename="grover_test.py", num_qubits=4):
    code = generate_grover_code(num_qubits=num_qubits)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"✅ 已生成子电路优化版本代码文件：{filename}")

if __name__ == "__main__":
    write_grover_code_to_file("grover_test.py", num_qubits=6)
