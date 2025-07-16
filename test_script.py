from qiskit import QuantumCircuit, QuantumRegister, AncillaRegister
from qiskit.circuit.library import *
import numpy as np
from qiskit_aer import Aer

def build_circuit():
    q = QuantumRegister(6, 'q')
    qc = QuantumCircuit(q)

    # === 插入你的append代码块 ===
    {INSERT_HERE}

    qc.measure_all()
    return qc

if __name__ == "__main__":
    circuit = build_circuit()
    backend = Aer.get_backend("aer_simulator")
    job = backend.run(circuit)
    result = job.result()
    print(result.get_counts())
