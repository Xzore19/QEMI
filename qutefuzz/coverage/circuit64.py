
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi


def main():
    
    subcirc0 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(2)
    subcirc0.add_register(qreg_0)
    qreg_2 = QuantumRegister(1)
    subcirc0.add_register(qreg_2)
    qreg_3 = QuantumRegister(1)
    subcirc0.add_register(qreg_3)
    # Adding creg resources 
    subcirc0.rx(-0.076000, qreg_3[0])
    subcirc0.rx(0.997000, qreg_3[0])
    subcirc0.rz(-0.070000, qreg_0[0])
    subcirc0.u(0,0,0.101000, qreg_0[0])
    subcirc0.u(0,0,0.124000, qreg_2[0])
    subcirc0.y(qreg_2[0])
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
    param_3 = Parameter("param_3")
    param_4 = Parameter("param_4")
    param_5 = Parameter("param_5")
    param_6 = Parameter("param_6")
    param_7 = Parameter("param_7")
    
    main_circ.y(2)
    main_circ.u(param_3,param_2,param_4, 3)
    main_circ.y(3)
    main_circ.y(2)
    main_circ.rx(-0.149000, 3)
    main_circ.u(param_2,param_4,0.569000, 3)
    main_circ.rx(0.830000, 0)
    main_circ.rz(param_2, 0)
    main_circ.rz(0.086000, 1)
    main_circ.y(3)
    main_circ.u(param_7,0,-0.862000, 1)
    main_circ.u(0,param_2,param_4, 2)
    main_circ.rz(param_6, 0)
    main_circ.u(param_0,0,0.534000, 1)
    main_circ.y(0)
    main_circ.y(1)
    main_circ.rx(param_0, 1)
    main_circ.u(0,param_1,param_6, 0)
    main_circ.u(0,0,-0.995000, 2)
    main_circ.u(param_3,0,param_7, 2)
    main_circ.y(3)
    main_circ.u(param_6,param_0,param_6, 3)
    main_circ.u(0,0,param_1, 0)
    main_circ.y(0)
    main_circ.u(param_5,0,param_3, 3)
    main_circ.rz(0.532000, 2)
    main_circ.rz(-0.970000, 3)
    main_circ.rx(0.473000, 3)
    main_circ.y(1)
    main_circ.rx(param_3, 0)
    main_circ.rz(param_1, 2)
    main_circ.rz(param_3, 2)
    main_circ.u(param_4,param_4,-0.725000, 0)
    main_circ.rz(-0.330000, 1)
    main_circ.rz(param_7, 0)
    main_circ.rz(0.529000, 0)
    main_circ.rz(0.421000, 0)
    main_circ.rz(-0.008000, 0)
    main_circ.rz(0.107000, 0)
    main_circ.y(3)
    main_circ.rz(-0.925000, 1)
    main_circ.rx(param_2, 3)
    main_circ.rx(0.094000, 1)
    main_circ.rz(param_3, 1)
    main_circ.u(0,param_6,param_0, 3)
    main_circ.u(param_4,0,0.746000, 2)
    main_circ.rz(param_4, 0)
    main_circ.u(0,param_7,0.652000, 1)
    main_circ.y(3)
    main_circ.u(param_3,param_1,param_7, 2)
    main_circ.u(param_1,param_0,param_3, 1)
    main_circ.u(0,param_5,-0.477000, 1)
    main_circ.y(1)
    main_circ.y(3)
    main_circ.rz(-0.542000, 2)
    bindings = {param_0: -0.715000, param_1: 0.892000, param_2: -0.116000, param_3: 0.480000, param_4: -0.106000, param_5: 0.907000, param_6: -0.380000, param_7: 0.033000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_routing_simulation(main_circ, "64")


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
