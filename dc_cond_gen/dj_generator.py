import random
from math import pi
from qiskit import QuantumCircuit, ClassicalRegister

################################################################################
# 平衡函数 Oracle 构造方法（默认随机选择 dot_product 或 majority）
def generate_balanced_oracle_code(num_qubits, cir_name="qc", qreg_name="dj_qreg", dj_qubit_indices=None, aux_index=None, method=None):
    if dj_qubit_indices is None or aux_index is None:
        raise ValueError("dj_qubit_indices and aux_index must be provided")

    if method is None:
        method = random.choice(["dot_product"])

    lines = [f"# === Oracle 主体部分（平衡函数：{method}） ==="]

    if method == "dot_product":
        active_bits = random.sample(dj_qubit_indices, k=random.randint(1, len(dj_qubit_indices)))
        for idx in active_bits:
            lines.append(f"{cir_name}.cx({qreg_name}[{idx}], {qreg_name}[{aux_index}])  # 平衡函数：x[{idx}] ⊕ ...")
    elif method == "majority":
        subset = random.sample(dj_qubit_indices, k=3)
        lines.append(f"{cir_name}.ccx({qreg_name}[{subset[0]}], {qreg_name}[{subset[1]}], {qreg_name}[{aux_index}])  # 平衡函数（majority 控制）")
        lines.append(f"{cir_name}.cx({qreg_name}[{subset[2]}], {qreg_name}[{aux_index}])")
    else:
        raise ValueError("Unsupported balanced oracle method")

    return lines

################################################################################
# 增强逻辑 Oracle 生成器（严格隔离 DJ 区）
def generate_enhanced_oracle_code(
    num_qubits,
    cir_name="qc",
    qreg_name="dj_qreg",
    dj_qubit_indices=None,
    enhanced_qubit_indices=None,
    aux_index=None,
    num_extra_gates=8
):
    if dj_qubit_indices is None or aux_index is None:
        raise ValueError("dj_qubit_indices and aux_index must be provided")

    # 可用的特殊角度值（float 极值、数学常数等）
    special_angles = [
        0.0,
        3.141592653589793, -3.141592653589793,      # pi, -pi
        1.5707963267948966, -1.5707963267948966,     # pi/2, -pi/2
        1.0, -1.0,
        1.4142135623730951, -1.4142135623730951,     # sqrt(2)
        1.7976931348623157e+308,                    # float max
        -1.7976931348623157e+308,
        2.2250738585072014e-308,                    # float min positive
        -2.2250738585072014e-308
    ]

    def get_special_theta():
        return random.choice(special_angles)

    safe_indices = list(set(range(num_qubits)) - set(dj_qubit_indices) - {aux_index})
    if not safe_indices or len(safe_indices) < 2:
        return ["# ⚠️ 无可用增强 qubit，跳过增强 oracle"]

    lines = ["# === Oracle 增强部分（不影响 DJ 区） ==="]
    for _ in range(num_extra_gates):
        gate = random.choice(["cx", "crx", "crz", "iswap", "rz", "h"])

        if gate == "cx":
            ctrl, tgt = random.sample(safe_indices, 2)
            lines.append(f"{cir_name}.cx({qreg_name}[{ctrl}], {qreg_name}[{tgt}])")
        elif gate == "crx":
            theta = get_special_theta()
            ctrl, tgt = random.sample(safe_indices, 2)
            lines.append(f"{cir_name}.crx({theta}, {qreg_name}[{ctrl}], {qreg_name}[{tgt}])")
        elif gate == "crz":
            theta = get_special_theta()
            ctrl, tgt = random.sample(safe_indices, 2)
            lines.append(f"{cir_name}.crz({theta}, {qreg_name}[{ctrl}], {qreg_name}[{tgt}])")
        elif gate == "iswap":
            q1, q2 = random.sample(safe_indices, 2)
            lines.append(f"{cir_name}.iswap({qreg_name}[{q1}], {qreg_name}[{q2}])")
        elif gate == "rz":
            tgt = random.choice(safe_indices)
            theta = get_special_theta()
            lines.append(f"{cir_name}.rz({theta}, {qreg_name}[{tgt}])")
        elif gate == "h":
            tgt = random.choice(safe_indices)
            lines.append(f"{cir_name}.h({qreg_name}[{tgt}])")

    return lines

################################################################################
# 组合 Oracle

def generate_combined_oracle(num_qubits, cir_name="qc", qreg_name="dj_qreg", dj_qubit_indices=None, aux_index=None, method=None):
    if dj_qubit_indices is None or aux_index is None:
        raise ValueError("dj_qubit_indices and aux_index must be provided")

    oracle = generate_balanced_oracle_code(
        num_qubits=num_qubits,
        cir_name=cir_name,
        qreg_name=qreg_name,
        dj_qubit_indices=dj_qubit_indices,
        aux_index=aux_index,
        method=method
    )

    enhanced_indices = list(set(range(num_qubits)) - set(dj_qubit_indices))
    if enhanced_indices:
        oracle += generate_enhanced_oracle_code(
            num_qubits=num_qubits + 1,
            cir_name=cir_name,
            qreg_name=qreg_name,
            dj_qubit_indices=dj_qubit_indices,
            enhanced_qubit_indices=enhanced_indices,
            aux_index=aux_index
        )
    else:
        oracle.append(f"# ⚠️ 无可用增强目标 qubit（num_qubits={num_qubits}），增强逻辑被跳过")

    return oracle

################################################################################
# 生成 DJ 算法子电路（可复用）
def generate_dj_subcircuit(num_qubits=8, dj_bits=4, method=None):
    aux_index = num_qubits
    total_qubits = num_qubits + 1
    dj_qubit_indices = list(range(dj_bits))

    qreg = QuantumRegister(total_qubits, name="dj_qreg")
    creg = ClassicalRegister(dj_bits, name="dj_creg")
    qc = QuantumCircuit(qreg, creg, name="dj_subcircuit")

    qc.x(qreg[aux_index])  # 将辅助比特初始化为 |1⟩
    qc.h(qreg)  # 所有量子比特 Hadamard

    oracle_lines = generate_combined_oracle(
        num_qubits=num_qubits,
        cir_name="qc",
        qreg_name="qreg",
        dj_qubit_indices=dj_qubit_indices,
        aux_index=aux_index,
        method=method
    )

    for line in oracle_lines:
        if line.startswith("#"):
            continue
        exec(line.replace("qc", "qc").replace("dj_qreg", "qreg"))

    qc.h([qreg[i] for i in dj_qubit_indices])  # 再次 Hadamard
    for i in dj_qubit_indices:
        qc.measure(qreg[i], creg[i])

    return qc, creg

################################################################################
# 生成完整 Python 程序代码
def generate_dj_nonconstant_code(num_qubits=8, dj_bits=4, cir_name="qc", qreg_name="dj_qreg", creg_name="dj_creg"):
    aux_index = num_qubits
    dj_qubit_indices = list(range(dj_bits))

    header = [
        "from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile",
        "from qiskit_aer import Aer",
        "",
        f"{qreg_name} = QuantumRegister({num_qubits + 1})",
        f"{creg_name} = ClassicalRegister({dj_bits})",
        f"{cir_name} = QuantumCircuit({qreg_name}, {creg_name})",
        ""
    ]

    body = [
        f"{cir_name}.x({qreg_name}[{aux_index}])",
        f"{cir_name}.h([{', '.join(f'{qreg_name}[{i}]' for i in range(num_qubits + 1))}])"
    ]

    body += generate_combined_oracle(
        num_qubits=num_qubits,
        cir_name=cir_name,
        qreg_name=qreg_name,
        dj_qubit_indices=dj_qubit_indices,
        aux_index=aux_index
    )

    body.append(f"{cir_name}.h([{', '.join(f'{qreg_name}[{i}]' for i in dj_qubit_indices)}])")
    body += [f"{cir_name}.measure({qreg_name}[{i}], {creg_name}[{i}])" for i in dj_qubit_indices]

    footer = [
        "",
        "# 执行模拟器并获取测量结果",
        "backend = Aer.get_backend('aer_simulator')",
        f"compiled = transpile({cir_name}, backend)",
        f"job = backend.run(compiled, shots=1024)",
        "dj_result = job.result().get_counts()",
        "",
        "# 提取前 dj_bits 位作为 Deutsch-Jozsa 判定依据",
        f"dj_only_result = {{k[:{dj_bits}]: v for k, v in dj_result.items()}}",
        "print('Deutsch-Jozsa 结果 (前 dj_bits 位):', dj_only_result)",
        f"if sorted(dj_only_result.keys()) == ['{'0'*dj_bits}']:",
        "    print('❌ 被识别为恒定函数')",
        "else:",
        "    print('✅ 被识别为非恒定函数')"
    ]

    return "\n".join(header + body + footer)

################################################################################
def write_dj_code_to_file(filename="dj_test.py", num_qubits=8, dj_bits=4):
    code = generate_dj_nonconstant_code(num_qubits, dj_bits)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"✅ 已生成代码文件：{filename}")

if __name__ == "__main__":
    write_dj_code_to_file("dj_test.py", num_qubits=8, dj_bits=4)
