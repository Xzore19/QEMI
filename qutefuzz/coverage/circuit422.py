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
subcirc0.rx(0.691000, qreg_0[1])
subcirc0.u(-0.574000,0.056000,-0.508000, qreg_0[2])
subcirc0.y(qreg_0[3])
subcirc0.cz(qreg_0[3],qreg_0[1])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc1.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(-0.967000,-0.692000,0.292000, qreg_0[1])
subcirc1.rx(0.875000, qreg_0[0])
subcirc1.u(-0.510000,-0.522000,0.107000, qreg_2[0])
subcirc1.rx(0.150000, qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rx(0.025000, qreg_3[0])
subcirc2.u(-0.623000,0.389000,0.127000, qreg_3[0])
subcirc2.u(0.258000,-0.727000,0.307000, qreg_0[2])
subcirc2.rx(0.724000, qreg_0[1])
subcirc2 = subcirc2.to_gate().control(1)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.cz(qreg_3[0],qreg_0[2])
subcirc3.y(qreg_0[2])
subcirc3.rx(-0.410000, qreg_0[2])
subcirc3.rx(-0.940000, qreg_0[1])
subcirc3 = subcirc3.to_gate().control(1)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")

main_circ.rx(-0.978000, 0)
main_circ.append(subcirc1,[qreg_0[2],0,qreg_0[3],qreg_0[1]])
main_circ.append(subcirc3,[qreg_0[0],qreg_0[2],qreg_0[3],qreg_0[1],0])
main_circ.append(subcirc3,[0,qreg_0[0],qreg_0[1],qreg_0[3],qreg_0[2]])
main_circ.rx(-0.519000, qreg_0[3])
main_circ.append(subcirc3,[qreg_0[2],qreg_0[1],qreg_0[3],qreg_0[0],0])
main_circ.rx(0.882000, qreg_0[0])
main_circ.u(-0.562000,param_0,-0.879000, qreg_0[2])
main_circ.y(qreg_0[1])
main_circ.append(subcirc2,[0,qreg_0[0],qreg_0[2],qreg_0[3],qreg_0[1]])
main_circ.append(subcirc2,[qreg_0[2],qreg_0[0],qreg_0[1],0,qreg_0[3]])
main_circ.rx(-0.244000, qreg_0[1])
main_circ.y(qreg_0[2])
main_circ.y(0)
main_circ.append(subcirc3,[qreg_0[3],qreg_0[2],qreg_0[0],qreg_0[1],0])
main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.append(subcirc2,[qreg_0[3],0,qreg_0[0],qreg_0[2],qreg_0[1]])
main_circ.cz(qreg_0[0],qreg_0[3])
main_circ.cz(qreg_0[2],qreg_0[1])
main_circ.cz(qreg_0[0],qreg_0[2])
main_circ.cz(qreg_0[0],qreg_0[2])
main_circ.cz(qreg_0[2],0)
main_circ.cz(qreg_0[3],qreg_0[1])
main_circ.cz(qreg_0[3],0)
main_circ.cz(qreg_0[2],0)
main_circ.cz(0,qreg_0[3])
main_circ.cz(qreg_0[0],0)
main_circ.cz(qreg_0[2],0)
main_circ.y(qreg_0[3])
main_circ.u(-0.207000,param_1,0.256000, qreg_0[0])
main_circ.y(qreg_0[1])
bindings = {param_0: 0.844000, param_1: 0.206000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "422")
