from qiskit import QuantumCircuit, transpile, QuantumRegister, ClassicalRegister
from qiskit_aer import Aer
from dj_generator import generate_dj_subcircuit  # ✅ 你的模块文件名

def test_generate_dj_subcircuit(num_qubits=8, dj_bits=4, method=None):
    # 获取子电路（仅这一行保持不变）
    sub_circuit, creg = generate_dj_subcircuit(num_qubits=num_qubits, dj_bits=dj_bits, method=method)
    
    # 显示原始电路
    print("【原始电路】")
    print(sub_circuit.draw('text'))
    
    backend = Aer.get_backend("aer_simulator")
    
    # 对电路进行 O3 级别优化
    compiled = transpile(sub_circuit, backend, optimization_level=3)
    
    # 显示优化后的电路
    print("【优化后的电路】")
    print(compiled.draw('text'))
    
    # 执行模拟器并获取测量结果
    job = backend.run(compiled, shots=1024)
    result = job.result().get_counts()
    
    # 提取前 dj_bits 位作为 Deutsch-Jozsa 判定依据
    reduced_result = {k[:dj_bits]: v for k, v in result.items()}
    print(f"Deutsch-Jozsa 测试结果（前 {dj_bits} 位）:", reduced_result)
    
    # 如果检测到存在任意全零的字符串，就判定为错误
    if any(key == '0'*dj_bits for key in reduced_result.keys()):
        print("❌ 出现全零字符串，错误")
    else:
        print("✅ 未出现全零字符串")
    
if __name__ == "__main__":
    test_generate_dj_subcircuit()
