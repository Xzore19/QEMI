
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
    subcirc0.u(pi/2,-0.669000,-0.838000, qreg_0[1])
    subcirc0.u(0,0,0.888000, qreg_0[3])
    subcirc0.z(qreg_0[0])
    subcirc0.z(qreg_0[0])
    subcirc0.ry(0.851000, qreg_0[3])
    subcirc0 = subcirc0.to_gate().control(3)
    
    subcirc1 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(2)
    subcirc1.add_register(qreg_0)
    qreg_2 = QuantumRegister(1)
    subcirc1.add_register(qreg_2)
    qreg_3 = QuantumRegister(1)
    subcirc1.add_register(qreg_3)
    # Adding creg resources 
    subcirc1.u(0,0,0.807000, qreg_3[0])
    subcirc1.z(qreg_2[0])
    subcirc1.z(qreg_0[0])
    subcirc1.u(0,0,-0.110000, qreg_0[1])
    subcirc1.u(0,0,0.703000, qreg_2[0])
    
    subcirc2 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(4)
    subcirc2.add_register(qreg_0)
    # Adding creg resources 
    subcirc2.u(pi/2,0.219000,-0.804000, qreg_0[1])
    subcirc2.z(qreg_0[1])
    subcirc2.u(0,0,-0.530000, qreg_0[0])
    subcirc2.u(pi/2,-0.478000,-0.803000, qreg_0[3])
    subcirc2.u(0,0,0.939000, qreg_0[3])
    subcirc2 = subcirc2.to_gate().control(3)
    
    subcirc3 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(4)
    subcirc3.add_register(qreg_0)
    # Adding creg resources 
    subcirc3.u(pi/2,-0.266000,-0.445000, qreg_0[0])
    subcirc3.z(qreg_0[1])
    subcirc3.u(pi/2,0.794000,-0.021000, qreg_0[1])
    subcirc3.u(0,0,-0.974000, qreg_0[0])
    subcirc3.u(0,0,0.312000, qreg_0[3])
    subcirc3 = subcirc3.to_gate().control(1)
    
    main_circ = QuantumCircuit(4)
    # Adding qregs 
    # Adding creg resources 
    creg_0 = ClassicalRegister(2)
    main_circ.add_register(creg_0)
    # Adding symbols 
    param_0 = Parameter("param_0")
    param_1 = Parameter("param_1")
    param_2 = Parameter("param_2")
    
    main_circ.u(0,0,param_1, 1)
    main_circ.z(0)
    main_circ.ry(param_2, 0)
    main_circ.ry(0.409000, 3)
    main_circ.append(subcirc1,[1,3,2,0])
    main_circ.z(2)
    main_circ.ry(param_1, 2)
    main_circ.u(param_0,0.726000,param_1, 1)
    main_circ.u(param_1,-0.411000,param_1, 2)
    main_circ.u(param_0,0,-0.725000, 1)
    main_circ.z(1)
    main_circ.u(pi/2,param_0,param_0, 1)
    main_circ.u(pi/2,param_2,0.559000, 3)
    main_circ.z(1)
    main_circ.ry(param_2, 0)
    main_circ.ry(param_0, 2)
    main_circ.u(0,0,param_1, 1)
    main_circ.append(subcirc1,[1,0,3,2])
    main_circ.z(3)
    main_circ.z(2)
    main_circ.ry(0.929000, 0)
    main_circ.ry(-0.970000, 3)
    main_circ.z(3)
    main_circ.ry(param_1, 1)
    main_circ.z(0)
    main_circ.append(subcirc1,[0,3,1,2])
    main_circ.u(param_0,0,0.412000, 3)
    main_circ.u(param_2,param_1,param_0, 3)
    main_circ.ry(param_0, 2)
    main_circ.u(param_0,param_2,-0.018000, 3)
    main_circ.u(pi/2,0.553000,param_2, 2)
    main_circ.u(pi/2,param_1,param_0, 3)
    main_circ.u(0,0,-0.662000, 0)
    main_circ.u(param_2,param_0,-0.153000, 3)
    main_circ.z(0)
    main_circ.u(0,0,0.281000, 1)
    main_circ.z(2)
    main_circ.u(param_1,param_2,-0.960000, 3)
    main_circ.u(param_1,-0.399000,0.284000, 0)
    main_circ.u(0,0,0.143000, 3)
    main_circ.z(3)
    main_circ.z(2)
    main_circ.ry(-0.957000, 0)
    main_circ.u(pi/2,param_2,-0.554000, 3)
    main_circ.z(2)
    main_circ.ry(param_0, 0)
    main_circ.u(param_2,param_0,-0.449000, 1)
    bindings = {param_0: -0.170000, param_1: -0.044000, param_2: 0.836000, }
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
