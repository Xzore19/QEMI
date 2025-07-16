
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
    qreg_1 = QuantumRegister(3)
    subcirc0.add_register(qreg_1)
    # Adding creg resources 
    subcirc0.rx(0.395000, qreg_0[0])
    subcirc0.rz(-0.011000, qreg_1[1])
    subcirc0.rx(0.243000, qreg_0[0])
    subcirc0.ry(-0.688000, qreg_1[1])
    subcirc0.ry(-0.759000, qreg_1[0])
    subcirc0.rz(-0.289000, qreg_1[1])
    subcirc0 = subcirc0.to_gate().control(2)
    
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
    
    main_circ.ry(param_1, 1)
    main_circ.ry(param_2, 2)
    main_circ.rz(param_2, 1)
    main_circ.u(param_2,param_1,-0.368000, 1)
    main_circ.u(0,0,0.509000, 2)
    main_circ.rz(param_0, 1)
    main_circ.rz(0.353000, 3)
    main_circ.ry(param_0, 1)
    main_circ.rx(param_2, 1)
    main_circ.u(param_2,param_2,param_2, 2)
    main_circ.rx(param_0, 1)
    main_circ.rz(param_2, 2)
    main_circ.rz(0.283000, 2)
    main_circ.u(0,0,-0.171000, 1)
    main_circ.rx(-0.608000, 2)
    main_circ.u(param_0,param_2,param_2, 1)
    main_circ.rz(param_1, 2)
    main_circ.rx(param_2, 0)
    main_circ.rz(param_2, 3)
    main_circ.u(param_1,param_2,param_1, 0)
    main_circ.rx(param_2, 1)
    main_circ.rx(-0.482000, 2)
    main_circ.rz(0.198000, 3)
    main_circ.ry(-0.194000, 1)
    main_circ.u(param_0,param_2,param_0, 2)
    main_circ.rx(param_0, 0)
    main_circ.u(param_0,0,0.102000, 0)
    main_circ.rx(param_1, 1)
    main_circ.rz(param_2, 1)
    main_circ.ry(0.125000, 2)
    main_circ.ry(-0.200000, 2)
    main_circ.ry(0.128000, 3)
    main_circ.rz(0.310000, 0)
    main_circ.rx(-0.375000, 1)
    main_circ.rz(param_0, 3)
    main_circ.u(param_0,param_1,param_2, 2)
    main_circ.rz(param_1, 1)
    main_circ.ry(param_0, 3)
    main_circ.rx(0.657000, 3)
    main_circ.rx(param_2, 2)
    main_circ.ry(param_0, 2)
    main_circ.ry(param_1, 3)
    main_circ.rx(param_2, 1)
    main_circ.rz(-0.496000, 0)
    main_circ.ry(param_2, 3)
    main_circ.ry(0.150000, 2)
    main_circ.rx(param_2, 3)
    main_circ.rx(-0.745000, 1)
    main_circ.u(param_0,0,-0.840000, 1)
    main_circ.u(0,0,param_1, 0)
    main_circ.ry(-0.802000, 1)
    main_circ.rx(param_2, 0)
    main_circ.rx(-0.552000, 1)
    main_circ.ry(param_0, 2)
    main_circ.rx(param_1, 1)
    main_circ.rx(param_1, 0)
    main_circ.rx(0.652000, 3)
    main_circ.rx(param_1, 3)
    bindings = {param_0: -0.991000, param_1: 0.352000, param_2: -0.856000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    compare_statevectors(main_circ, "Collect1qRuns")


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
