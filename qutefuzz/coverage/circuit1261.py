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
subcirc0.cx(qreg_0[2],qreg_0[0])
subcirc0.cy(qreg_0[3],qreg_0[1])
subcirc0.y(qreg_0[3])
subcirc0.u(-0.457000,0.729000,-0.555000, qreg_0[3])

main_circ = QuantumCircuit(4)
# Adding qregs 
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")
param_6 = Parameter("param_6")

main_circ.append(subcirc0,[1,3,2,0])
main_circ.append(subcirc0,[3,2,1,0])
main_circ.u(0.632000,-0.339000,param_3, 2)
main_circ.cy(2,1)
main_circ.cy(0,2)
main_circ.append(subcirc0,[3,1,0,2])
main_circ.u(0.670000,-0.386000,param_0, 3)
main_circ.append(subcirc0,[1,0,3,2])
main_circ.cy(1,0)
main_circ.cy(3,0)
main_circ.cx(0,3)
main_circ.append(subcirc0,[0,2,1,3])
main_circ.u(param_4,0.330000,0.955000, 3)
main_circ.cy(1,3)
main_circ.cy(2,0)
main_circ.cx(2,1)
main_circ.cx(0,3)
main_circ.cx(0,2)
main_circ.cy(0,1)
main_circ.cx(1,2)
main_circ.y(2)
main_circ.cx(3,1)
main_circ.append(subcirc0,[1,0,2,3])
main_circ.y(0)
main_circ.u(param_4,-0.202000,-0.808000, 3)
main_circ.y(0)
main_circ.y(0)
main_circ.u(-0.364000,param_4,param_1, 2)
bindings = {param_0: -0.158000, param_1: -0.886000, param_3: -0.659000, param_4: 0.213000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1261")
