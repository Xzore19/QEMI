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
subcirc0.cx(qreg_0[3],qreg_0[1])
subcirc0.cy(qreg_0[0],qreg_0[3])
subcirc0.cx(qreg_0[1],qreg_0[3])
subcirc0.cy(qreg_0[3],qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.cx(qreg_0[0],qreg_0[3])
subcirc1.u(0.923000,0.787000,-0.651000, qreg_0[0])
subcirc1.cx(qreg_0[3],qreg_0[1])
subcirc1.u(-0.917000,0.157000,0.826000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rx(-0.652000, qreg_0[1])
subcirc2.u(0.774000,-0.877000,-0.239000, qreg_0[1])
subcirc2.u(0.471000,-0.313000,-0.096000, qreg_0[0])
subcirc2.rx(-0.091000, qreg_0[0])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.rx(0.363000, qreg_0[0])
subcirc3.cy(qreg_0[3],qreg_0[1])
subcirc3.cx(qreg_0[2],qreg_0[0])
subcirc3.cy(qreg_0[3],qreg_0[1])

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
param_2 = Parameter("param_2")

main_circ.cx(3,1)
main_circ.cy(qreg_0[0],3)
main_circ.cy(2,0)
main_circ.append(subcirc3,[0,2,qreg_0[0],1])
main_circ.u(param_0,0.787000,-0.898000, 3)
main_circ.cx(0,2)
main_circ.cx(0,3)
main_circ.u(param_0,param_0,0.044000, 2)
main_circ.append(subcirc0,[2,1,3,0])
main_circ.u(-0.201000,param_2,-0.648000, 2)
main_circ.cy(3,2)
main_circ.u(param_0,param_2,-0.845000, 3)
main_circ.cx(2,0)
main_circ.cx(0,2)
main_circ.rx(0.570000, 0)
main_circ.append(subcirc3,[1,2,3,0])
main_circ.rx(param_0, 0)
main_circ.u(param_2,0.905000,param_1, 3)
main_circ.append(subcirc3,[qreg_0[0],0,3,1])
main_circ.append(subcirc3,[qreg_0[0],1,2,0])
main_circ.append(subcirc0,[3,2,1,0])
main_circ.append(subcirc0,[0,qreg_0[0],1,3])
main_circ.cx(2,0)
main_circ.cx(2,1)
main_circ.append(subcirc0,[2,qreg_0[0],0,1])
main_circ.u(param_2,-0.881000,param_0, 2)
main_circ.rx(-0.518000, 2)
main_circ.append(subcirc3,[3,qreg_0[0],0,2])
main_circ.cx(2,1)
main_circ.append(subcirc3,[0,2,3,1])
bindings = {param_0: 0.107000, param_1: -0.785000, param_2: 0.410000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "ResetAfterMeasureSimplification")
