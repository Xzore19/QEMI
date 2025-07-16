from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc0.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.cy(qreg_0[0],qreg_0[2])
subcirc0.rx(0.660000, qreg_3[0])
subcirc0.ry(-0.966000, qreg_0[2])
subcirc0.rx(0.485000, qreg_0[2])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cy(qreg_0[0],qreg_0[2])
subcirc1.rz(0.881000, qreg_0[2])
subcirc1.rx(-0.117000, qreg_0[0])
subcirc1.rx(0.932000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cy(qreg_1[0],qreg_3[0])
subcirc2.cy(qreg_1[1],qreg_1[0])
subcirc2.ry(-0.166000, qreg_0[0])
subcirc2.ry(0.220000, qreg_1[1])
subcirc2 = subcirc2.to_gate().control(2)

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.append(subcirc1,[0,qreg_0[0],qreg_0[1],qreg_0[3],1,qreg_0[2]])
main_circ.ry(param_0, qreg_0[1])
main_circ.cy(qreg_0[3],1)
main_circ.rx(param_0, qreg_0[3])
main_circ.append(subcirc2,[1,qreg_0[0],qreg_0[2],qreg_0[1],0,qreg_0[3]])
main_circ.rx(-0.874000, qreg_0[1])
main_circ.append(subcirc2,[qreg_0[3],qreg_0[0],qreg_0[1],1,qreg_0[2],0])
main_circ.append(subcirc2,[0,1,qreg_0[3],qreg_0[1],qreg_0[2],qreg_0[0]])
main_circ.rx(param_0, qreg_0[1])
main_circ.ry(0.056000, qreg_0[1])
main_circ.ry(-0.999000, qreg_0[2])
main_circ.append(subcirc1,[0,1,qreg_0[3],qreg_0[0],qreg_0[1],qreg_0[2]])
main_circ.rx(param_0, qreg_0[0])
main_circ.rx(param_0, qreg_0[0])
main_circ.cy(0,1)
main_circ.ry(0.275000, 0)
main_circ.ry(param_0, 0)
main_circ.rz(-0.606000, qreg_0[1])
main_circ.rx(param_0, qreg_0[0])
main_circ.append(subcirc1,[qreg_0[3],1,0,qreg_0[2],qreg_0[0],qreg_0[1]])
main_circ.cy(qreg_0[1],qreg_0[2])
main_circ.cy(qreg_0[0],1)
main_circ.cy(1,qreg_0[1])
main_circ.cy(qreg_0[1],1)
main_circ.ry(-0.289000, 0)
main_circ.rz(param_0, qreg_0[1])
main_circ.rz(-0.334000, qreg_0[1])
main_circ.ry(param_0, qreg_0[2])
main_circ.ry(param_0, qreg_0[2])
main_circ.ry(0.125000, qreg_0[1])
main_circ.rx(param_0, qreg_0[0])
main_circ.cy(qreg_0[1],qreg_0[3])
main_circ.cy(1,0)
main_circ.rz(param_0, qreg_0[2])
bindings = {param_0: 0.424000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1515")
