from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(1)
subcirc0.add_register(qreg_0)
qreg_1 = QuantumRegister(1)
subcirc0.add_register(qreg_1)
qreg_2 = QuantumRegister(2)
subcirc0.add_register(qreg_2)
# Adding creg resources 
subcirc0.u(0,0,0.714000, qreg_0[0])
subcirc0.u(-0.524000,-0.760000,-0.034000, qreg_2[1])
subcirc0.u(0,0,0.444000, qreg_2[1])
subcirc0.x(qreg_1[0])
subcirc0.u(0.769000,-0.050000,0.479000, qreg_2[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc1.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc1.add_register(qreg_2)
# Adding creg resources 
subcirc1.u(0.820000,-0.961000,-0.902000, qreg_0[1])
subcirc1.u(0,0,0.902000, qreg_2[0])
subcirc1.u(-0.067000,-0.635000,0.770000, qreg_2[0])
subcirc1.u(0,0,-0.425000, qreg_2[0])
subcirc1.x(qreg_0[1])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.x(qreg_0[1])
subcirc2.u(0,0,0.372000, qreg_0[1])
subcirc2.u(0.615000,0.866000,0.732000, qreg_0[0])
subcirc2.cx(qreg_0[0],qreg_3[0])
subcirc2.cx(qreg_3[0],qreg_0[1])
subcirc2 = subcirc2.to_gate().control(1)

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
qreg_1 = QuantumRegister(3)
main_circ.add_register(qreg_1)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.append(subcirc1,[qreg_1[2],qreg_1[0],0,qreg_0[0]])
main_circ.u(-0.689000,param_0,0.102000, qreg_1[2])
main_circ.x(qreg_1[0])
main_circ.append(subcirc1,[qreg_1[2],qreg_1[1],qreg_0[0],qreg_1[0]])
main_circ.u(param_0,0,param_0, qreg_0[0])
main_circ.cx(qreg_1[0],qreg_0[0])
main_circ.x(qreg_1[1])
main_circ.u(param_0,0,0.293000, qreg_1[0])
main_circ.append(subcirc1,[0,qreg_1[1],qreg_1[0],qreg_1[2]])
main_circ.u(0,0,-0.570000, qreg_0[0])
main_circ.x(qreg_1[1])
main_circ.x(qreg_0[0])
main_circ.u(param_0,param_0,0.074000, qreg_1[2])
main_circ.u(0,param_0,-0.896000, qreg_0[0])
main_circ.append(subcirc1,[qreg_1[2],0,qreg_1[0],qreg_1[1]])
main_circ.cx(0,qreg_1[1])
main_circ.u(param_0,param_0,-0.438000, qreg_1[1])
main_circ.cx(qreg_1[0],qreg_1[2])
main_circ.cx(qreg_1[2],0)
main_circ.cx(qreg_1[2],qreg_0[0])
main_circ.cx(0,qreg_0[0])
main_circ.cx(qreg_1[0],qreg_0[0])
main_circ.cx(qreg_1[0],qreg_1[1])
main_circ.cx(qreg_1[2],0)
main_circ.cx(qreg_1[1],qreg_1[0])
main_circ.cx(qreg_0[0],qreg_1[0])
main_circ.cx(qreg_1[2],qreg_0[0])
main_circ.cx(qreg_1[0],qreg_1[2])
main_circ.cx(qreg_1[2],qreg_1[0])
main_circ.u(0,0,param_0, qreg_1[0])
main_circ.u(param_0,0.851000,-0.906000, 0)
bindings = {param_0: 0.573000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "1008")
