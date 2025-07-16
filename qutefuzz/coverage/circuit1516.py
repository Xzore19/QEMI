from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

main_circ = QuantumCircuit(1)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
qreg_2 = QuantumRegister(2)
main_circ.add_register(qreg_2)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.cx(qreg_0[0],0)
main_circ.x(qreg_2[1])
main_circ.rz(-0.698000, qreg_2[1])
main_circ.cx(0,qreg_2[1])
main_circ.cx(0,qreg_2[0])
main_circ.x(0)
main_circ.rz(param_0, qreg_0[0])
main_circ.cx(0,qreg_2[0])
main_circ.cx(qreg_2[0],qreg_0[1])
main_circ.rz(-0.982000, qreg_2[1])
main_circ.x(qreg_2[0])
main_circ.rz(param_0, qreg_0[0])
main_circ.cx(qreg_2[0],qreg_2[1])
main_circ.u(-0.207000,-0.802000,param_0, qreg_2[0])
main_circ.rz(-0.733000, qreg_2[1])
main_circ.x(qreg_2[0])
main_circ.u(param_0,0.581000,param_0, 0)
main_circ.x(0)
main_circ.u(0.089000,param_0,param_0, qreg_0[1])
main_circ.x(qreg_0[1])
main_circ.x(0)
main_circ.x(qreg_0[1])
main_circ.rz(-0.143000, qreg_2[0])
main_circ.cx(0,qreg_0[0])
main_circ.x(qreg_2[0])
main_circ.cx(qreg_0[1],0)
main_circ.cx(0,qreg_0[0])
main_circ.rz(-0.016000, 0)
main_circ.cx(qreg_2[0],0)
main_circ.cx(qreg_0[1],0)
main_circ.cx(qreg_2[1],qreg_0[0])
main_circ.rz(param_0, 0)
main_circ.x(qreg_0[0])
main_circ.u(param_0,param_0,param_0, qreg_2[1])
main_circ.x(0)
main_circ.rz(param_0, 0)
main_circ.x(qreg_0[1])
main_circ.x(qreg_2[1])
main_circ.rz(-0.245000, qreg_2[1])
main_circ.rz(param_0, qreg_2[0])
bindings = {param_0: 0.529000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CommutativeInverseCancellation")
