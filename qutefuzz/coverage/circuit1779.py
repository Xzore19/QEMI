from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.cx(qreg_1[0],qreg_2[1])
subcirc0.u(0.691000,-0.681000,-0.278000, qreg_1[0])
subcirc0.ry(-0.241000, qreg_2[0])
subcirc0.u(-0.030000,0.925000,-0.098000, qreg_0[0])
subcirc0.u(0.562000,0.924000,-0.905000, qreg_1[0])
subcirc0.cx(qreg_2[1],qreg_2[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.ry(0.315000, qreg_2[0])
subcirc1.z(qreg_2[0])
subcirc1.cx(qreg_2[1],qreg_0[0])
subcirc1.u(0.795000,-0.768000,0.834000, qreg_2[1])
subcirc1.z(qreg_2[1])
subcirc1.u(0.679000,0.189000,-0.492000, qreg_2[1])
subcirc1 = subcirc1.to_gate().control(1)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.append(subcirc0,[qreg_0[0],2,qreg_0[1],1])
main_circ.append(subcirc1,[qreg_0[0],0,1,qreg_0[1],3])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],2,3])
main_circ.append(subcirc1,[qreg_0[1],2,0,3,qreg_0[0]])
main_circ.z(qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],1,3,2])
main_circ.cx(1,3)
main_circ.cx(qreg_0[0],qreg_0[1])
main_circ.cx(1,3)
main_circ.cx(0,2)
main_circ.cx(qreg_0[1],3)
main_circ.append(subcirc1,[qreg_0[0],1,qreg_0[1],0,2])
main_circ.u(0.085000,param_0,param_2, qreg_0[0])
main_circ.cx(3,qreg_0[0])
bindings = {param_0: 0.976000, param_2: 0.423000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1779")
