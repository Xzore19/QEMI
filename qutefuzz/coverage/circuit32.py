
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
    subcirc0.rx(-0.414000, qreg_1[0])
    subcirc0.cx(qreg_0[0],qreg_1[1])
    subcirc0.cx(qreg_1[2],qreg_1[0])
    subcirc0.cy(qreg_1[0],qreg_1[2])
    subcirc0.cy(qreg_0[0],qreg_1[1])
    subcirc0 = subcirc0.to_gate().control(3)
    
    main_circ = QuantumCircuit(4)
    # Adding qregs 
    # Adding creg resources 
    creg_0 = ClassicalRegister(2)
    main_circ.add_register(creg_0)
    # Adding symbols 
    param_0 = Parameter("param_0")
    param_1 = Parameter("param_1")
    
    main_circ.rx(param_0, 2)
    main_circ.cx(3,2)
    main_circ.cy(3,0)
    main_circ.u(0.205000,param_0,-0.188000, 3)
    main_circ.cy(3,2)
    main_circ.cx(1,2)
    main_circ.rx(-0.663000, 3)
    main_circ.cx(3,2)
    main_circ.u(-0.580000,param_0,-0.969000, 2)
    main_circ.rx(param_1, 1)
    main_circ.cx(2,1)
    main_circ.u(param_1,param_1,0.036000, 2)
    main_circ.u(0.276000,param_1,0.844000, 3)
    main_circ.rx(param_0, 2)
    main_circ.cx(3,0)
    main_circ.cy(2,0)
    main_circ.u(param_0,-0.011000,0.159000, 2)
    main_circ.u(-0.619000,0.254000,-0.196000, 2)
    main_circ.cy(2,3)
    main_circ.cx(0,3)
    main_circ.cy(2,3)
    main_circ.cx(0,1)
    main_circ.cy(3,0)
    main_circ.u(param_0,param_1,0.779000, 3)
    main_circ.rx(param_1, 0)
    main_circ.rx(param_0, 2)
    main_circ.u(param_1,param_1,param_0, 0)
    main_circ.u(0.897000,0.399000,-0.523000, 1)
    main_circ.cy(2,1)
    main_circ.cy(0,1)
    main_circ.cx(0,2)
    main_circ.rx(param_0, 2)
    main_circ.u(0.274000,param_1,param_0, 0)
    main_circ.cy(0,1)
    main_circ.u(-0.667000,0.140000,-0.573000, 1)
    main_circ.cy(1,0)
    main_circ.cx(3,2)
    main_circ.u(-0.787000,param_0,0.194000, 1)
    main_circ.u(-0.277000,-0.595000,param_0, 3)
    main_circ.cy(1,3)
    main_circ.cx(2,0)
    main_circ.cx(2,0)
    main_circ.cy(3,1)
    main_circ.cy(0,3)
    main_circ.rx(param_0, 0)
    main_circ.cx(3,0)
    main_circ.cy(1,0)
    main_circ.cy(1,3)
    main_circ.rx(0.775000, 1)
    main_circ.cx(2,0)
    main_circ.cy(0,1)
    main_circ.cx(2,3)
    main_circ.cy(1,0)
    main_circ.rx(-0.599000, 1)
    bindings = {param_0: 0.083000, param_1: 0.340000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_routing_simulation(main_circ, "32")


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
