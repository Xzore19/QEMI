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
subcirc0.ry(-0.793000, qreg_0[0])
subcirc0.z(qreg_0[2])
subcirc0.u(-0.850000,0.845000,-0.713000, qreg_0[2])
subcirc0.ry(-0.951000, qreg_0[2])
subcirc0.z(qreg_0[3])

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
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
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")

main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_0[2],qreg_3[0]])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],qreg_3[0],qreg_0[1]])
main_circ.u(0.824000,0.055000,param_5, qreg_0[1])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_0[2],qreg_3[0]])
main_circ.u(param_6,0.769000,-0.456000, qreg_3[0])
main_circ.u(param_5,-0.280000,0.293000, qreg_3[0])
main_circ.z(qreg_0[1])
main_circ.ry(0.497000, qreg_0[1])
main_circ.ry(0.386000, qreg_0[0])
main_circ.cx(qreg_3[0],qreg_0[0])
main_circ.ry(-0.392000, qreg_0[1])
main_circ.append(subcirc0,[qreg_0[2],qreg_3[0],qreg_0[0],qreg_0[1]])
main_circ.ry(0.296000, qreg_0[0])
main_circ.u(param_5,-0.533000,-0.689000, qreg_0[1])
main_circ.z(qreg_0[0])
main_circ.cx(qreg_0[2],qreg_3[0])
main_circ.cx(qreg_0[1],qreg_0[0])
main_circ.cx(qreg_0[0],qreg_0[1])
main_circ.cx(qreg_0[2],qreg_3[0])
main_circ.cx(qreg_0[2],qreg_0[1])
main_circ.cx(qreg_3[0],qreg_0[2])
main_circ.cx(qreg_0[0],qreg_0[2])
main_circ.cx(qreg_0[0],qreg_0[2])
main_circ.cx(qreg_0[1],qreg_3[0])
main_circ.cx(qreg_0[1],qreg_0[0])
main_circ.cx(qreg_0[1],qreg_3[0])
main_circ.ry(-0.312000, qreg_0[2])
bindings = {param_5: 0.625000, param_6: -0.232000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Collect2qBlocks")
