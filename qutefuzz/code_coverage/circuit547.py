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
subcirc0.u(-0.602000,0.662000,0.374000, qreg_0[0])
subcirc0.rz(-0.501000, qreg_3[0])
subcirc0.rx(0.801000, qreg_0[2])
subcirc0.rz(-0.098000, qreg_3[0])
subcirc0 = subcirc0.to_gate().control(3)

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc1.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc1.add_register(qreg_3)
# Adding creg resources 
subcirc1.rz(-0.831000, qreg_3[0])
subcirc1.u(-0.661000,0.912000,-0.539000, qreg_0[2])
subcirc1.z(qreg_0[1])
subcirc1.z(qreg_0[0])
subcirc1 = subcirc1.to_gate().control(2)

subcirc2 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc2.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc2.add_register(qreg_3)
# Adding creg resources 
subcirc2.rz(-0.172000, qreg_0[2])
subcirc2.rx(0.864000, qreg_0[2])
subcirc2.rx(0.219000, qreg_0[1])
subcirc2.u(0.044000,0.140000,-0.717000, qreg_3[0])
subcirc2 = subcirc2.to_gate().control(2)

subcirc3 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(3)
subcirc3.add_register(qreg_0)
qreg_3 = QuantumRegister(1)
subcirc3.add_register(qreg_3)
# Adding creg resources 
subcirc3.u(-0.865000,0.270000,-0.956000, qreg_0[1])
subcirc3.u(0.339000,0.575000,-0.009000, qreg_0[2])
subcirc3.u(-0.199000,0.024000,0.647000, qreg_3[0])
subcirc3.z(qreg_3[0])

subcirc4 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc4.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
subcirc4.add_register(qreg_2)
# Adding creg resources 
subcirc4.z(qreg_2[1])
subcirc4.rz(-0.081000, qreg_0[1])
subcirc4.rz(0.680000, qreg_0[0])
subcirc4.z(qreg_0[1])
subcirc4 = subcirc4.to_gate().control(1)

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

main_circ.append(subcirc3,[2,0,1,3])
main_circ.u(param_2,param_2,param_0, 0)
main_circ.append(subcirc3,[3,0,2,1])
main_circ.append(subcirc3,[1,0,3,2])
main_circ.z(0)
main_circ.append(subcirc3,[3,2,1,0])
main_circ.rz(param_3, 3)
main_circ.rx(param_0, 2)
main_circ.rz(param_3, 1)
main_circ.append(subcirc3,[3,0,1,2])
main_circ.rz(param_3, 1)
main_circ.append(subcirc3,[2,1,3,0])
main_circ.append(subcirc3,[0,2,3,1])
main_circ.z(0)
main_circ.z(0)
main_circ.u(param_1,0.711000,param_0, 0)
main_circ.rx(param_3, 3)
main_circ.z(3)
main_circ.rz(-0.075000, 1)
main_circ.append(subcirc3,[0,3,2,1])
main_circ.u(0.860000,param_3,0.718000, 3)
main_circ.rx(param_0, 2)
bindings = {param_0: 0.470000, param_1: 0.322000, param_2: 0.542000, param_3: 0.590000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
main_circ.measure_active()
run_routing_simulation(main_circ, "547")
