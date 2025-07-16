
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi


def main():
    
    subcirc0 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(4)
    subcirc0.add_register(qreg_0)
    # Adding creg resources 
    subcirc0.h(qreg_0[1])
    subcirc0.u(0,0,0.901000, qreg_0[2])
    subcirc0.ry(-0.661000, qreg_0[2])
    subcirc0.u(0,0,0.343000, qreg_0[2])
    
    subcirc1 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(2)
    subcirc1.add_register(qreg_0)
    qreg_2 = QuantumRegister(2)
    subcirc1.add_register(qreg_2)
    # Adding creg resources 
    subcirc1.h(qreg_2[0])
    subcirc1.ry(0.736000, qreg_0[1])
    subcirc1.h(qreg_0[1])
    subcirc1.rz(-0.488000, qreg_2[1])
    
    subcirc2 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(3)
    subcirc2.add_register(qreg_0)
    qreg_3 = QuantumRegister(1)
    subcirc2.add_register(qreg_3)
    # Adding creg resources 
    subcirc2.rz(-0.256000, qreg_0[1])
    subcirc2.rz(-0.627000, qreg_0[1])
    subcirc2.ry(-0.130000, qreg_3[0])
    subcirc2.ry(-0.533000, qreg_0[1])
    
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
    param_4 = Parameter("param_4")
    
    main_circ.h(0)
    main_circ.ry(-0.482000, 1)
    main_circ.ry(param_0, 3)
    main_circ.append(subcirc2,[2,1,0,3])
    main_circ.u(param_3,0,0.461000, 0)
    main_circ.append(subcirc2,[1,2,3,0])
    main_circ.u(0,0,param_2, 1)
    main_circ.append(subcirc1,[1,0,2,3])
    main_circ.h(3)
    main_circ.h(3)
    main_circ.append(subcirc2,[1,3,2,0])
    main_circ.ry(0.082000, 2)
    main_circ.rz(param_2, 1)
    main_circ.append(subcirc2,[2,0,3,1])
    main_circ.append(subcirc1,[2,0,1,3])
    main_circ.append(subcirc2,[2,0,3,1])
    main_circ.ry(param_3, 2)
    main_circ.ry(param_0, 0)
    main_circ.append(subcirc2,[2,0,1,3])
    main_circ.rz(-0.340000, 3)
    main_circ.append(subcirc2,[2,3,0,1])
    main_circ.append(subcirc0,[0,1,3,2])
    main_circ.rz(-0.267000, 3)
    bindings = {param_0: -0.712000, param_2: 0.785000, param_3: 0.716000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    compare_statevectors(main_circ, "ElidePermutations")


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
