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
subcirc0.y(qreg_0[3])
subcirc0.u(0,0,-0.476000, qreg_0[0])
subcirc0.y(qreg_0[0])
subcirc0.u(0,0,0.360000, qreg_0[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.s(qreg_0[1])
subcirc1.ry(0.339000, qreg_0[0])
subcirc1.u(0,0,-0.304000, qreg_0[3])
subcirc1.u(0,0,-0.298000, qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.ry(-0.512000, qreg_1[1])
subcirc2.u(0,0,-0.724000, qreg_3[0])
subcirc2.ry(-0.623000, qreg_3[0])
subcirc2.u(0,0,0.215000, qreg_1[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.y(qreg_0[1])
subcirc3.s(qreg_0[1])
subcirc3.y(qreg_0[3])
subcirc3.ry(0.227000, qreg_0[2])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc4.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.ry(0.380000, qreg_3[0])
subcirc4.ry(-0.280000, qreg_1[1])
subcirc4.s(qreg_1[1])
subcirc4.y(qreg_1[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.y(3)
main_circ.append(subcirc2,[2,qreg_0[0],1,3])
main_circ.ry(param_1, 1)
main_circ.append(subcirc2,[2,1,qreg_0[0],qreg_0[1]])
main_circ.u(param_1,param_0,param_2, qreg_0[1])
main_circ.append(subcirc0,[1,0,3,qreg_0[1],qreg_0[0],2])
main_circ.append(subcirc4,[qreg_0[0],qreg_0[1],3,1])
main_circ.append(subcirc0,[3,qreg_0[0],qreg_0[1],2,0,1])
main_circ.append(subcirc4,[qreg_0[0],3,qreg_0[1],0])
main_circ.ry(param_0, 2)
main_circ.append(subcirc2,[3,1,qreg_0[0],2])
main_circ.s(qreg_0[0])
main_circ.append(subcirc4,[qreg_0[0],3,0,1])
main_circ.append(subcirc1,[2,qreg_0[0],1,3])
main_circ.ry(param_1, 3)
main_circ.y(qreg_0[0])
main_circ.s(qreg_0[0])
bindings = {param_0: 0.836000, param_1: 0.201000, param_2: -0.402000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "41")
