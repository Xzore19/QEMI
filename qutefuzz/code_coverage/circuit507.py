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
subcirc0.rx(0.932000, qreg_0[1])
subcirc0.cx(qreg_0[1],qreg_0[2])
subcirc0.u(-0.375000,-0.986000,0.592000, qreg_0[3])
subcirc0.u(0.228000,0.078000,0.861000, qreg_0[0])
subcirc0.u(-0.920000,0.282000,0.133000, qreg_0[2])
subcirc0.u(0,0,0.626000, qreg_0[2])
subcirc0 = subcirc0.to_gate().control(2)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.u(0.057000,0.579000,-0.780000, qreg_0[1])
subcirc1.u(0,0,-0.690000, qreg_0[3])
subcirc1.rx(-0.845000, qreg_0[0])
subcirc1.u(0,0,-0.658000, qreg_0[1])
subcirc1.u(0.522000,0.284000,-0.052000, qreg_0[3])
subcirc1.cx(qreg_0[1],qreg_0[2])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.u(0.021000,0.168000,0.250000, qreg_3[0])
subcirc2.u(0,0,0.665000, qreg_0[0])
subcirc2.cx(qreg_0[1],qreg_3[0])
subcirc2.u(0,0,0.303000, qreg_3[0])
subcirc2.rx(-0.070000, qreg_0[1])
subcirc2.cx(qreg_0[2],qreg_3[0])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc3.add_register(qreg_0)
# Adding creg resources 
subcirc3.cx(qreg_0[3],qreg_0[0])
subcirc3.rx(0.511000, qreg_0[1])
subcirc3.rx(-0.508000, qreg_0[0])
subcirc3.rx(-0.330000, qreg_0[0])
subcirc3.u(0,0,0.054000, qreg_0[2])
subcirc3.u(0.727000,-0.544000,-0.435000, qreg_0[2])
subcirc3 = subcirc3.to_gate().control(3)

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
param_3 = Parameter("param_3")
param_4 = Parameter("param_4")
param_5 = Parameter("param_5")

main_circ.u(0,param_1,0.302000, 0)
main_circ.rx(param_0, qreg_0[3])
main_circ.u(0.777000,0.441000,-0.013000, qreg_0[1])
main_circ.u(0.479000,param_2,param_5, 0)
main_circ.u(0.971000,param_5,param_4, qreg_0[0])
main_circ.append(subcirc0,[qreg_0[3],1,0,qreg_0[0],qreg_0[2],qreg_0[1]])
main_circ.append(subcirc1,[1,qreg_0[1],qreg_0[3],0,qreg_0[0],qreg_0[2]])
main_circ.u(param_3,-0.494000,param_5, 1)
main_circ.u(param_5,param_4,param_5, 1)
main_circ.u(0,0,0.838000, qreg_0[2])
main_circ.u(param_5,0,0.674000, 1)
main_circ.u(param_2,0,-0.810000, 0)
main_circ.append(subcirc1,[qreg_0[1],1,qreg_0[3],0,qreg_0[2],qreg_0[0]])
main_circ.cx(0,1)
main_circ.append(subcirc2,[qreg_0[1],qreg_0[0],1,0,qreg_0[3],qreg_0[2]])
main_circ.cx(qreg_0[0],qreg_0[3])
main_circ.cx(qreg_0[2],qreg_0[1])
main_circ.cx(qreg_0[0],qreg_0[2])
main_circ.cx(0,qreg_0[0])
main_circ.cx(0,1)
main_circ.cx(qreg_0[0],qreg_0[1])
main_circ.cx(0,1)
main_circ.cx(qreg_0[0],qreg_0[3])
main_circ.rx(0.373000, qreg_0[2])
main_circ.rx(param_1, 1)
main_circ.cx(qreg_0[1],qreg_0[0])
bindings = {param_0: -0.062000, param_1: -0.195000, param_2: -0.307000, param_3: 0.907000, param_4: 0.462000, param_5: -0.717000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "507")
