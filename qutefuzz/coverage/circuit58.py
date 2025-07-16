
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
    subcirc0.rz(-0.067000, qreg_3[0])
    subcirc0.s(qreg_3[0])
    subcirc0.rz(0.959000, qreg_3[0])
    subcirc0.u(0.902000,-0.381000,-0.797000, qreg_0[1])
    subcirc0.u(-0.031000,0.599000,-0.780000, qreg_0[2])
    subcirc0.s(qreg_0[0])
    
    subcirc1 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(1)
    subcirc1.add_register(qreg_0)
    qreg_1 = QuantumRegister(2)
    subcirc1.add_register(qreg_1)
    qreg_3 = QuantumRegister(1)
    subcirc1.add_register(qreg_3)
    # Adding creg resources 
    subcirc1.s(qreg_3[0])
    subcirc1.h(qreg_0[0])
    subcirc1.u(0.427000,0.125000,0.934000, qreg_3[0])
    subcirc1.rz(-0.624000, qreg_1[1])
    subcirc1.rz(0.107000, qreg_0[0])
    subcirc1.h(qreg_3[0])
    subcirc1 = subcirc1.to_gate().control(1)
    
    subcirc2 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(1)
    subcirc2.add_register(qreg_0)
    qreg_1 = QuantumRegister(2)
    subcirc2.add_register(qreg_1)
    qreg_3 = QuantumRegister(1)
    subcirc2.add_register(qreg_3)
    # Adding creg resources 
    subcirc2.u(-0.046000,0.703000,-0.108000, qreg_0[0])
    subcirc2.s(qreg_1[0])
    subcirc2.u(-0.485000,0.374000,0.340000, qreg_0[0])
    subcirc2.rz(-0.585000, qreg_1[0])
    subcirc2.rz(-0.931000, qreg_1[0])
    subcirc2.h(qreg_0[0])
    
    subcirc3 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(3)
    subcirc3.add_register(qreg_0)
    qreg_3 = QuantumRegister(1)
    subcirc3.add_register(qreg_3)
    # Adding creg resources 
    subcirc3.rz(0.703000, qreg_0[2])
    subcirc3.u(-0.175000,0.574000,0.034000, qreg_0[0])
    subcirc3.s(qreg_0[0])
    subcirc3.rz(0.619000, qreg_0[0])
    subcirc3.u(-0.256000,0.241000,0.651000, qreg_0[1])
    subcirc3.h(qreg_3[0])
    
    subcirc4 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(2)
    subcirc4.add_register(qreg_0)
    qreg_2 = QuantumRegister(1)
    subcirc4.add_register(qreg_2)
    qreg_3 = QuantumRegister(1)
    subcirc4.add_register(qreg_3)
    # Adding creg resources 
    subcirc4.u(-0.061000,-0.094000,-0.544000, qreg_2[0])
    subcirc4.s(qreg_0[0])
    subcirc4.s(qreg_3[0])
    subcirc4.rz(0.704000, qreg_0[0])
    subcirc4.h(qreg_3[0])
    subcirc4.h(qreg_0[1])
    
    main_circ = QuantumCircuit(4)
    # Adding qregs 
    qreg_0 = QuantumRegister(1)
    main_circ.add_register(qreg_0)
    qreg_1 = QuantumRegister(1)
    main_circ.add_register(qreg_1)
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
    
    main_circ.rz(-0.451000, qreg_0[0])
    main_circ.append(subcirc4,[3,qreg_1[0],qreg_0[0],0])
    main_circ.u(-0.434000,param_1,-0.948000, 1)
    main_circ.append(subcirc1,[1,qreg_0[0],3,0,2])
    main_circ.append(subcirc2,[1,2,qreg_0[0],0])
    main_circ.append(subcirc0,[1,0,3,qreg_0[0]])
    main_circ.append(subcirc0,[qreg_0[0],0,qreg_1[0],2])
    main_circ.append(subcirc0,[qreg_1[0],3,1,2])
    main_circ.u(-0.624000,0.580000,0.544000, 1)
    main_circ.s(2)
    main_circ.append(subcirc3,[qreg_1[0],qreg_0[0],2,3])
    main_circ.append(subcirc4,[1,0,2,3])
    main_circ.rz(0.466000, 0)
    main_circ.rz(param_0, qreg_1[0])
    bindings = {param_0: -0.343000, param_1: -0.765000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_routing_simulation(main_circ, "58")


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
