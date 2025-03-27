import random

def generate_nonconstant_oracle_code(num_qubits, cir_name="qc", qreg_name="qreg"):
    aux = num_qubits
    num_ctrls = random.randint(1, num_qubits)
    ctrl_qubits = random.sample(range(num_qubits), num_ctrls)
    lines = []
    for ctrl in ctrl_qubits:
        lines.append(f"{cir_name}.cx({qreg_name}[{ctrl}], {qreg_name}[{aux}])  # 非恒定函数：控制比特 {ctrl}")
    return lines


def generate_dj_alg_code(num_qubits=4, cir_name="qc", qreg_name="qreg", creg_name="creg"):
    aux = num_qubits
    lines = [
        f"{cir_name}.x({qreg_name}[{aux}])  # 将辅助比特初始化为 |1⟩",
        f"{cir_name}.h({qreg_name})  # 所有量子比特 Hadamard",
    ]

    lines += generate_nonconstant_oracle_code(num_qubits, cir_name, qreg_name)

    lines.append(
        f"{cir_name}.h([{', '.join(f'{qreg_name}[{i}]' for i in range(num_qubits))}])  # 输入比特再次 Hadamard"
    )

    for i in range(num_qubits):
        lines.append(f"{cir_name}.measure({qreg_name}[{i}], {creg_name}[{i}])")

    return lines


def generate_dj_nonconstant_code(num_qubits=4, cir_name="qc", qreg_name="qreg", creg_name="creg"):
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
        "print('Deutsch-Jozsa 测量结果:', dj_result)",
        f"if list(dj_result.keys()) == ['{'0'*num_qubits}']:",
        "    print('❌ 错误：被识别为恒定函数')",
        "else:",
        "    print('✅ 正确：该函数是非恒定函数')"
    ]

    return "\n".join(header + body + footer)


def write_dj_code_to_file(filename="dj_test.py", num_qubits=4):
    code = generate_dj_nonconstant_code(num_qubits)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"✅ 已生成代码文件：{filename}")


if __name__ == "__main__":
    write_dj_code_to_file("dj_test.py", num_qubits=4)
