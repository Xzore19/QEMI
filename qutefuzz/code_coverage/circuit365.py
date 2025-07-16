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
subcirc0.y(qreg_0[1])
subcirc0.u(-0.145000,-0.914000,-0.574000, qreg_0[0])
subcirc0.cy(qreg_0[2],qreg_0[0])
subcirc0.u(-0.149000,0.186000,0.194000, qreg_0[0])
subcirc0.y(qreg_0[1])

subcirc1 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(4)
subcirc1.add_register(qreg_0)
# Adding creg resources 
subcirc1.y(qreg_0[2])
subcirc1.cy(qreg_0[0],qreg_0[3])
subcirc1.u(-0.473000,0.697000,-0.526000, qreg_0[3])
subcirc1.cx(qreg_0[3],qreg_0[2])
subcirc1.y(qreg_0[1])
subcirc1 = subcirc1.to_gate().control(3)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(1)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.cx(2,0)
main_circ.u(0.760000,-0.737000,param_0, 1)
main_circ.y(3)
main_circ.cx(qreg_0[0],0)
main_circ.u(-0.373000,-0.269000,-0.813000, 1)
main_circ.y(2)
main_circ.u(-0.943000,-0.764000,param_0, 1)
main_circ.cy(0,3)
main_circ.u(param_0,-0.977000,param_0, 3)
main_circ.cy(qreg_0[0],0)
main_circ.cy(3,qreg_0[0])
main_circ.cy(1,2)
main_circ.cy(2,1)
main_circ.u(param_0,-0.024000,param_0, 1)
main_circ.y(0)
main_circ.cx(qreg_0[0],3)
main_circ.y(1)
main_circ.cx(qreg_0[0],0)
main_circ.u(param_0,param_0,0.331000, 0)
main_circ.cy(0,3)
main_circ.u(param_0,-0.527000,param_0, qreg_0[0])
main_circ.y(qreg_0[0])
main_circ.append(subcirc0,[qreg_0[0],3,2,1])
main_circ.y(3)
main_circ.u(-0.568000,-0.908000,param_0, 0)
main_circ.u(-0.865000,param_0,param_0, 0)
main_circ.cx(1,2)
main_circ.cx(3,2)
main_circ.cy(1,2)
main_circ.cx(0,2)
main_circ.cy(3,2)
main_circ.cx(qreg_0[0],1)
main_circ.append(subcirc0,[1,qreg_0[0],0,3])
main_circ.u(param_0,param_0,param_0, 1)
main_circ.cy(qreg_0[0],2)
main_circ.u(param_0,param_0,param_0, qreg_0[0])
main_circ.u(param_0,param_0,-0.944000, 3)
main_circ.cx(1,2)
main_circ.append(subcirc0,[2,3,0,1])
main_circ.y(2)
main_circ.u(-0.551000,param_0,param_0, 1)
main_circ.cy(1,qreg_0[0])
main_circ.cx(1,0)
bindings = {param_0: 0.970000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "RemoveResetInZeroState")
