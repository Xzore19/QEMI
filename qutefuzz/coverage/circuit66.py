
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi


def main():
    
    subcirc0 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(1)
    subcirc0.add_register(qreg_0)
    qreg_1 = QuantumRegister(1)
    subcirc0.add_register(qreg_1)
    qreg_2 = QuantumRegister(1)
    subcirc0.add_register(qreg_2)
    qreg_3 = QuantumRegister(1)
    subcirc0.add_register(qreg_3)
    # Adding creg resources 
    subcirc0.ry(-0.494000, qreg_1[0])
    subcirc0.rz(-0.323000, qreg_1[0])
    subcirc0.u(-0.421000,0.434000,0.140000, qreg_1[0])
    subcirc0.u(-0.507000,0.347000,-0.551000, qreg_0[0])
    subcirc0.u(0.693000,-0.192000,0.035000, qreg_2[0])
    
    subcirc1 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(4)
    subcirc1.add_register(qreg_0)
    # Adding creg resources 
    subcirc1.rz(0.793000, qreg_0[1])
    subcirc1.z(qreg_0[3])
    subcirc1.ry(-0.290000, qreg_0[1])
    subcirc1.z(qreg_0[3])
    subcirc1.z(qreg_0[0])
    
    main_circ = QuantumCircuit(4)
    # Adding qregs 
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
    
    main_circ.rz(param_2, 3)
    main_circ.rz(param_2, 0)
    main_circ.append(subcirc1,[3,1,0,2])
    main_circ.z(0)
    main_circ.rz(0.654000, 3)
    main_circ.append(subcirc1,[1,3,2,0])
    main_circ.z(1)
    main_circ.append(subcirc0,[1,0,3,2])
    main_circ.u(0.958000,param_1,-0.215000, 3)
    main_circ.rz(param_3, 1)
    main_circ.u(-0.421000,-0.914000,0.255000, 3)
    main_circ.rz(-0.297000, 0)
    main_circ.append(subcirc0,[3,1,2,0])
    main_circ.u(param_0,-0.143000,-0.222000, 3)
    main_circ.rz(-0.511000, 3)
    main_circ.z(2)
    main_circ.u(0.105000,0.775000,0.953000, 0)
    main_circ.u(-0.514000,0.434000,param_2, 1)
    main_circ.append(subcirc0,[1,3,0,2])
    main_circ.rz(param_2, 0)
    main_circ.append(subcirc0,[2,3,1,0])
    main_circ.u(0.104000,-0.400000,param_3, 1)
    main_circ.ry(param_2, 0)
    bindings = {param_0: -0.963000, param_1: 0.389000, param_2: 0.208000, param_3: -0.749000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    compare_statevectors(main_circ, "ConsolidateBlocks")


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
