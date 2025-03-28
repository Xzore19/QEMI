import random
from math import pi

################################################################################
# 这里是oracle的生成代码
def generate_nonconstant_oracle_code(num_qubits, cir_name="qc", qreg_name="dj_qreg", dj_qubit_indices=None, aux_index=None):
    if dj_qubit_indices is None or aux_index is None:
        raise ValueError("dj_qubit_indices and aux_index must be provided")

    num_ctrls = random.randint(1, len(dj_qubit_indices))
    ctrl_qubits = random.sample(dj_qubit_indices, num_ctrls)
    lines = ["# === Oracle 主体部分 ==="]
    for ctrl in ctrl_qubits:
        lines.append(f"{cir_name}.cx({qreg_name}[{ctrl}], {qreg_name}[{aux_index}])  # 非恒定函数：控制比特 {ctrl}")
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

    # 只允许非 DJ 区参与增强逻辑（控制和目标）
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
            theta = round(random.uniform(0.1, pi), 4)
            ctrl, tgt = random.sample(safe_indices, 2)
            lines.append(f"{cir_name}.crx({theta}, {qreg_name}[{ctrl}], {qreg_name}[{tgt}])")
        elif gate == "crz":
            theta = round(random.uniform(0.1, pi), 4)
            ctrl, tgt = random.sample(safe_indices, 2)
            lines.append(f"{cir_name}.crz({theta}, {qreg_name}[{ctrl}], {qreg_name}[{tgt}])")
        elif gate == "iswap":
            q1, q2 = random.sample(safe_indices, 2)
            lines.append(f"{cir_name}.iswap({qreg_name}[{q1}], {qreg_name}[{q2}])")
        elif gate == "rz":
            tgt = random.choice(safe_indices)
            theta = round(random.uniform(0.1, pi), 4)
            lines.append(f"{cir_name}.rz({theta}, {qreg_name}[{tgt}])")
        elif gate == "h":
            tgt = random.choice(safe_indices)
            lines.append(f"{cir_name}.h({qreg_name}[{tgt}])")

    return lines

# 用于构建整合后的 oracle

def generate_combined_oracle(num_qubits, cir_name="qc", qreg_name="dj_qreg", dj_qubit_indices=None, aux_index=None):
    if dj_qubit_indices is None or aux_index is None:
        raise ValueError("dj_qubit_indices and aux_index must be provided")

    enhanced_indices = list(set(range(num_qubits)) - set(dj_qubit_indices))

    oracle = generate_nonconstant_oracle_code(
        num_qubits=num_qubits,
        cir_name=cir_name,
        qreg_name=qreg_name,
        dj_qubit_indices=dj_qubit_indices,
        aux_index=aux_index
    )

    if enhanced_indices:
        oracle += generate_enhanced_oracle_code(
            num_qubits=num_qubits + 1,
            cir_name=cir_name,
            qreg_name=qreg_name,
            dj_qubit_indices=dj_qubit_indices,
            enhanced_qubit_indices=enhanced_indices,
            aux_index=aux_index,
            num_extra_gates=8
        )
    else:
        oracle.append(f"# ⚠️ 无可用增强目标 qubit（num_qubits={num_qubits}），增强逻辑被跳过")

    return oracle

################################################################################
# 生成+测量的dj算法的代码生成都在这里，把dj_creg丢进去condition就可以控制了
def generate_dj_alg_code(num_qubits=8, dj_bits=4, cir_name="qc", qreg_name="dj_qreg", creg_name="dj_creg"):
    aux_index = num_qubits
    dj_qubit_indices = list(range(dj_bits))

    lines = [
        f"{cir_name}.x({qreg_name}[{aux_index}])  # 将辅助比特初始化为 |1⟩",
        f"{cir_name}.h([{', '.join(f'{qreg_name}[{i}]' for i in range(num_qubits + 1))}])  # 所有量子比特 Hadamard",
    ]

    lines += generate_combined_oracle(
        num_qubits=num_qubits,
        cir_name=cir_name,
        qreg_name=qreg_name,
        dj_qubit_indices=dj_qubit_indices,
        aux_index=aux_index
    )

    lines.append(
        f"{cir_name}.h([{', '.join(f'{qreg_name}[{i}]' for i in dj_qubit_indices)}])  # 输入比特再次 Hadamard"
    )

    for i in dj_qubit_indices:
        lines.append(f"{cir_name}.measure({qreg_name}[{i}], {creg_name}[{i}])")

    return lines

################################################################################
# 输出完整的可执行 Python 程序代码
def generate_dj_nonconstant_code(num_qubits=8, dj_bits=4, cir_name="qc", qreg_name="dj_qreg", creg_name="dj_creg"):
    header = [
        "from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile",
        "from qiskit_aer import Aer",
        "",
        f"{qreg_name} = QuantumRegister({num_qubits + 1})  # {num_qubits} 输入 + 1 辅助",
        f"{creg_name} = ClassicalRegister({dj_bits})",
        f"{cir_name} = QuantumCircuit({qreg_name}, {creg_name})",
        ""
    ]

    body = generate_dj_alg_code(num_qubits, dj_bits, cir_name, qreg_name, creg_name)

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


def write_dj_code_to_file(filename="dj_test.py", num_qubits=8, dj_bits=4):
    code = generate_dj_nonconstant_code(num_qubits, dj_bits)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"✅ 已生成代码文件：{filename}")

# 要总共几个qubit，dj算法几个qubit（到时候生成的dj_creg会用于分支判断上）
if __name__ == "__main__":
    write_dj_code_to_file("dj_test.py", num_qubits=8, dj_bits=2)
