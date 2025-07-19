# QEMI: A Quantum Software Stacks Testing Framework via Equivalence Module Inputs

QEMI is a framework to automatically test the quantum software stacks with Equivalence Modulo Inputs (EMI). 

## ✨ Supported Backends

- **Qiskit**
- **Cirq**
- **Q#**

Each backend has a tailored generator and executor that ensures compatibility with its native compiler and simulator stack.

## 🚀 Quick Start

1. Clone the repository
2. Run the following command: 
```bash
cd QEMI
pip install -r requirements.txt
```
3. For different QSSes: 
### Qiskit
```bash
python main.py --qubits 6
```

### Cirq
```bash
python cirq_main.py
```

### Q#
```bash
cd qsharp
python stress_test.py --qubits 6 --iter 100 --delta 0.1
```
