from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.rz(-0.965000, qreg_0[1])
subcirc0.s(qreg_0[1])
subcirc0.rx(0.783000, qreg_2[0])
subcirc0.u(0.098000,0.115000,-0.918000, qreg_2[1])
subcirc0.rz(-0.757000, qreg_0[0])

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(3)
main_circ.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.u(param_0,0.074000,param_0, qreg_3[0])
main_circ.append(subcirc0,[1,qreg_3[0],qreg_0[1],qreg_0[2]])
main_circ.rx(0.253000, 1)
main_circ.u(0.717000,param_2,-0.322000, 0)
main_circ.rx(-0.844000, qreg_0[0])
main_circ.rx(-0.134000, qreg_0[0])
main_circ.rz(-0.450000, 1)
main_circ.rx(0.141000, qreg_3[0])
main_circ.s(qreg_0[2])
main_circ.append(subcirc0,[qreg_0[2],1,qreg_0[0],qreg_0[1]])
main_circ.u(-0.179000,param_1,param_0, qreg_0[1])
main_circ.s(1)
main_circ.s(qreg_0[0])
main_circ.rz(param_2, qreg_0[1])
main_circ.s(0)
main_circ.rz(-0.034000, qreg_0[0])
main_circ.rz(param_2, 1)
main_circ.rx(0.585000, qreg_0[2])
main_circ.append(subcirc0,[0,qreg_0[0],1,qreg_0[2]])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[2],1,0])
main_circ.append(subcirc0,[qreg_3[0],0,1,qreg_0[2]])
main_circ.rz(0.845000, 1)
main_circ.rz(-0.172000, qreg_3[0])
main_circ.rz(param_1, qreg_3[0])
main_circ.rz(param_1, qreg_3[0])
main_circ.append(subcirc0,[qreg_0[0],1,qreg_0[1],qreg_0[2]])
main_circ.u(param_0,param_2,0.995000, qreg_0[1])
main_circ.rz(0.516000, qreg_3[0])
main_circ.s(qreg_3[0])
main_circ.append(subcirc0,[qreg_0[2],qreg_3[0],qreg_0[1],1])
main_circ.s(qreg_0[1])
main_circ.s(qreg_0[0])
bindings = {param_0: 0.124000, param_1: 0.086000, param_2: -0.625000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "948")
