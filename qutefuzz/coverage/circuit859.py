from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(2)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.y(qreg_0[1])
main_circ.y(qreg_0[0])
main_circ.cy(qreg_0[0],qreg_0[1])
main_circ.y(qreg_2[1])
main_circ.y(qreg_2[1])
main_circ.cy(qreg_0[0],1)
main_circ.cy(qreg_2[1],qreg_2[0])
main_circ.cy(qreg_0[1],0)
main_circ.y(qreg_2[1])
main_circ.cy(1,qreg_2[0])
main_circ.cy(qreg_0[1],0)
main_circ.y(1)
main_circ.cz(qreg_2[1],qreg_2[0])
main_circ.y(1)
main_circ.y(0)
main_circ.cy(qreg_2[0],0)
main_circ.cz(qreg_2[1],qreg_0[1])
main_circ.cz(1,qreg_2[0])
main_circ.cz(qreg_2[1],0)
main_circ.cz(qreg_0[1],qreg_2[1])
main_circ.cy(qreg_2[0],qreg_0[0])
main_circ.y(qreg_2[0])
main_circ.y(0)
main_circ.cz(qreg_0[1],qreg_2[0])
main_circ.rx(param_0, 0)
main_circ.cz(qreg_2[1],1)
main_circ.cz(qreg_2[0],qreg_0[1])
main_circ.cz(qreg_0[0],qreg_2[0])
main_circ.cz(1,qreg_2[1])
main_circ.y(qreg_0[0])
main_circ.cz(qreg_0[0],1)
main_circ.cy(qreg_2[1],1)
main_circ.cz(qreg_2[1],1)
main_circ.y(qreg_0[0])
main_circ.rx(param_0, 1)
main_circ.rx(param_0, qreg_0[1])
main_circ.rx(param_0, 0)
main_circ.y(0)
main_circ.cy(1,qreg_2[0])
main_circ.y(qreg_0[0])
bindings = {param_0: 0.762000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "859")
