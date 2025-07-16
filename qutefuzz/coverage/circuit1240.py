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
subcirc0.cz(qreg_0[2],qreg_0[3])
subcirc0.cz(qreg_0[3],qreg_0[0])
subcirc0.cy(qreg_0[2],qreg_0[0])
subcirc0.y(qreg_0[0])
subcirc0.cy(qreg_0[3],qreg_0[0])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.cy(qreg_0[0],qreg_0[1])
subcirc1.y(qreg_0[1])
subcirc1.u(pi/2,-0.186000,-0.338000, qreg_3[0])
subcirc1.cy(qreg_0[1],qreg_0[2])
subcirc1.cy(qreg_3[0],qreg_0[2])
subcirc1 = subcirc1.to_gate().control(1)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.cy(qreg_0[2],qreg_0[0])
subcirc2.cy(qreg_0[2],qreg_3[0])
subcirc2.u(pi/2,0.623000,0.797000, qreg_0[1])
subcirc2.cz(qreg_0[0],qreg_0[2])
subcirc2.u(pi/2,0.261000,0.447000, qreg_0[1])

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.y(qreg_3[0])
subcirc3.u(pi/2,0.083000,-0.838000, qreg_0[2])
subcirc3.u(pi/2,0.726000,-0.514000, qreg_3[0])
subcirc3.cy(qreg_0[0],qreg_0[2])
subcirc3.u(pi/2,0.237000,-0.344000, qreg_0[0])
subcirc3 = subcirc3.to_gate().control(3)

main_circ = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.cz(qreg_0[2],qreg_0[0])
main_circ.cz(qreg_0[3],qreg_0[0])
main_circ.append(subcirc0,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_0[3]])
main_circ.cz(qreg_0[1],qreg_0[3])
main_circ.cz(qreg_0[0],qreg_0[2])
main_circ.append(subcirc2,[qreg_0[3],qreg_0[0],qreg_0[2],qreg_0[1]])
main_circ.append(subcirc2,[qreg_0[0],qreg_0[2],qreg_0[3],qreg_0[1]])
main_circ.u(param_0,0.401000,param_0, qreg_0[1])
main_circ.u(pi/2,param_0,param_0, qreg_0[0])
main_circ.u(pi/2,0.379000,param_0, qreg_0[1])
main_circ.cz(qreg_0[1],qreg_0[0])
main_circ.u(param_0,param_0,0.958000, qreg_0[3])
main_circ.append(subcirc2,[qreg_0[3],qreg_0[2],qreg_0[0],qreg_0[1]])
main_circ.u(param_0,0.946000,param_0, qreg_0[0])
main_circ.append(subcirc2,[qreg_0[2],qreg_0[1],qreg_0[0],qreg_0[3]])
main_circ.cz(qreg_0[3],qreg_0[2])
main_circ.y(qreg_0[2])
main_circ.u(param_0,0.651000,param_0, qreg_0[2])
main_circ.append(subcirc2,[qreg_0[2],qreg_0[1],qreg_0[3],qreg_0[0]])
main_circ.append(subcirc2,[qreg_0[0],qreg_0[3],qreg_0[1],qreg_0[2]])
main_circ.cy(qreg_0[3],qreg_0[0])
main_circ.cy(qreg_0[3],qreg_0[0])
bindings = {param_0: -0.296000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "Collect1qRuns")
