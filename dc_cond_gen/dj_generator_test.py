from qiskit import QuantumCircuit, transpile, QuantumRegister, ClassicalRegister
from qiskit_aer import Aer
from qiskit.qasm3 import dumps  # ✅ 导入 QASM3 导出工具
from dj_generator import generate_dj_subcircuit
from datetime import datetime
import os

def test_generate_dj_subcircuit(num_qubits=8, dj_bits=4, method=None):
    # 获取子电路（包含 oracle 和测量）
    sub_circuit, creg = generate_dj_subcircuit(num_qubits=num_qubits, dj_bits=dj_bits, method=method)

    # 构造保存路径
    ts = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    log_dir = "test_runs"
    os.makedirs(log_dir, exist_ok=True)
    qasm3_path = f"{log_dir}/{ts}_dj_{num_qubits}q_{dj_bits}bits.qasm3"

    # 保存为 QASM3 文件
    with open(qasm3_path, "w", encoding="utf-8") as f:
        f.write(dumps(sub_circuit))
    print(f"📄 已保存 QASM3 文件到: {qasm3_path}")

    print("【原始 Deutsch-Jozsa 电路】")
    print(sub_circuit.draw('text'))

    backend = Aer.get_backend("aer_simulator")
    compiled = transpile(sub_circuit, backend, optimization_level=3)

    print("【优化后的电路】")
    print(compiled.draw('text'))

    # 执行模拟器并获取测量结果
    job = backend.run(compiled, shots=1024)
    result = job.result().get_counts()

    # 提取前 dj_bits 位作为 Deutsch-Jozsa 判定依据
    reduced_result = {k[:dj_bits]: v for k, v in result.items()}
    print(f"Deutsch-Jozsa 测试结果（前 {dj_bits} 位）:", reduced_result)

    # 如果检测到存在任意全零的字符串，就判定为错误
    if any(key == '0' * dj_bits for key in reduced_result.keys()):
        print("❌ 出现全零字符串，错误")
    else:
        print("✅ 未出现全零字符串")

if __name__ == "__main__":
    test_generate_dj_subcircuit()
