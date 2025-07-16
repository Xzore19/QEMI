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
subcirc0.u(pi/2,-0.292000,-0.174000, qreg_0[1])
subcirc0.rx(0.660000, qreg_0[2])
subcirc0.rz(-0.845000, qreg_0[2])
subcirc0.cz(qreg_0[2],qreg_0[3])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rx(0.938000, qreg_0[3])
subcirc1.u(pi/2,0.546000,-0.969000, qreg_0[3])
subcirc1.u(pi/2,-0.974000,0.201000, qreg_0[3])
subcirc1.rx(0.043000, qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.rx(0.458000, qreg_0[2])
subcirc2.cz(qreg_0[2],qreg_0[1])
subcirc2.u(pi/2,-0.287000,-0.395000, qreg_0[3])
subcirc2.rz(0.576000, qreg_0[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.rz(0.845000, qreg_0[0])
subcirc3.rz(0.376000, qreg_0[0])
subcirc3.rz(-0.633000, qreg_0[1])
subcirc3.rz(0.993000, qreg_0[1])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.cz(qreg_0[3],qreg_0[0])
subcirc4.u(pi/2,0.211000,-0.913000, qreg_0[2])
subcirc4.rx(0.787000, qreg_0[3])
subcirc4.rz(-0.212000, qreg_0[1])

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

main_circ.append(subcirc1,[0,qreg_0[0],3,qreg_0[1]])
main_circ.append(subcirc1,[3,qreg_0[1],qreg_0[0],1])
main_circ.append(subcirc0,[1,2,0,3,qreg_0[0]])
main_circ.append(subcirc1,[qreg_0[0],2,0,1])
main_circ.rz(0.542000, 0)
main_circ.append(subcirc4,[qreg_0[1],1,2,3])
main_circ.append(subcirc4,[3,qreg_0[0],1,qreg_0[1]])
main_circ.u(param_1,0.067000,param_1, qreg_0[1])
main_circ.append(subcirc2,[0,2,qreg_0[1],1])
main_circ.u(pi/2,param_3,-0.757000, qreg_0[1])
main_circ.append(subcirc0,[2,3,1,qreg_0[0],0])
main_circ.cz(0,2)
main_circ.cz(2,1)
main_circ.cz(1,qreg_0[1])
main_circ.cz(2,0)
main_circ.cz(0,qreg_0[0])
main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.cz(3,qreg_0[0])
main_circ.cz(1,0)
main_circ.cz(qreg_0[0],0)
main_circ.append(subcirc1,[2,1,3,qreg_0[1]])
main_circ.cz(0,qreg_0[1])
bindings = {param_1: 0.065000, param_3: 0.993000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveResetInZeroState")
