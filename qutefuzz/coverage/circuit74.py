
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
    subcirc0.rz(0.725000, qreg_3[0])
    subcirc0.rz(0.635000, qreg_1[0])
    subcirc0.h(qreg_0[0])
    subcirc0.z(qreg_2[0])
    subcirc0.z(qreg_1[0])
    subcirc0.z(qreg_1[0])
    
    subcirc1 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(2)
    subcirc1.add_register(qreg_0)
    qreg_2 = QuantumRegister(1)
    subcirc1.add_register(qreg_2)
    qreg_3 = QuantumRegister(1)
    subcirc1.add_register(qreg_3)
    # Adding creg resources 
    subcirc1.rx(-0.557000, qreg_2[0])
    subcirc1.z(qreg_0[0])
    subcirc1.rz(-0.380000, qreg_2[0])
    subcirc1.rx(0.946000, qreg_0[0])
    subcirc1.rz(-0.866000, qreg_0[0])
    subcirc1.h(qreg_2[0])
    subcirc1 = subcirc1.to_gate().control(1)
    
    subcirc2 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(4)
    subcirc2.add_register(qreg_0)
    # Adding creg resources 
    subcirc2.rz(-0.258000, qreg_0[3])
    subcirc2.z(qreg_0[3])
    subcirc2.rz(0.349000, qreg_0[2])
    subcirc2.rx(0.169000, qreg_0[3])
    subcirc2.rx(0.574000, qreg_0[1])
    subcirc2.rz(-0.254000, qreg_0[3])
    
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
    
    main_circ.z(3)
    main_circ.rx(0.998000, 1)
    main_circ.rx(param_5, 1)
    main_circ.h(1)
    main_circ.append(subcirc2,[2,0,1,3])
    main_circ.rz(param_5, 2)
    main_circ.append(subcirc2,[1,0,2,3])
    main_circ.append(subcirc0,[0,1,2,3])
    main_circ.rx(param_2, 0)
    main_circ.h(0)
    main_circ.h(2)
    main_circ.z(2)
    main_circ.z(3)
    main_circ.z(2)
    main_circ.rx(param_2, 1)
    main_circ.rx(param_2, 1)
    main_circ.h(1)
    main_circ.append(subcirc2,[0,1,3,2])
    main_circ.append(subcirc2,[3,0,1,2])
    main_circ.h(3)
    main_circ.append(subcirc2,[1,3,0,2])
    main_circ.h(3)
    main_circ.append(subcirc2,[2,3,1,0])
    bindings = {param_2: 0.877000, param_5: 0.576000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_routing_simulation(main_circ, "74")


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
