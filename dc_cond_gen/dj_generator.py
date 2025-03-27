import random

def generate_nonconstant_oracle_code(num_qubits, cir_name="qc"):
    """
    生成非恒定函数的 Deutsch-Jozsa Oracle 代码（字符串列表）
    输出格式为多行字符串，例如：
        qc.cx(0, 4)
        qc.cx(2, 4)
    """
    aux = num_qubits
    code_lines = []

    num_ctrls = random.randint(1, num_qubits)
    ctrl_qubits = random.sample(range(num_qubits), num_ctrls)
    for ctrl in ctrl_qubits:
        code_lines.append(f"{cir_name}.cx({ctrl}, {aux})  # 非恒定函数：f(x) XOR 控制比特 {ctrl}")

    return code_lines


def generate_dj_nonconstant_code(num_qubits=4, circuit_name="qc"):
    """
    生成完整的 Deutsch-Jozsa 算法（非恒定函数版本）Python 源码（字符串形式）
    """
    aux = num_qubits
    header = [
        "from qiskit import QuantumCircuit, transpile",
        "from qiskit_aer import Aer",
        "",
        f"{circuit_name} = QuantumCircuit({num_qubits+1}, {num_qubits})  # {num_qubits} 输入比特 + 1 辅助比特",
        f"{circuit_name}.x({aux})  # 将辅助比特初始化为 |1⟩",
        f"{circuit_name}.h(range({num_qubits+1}))  # 所有比特做 Hadamard"
    ]

    # 插入 Oracle（调用独立函数）
    oracle_code = generate_nonconstant_oracle_code(num_qubits, cir_name=circuit_name)

    # 下面这一块不用管，走的一个标准的执行代码的流程而已
    tail = [
        f"{circuit_name}.h(range({num_qubits}))  # 再次 Hadamard（输入比特）",
        f"{circuit_name}.measure(range({num_qubits}), range({num_qubits}))",
        "",
        "# 编译并运行",
        "backend = Aer.get_backend('aer_simulator')",
        f"compiled = transpile({circuit_name}, backend)",
        f"job = backend.run(compiled, shots=1024)",
        "result = job.result().get_counts()",
        "print('Deutsch-Jozsa 测量结果:', result)",
        "",
        "# 判定是否为非恒定函数",
        f"if list(result.keys()) == ['{'0'*num_qubits}']:",
        "    print('❌ 错误：被识别为恒定函数')",
        "else:",
        "    print('✅ 正确：该函数是非恒定函数')"
    ]

    code = "\n".join(header + [""] + oracle_code + [""] + tail)
    return code


if __name__ == "__main__":
    filename = "dj_test.py"
    code = generate_dj_nonconstant_code(num_qubits=4)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)

    print(f"✅ 已生成非恒定 Deutsch-Jozsa 算法脚本：{filename}")
