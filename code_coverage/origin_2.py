
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
    
    qc.append(TwoLocal(5, reps=1, parameter_prefix='theta_39349d'), [qreg[4], qreg[1], qreg[3], qreg[2], qreg[0]])
    qc.append(Permutation(4, pattern=[3, 1, 2, 0]), [qreg[0], qreg[1], qreg[4], qreg[3]])
    qc.append(HGate(), [qreg[3]])
    qc.append(SwapGate(), [qreg[1], qreg[0]])
    with qc.for_loop(range(3)) as i_3edeca:
    	
    	qr_9c7a30 = QuantumRegister(2)
    	cr_9c7a30 = ClassicalRegister(2)
    	qc.add_register(qr_9c7a30)
    	qc.add_register(cr_9c7a30)
    	qc.x(qr_9c7a30[0])
    	qc.x(qr_9c7a30[1])
    	qc.measure(qr_9c7a30[0], cr_9c7a30[0]) 
    	qc.measure(qr_9c7a30[1], cr_9c7a30[1]) 
    	with qc.while_loop((cr_9c7a30, 0b10)): 
    		qc.append(MCXGate(4), [qreg[3], qreg[0], qreg[1], qreg[2], qreg[4]])
    		qc.append(SwapGate(), [qreg[3], qreg[4]])
    		qc.append(CUGate(4.332, 5.097, 0.39, 2.113), [qreg[4], qreg[0]])
    		qc.append(C3XGate(), [qreg[3], qreg[1], qreg[2], qreg[0]])
    		qc.measure(qr_9c7a30[0], cr_9c7a30[0]) 
    		qc.measure(qr_9c7a30[1], cr_9c7a30[1]) 
    	qc.reset(qr_9c7a30)
    	
    	qc.continue_loop()
    qc.append(EfficientSU2(2, reps=1, parameter_prefix='theta_2c51fa'), [qreg[3], qreg[4]])
    qc.append(RZGate(5.378), [qreg[3]])
    qc.append(ZZFeatureMap(4, reps=1, parameter_prefix='x_f8d2b7'), [qreg[4], qreg[3], qreg[0], qreg[1]])
    qc.append(Diagonal(np.array([np.complex128(-0.948912436648045+0.3155395182456072j), np.complex128(-0.46661613346678277+0.8844599391654263j), np.complex128(0.9871504995741751-0.15979327642443666j), np.complex128(0.5135574848820985-0.858055190370394j), np.complex128(-0.8379073113278976-0.5458125480632097j), np.complex128(-0.7228275167307873-0.6910284951120348j), np.complex128(-0.13016579929282868+0.9914922413687659j), np.complex128(0.9205790897465541-0.3905561925272801j)])), [qreg[1], qreg[3], qreg[2]])
    qc.measure(qreg[0], creg[0]) 
    qc.measure(qreg[1], creg[1]) 
    qc.measure(qreg[2], creg[2]) 
    qc.measure(qreg[3], creg[3]) 
    qc.measure(qreg[4], creg[4]) 
    
    qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})
    
    
    simulator = Aer.get_backend("aer_simulator") 
    
    p = PassManager([RemoveIdentityEquivalent(),TemplateOptimization(),OptimizeAnnotated()]) 
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
