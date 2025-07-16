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
subcirc0.u(0,0,0.448000, qreg_0[1])
subcirc0.x(qreg_0[3])
subcirc0.x(qreg_0[2])
subcirc0.cx(qreg_0[0],qreg_0[2])

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
param_4 = Parameter("param_4")

main_circ.u(param_1,0,-0.301000, 3)
main_circ.append(subcirc0,[2,qreg_0[0],0,3])
main_circ.u(0,param_4,0.862000, 3)
main_circ.x(1)
main_circ.z(2)
main_circ.x(qreg_0[0])
main_circ.z(0)
main_circ.append(subcirc0,[2,qreg_0[0],3,1])
main_circ.append(subcirc0,[qreg_0[0],0,3,2])
main_circ.cx(1,qreg_0[0])
main_circ.x(3)
main_circ.cx(2,3)
main_circ.x(1)
main_circ.cx(3,1)
main_circ.append(subcirc0,[qreg_0[0],1,2,3])
main_circ.append(subcirc0,[2,3,0,qreg_0[0]])
main_circ.z(2)
main_circ.z(qreg_0[0])
main_circ.x(2)
main_circ.u(param_1,param_1,0.645000, qreg_0[0])
main_circ.x(2)
main_circ.cx(qreg_0[0],1)
main_circ.cx(qreg_0[0],0)
main_circ.cx(3,qreg_0[0])
main_circ.cx(3,qreg_0[0])
main_circ.cx(qreg_0[0],1)
main_circ.cx(2,3)
main_circ.cx(qreg_0[0],3)
main_circ.x(1)
main_circ.x(2)
main_circ.cx(3,2)
main_circ.u(0,param_2,param_2, 3)
main_circ.cx(2,1)
main_circ.u(0,param_1,param_1, 1)
main_circ.u(param_2,param_3,0.235000, qreg_0[0])
main_circ.u(0,param_0,-0.727000, 1)
bindings = {param_0: -0.865000, param_1: -0.274000, param_2: 0.271000, param_3: -0.845000, param_4: -0.047000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "620")
