# QEMI: A Quantum Software Stacks Testing Framework via Equivalence Modulo Inputs

QEMI is a framework to automatically test the quantum software stacks (QSSes) with Equivalence Modulo Inputs (EMI). 

## ✨ Supported Backends

- **Qiskit**
- **Cirq**
- **Q#**

Each backend has a tailored generator and executor that ensures compatibility with its native compiler and simulator stack.

## 🚀 Quick Start

1. Clone the repository
2. Run the following command
```bash
cd EMI
pip install -r requirements.txt
```
3. For different QSSes, run the following command
### Qiskit
```bash
python main.py --qubits 6 --iter 100
```

### Cirq
```bash
python cirq_main.py --qubits 6 --iter 100
```

### Q#
```bash
cd qsharp
python stress_test.py --qubits 6 --iter 100
```
