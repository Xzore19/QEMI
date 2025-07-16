from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi

subcirc0 = QuantumCircuit(0)
# Adding qregs 
qreg_0 = QuantumRegister(2)
subcirc0.add_register(qreg_0)
qreg_2 = QuantumRegister(1)
subcirc0.add_register(qreg_2)
qreg_3 = QuantumRegister(1)
subcirc0.add_register(qreg_3)
# Adding creg resources 
subcirc0.rx(0.868000, qreg_0[0])
subcirc0.u(0.698000,-0.336000,-0.915000, qreg_3[0])
subcirc0.rx(0.304000, qreg_2[0])
subcirc0.rx(-0.731000, qreg_2[0])
subcirc0 = subcirc0.to_gate().control(2)

main_circ = QuantumCircuit(4)
# Adding qregs 
qreg_0 = QuantumRegister(2)
main_circ.add_register(qreg_0)
# Adding creg resources 
creg_0 = ClassicalRegister(2)
main_circ.add_register(creg_0)
# Adding symbols 
param_0 = Parameter("param_0")

main_circ.y(0)
main_circ.rx(0.977000, 1)
main_circ.append(subcirc0,[qreg_0[0],1,0,2,qreg_0[1],3])
main_circ.y(1)
main_circ.y(3)
main_circ.u(0,param_0,param_0, 2)
main_circ.u(0,param_0,0.412000, 1)
main_circ.u(param_0,param_0,param_0, qreg_0[0])
main_circ.u(param_0,0.791000,0.646000, 2)
main_circ.u(0,0,0.578000, 0)
main_circ.u(0.828000,param_0,0.871000, 0)
main_circ.append(subcirc0,[2,qreg_0[1],0,qreg_0[0],1,3])
main_circ.u(-0.814000,-0.592000,param_0, 0)
main_circ.append(subcirc0,[2,3,qreg_0[1],qreg_0[0],1,0])
main_circ.u(-0.875000,param_0,0.069000, qreg_0[1])
main_circ.rx(0.122000, qreg_0[1])
main_circ.rx(-0.640000, 0)
main_circ.append(subcirc0,[qreg_0[1],qreg_0[0],3,1,0,2])
main_circ.rx(-0.571000, qreg_0[1])
main_circ.u(0.409000,-0.321000,-0.964000, 3)
main_circ.u(0.894000,-0.085000,param_0, 3)
main_circ.y(0)
main_circ.u(param_0,param_0,-0.788000, 1)
main_circ.u(param_0,param_0,param_0, 3)
main_circ.u(0.537000,0.433000,param_0, 3)
main_circ.u(-0.739000,param_0,-0.250000, 1)
main_circ.u(0.466000,0.641000,param_0, 2)
main_circ.rx(param_0, 2)
main_circ.u(0.516000,param_0,0.795000, 3)
main_circ.y(3)
main_circ.append(subcirc0,[1,qreg_0[0],qreg_0[1],3,0,2])
main_circ.u(-0.072000,-0.160000,-0.478000, qreg_0[1])
main_circ.u(param_0,-0.617000,0.105000, 1)
main_circ.rx(param_0, 1)
main_circ.y(qreg_0[1])
main_circ.u(param_0,0,0.059000, qreg_0[0])
main_circ.rx(-0.235000, qreg_0[1])
main_circ.append(subcirc0,[0,3,1,qreg_0[0],qreg_0[1],2])
main_circ.u(0,param_0,-0.841000, 0)
main_circ.u(-0.686000,-0.683000,-0.901000, 2)
bindings = {param_0: 0.945000, }
main_circ = main_circ.assign_parameters(bindings)

print(Path(__file__).name, " results:")
compare_statevectors(main_circ, "CollectMultiQBlocks")
