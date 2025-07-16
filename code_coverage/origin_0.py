
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile, AncillaRegister
from qiskit_aer import Aer
from qiskit.providers.fake_provider import GenericBackendV2
from qiskit.providers.fake_provider import GenericBackendV2
from qiskit.circuit import Parameter, ParameterVector
from qiskit.circuit.library import XGate
from qiskit.transpiler.passes import *
from qiskit.circuit.library import *
from qiskit.transpiler import PassManager, generate_preset_pass_manager
from math import pi
import numpy as np


def main():
    np.random.seed(42) 
    
    qreg = QuantumRegister(5) 
    creg = ClassicalRegister(5) 
    qc = QuantumCircuit(qreg, creg) 
    
    qc.append(NLocal(3, reps=1, parameter_prefix='theta_4dc143'), [qreg[2], qreg[4], qreg[3]])
    qc.append(EfficientSU2(3, reps=1, parameter_prefix='theta_08c1ed'), [qreg[4], qreg[1], qreg[0]])
    qc.append(CCXGate(), [qreg[1], qreg[3], qreg[4]])
    qc.append(Isometry(np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]), 0, 0), [qreg[1], qreg[3]])
    pass
    qc.append(StatePreparation([(0.7918334666492596+0.1458264819328434j), (0.39501428215518997-0.4423777968600206j)]), [qreg[1]])
    qc.append(C3XGate(), [qreg[4], qreg[1], qreg[2], qreg[0]])
    qc.append(CUGate(2.067, 5.84, 1.659, 1.083), [qreg[3], qreg[1]])
    qc.append(MCPhaseGate(1.0, num_ctrl_qubits=1), [qreg[4], qreg[3]])
    qc.measure(qreg[0], creg[0]) 
    qc.measure(qreg[1], creg[1]) 
    qc.measure(qreg[2], creg[2]) 
    qc.measure(qreg[3], creg[3]) 
    qc.measure(qreg[4], creg[4]) 
    
    qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})
    
    
    simulator = Aer.get_backend("aer_simulator") 
    
    p = PassManager([ElidePermutations(),RemoveResetInZeroState(),RemoveIdentityEquivalent()]) 
    qc = p.run(qc) 
    
    compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 
    
    qc = qc.decompose(reps=10)
    
    job = simulator.run(compiled_circuit, shots=400) 
    result = job.result().get_counts() 
    print(result)


if __name__ == "__main__":
    from coverage import Coverage

    cov = Coverage(
        source=["qiskit"],
        branch=False,
        data_suffix=True
    )
    cov.start()

    main()

    cov.stop()
    cov.save()
    cov.combine()
    cov.report()
