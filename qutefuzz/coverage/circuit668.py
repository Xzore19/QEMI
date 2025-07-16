from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.cz(qreg_2[0],qreg_1[0])
subcirc0.u(0.446000,-0.744000,0.389000, qreg_3[0])
subcirc0.z(qreg_1[0])
subcirc0.cz(qreg_3[0],qreg_1[0])
subcirc0.cz(qreg_0[0],qreg_1[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc1.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc1.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.rx(0.764000, qreg_2[1])
subcirc1.rx(-0.564000, qreg_2[0])
subcirc1.z(qreg_0[0])
subcirc1.cz(qreg_2[1],qreg_0[0])
subcirc1.cz(qreg_1[0],qreg_2[1])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0.746000,-0.238000,0.865000, qreg_0[2])
subcirc2.cz(qreg_0[0],qreg_3[0])
subcirc2.u(0.855000,-0.421000,0.831000, qreg_0[1])
subcirc2.cz(qreg_3[0],qreg_0[2])
subcirc2.u(-0.570000,-0.451000,0.311000, qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cz(qreg_0[3],qreg_0[2])
subcirc3.z(qreg_0[3])
subcirc3.rx(-0.029000, qreg_0[3])
subcirc3.u(0.501000,0.994000,0.168000, qreg_0[0])
subcirc3.cz(qreg_0[1],qreg_0[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.rx(-0.056000, qreg_0[1])
subcirc4.cz(qreg_0[2],qreg_0[1])
subcirc4.z(qreg_0[1])
subcirc4.u(-0.854000,0.140000,0.843000, qreg_0[2])
subcirc4.z(qreg_0[2])
subcirc4 = subcirc4.to_gate().control(1)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
main_circ.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
main_circ.add_register(qreg_2)
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

main_circ.u(-0.177000,-0.267000,param_0, qreg_1[0])
main_circ.cz(qreg_1[0],qreg_2[0])
main_circ.append(subcirc4,[qreg_0[0],qreg_3[0],qreg_1[0],0,1])
main_circ.cz(1,qreg_1[0])
main_circ.z(qreg_3[0])
main_circ.z(1)
main_circ.z(1)
main_circ.append(subcirc3,[qreg_1[0],0,qreg_0[0],1])
main_circ.append(subcirc3,[1,qreg_1[0],0,qreg_0[0]])
main_circ.append(subcirc4,[qreg_2[0],qreg_0[0],qreg_3[0],1,qreg_1[0]])
main_circ.append(subcirc3,[qreg_1[0],0,qreg_3[0],1])
main_circ.append(subcirc2,[1,qreg_1[0],0,qreg_2[0]])
main_circ.cz(qreg_3[0],qreg_1[0])
main_circ.cz(1,qreg_1[0])
main_circ.cz(1,qreg_2[0])
main_circ.append(subcirc0,[qreg_2[0],qreg_1[0],qreg_3[0],0])
main_circ.rx(-0.336000, qreg_0[0])
main_circ.rx(param_0, 1)
main_circ.cz(qreg_3[0],1)
main_circ.cz(1,qreg_2[0])
bindings = {param_0: -0.602000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "668")
