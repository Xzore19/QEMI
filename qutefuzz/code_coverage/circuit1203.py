from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc0.add_register(qreg_0)
# Adding creg resources 
subcirc0.cz(qreg_0[3],qreg_0[1])
subcirc0.s(qreg_0[0])
subcirc0.s(qreg_0[1])
subcirc0.cx(qreg_0[3],qreg_0[0])
subcirc0.cz(qreg_0[2],qreg_0[1])
subcirc0 = subcirc0.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.append(subcirc0,[2,qreg_0[0],1,0,3])
main_circ.s(2)
main_circ.cz(3,1)
main_circ.cx(0,1)
main_circ.x(3)
main_circ.cx(2,1)
main_circ.cz(1,0)
main_circ.x(3)
main_circ.s(1)
main_circ.s(qreg_0[0])
main_circ.x(qreg_0[0])
main_circ.s(0)
main_circ.x(0)
main_circ.append(subcirc0,[0,1,qreg_0[0],2,3])
main_circ.cz(qreg_0[0],1)
main_circ.cz(2,1)
main_circ.cz(1,qreg_0[0])
main_circ.append(subcirc0,[3,1,2,qreg_0[0],0])
main_circ.cz(0,qreg_0[0])
main_circ.append(subcirc0,[2,qreg_0[0],1,3,0])
main_circ.append(subcirc0,[qreg_0[0],0,1,2,3])
main_circ.append(subcirc0,[3,1,0,2,qreg_0[0]])
main_circ.cx(2,3)
main_circ.cz(2,1)
main_circ.s(0)
main_circ.cz(qreg_0[0],1)
main_circ.cz(3,qreg_0[0])
main_circ.cz(2,qreg_0[0])
bindings = {}
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1203")
