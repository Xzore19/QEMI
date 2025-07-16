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
subcirc0.u(-0.662000,-0.140000,-0.770000, qreg_3[0])
subcirc0.cz(qreg_0[2],qreg_0[1])
subcirc0.cx(qreg_0[0],qreg_0[1])
subcirc0.u(0.214000,0.740000,0.965000, qreg_0[1])
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
subcirc1.u(0.352000,0.840000,0.981000, qreg_0[0])
subcirc1.cz(qreg_3[0],qreg_0[0])
subcirc1.cz(qreg_0[0],qreg_0[1])
subcirc1.u(-0.407000,0.078000,0.085000, qreg_3[0])

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc2.add_register(qreg_0)
# Adding creg resources 
subcirc2.cx(qreg_0[0],qreg_0[2])
subcirc2.u(0.641000,0.666000,0.489000, qreg_0[1])
subcirc2.rx(0.802000, qreg_0[2])
subcirc2.cz(qreg_0[3],qreg_0[2])
subcirc2 = subcirc2.to_gate().control(2)

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
param_5 = Parameter("param_5")

main_circ.u(-0.460000,param_2,param_0, 0)
main_circ.cx(0,1)
main_circ.cz(qreg_0[0],3)
main_circ.cx(qreg_0[0],0)
main_circ.u(param_2,param_3,-0.710000, 0)
main_circ.u(param_3,param_3,-0.409000, 3)
main_circ.rx(param_1, 2)
main_circ.rx(param_1, 3)
main_circ.u(0.323000,param_3,-0.646000, 2)
main_circ.append(subcirc1,[2,qreg_0[0],3,0])
main_circ.rx(param_1, 3)
main_circ.rx(-0.696000, 0)
main_circ.cz(qreg_0[0],3)
main_circ.u(param_3,param_2,param_1, 1)
main_circ.rx(param_2, 0)
main_circ.cz(qreg_0[0],1)
main_circ.rx(param_4, 0)
main_circ.cz(2,1)
main_circ.u(0.650000,param_1,-0.645000, qreg_0[0])
main_circ.cx(qreg_0[0],2)
main_circ.cx(2,0)
main_circ.cx(qreg_0[0],3)
main_circ.append(subcirc1,[qreg_0[0],3,2,0])
main_circ.cx(3,qreg_0[0])
main_circ.rx(-0.296000, 0)
main_circ.u(-0.147000,param_5,param_1, 0)
main_circ.cz(3,0)
main_circ.u(param_1,-0.421000,param_1, qreg_0[0])
main_circ.cz(0,1)
main_circ.cx(0,3)
main_circ.rx(-0.793000, 0)
main_circ.cx(qreg_0[0],1)
main_circ.u(0.404000,-0.375000,0.262000, 1)
main_circ.append(subcirc1,[0,qreg_0[0],2,3])
main_circ.cz(qreg_0[0],3)
main_circ.rx(param_1, 2)
main_circ.cx(qreg_0[0],0)
main_circ.u(0.393000,0.496000,0.689000, 3)
main_circ.cx(qreg_0[0],3)
main_circ.rx(0.315000, qreg_0[0])
main_circ.rx(param_2, 0)
bindings = {param_0: -0.183000, param_1: -0.211000, param_2: 0.054000, param_3: -0.012000, param_4: 0.216000, param_5: -0.019000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "486")
