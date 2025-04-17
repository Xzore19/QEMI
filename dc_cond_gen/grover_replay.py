import json
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.circuit.library import MCXGate
from qiskit_aer import Aer
from math import pi, sqrt, floor

def replay_grover_case(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    num_qubits = data["num_qubits"]
    target = data["target_bitstring"]
    target_qiskit_order = target[::-1]  # Reverse again for construction

    # 构造 Grover 电路
    qreg = QuantumRegister(num_qubits)
    creg = ClassicalRegister(num_qubits)
    qc = QuantumCircuit(qreg, creg)

    qc.h(qreg)

    oracle = QuantumCircuit(num_qubits, name="Oracle")
    for i in range(num_qubits):
        if target_qiskit_order[i] == '0':
            oracle.x(i)
    oracle.h(num_qubits - 1)
    oracle.append(MCXGate(num_qubits - 1), qargs=list(range(num_qubits)))
    oracle.h(num_qubits - 1)
    for i in range(num_qubits):
        if target_qiskit_order[i] == '0':
            oracle.x(i)
    oracle_gate = oracle.to_gate(label="Oracle")

    diffuser = QuantumCircuit(num_qubits, name="Diffuser")
    diffuser.h(range(num_qubits))
    diffuser.x(range(num_qubits))
    diffuser.h(num_qubits - 1)
    diffuser.append(MCXGate(num_qubits - 1), qargs=list(range(num_qubits)))
    diffuser.h(num_qubits - 1)
    diffuser.x(range(num_qubits))
    diffuser.h(range(num_qubits))
    diffuser_gate = diffuser.to_gate(label="Diffuser")

    iterations = floor(pi / 4 * sqrt(2 ** num_qubits))
    for _ in range(iterations):
        qc.append(oracle_gate, qargs=qreg)
        qc.append(diffuser_gate, qargs=qreg)

    qc.measure(qreg, creg)

    backend = Aer.get_backend("aer_simulator")
    compiled = transpile(qc, backend)
    job = backend.run(compiled, shots=1)
    result = job.result().get_counts()
    measured = list(result.keys())[0]

    print("🧪 复现实验：", json_path)
    print("🎯 目标态:", target)
    print("📏 实际测量:", measured)
    print("✅ 命中目标:", measured == target)

# if __name__ == "__main__":
