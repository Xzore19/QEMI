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
subcirc0.cz(qreg_0[1],qreg_0[0])
subcirc0.cz(qreg_0[3],qreg_0[1])
subcirc0.rz(0.564000, qreg_0[1])
subcirc0.rz(0.549000, qreg_0[1])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.s(qreg_0[0])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[3],1,0])
main_circ.s(1)
main_circ.cz(1,0)
main_circ.cz(qreg_0[3],qreg_0[2])
main_circ.rz(0.734000, qreg_0[3])
main_circ.append(subcirc0,[qreg_0[2],qreg_0[3],1,qreg_0[0]])
main_circ.append(subcirc0,[0,qreg_0[2],qreg_0[0],qreg_0[1]])
main_circ.s(qreg_0[1])
main_circ.rz(param_0, qreg_0[0])
main_circ.cz(qreg_0[1],qreg_0[3])
main_circ.s(qreg_0[2])
main_circ.rz(param_0, qreg_0[1])
main_circ.rz(-0.416000, 0)
main_circ.s(qreg_0[2])
main_circ.s(qreg_0[1])
main_circ.rz(param_0, 0)
main_circ.u(0,param_0,0.954000, qreg_0[0])
main_circ.append(subcirc0,[1,qreg_0[0],qreg_0[2],0])
main_circ.u(param_0,param_0,param_0, 0)
main_circ.s(1)
main_circ.cz(qreg_0[2],1)
main_circ.cz(0,1)
main_circ.append(subcirc0,[qreg_0[2],qreg_0[0],0,qreg_0[3]])
main_circ.cz(0,qreg_0[1])
main_circ.rz(-0.012000, qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[3],qreg_0[1],1])
main_circ.cz(qreg_0[0],qreg_0[3])
bindings = {param_0: 0.482000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "ConsolidateBlocks")
