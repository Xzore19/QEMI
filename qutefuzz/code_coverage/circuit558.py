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
subcirc0.ry(-0.751000, qreg_0[2])
subcirc0.x(qreg_0[3])
subcirc0.ry(-0.689000, qreg_0[0])
subcirc0.ry(-0.959000, qreg_0[2])
subcirc0.ry(0.603000, qreg_0[2])
subcirc0.u(0.703000,-0.824000,-0.773000, qreg_0[2])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.u(-0.697000,-0.300000,0.864000, qreg_0[2])
subcirc1.cz(qreg_0[2],qreg_3[0])
subcirc1.ry(-0.739000, qreg_0[0])
subcirc1.ry(-0.814000, qreg_3[0])
subcirc1.cz(qreg_0[0],qreg_0[2])
subcirc1.x(qreg_3[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc2.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc2.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.x(qreg_2[0])
subcirc2.u(0.227000,0.150000,-0.172000, qreg_0[0])
subcirc2.u(-0.704000,-0.404000,-0.117000, qreg_3[0])
subcirc2.x(qreg_3[0])
subcirc2.x(qreg_3[0])
subcirc2.ry(-0.506000, qreg_0[1])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.x(qreg_0[0])
subcirc3.u(-0.808000,0.291000,0.349000, qreg_3[0])
subcirc3.x(qreg_3[0])
subcirc3.ry(-0.403000, qreg_0[0])
subcirc3.u(0.685000,-0.063000,0.287000, qreg_3[0])
subcirc3.u(-0.196000,-0.042000,-0.596000, qreg_0[1])
subcirc3 = subcirc3.to_gate().control(2)

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc4.add_register(qreg_0)
# Adding creg resources 
subcirc4.u(-0.232000,-0.551000,0.775000, qreg_0[2])
subcirc4.cz(qreg_0[2],qreg_0[3])
subcirc4.ry(0.533000, qreg_0[3])
subcirc4.ry(0.998000, qreg_0[2])
subcirc4.x(qreg_0[1])
subcirc4.x(qreg_0[3])
subcirc4 = subcirc4.to_gate().control(1)

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

main_circ.append(subcirc0,[0,qreg_0[1],qreg_0[0],qreg_0[3]])
main_circ.append(subcirc4,[qreg_0[3],qreg_0[1],qreg_0[2],0,qreg_0[0]])
main_circ.u(param_0,param_3,param_3, qreg_0[3])
main_circ.x(qreg_0[1])
main_circ.cz(qreg_0[3],qreg_0[2])
main_circ.x(qreg_0[0])
main_circ.append(subcirc4,[qreg_0[2],qreg_0[0],qreg_0[1],qreg_0[3],0])
main_circ.u(param_1,param_0,param_3, qreg_0[3])
main_circ.ry(param_3, 0)
main_circ.append(subcirc4,[0,qreg_0[2],qreg_0[3],qreg_0[0],qreg_0[1]])
main_circ.ry(-0.558000, qreg_0[3])
main_circ.cz(qreg_0[0],qreg_0[2])
main_circ.u(0.702000,-0.748000,-0.975000, qreg_0[2])
main_circ.cz(qreg_0[0],qreg_0[3])
main_circ.x(qreg_0[2])
main_circ.cz(qreg_0[2],qreg_0[1])
main_circ.u(0.264000,param_0,0.890000, 0)
main_circ.ry(param_2, 0)
main_circ.cz(qreg_0[0],qreg_0[3])
main_circ.cz(qreg_0[2],qreg_0[1])
main_circ.cz(0,qreg_0[2])
main_circ.cz(qreg_0[2],0)
main_circ.cz(qreg_0[1],qreg_0[2])
main_circ.cz(qreg_0[2],qreg_0[1])
main_circ.cz(qreg_0[0],qreg_0[1])
main_circ.cz(qreg_0[1],qreg_0[2])
main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],0,qreg_0[3]])
main_circ.x(qreg_0[1])
bindings = {param_0: 0.684000, param_1: 0.997000, param_2: 0.412000, param_3: -0.380000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "558")
