from qiskit import transpile
from qiskit_aer import Aer
from gr_generator import generate_grover_subcircuit  # ← 你自己模块路径

def test_generate_grover_subcircuit(num_qubits=4, target_bitstring=None):
    # 获取已构建好的电路（已包含测量），其中电路对应频率最高的输出态
    circuit, creg, target = generate_grover_subcircuit(num_qubits, target_bitstring)

    print("🎯 目标态应为:", target)
    print("📦 返回 ClassicalRegister 名称:", creg.name)

    print("【原始 Grover 电路】")
    print(circuit.draw('text'))

    backend = Aer.get_backend("aer_simulator")
    compiled = transpile(circuit, backend, optimization_level=3)

    print("【优化后电路】")
    print(compiled.draw('text'))

    # ⚠️ 此时只再运行 1 次，不需要 1024 次，因为前面已经执行过多次用于统计
    job = backend.run(compiled, shots=1)
    result = job.result().get_counts()

    measured = list(result.keys())[0]
    print("🔍 实际运行得到的测量结果:", measured)
    print("🎉 是否命中目标态:", measured == target)

if __name__ == "__main__":
    test_generate_grover_subcircuit(num_qubits=5)
