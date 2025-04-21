import os
from datetime import datetime
from qiskit import transpile
from qiskit_aer import Aer
from qiskit.qasm3 import dumps  # ✅ QASM3 导出支持
from collections import Counter
from gr_generator import generate_grover_subcircuit  # ✅ 你的构建器

def test_generate_grover_subcircuit(num_qubits=4, target_bitstring=None):
    # === 构造输出路径 ===
    ts = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    log_dir = "test_runs"
    os.makedirs(log_dir, exist_ok=True)
    
    json_path = f"{log_dir}/{ts}_grover_{num_qubits}q.json"
    qasm3_path = f"{log_dir}/{ts}_grover_{num_qubits}q.qasm3"

    # === 构建 Grover 电路并保存 JSON ===
    qc, creg, target = generate_grover_subcircuit(
        num_qubits=num_qubits,
        target_bitstring=target_bitstring,
        save_info_to=json_path
    )

    # === 保存 QASM3 ===
    with open(qasm3_path, "w", encoding="utf-8") as f:
        f.write(dumps(qc))
    print(f"📄 已保存 QASM3 文件到: {qasm3_path}")

    # === 显示信息 ===
    print("🎯 目标态应为:", target)
    print("📦 ClassicalRegister 名称:", creg.name)

    print("【原始 Grover 电路】")
    print(qc.draw('text'))

    backend = Aer.get_backend("aer_simulator")
    compiled = transpile(qc, backend, optimization_level=3)

    print("【优化后电路】")
    print(compiled.draw('text'))

    # === 执行最终验证测量 ===
    job = backend.run(compiled, shots=1)
    result = job.result().get_counts()
    measured = list(result.keys())[0]
    print("🔍 实际运行得到的测量结果:", measured)
    print("🎉 是否命中目标态:", measured == target)

if __name__ == "__main__":
    test_generate_grover_subcircuit(num_qubits=5)
