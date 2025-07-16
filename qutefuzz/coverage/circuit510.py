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
subcirc0.ry(0.208000, qreg_3[0])
subcirc0.ry(-0.549000, qreg_3[0])
subcirc0.rx(-0.476000, qreg_0[2])
subcirc0.ry(-0.641000, qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.rx(-0.282000, qreg_0[0])
subcirc1.s(qreg_0[1])
subcirc1.u(0,0,-0.804000, qreg_0[0])
subcirc1.ry(-0.262000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc2.add_register(qreg_1)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0,0,-0.699000, qreg_2[0])
subcirc2.s(qreg_2[0])
subcirc2.rx(-0.851000, qreg_1[0])
subcirc2.ry(-0.354000, qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.s(qreg_3[0])
subcirc3.rx(-0.131000, qreg_3[0])
subcirc3.u(0,0,-0.094000, qreg_0[2])
subcirc3.s(qreg_0[2])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.rx(0.201000, qreg_0[2])
subcirc4.rx(-0.880000, qreg_0[3])
subcirc4.u(0,0,0.655000, qreg_0[0])
subcirc4.u(0,0,0.895000, qreg_0[1])
subcirc4 = subcirc4.to_gate().control(1)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(1)
main_circ.add_register(creg_0)
creg_1 = ClassicalRegister(1)
main_circ.add_register(creg_1)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.u(0,0,param_0, qreg_0[0])
main_circ.u(0,0,param_0, qreg_2[0])
main_circ.ry(param_0, qreg_2[1])
main_circ.s(qreg_2[0])
main_circ.ry(-0.930000, qreg_0[0])
main_circ.u(param_0,0,0.330000, qreg_2[0])
main_circ.ry(0.120000, qreg_0[0])
main_circ.rx(-0.017000, qreg_2[1])
main_circ.append(subcirc2,[qreg_0[1],qreg_0[0],qreg_2[1],qreg_2[0]])
main_circ.rx(0.789000, qreg_0[1])
main_circ.append(subcirc0,[qreg_0[0],qreg_2[0],qreg_0[1],qreg_2[1]])
main_circ.rx(0.937000, qreg_0[0])
main_circ.s(qreg_0[0])
main_circ.append(subcirc3,[qreg_2[1],qreg_0[1],qreg_0[0],qreg_2[0]])
main_circ.u(param_0,0,param_0, qreg_2[1])
main_circ.append(subcirc2,[qreg_0[0],qreg_0[1],qreg_2[1],qreg_2[0]])
main_circ.rx(param_0, qreg_2[1])
main_circ.ry(param_0, qreg_2[0])
main_circ.append(subcirc2,[qreg_0[0],qreg_2[0],qreg_2[1],qreg_0[1]])
main_circ.rx(param_0, qreg_2[1])
main_circ.append(subcirc2,[qreg_0[1],qreg_2[0],qreg_0[0],qreg_2[1]])
main_circ.s(qreg_0[0])
main_circ.rx(0.509000, qreg_2[0])
main_circ.s(qreg_0[0])
main_circ.u(0,0,param_0, qreg_0[1])
main_circ.s(qreg_2[1])
main_circ.rx(param_0, qreg_2[0])
bindings = {param_0: 0.450000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "510")
