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
subcirc0.rx(-0.027000, qreg_0[1])
subcirc0.rx(0.685000, qreg_0[2])
subcirc0.u(pi/2,0.541000,0.866000, qreg_0[3])
subcirc0.cx(qreg_0[1],qreg_0[2])
subcirc0.cx(qreg_0[1],qreg_0[0])
subcirc0.rx(0.266000, qreg_0[3])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(pi/2,0.914000,0.306000, qreg_0[1])
subcirc1.u(pi/2,0.178000,-0.541000, qreg_0[1])
subcirc1.cz(qreg_0[1],qreg_0[0])
subcirc1.u(pi/2,0.683000,0.232000, qreg_2[0])
subcirc1.cx(qreg_2[0],qreg_0[0])
subcirc1.rx(-0.295000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.cz(qreg_2[1],qreg_2[0])
subcirc2.u(pi/2,0.729000,-0.719000, qreg_0[0])
subcirc2.u(pi/2,-0.861000,0.041000, qreg_2[1])
subcirc2.cx(qreg_2[1],qreg_2[0])
subcirc2.cz(qreg_2[1],qreg_2[0])
subcirc2.u(pi/2,0.867000,-0.411000, qreg_0[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc3.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc3.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.cz(qreg_0[0],qreg_1[0])
subcirc3.u(pi/2,-0.712000,-0.582000, qreg_0[0])
subcirc3.cz(qreg_0[0],qreg_1[0])
subcirc3.cx(qreg_0[0],qreg_1[0])
subcirc3.cz(qreg_3[0],qreg_1[1])
subcirc3.cx(qreg_1[1],qreg_1[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc4.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.cz(qreg_0[0],qreg_1[0])
subcirc4.cx(qreg_1[1],qreg_1[0])
subcirc4.u(pi/2,0.287000,0.551000, qreg_0[0])
subcirc4.cx(qreg_0[0],qreg_1[0])
subcirc4.cx(qreg_0[0],qreg_3[0])
subcirc4.cz(qreg_1[1],qreg_0[0])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.u(param_0,-0.329000,-0.623000, qreg_3[0])
main_circ.cx(qreg_0[1],0)
main_circ.append(subcirc4,[1,qreg_2[0],0,qreg_0[0]])
main_circ.rx(param_2, qreg_3[0])
main_circ.append(subcirc4,[qreg_3[0],qreg_0[1],0,qreg_0[0]])
main_circ.cz(qreg_2[0],qreg_0[0])
main_circ.append(subcirc3,[qreg_0[1],1,qreg_0[0],0])
main_circ.rx(-0.985000, qreg_2[0])
main_circ.append(subcirc2,[0,qreg_2[0],qreg_0[1],1])
main_circ.u(pi/2,-0.482000,-0.133000, qreg_3[0])
main_circ.cz(qreg_0[0],0)
main_circ.cx(0,1)
main_circ.cz(0,qreg_3[0])
main_circ.rx(param_0, qreg_0[0])
main_circ.cx(qreg_3[0],qreg_2[0])
main_circ.u(param_0,0.182000,param_0, qreg_3[0])
main_circ.cx(qreg_3[0],qreg_2[0])
main_circ.cx(qreg_0[0],1)
main_circ.rx(0.701000, 0)
main_circ.cz(qreg_3[0],1)
main_circ.cz(1,qreg_0[0])
bindings = {param_0: 0.015000, param_2: 0.686000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "425")
