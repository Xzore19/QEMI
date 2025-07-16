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
subcirc0.u(0,0,0.874000, qreg_0[0])
subcirc0.u(pi/2,-0.824000,0.953000, qreg_0[0])
subcirc0.u(pi/2,0.910000,-0.800000, qreg_0[3])
subcirc0.cx(qreg_0[1],qreg_0[0])
subcirc0.u(0,0,0.711000, qreg_0[3])
subcirc0.cx(qreg_0[3],qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.cx(qreg_0[0],qreg_2[1])
subcirc1.u(0,0,-0.421000, qreg_2[0])
subcirc1.cx(qreg_0[0],qreg_2[0])
subcirc1.u(pi/2,-0.153000,-0.800000, qreg_0[1])
subcirc1.u(0,0,0.889000, qreg_2[0])
subcirc1.u(0,0,-0.931000, qreg_2[1])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc2.add_register(qreg_2)
# Adding creg resources 
subcirc2.cx(qreg_0[1],qreg_0[0])
subcirc2.cz(qreg_2[1],qreg_2[0])
subcirc2.cz(qreg_0[0],qreg_2[1])
subcirc2.u(pi/2,0.392000,0.512000, qreg_2[0])
subcirc2.u(pi/2,0.829000,0.517000, qreg_2[0])
subcirc2.u(pi/2,-0.139000,-0.772000, qreg_0[1])

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")

main_circ.append(subcirc2,[qreg_0[0],1,2,3])
main_circ.u(param_1,param_0,param_1, 2)
main_circ.u(pi/2,param_1,param_0, 0)
main_circ.append(subcirc2,[2,0,1,3])
main_circ.u(param_1,param_0,param_1, 0)
main_circ.append(subcirc2,[3,0,qreg_0[0],2])
main_circ.u(pi/2,param_0,param_1, 0)
main_circ.cz(0,3)
main_circ.append(subcirc2,[2,3,1,0])
main_circ.cx(qreg_0[0],1)
main_circ.append(subcirc0,[qreg_0[0],0,3,1])
main_circ.append(subcirc2,[1,qreg_0[0],0,3])
main_circ.append(subcirc0,[3,0,qreg_0[0],2])
main_circ.append(subcirc0,[1,2,qreg_0[0],0])
main_circ.u(pi/2,param_1,param_1, 0)
main_circ.u(param_0,0,param_1, 0)
main_circ.u(param_1,param_1,-0.645000, 2)
main_circ.cz(3,1)
bindings = {param_0: 0.311000, param_1: 0.188000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "NormalizeRXAngle")
