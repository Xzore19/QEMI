# fuzzing/fuzzing_test.py

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile, AncillaRegister
from qiskit_aer import Aer
from qiskit.circuit.library import *
from qiskit.transpiler.passes import Optimize1qGates
from qiskit.transpiler import PassManager
import numpy as np

def build_circuit():
    np.random.seed(42)
    qreg = QuantumRegister(5)
    creg = ClassicalRegister(5)
    qc = QuantumCircuit(qreg, creg)

    qc.append(RealAmplitudes(4, reps=1, parameter_prefix='theta_604211'), [qreg[3], qreg[2], qreg[0], qreg[4]])
    qc.rz(0.39269908169872414, 3)
    qc.append(CUGate(0.265, 1.499, 3.264, 2.942), [qreg[2], qreg[1]])

    aux = AncillaRegister(5, 'aux')
    qc.add_register(aux)
    qc.append(DraperQFTAdder(5), [aux[4], qreg[1], aux[1], aux[2], aux[0], aux[3], qreg[3], qreg[4], qreg[2], qreg[0]])
    qc.append(XGate(), [qreg[4]])

    qr2 = QuantumRegister(2)
    cr2 = ClassicalRegister(2)
    qc.add_register(qr2)
    qc.add_register(cr2)
    qc.h(qr2[0])
    qc.cx(qr2[0], qr2[1])
    qc.measure(qr2[0], cr2[0])
    qc.measure(qr2[1], cr2[1])

    with qc.switch(cr2) as case:
        with case(0b00, 0b11):
            qrx = QuantumRegister(2)
            crx = ClassicalRegister(2)
            qc.add_register(qrx)
            qc.add_register(crx)
            qc.x(qrx[0])
            qc.x(qrx[1])
            qc.measure(qrx[0], crx[0])
            qc.measure(qrx[1], crx[1])
            with qc.if_test((crx, 0b11)) as else_blk:
                qc.tdg(1)
                qc.append(C3XGate(), [qreg[4], qreg[1], qreg[0], qreg[3]])
                qc.ccz(3, 2, 1)
                qc.append(SwapGate(), [qreg[0], qreg[2]])
                qc.append(C3XGate(), [qreg[4], qreg[3], qreg[2], qreg[1]])
            with else_blk:
                qc.swap(3, 2)
                qc.append(CRXGate(0.217), [qreg[4], qreg[0]])
                qc.cp(np.pi/2, 2, 0)
                qc.crx(0.39269908169872414, 1, 0)
                qc.append(NLocal(4, reps=1, parameter_prefix='theta_4a2a3d'), [qreg[4], qreg[2], qreg[0], qreg[1]])
            qc.reset(qrx)

        with case(case.DEFAULT):
            with qc.for_loop(range(3)):
                aux2 = AncillaRegister(3, 'aux2')
                qc.add_register(aux2)
                qc.append(DraperQFTAdder(4), [aux2[1], qreg[4], qreg[0], qreg[2], qreg[1], qreg[3], aux2[0], aux2[2]])
                qc.ry(np.pi/4, 1)
                qc.append(Permutation(3, pattern=[0, 2, 1]), [qreg[4], qreg[3], qreg[2]])
                qc.append(CRXGate(4.793), [qreg[1], qreg[2]])
                qc.iswap(2, 0)
                qc.break_loop()
                qc.cry(0.39269908169872414, 4, 3)
                qc.append(RZGate(4.594), [qreg[2]])
                qc.append(RZGate(3.121), [qreg[0]])
                qc.append(MCXGate(2), [qreg[4], qreg[0], qreg[3]])
                qc.append(StatePreparation(np.random.randn(32) + 1j * np.random.randn(32)), 
                           [qreg[0], qreg[4], qreg[2], qreg[3], qreg[1]])

    qc.reset(qr2)
    qc.append(SwapGate(), [qreg[2], qreg[4]])
    qc.cz(2, 4)
    qc.append(RXGate(5.268), [qreg[0]])
    qc.cx(2, 0)
    qc.append(U3Gate(4.605, 0.437, 0.991), [qreg[4]])
    qc.measure(qreg[0], creg[0])
    qc.measure(qreg[1], creg[1])
    qc.measure(qreg[2], creg[2])
    qc.measure(qreg[3], creg[3])
    qc.measure(qreg[4], creg[4])
    return qc

def run():
    qc = build_circuit()
    qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})
    pm = PassManager(Optimize1qGates())
    qc = pm.run(qc)
    qc = qc.decompose(reps=10)
    backend = Aer.get_backend("aer_simulator")
    job = backend.run(transpile(qc, backend, optimization_level=3, routing_method="default", layout_method="noise_adaptive", approximation_degree=1), shots=1)
    return job.result().get_counts()
