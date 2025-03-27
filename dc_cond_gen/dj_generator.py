import random
from math import pi

################################################################################
# 这里是oracle的生成代码
def generate_nonconstant_oracle_code(num_qubits, cir_name="qc", qreg_name="dj_qreg"):
    aux = num_qubits - 1  # 默认最后一位作为辅助位
    num_ctrls = random.randint(1, num_qubits - 1)
    ctrl_qubits = random.sample(range(num_qubits - 1), num_ctrls)
    lines = []
    for ctrl in ctrl_qubits:
        lines.append(f"{cir_name}.cx({qreg_name}[{ctrl}], {qreg_name}[{aux}])  # 非恒定函数：控制比特 {ctrl}")
    return lines
################################################################################

# 增强逻辑 Oracle 生成器

def generate_enhanced_oracle_code(
    num_qubits,
    cir_name="qc",
    qreg_name="dj_qreg",
    dj_qubit_indices=None,
    enhanced_qubit_indices=None,
    num_extra_gates=6
):
    if dj_qubit_indices is None:
        dj_qubit_indices = list(range(4))
    if enhanced_qubit_indices is None:
        enhanced_qubit_indices = list(range(4, num_qubits))

    available_controls = list(range(num_qubits))
    target_qubits = enhanced_qubit_indices

    gate_templates = []

    for _ in range(num_extra_gates):
        gate_type = random.choice(["cx", "ccx", "crx", "crz", "rz", "iswap", "h"])
        if gate_type == "cx":
            pair = random.sample(range(num_qubits), 2)
            gate_templates.append(f"{cir_name}.cx({qreg_name}[{pair[0]}], {qreg_name}[{pair[1]}])")
        elif gate_type == "ccx":
            triplet = random.sample(range(num_qubits), 3)
            gate_templates.append(f"{cir_name}.ccx({qreg_name}[{triplet[0]}], {qreg_name}[{triplet[1]}], {qreg_name}[{triplet[2]}])")
        elif gate_type == "crx":
            ctrl, tgt = random.sample(range(num_qubits), 2)
            theta = round(random.uniform(0.1, pi), 4)
            gate_templates.append(f"{cir_name}.crx({theta}, {qreg_name}[{ctrl}], {qreg_name}[{tgt}])")
        elif gate_type == "crz":
            ctrl, tgt = random.sample(range(num_qubits), 2)
            theta = round(random.uniform(0.1, pi), 4)
            gate_templates.append(f"{cir_name}.crz({theta}, {qreg_name}[{ctrl}], {qreg_name}[{tgt}])")
        elif gate_type == "rz":
            tgt = random.choice(target_qubits)
            theta = round(random.uniform(0.1, pi), 4)
            gate_templates.append(f"{cir_name}.rz({theta}, {qreg_name}[{tgt}])")
        elif gate_type == "iswap":
            q1, q2 = random.sample(target_qubits, 2)
            gate_templates.append(f"{cir_name}.iswap({qreg_name}[{q1}], {qreg_name}[{q2}])")
        elif gate_type == "h":
            tgt = random.choice(target_qubits)
            gate_templates.append(f"{cir_name}.h({qreg_name}[{tgt}])")

    return gate_templates

# 用于构建整合后的 oracle

def generate_combined_oracle(num_qubits, cir_name="qc", qreg_name="dj_qreg"):
    dj_indices = list(range(min(4, num_qubits - 1)))  # 防止越界
    enhanced_indices = list(set(range(num_qubits)) - set(dj_indices) - {num_qubits - 1})  # 保留一个辅助位

    oracle = generate_nonconstant_oracle_code(num_qubits, cir_name, qreg_name)

    if enhanced_indices:
        oracle += generate_enhanced_oracle_code(
            num_qubits=num_qubits,
            cir_name=cir_name,
            qreg_name=qreg_name,
            dj_qubit_indices=dj_indices,
            enhanced_qubit_indices=enhanced_indices,
            num_extra_gates=8
        )
    else:
        oracle.append(f"# ⚠️ 无可用增强目标 qubit（num_qubits={num_qubits}），增强逻辑被跳过")

    return oracle


################################################################################
# 生成+测量的dj算法的代码生成都在这里，把dj_creg丢进去condition就可以控制了
# 这里生成的是非恒定函数的代码，所以condition设置为not 0000才能变成dead code
def generate_dj_alg_code(num_qubits=4, cir_name="qc", qreg_name="dj_qreg", creg_name="dj_creg"):
    aux = num_qubits
    lines = [
        f"{cir_name}.x({qreg_name}[{aux}])  # 将辅助比特初始化为 |1⟩",
        f"{cir_name}.h({qreg_name})  # 所有量子比特 Hadamard",
    ]

    lines += generate_combined_oracle(num_qubits, cir_name, qreg_name)

    lines.append(
        f"{cir_name}.h([{', '.join(f'{qreg_name}[{i}]' for i in range(num_qubits))}])  # 输入比特再次 Hadamard"
    )

    for i in range(num_qubits):
        lines.append(f"{cir_name}.measure({qreg_name}[{i}], {creg_name}[{i}])")

    return lines
################################################################################

def generate_dj_nonconstant_code(num_qubits=4, cir_name="qc", qreg_name="dj_qreg", creg_name="dj_creg"):
    header = [
        "from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile",
        "from qiskit_aer import Aer",
        "",
        f"{qreg_name} = QuantumRegister({num_qubits + 1})  # {num_qubits} 输入 + 1 辅助",
        f"{creg_name} = ClassicalRegister({num_qubits})",
        f"{cir_name} = QuantumCircuit({qreg_name}, {creg_name})",
        ""
    ]

    body = generate_dj_alg_code(num_qubits, cir_name, qreg_name, creg_name)

    footer = [
        "",
        "# 执行模拟器并获取测量结果",
        "backend = Aer.get_backend('aer_simulator')",
        f"compiled = transpile({cir_name}, backend)",
        f"job = backend.run(compiled, shots=1024)",
        "dj_result = job.result().get_counts()",
        "",
        "# 提取前 4 位作为 Deutsch-Jozsa 判定依据",
        "dj_only_result = {k[:4]: v for k, v in dj_result.items()}",
        "print('Deutsch-Jozsa 结果 (前4位):', dj_only_result)",
        f"if list(dj_only_result.keys()) == ['{'0'*4}']:",
        "    print('❌ 被识别为恒定函数')",
        "else:",
        "    print('✅ 被识别为非恒定函数')"
    ]

    return "\n".join(header + body + footer)


def write_dj_code_to_file(filename="dj_test.py", num_qubits=4):
    code = generate_dj_nonconstant_code(num_qubits)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"✅ 已生成代码文件：{filename}")


if __name__ == "__main__":
    write_dj_code_to_file("dj_test.py", num_qubits=8)
