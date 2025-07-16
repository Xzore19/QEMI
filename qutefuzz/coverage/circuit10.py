
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
    subcirc0.cx(qreg_0[1],qreg_0[0])
    subcirc0.rx(0.434000, qreg_0[3])
    subcirc0.rx(-0.503000, qreg_0[0])
    subcirc0.h(qreg_0[2])
    subcirc0.cx(qreg_0[1],qreg_0[2])
    subcirc0.cx(qreg_0[1],qreg_0[0])
    subcirc0 = subcirc0.to_gate().control(2)
    
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
    param_1 = Parameter("param_1")
    
    main_circ.h(qreg_2[1])
    main_circ.z(0)
    main_circ.rx(0.219000, qreg_2[0])
    main_circ.cx(qreg_0[0],qreg_0[1])
    main_circ.h(qreg_2[0])
    main_circ.cx(qreg_0[0],0)
    main_circ.z(0)
    main_circ.rx(param_1, qreg_2[0])
    main_circ.z(qreg_2[0])
    main_circ.cx(qreg_2[0],0)
    main_circ.z(qreg_2[1])
    main_circ.rx(-0.661000, qreg_2[1])
    main_circ.cx(qreg_0[1],qreg_2[0])
    main_circ.h(qreg_2[1])
    main_circ.rx(-0.642000, qreg_0[0])
    main_circ.rx(param_0, qreg_0[0])
    main_circ.z(qreg_2[1])
    main_circ.rx(param_1, 0)
    main_circ.rx(-0.526000, qreg_2[0])
    main_circ.z(qreg_0[0])
    main_circ.rx(param_1, qreg_2[0])
    main_circ.rx(-0.541000, qreg_0[0])
    main_circ.h(qreg_2[0])
    main_circ.cx(qreg_0[0],qreg_0[1])
    main_circ.z(qreg_2[1])
    main_circ.cx(qreg_0[0],0)
    main_circ.h(qreg_0[1])
    main_circ.z(qreg_0[0])
    main_circ.rx(param_1, qreg_2[1])
    main_circ.rx(-0.087000, 0)
    main_circ.z(qreg_2[1])
    main_circ.rx(param_1, 0)
    main_circ.cx(qreg_0[0],qreg_2[0])
    main_circ.cx(0,qreg_2[1])
    main_circ.cx(qreg_2[0],qreg_0[0])
    main_circ.cx(qreg_0[0],qreg_0[1])
    main_circ.cx(qreg_2[0],0)
    main_circ.cx(qreg_0[1],0)
    main_circ.cx(0,qreg_0[0])
    main_circ.z(qreg_0[0])
    main_circ.rx(0.464000, qreg_0[1])
    main_circ.rx(param_1, qreg_0[0])
    main_circ.z(qreg_2[0])
    main_circ.z(qreg_0[1])
    main_circ.rx(-0.839000, 0)
    bindings = {param_0: 0.206000, param_1: 0.379000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    compare_statevectors(main_circ, "CollectMultiQBlocks")


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
