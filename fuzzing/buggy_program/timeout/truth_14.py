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
np.random.seed(42) 

qreg = QuantumRegister(5) 
creg = ClassicalRegister(5) 
qc = QuantumCircuit(qreg, creg) 

qc.append(RZGate(4.77), [qreg[0]])
qc.append(NLocal(5, reps=1, parameter_prefix='theta_b8f57a'), [qreg[3], qreg[2], qreg[1], qreg[4], qreg[0]])
qc.append(Permutation(3, pattern=[2, 0, 1]), [qreg[4], qreg[3], qreg[1]])
qc.append(C3XGate(), [qreg[2], qreg[0], qreg[3], qreg[1]])
qc.append(HGate(), [qreg[4]])
with qc.for_loop(range(3)) as i:
	with qc.for_loop(range(3)) as i:
		aux_db7c22 = AncillaRegister(5, 'aux_db7c22')
		qc.add_register(aux_db7c22)
		qc.append(DraperQFTAdder(5), [qreg[1], aux_db7c22[3], aux_db7c22[4], qreg[2], qreg[4], qreg[0], aux_db7c22[0], aux_db7c22[1], qreg[3], aux_db7c22[2]])
		qc.append(CUGate(4.26, 3.718, 5.099, 5.234), [qreg[0], qreg[2]])
		aux_fecb00 = AncillaRegister(5, 'aux_fecb00')
		qc.add_register(aux_fecb00)
		qc.append(DraperQFTAdder(5), [qreg[1], qreg[4], aux_fecb00[1], aux_fecb00[2], aux_fecb00[4], aux_fecb00[0], aux_fecb00[3], qreg[3], qreg[2], qreg[0]])
		qc.append(C3XGate(), [qreg[2], qreg[4], qreg[1], qreg[3]])
		qc.iswap(3, 0)
		qc.break_loop()
		qc.append(HGate(), [qreg[1]])
		aux_ec5103 = AncillaRegister(5, 'aux_ec5103')
		qc.add_register(aux_ec5103)
		qc.append(DraperQFTAdder(5), [qreg[2], qreg[1], qreg[4], aux_ec5103[2], aux_ec5103[3], aux_ec5103[1], aux_ec5103[4], qreg[3], aux_ec5103[0], qreg[0]])
		qc.append(CCXGate(), [qreg[0], qreg[4], qreg[1]])
		qc.ch(4, 0)
		qc.append(CXGate(), [qreg[1], qreg[3]])
	
	qc.break_loop()
qc.append(C3XGate(), [qreg[3], qreg[1], qreg[4], qreg[2]])
qc.append(Permutation(4, pattern=[2, 0, 3, 1]), [qreg[2], qreg[0], qreg[4], qreg[1]])
qc.append(AND(2), [qreg[0], qreg[3], qreg[1]])
qc.append(XGate(), [qreg[1]])
qc.append(XGate(), [qreg[2]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager(TemplateOptimization()) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1 ) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=10000) 
result = job.result().get_counts() 
print(result)
