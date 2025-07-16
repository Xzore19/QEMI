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

qc.append(C3XGate(), [qreg[1], qreg[2], qreg[3], qreg[0]])
qc.append(CRXGate(0.032), [qreg[1], qreg[2]])
qc.append(U3Gate(1.129, 3.178, 0.208), [qreg[1]])
qc.append(Initialize([(-0.27732816637372915-0.219704221949974j), (0.16972771372545165+0.16643193076701127j), (0.16360071777160864+0.23926624384252596j), (-0.26940876062536095-0.30270259330207844j), (0.0416900435504711-0.02063998799112922j), (-0.07308613217199113+0.06670238922117709j), (0.2488738709878186+0.24902584735132705j), (0.04266814812727697-0.14196807160055874j), (-0.2025279682867027+0.060840854950754905j), (-0.1999673555424297-0.11573386973667987j), (-0.05052358830262615+0.2210034427477724j), (0.004900429234277345-0.22210661225238476j), (0.30823327294411695+0.03548970976360757j), (0.0015379795214753922+0.02493700536203646j), (-0.11260788930578947+0.18310730850848517j), (-0.1613006542044894-0.2103258371723729j)]), [qreg[0], qreg[4], qreg[1], qreg[2]])
with qc.for_loop(range(3)) as i_0db392:
	qc.append(CXGate(), [qreg[2], qreg[4]])
	qc.append(CUGate(1.011, 0.315, 0.816, 1.843), [qreg[3], qreg[4]])
	qc.append(U3Gate(3.305, 5.32, 0.682), [qreg[2]])
	qc.append(MCPhaseGate(1.0, num_ctrl_qubits=4), [qreg[2], qreg[1], qreg[0], qreg[4], qreg[3]])
	qc.break_loop()
	qc.append(RXGate(1.106), [qreg[0]])
	qc.append(ZFeatureMap(5, reps=1, parameter_prefix='x_6aaff8'), [qreg[4], qreg[0], qreg[1], qreg[2], qreg[3]])
	qc.append(RZGate(0.538), [qreg[0]])
	qc.append(RXGate(3.709), [qreg[4]])
qc.append(RZGate(1.752), [qreg[0]])
qc.append(CCXGate(), [qreg[0], qreg[2], qreg[1]])
qc.append(SwapGate(), [qreg[2], qreg[4]])
qc.append(XGate(), [qreg[4]])
qc.measure(qreg[0], creg[0]) 
qc.measure(qreg[1], creg[1]) 
qc.measure(qreg[2], creg[2]) 
qc.measure(qreg[3], creg[3]) 
qc.measure(qreg[4], creg[4]) 

qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})


simulator = Aer.get_backend("aer_simulator") 

p = PassManager([RemoveFinalReset(),ResetAfterMeasureSimplification(),OptimizeSwapBeforeMeasure()]) 
qc = p.run(qc) 

compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 

qc = qc.decompose(reps=10)

job = simulator.run(compiled_circuit, shots=400) 
result = job.result().get_counts() 
print(result)
