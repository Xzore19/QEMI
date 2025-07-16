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
subcirc0.ry(0.309000, qreg_0[1])
subcirc0.z(qreg_0[0])
subcirc0.ry(-0.974000, qreg_0[1])
subcirc0.y(qreg_0[0])
subcirc0.u(-0.352000,0.639000,-0.464000, qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.z(qreg_3[0])
subcirc1.z(qreg_3[0])
subcirc1.u(0.614000,-0.423000,0.983000, qreg_0[0])
subcirc1.ry(-0.259000, qreg_0[0])
subcirc1.u(0.227000,-0.884000,-0.108000, qreg_0[0])
subcirc1 = subcirc1.to_gate().control(3)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc2.add_register(qreg_0)
qreg_1 = QuantumRegister(2)
subcirc2.add_register(qreg_1)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.ry(0.605000, qreg_0[0])
subcirc2.u(0.234000,-0.920000,-0.402000, qreg_1[1])
subcirc2.z(qreg_1[0])
subcirc2.u(-0.854000,0.799000,-0.678000, qreg_1[0])
subcirc2.y(qreg_0[0])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.u(0.558000,-0.027000,-0.298000, qreg_0[3])
subcirc3.u(-0.809000,0.068000,0.220000, qreg_0[3])
subcirc3.y(qreg_0[2])
subcirc3.ry(-0.884000, qreg_0[0])
subcirc3.y(qreg_0[3])
subcirc3 = subcirc3.to_gate().control(1)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.ry(-0.341000, qreg_0[0])
subcirc4.ry(-0.171000, qreg_0[1])
subcirc4.z(qreg_0[0])
subcirc4.ry(-0.886000, qreg_0[0])
subcirc4.z(qreg_0[1])
subcirc4 = subcirc4.to_gate().control(2)

main_circ = QuantumCircuit(2)
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

main_circ.append(subcirc4,[0,1,qreg_0[1],qreg_0[2],qreg_0[0],qreg_0[3]])
main_circ.append(subcirc2,[qreg_0[1],qreg_0[0],0,1])
main_circ.ry(param_2, 0)
main_circ.append(subcirc2,[qreg_0[1],qreg_0[3],qreg_0[0],1])
main_circ.append(subcirc2,[qreg_0[2],qreg_0[1],0,qreg_0[0]])
main_circ.y(1)
main_circ.append(subcirc3,[qreg_0[1],0,qreg_0[2],1,qreg_0[0]])
main_circ.append(subcirc0,[qreg_0[1],1,qreg_0[3],0])
main_circ.append(subcirc2,[qreg_0[0],0,qreg_0[3],qreg_0[2]])
main_circ.u(param_1,param_1,param_2, qreg_0[0])
main_circ.z(qreg_0[0])
main_circ.ry(0.204000, qreg_0[0])
main_circ.y(0)
main_circ.ry(0.348000, 1)
main_circ.z(qreg_0[3])
main_circ.z(1)
main_circ.z(qreg_0[2])
main_circ.y(1)
main_circ.y(qreg_0[3])
main_circ.y(qreg_0[3])
main_circ.u(0.890000,param_2,param_1, qreg_0[1])
main_circ.z(qreg_0[3])
bindings = {param_1: -0.905000, param_2: 0.387000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "InverseCancellation")
