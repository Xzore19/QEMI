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
subcirc0.u(-0.448000,-0.194000,-0.629000, qreg_0[3])
subcirc0.z(qreg_0[0])
subcirc0.u(-0.618000,0.315000,0.435000, qreg_0[3])
subcirc0.cz(qreg_0[0],qreg_0[3])
subcirc0.cz(qreg_0[3],qreg_0[2])
subcirc0.z(qreg_0[2])
subcirc0 = subcirc0.to_gate().control(1)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(0.071000,-0.861000,0.384000, qreg_0[0])
subcirc1.rx(0.269000, qreg_0[0])
subcirc1.cz(qreg_3[0],qreg_2[0])
subcirc1.cz(qreg_0[0],qreg_3[0])
subcirc1.u(0.769000,-0.910000,0.945000, qreg_0[1])
subcirc1.cz(qreg_3[0],qreg_0[0])
subcirc1 = subcirc1.to_gate().control(3)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")

main_circ.rx(-0.927000, qreg_0[0])
main_circ.append(subcirc0,[qreg_1[1],0,1,qreg_0[0],qreg_1[2]])
main_circ.u(0.784000,param_0,-0.367000, qreg_1[2])
main_circ.u(-0.080000,0.020000,param_1, qreg_1[2])
main_circ.cz(qreg_0[0],qreg_1[0])
main_circ.u(-0.951000,param_2,0.564000, 0)
main_circ.cz(qreg_0[0],1)
main_circ.z(qreg_1[0])
main_circ.z(1)
main_circ.cz(qreg_0[0],qreg_1[0])
main_circ.append(subcirc0,[1,qreg_1[2],qreg_0[0],qreg_1[0],0])
main_circ.u(-0.434000,param_0,param_0, qreg_0[0])
main_circ.append(subcirc0,[0,qreg_1[0],qreg_1[2],qreg_0[0],qreg_1[1]])
main_circ.cz(1,qreg_1[2])
main_circ.cz(qreg_0[0],qreg_1[1])
main_circ.cz(qreg_1[0],0)
main_circ.cz(0,qreg_1[2])
main_circ.z(0)
main_circ.cz(qreg_1[0],qreg_1[2])
main_circ.append(subcirc0,[qreg_1[0],qreg_1[1],1,0,qreg_0[0]])
bindings = {param_0: 0.960000, param_1: -0.577000, param_2: -0.958000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "645")
