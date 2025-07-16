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
subcirc0.u(0.020000,0.171000,-0.687000, qreg_0[1])
subcirc0.u(0.880000,-0.051000,0.210000, qreg_0[0])
subcirc0.cy(qreg_2[0],qreg_0[1])
subcirc0.cy(qreg_0[1],qreg_2[1])
subcirc0.u(0,0,-0.780000, qreg_0[0])
subcirc0.z(qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.z(qreg_0[1])
subcirc1.z(qreg_0[1])
subcirc1.u(0,0,-0.678000, qreg_0[2])
subcirc1.u(0.318000,0.324000,-0.765000, qreg_0[2])
subcirc1.z(qreg_0[1])
subcirc1.u(0,0,-0.972000, qreg_0[1])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(-0.392000,-0.788000,-0.880000, qreg_0[1])
subcirc2.z(qreg_0[1])
subcirc2.cy(qreg_0[1],qreg_0[2])
subcirc2.u(-0.152000,-0.642000,0.086000, qreg_0[1])
subcirc2.u(0,0,0.984000, qreg_0[1])
subcirc2.cy(qreg_0[2],qreg_0[0])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.u(0.008000,0.976000,0.183000, qreg_0[1])
subcirc3.cy(qreg_0[2],qreg_0[3])
subcirc3.cy(qreg_0[3],qreg_0[1])
subcirc3.cy(qreg_0[1],qreg_0[3])
subcirc3.z(qreg_0[3])
subcirc3.cy(qreg_0[2],qreg_0[3])
subcirc3 = subcirc3.to_gate().control(3)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc4.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc4.add_register(qreg_3)
# Adding creg resources 
subcirc4.u(0,0,0.482000, qreg_0[0])
subcirc4.z(qreg_3[0])
subcirc4.u(0.230000,0.948000,-0.278000, qreg_0[0])
subcirc4.u(0,0,-0.141000, qreg_3[0])
subcirc4.z(qreg_0[2])
subcirc4.cy(qreg_0[2],qreg_0[1])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
main_circ.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
main_circ.add_register(qreg_3)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")
param_1 = Parameter("param_1")
param_2 = Parameter("param_2")
param_3 = Parameter("param_3")

main_circ.cy(0,qreg_0[0])
main_circ.u(param_1,param_0,-0.572000, qreg_3[0])
main_circ.z(qreg_0[0])
main_circ.append(subcirc0,[qreg_1[0],qreg_0[0],qreg_3[0],qreg_1[1]])
main_circ.append(subcirc0,[qreg_0[0],0,qreg_3[0],qreg_1[1]])
main_circ.cy(0,qreg_3[0])
main_circ.u(param_2,param_3,param_1, qreg_0[0])
main_circ.z(qreg_3[0])
main_circ.u(0,0,param_2, 0)
main_circ.cy(qreg_1[0],qreg_0[0])
main_circ.append(subcirc0,[qreg_1[1],qreg_0[0],qreg_1[0],qreg_3[0]])
main_circ.cy(qreg_1[1],qreg_3[0])
main_circ.u(param_0,0,0.414000, qreg_0[0])
main_circ.u(0,0,0.662000, qreg_3[0])
main_circ.append(subcirc0,[qreg_1[0],qreg_3[0],0,qreg_0[0]])
main_circ.u(-0.401000,-0.380000,0.882000, qreg_1[0])
main_circ.u(param_3,-0.940000,param_1, qreg_0[0])
main_circ.z(qreg_1[0])
main_circ.cy(qreg_1[1],0)
main_circ.cy(qreg_1[0],0)
main_circ.cy(0,qreg_3[0])
main_circ.u(0.190000,param_3,param_2, qreg_1[1])
main_circ.u(param_0,param_0,0.301000, qreg_0[0])
main_circ.u(param_0,0.578000,-0.431000, qreg_1[1])
main_circ.u(param_1,-0.154000,param_3, qreg_0[0])
main_circ.z(0)
main_circ.cy(qreg_1[0],qreg_3[0])
main_circ.cy(qreg_1[1],0)
main_circ.cy(qreg_1[1],qreg_0[0])
main_circ.u(0,0,0.167000, qreg_1[1])
main_circ.z(qreg_1[0])
main_circ.u(0.340000,-0.611000,-0.117000, 0)
main_circ.z(qreg_3[0])
bindings = {param_0: -0.636000, param_1: 0.259000, param_2: -0.375000, param_3: -0.458000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "840")
