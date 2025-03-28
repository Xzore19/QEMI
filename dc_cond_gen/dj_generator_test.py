from qiskit import QuantumCircuit, transpile, QuantumRegister, ClassicalRegister
from qiskit_aer import Aer
from dj_generator import generate_dj_subcircuit  # ✅ 你的模块文件名

def test_generate_dj_subcircuit(num_qubits=8, dj_bits=4, method=None):
    sub_circuit, creg = generate_dj_subcircuit(num_qubits=num_qubits, dj_bits=dj_bits, method=method)

    backend = Aer.get_backend("aer_simulator")
    compiled = transpile(sub_circuit, backend)
    job = backend.run(compiled, shots=1024)
    result = job.result().get_counts()

    reduced_result = {k[:dj_bits]: v for k, v in result.items()}
    print(f"Deutsch-Jozsa 测试结果（前 {dj_bits} 位）:", reduced_result)

    if sorted(reduced_result.keys()) == [f"{'0'*dj_bits}"]:
        print("❌ 被识别为恒定函数")
    else:
        print("✅ 被识别为非恒定函数")

if __name__ == "__main__":
    test_generate_dj_subcircuit()

