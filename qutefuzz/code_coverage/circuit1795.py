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
subcirc0.u(-0.302000,-0.838000,0.681000, qreg_0[0])
subcirc0.u(pi/2,0.115000,0.374000, qreg_0[1])
subcirc0.cx(qreg_0[3],qreg_0[0])
subcirc0.u(-0.246000,0.030000,-0.472000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(pi/2,0.094000,-0.699000, qreg_0[0])
subcirc1.u(pi/2,0.677000,0.964000, qreg_0[0])
subcirc1.cx(qreg_0[1],qreg_0[2])
subcirc1.cx(qreg_0[2],qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.u(0.307000,-0.391000,0.927000, qreg_0[1])
subcirc2.u(pi/2,-0.811000,0.437000, qreg_0[3])
subcirc2.u(pi/2,-0.345000,-0.428000, qreg_0[2])
subcirc2.x(qreg_0[3])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc3.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.cx(qreg_1[0],qreg_0[0])
subcirc3.x(qreg_1[0])
subcirc3.x(qreg_1[1])
subcirc3.x(qreg_1[0])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.u(pi/2,param_2,-0.773000, 1)
main_circ.append(subcirc1,[qreg_1[1],1,qreg_0[0],qreg_1[0]])
main_circ.append(subcirc0,[qreg_0[0],qreg_1[1],1,qreg_1[0]])
main_circ.x(0)
main_circ.u(pi/2,param_1,-0.850000, qreg_1[2])
main_circ.append(subcirc0,[0,1,qreg_1[1],qreg_0[0]])
main_circ.x(qreg_0[0])
main_circ.u(param_3,param_2,-0.190000, qreg_1[1])
main_circ.u(param_3,-0.092000,-0.159000, 0)
main_circ.cx(0,qreg_1[1])
main_circ.u(param_2,param_2,param_0, 0)
main_circ.u(param_2,-0.959000,0.696000, 0)
main_circ.append(subcirc0,[1,0,qreg_1[1],qreg_1[0]])
main_circ.u(param_2,0.792000,param_2, qreg_1[1])
main_circ.u(param_0,0.695000,-0.794000, qreg_1[2])
main_circ.append(subcirc3,[qreg_0[0],qreg_1[0],qreg_1[1],qreg_1[2]])
main_circ.cx(qreg_0[0],qreg_1[0])
main_circ.x(0)
main_circ.x(qreg_1[2])
main_circ.append(subcirc2,[1,0,qreg_1[0],qreg_1[2],qreg_0[0],qreg_1[1]])
main_circ.u(param_3,param_1,param_1, qreg_1[0])
main_circ.cx(0,qreg_1[1])
main_circ.cx(qreg_1[0],qreg_1[1])
main_circ.cx(1,0)
main_circ.cx(0,qreg_0[0])
main_circ.cx(qreg_1[2],qreg_1[0])
main_circ.cx(qreg_1[2],qreg_0[0])
main_circ.cx(1,qreg_1[0])
main_circ.cx(qreg_0[0],qreg_1[1])
main_circ.append(subcirc0,[qreg_1[0],qreg_0[0],0,1])
main_circ.append(subcirc0,[qreg_1[1],0,qreg_1[2],qreg_0[0]])
bindings = {param_0: 0.622000, param_1: 0.936000, param_2: -0.756000, param_3: -0.960000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1795")
