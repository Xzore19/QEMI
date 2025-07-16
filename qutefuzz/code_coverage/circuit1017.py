from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.rx(-0.391000, qreg_2[0])
subcirc0.z(qreg_0[1])
subcirc0.z(qreg_0[0])
subcirc0.z(qreg_0[1])
subcirc0.z(qreg_2[0])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.ry(-0.633000, qreg_3[0])
subcirc1.rx(0.886000, qreg_0[2])
subcirc1.rx(-0.722000, qreg_0[0])
subcirc1.rx(0.466000, qreg_0[0])
subcirc1.rx(0.930000, qreg_0[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cy(qreg_3[0],qreg_0[1])
subcirc2.ry(-0.436000, qreg_0[1])
subcirc2.z(qreg_0[1])
subcirc2.rx(0.410000, qreg_0[2])
subcirc2.rx(0.916000, qreg_3[0])
subcirc2 = subcirc2.to_gate().control(3)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc3.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc3.add_register(qreg_2)
# Adding creg resources 
subcirc3.z(qreg_2[0])
subcirc3.rx(-0.925000, qreg_0[0])
subcirc3.rx(-0.867000, qreg_2[1])
subcirc3.ry(-0.501000, qreg_0[1])
subcirc3.z(qreg_0[1])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc4.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
subcirc4.add_register(qreg_1)
# Adding creg resources 
subcirc4.z(qreg_1[2])
subcirc4.cy(qreg_1[1],qreg_0[0])
subcirc4.z(qreg_1[2])
subcirc4.z(qreg_1[0])
subcirc4.ry(-0.574000, qreg_1[2])
subcirc4 = subcirc4.to_gate().control(3)

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
param_3 = Parameter("param_3")

main_circ.append(subcirc3,[2,qreg_0[0],1,0])
main_circ.ry(param_0, 2)
main_circ.append(subcirc1,[3,0,qreg_0[0],2])
main_circ.cy(3,1)
main_circ.append(subcirc3,[3,0,qreg_0[0],1])
main_circ.z(3)
main_circ.rx(0.635000, 1)
main_circ.append(subcirc1,[3,0,1,2])
main_circ.rx(param_2, 2)
main_circ.append(subcirc3,[0,2,1,qreg_0[0]])
main_circ.rx(-0.759000, qreg_0[0])
main_circ.ry(0.822000, qreg_0[0])
main_circ.cy(2,0)
main_circ.ry(param_2, qreg_0[0])
main_circ.ry(-0.066000, 3)
main_circ.z(1)
main_circ.cy(3,qreg_0[0])
main_circ.cy(1,0)
main_circ.cy(qreg_0[0],0)
main_circ.cy(1,2)
main_circ.cy(3,2)
main_circ.cy(2,3)
main_circ.cy(0,1)
main_circ.cy(3,qreg_0[0])
main_circ.cy(3,0)
main_circ.cy(qreg_0[0],3)
main_circ.cy(3,1)
main_circ.cy(1,2)
main_circ.cy(3,2)
main_circ.cy(qreg_0[0],2)
main_circ.z(3)
main_circ.cy(qreg_0[0],3)
bindings = {param_0: -0.262000, param_2: 0.694000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1017")
