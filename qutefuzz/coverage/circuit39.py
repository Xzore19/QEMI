
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi


def main():
    
    subcirc0 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(3)
    subcirc0.add_register(qreg_0)
    qreg_3 = QuantumRegister(1)
    subcirc0.add_register(qreg_3)
    # Adding creg resources 
    subcirc0.u(0.698000,0.947000,-0.581000, qreg_0[2])
    subcirc0.u(0.900000,0.037000,0.163000, qreg_0[1])
    subcirc0.cx(qreg_0[1],qreg_0[0])
    subcirc0.cx(qreg_0[1],qreg_0[0])
    subcirc0.cz(qreg_0[1],qreg_0[0])
    subcirc0.u(pi/2,-0.438000,0.157000, qreg_0[1])
    
    main_circ = QuantumCircuit(4)
    # Adding qregs 
    qreg_0 = QuantumRegister(1)
    main_circ.add_register(qreg_0)
    # Adding creg resources 
    creg_0 = ClassicalRegister(1)
    main_circ.add_register(creg_0)
    creg_1 = ClassicalRegister(1)
    main_circ.add_register(creg_1)
    # Adding symbols 
    param_0 = Parameter("param_0")
    param_1 = Parameter("param_1")
    param_2 = Parameter("param_2")
    param_3 = Parameter("param_3")
    
    main_circ.append(subcirc0,[1,3,qreg_0[0],0])
    main_circ.u(-0.536000,-0.482000,-0.651000, 3)
    main_circ.append(subcirc0,[0,qreg_0[0],3,1])
    main_circ.cz(0,1)
    main_circ.u(pi/2,param_1,param_1, qreg_0[0])
    main_circ.u(0.300000,param_2,param_2, 0)
    main_circ.u(param_0,0.435000,param_1, qreg_0[0])
    main_circ.cz(qreg_0[0],2)
    main_circ.append(subcirc0,[qreg_0[0],0,2,3])
    main_circ.append(subcirc0,[0,qreg_0[0],2,3])
    main_circ.append(subcirc0,[0,qreg_0[0],3,2])
    main_circ.cx(qreg_0[0],3)
    main_circ.cz(1,3)
    main_circ.u(0.452000,param_3,0.780000, 1)
    main_circ.u(param_1,0.531000,param_1, qreg_0[0])
    main_circ.u(param_2,0.864000,param_2, 0)
    main_circ.cx(0,3)
    main_circ.u(param_2,0.754000,-0.505000, 2)
    main_circ.u(param_2,0.177000,param_2, 1)
    main_circ.u(pi/2,param_3,param_2, 3)
    main_circ.u(param_0,0.374000,param_2, 3)
    main_circ.u(-0.860000,0.831000,param_2, 2)
    main_circ.cx(3,1)
    main_circ.u(param_2,param_2,param_1, 2)
    main_circ.cz(3,0)
    main_circ.cz(0,2)
    bindings = {param_0: -0.431000, param_1: -0.013000, param_2: -0.109000, param_3: 0.385000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    compare_statevectors(main_circ, "RemoveFinalReset")


if __name__ == "__main__":
    from coverage import Coverage

    cov = Coverage(
        source=["qiskit"],
        branch=False,
        data_suffix=True
    )
    cov.start()

    main()

    cov.stop()
    cov.save()
    cov.combine()
    cov.report()
