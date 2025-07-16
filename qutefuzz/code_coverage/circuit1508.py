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
subcirc0.u(0.574000,0.813000,-0.897000, qreg_0[2])
subcirc0.cz(qreg_0[2],qreg_0[1])
subcirc0.u(0.345000,-0.828000,-0.308000, qreg_0[3])
subcirc0.rz(-0.844000, qreg_0[1])
subcirc0.rz(0.494000, qreg_0[2])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cz(qreg_0[3],qreg_0[0])
subcirc1.u(-0.923000,-0.655000,0.798000, qreg_0[2])
subcirc1.cx(qreg_0[1],qreg_0[2])
subcirc1.rz(0.001000, qreg_0[3])
subcirc1.cx(qreg_0[2],qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.u(param_1,0.714000,param_1, qreg_2[0])
main_circ.u(0.831000,-0.756000,-0.434000, qreg_3[0])
main_circ.u(param_0,0.763000,0.203000, 0)
main_circ.cx(qreg_1[0],0)
main_circ.append(subcirc0,[0,qreg_0[0],qreg_3[0],qreg_1[0],qreg_2[0],1])
main_circ.rz(param_1, qreg_2[0])
main_circ.cz(qreg_1[0],1)
main_circ.append(subcirc1,[1,qreg_2[0],qreg_3[0],qreg_1[0],0,qreg_0[0]])
main_circ.cz(qreg_1[0],qreg_3[0])
main_circ.cz(qreg_2[0],qreg_0[0])
main_circ.rz(0.830000, qreg_3[0])
main_circ.append(subcirc1,[qreg_3[0],1,0,qreg_2[0],qreg_1[0],qreg_0[0]])
main_circ.cx(qreg_1[0],qreg_2[0])
main_circ.rz(param_0, qreg_0[0])
main_circ.cz(qreg_0[0],qreg_1[0])
main_circ.cx(1,qreg_2[0])
main_circ.cz(qreg_0[0],qreg_2[0])
main_circ.append(subcirc1,[qreg_3[0],qreg_1[0],qreg_0[0],qreg_2[0],1,0])
main_circ.cz(qreg_3[0],0)
main_circ.append(subcirc1,[1,qreg_1[0],0,qreg_3[0],qreg_0[0],qreg_2[0]])
main_circ.u(param_1,0.080000,-0.518000, qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],0,qreg_2[0],1,qreg_1[0],qreg_3[0]])
main_circ.u(param_0,param_1,param_0, 1)
main_circ.cx(0,qreg_2[0])
main_circ.cz(qreg_0[0],qreg_3[0])
main_circ.cz(qreg_0[0],1)
main_circ.cx(qreg_3[0],qreg_1[0])
main_circ.rz(param_0, qreg_2[0])
main_circ.u(param_0,param_1,-0.406000, qreg_2[0])
main_circ.cx(0,qreg_1[0])
bindings = {param_0: 0.434000, param_1: -0.810000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1508")
