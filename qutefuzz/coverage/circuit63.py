
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
    subcirc0.cx(qreg_0[1],qreg_0[2])
    subcirc0.cz(qreg_0[3],qreg_0[1])
    subcirc0.rx(0.568000, qreg_0[1])
    subcirc0.cz(qreg_0[2],qreg_0[3])
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
    subcirc1.rx(0.849000, qreg_0[0])
    subcirc1.ry(0.856000, qreg_2[0])
    subcirc1.ry(0.073000, qreg_0[1])
    subcirc1.ry(0.824000, qreg_3[0])
    
    subcirc2 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(3)
    subcirc2.add_register(qreg_0)
    qreg_3 = QuantumRegister(1)
    subcirc2.add_register(qreg_3)
    # Adding creg resources 
    subcirc2.ry(0.446000, qreg_3[0])
    subcirc2.cx(qreg_0[0],qreg_0[1])
    subcirc2.cx(qreg_0[2],qreg_3[0])
    subcirc2.cx(qreg_0[2],qreg_0[0])
    
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
    
    main_circ.append(subcirc1,[0,2,1,3])
    main_circ.cz(2,3)
    main_circ.ry(param_1, 3)
    main_circ.cz(3,0)
    main_circ.append(subcirc2,[2,3,0,1])
    main_circ.rx(param_0, 1)
    main_circ.ry(param_0, 1)
    main_circ.ry(param_0, 1)
    main_circ.cx(0,2)
    main_circ.ry(param_0, 1)
    main_circ.rx(param_0, 2)
    main_circ.append(subcirc2,[1,0,3,2])
    main_circ.append(subcirc2,[3,2,0,1])
    main_circ.append(subcirc2,[0,2,1,3])
    main_circ.rx(param_0, 3)
    main_circ.rx(param_1, 3)
    main_circ.cx(2,0)
    main_circ.cx(3,1)
    main_circ.cz(1,3)
    main_circ.cx(1,0)
    main_circ.append(subcirc2,[3,2,1,0])
    main_circ.ry(param_1, 1)
    main_circ.cz(1,3)
    main_circ.cz(2,0)
    main_circ.cz(3,2)
    main_circ.append(subcirc2,[3,1,2,0])
    main_circ.ry(0.705000, 1)
    main_circ.cz(3,0)
    main_circ.append(subcirc2,[3,0,1,2])
    main_circ.cx(1,2)
    main_circ.cx(1,3)
    main_circ.rx(-0.385000, 1)
    main_circ.rx(-0.781000, 2)
    bindings = {param_0: 0.647000, param_1: 0.540000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_routing_simulation(main_circ, "63")


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
