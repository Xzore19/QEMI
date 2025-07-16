
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
    subcirc0.cz(qreg_0[0],qreg_0[1])
    subcirc0.y(qreg_3[0])
    subcirc0.cz(qreg_0[2],qreg_0[0])
    subcirc0.rx(0.518000, qreg_0[1])
    subcirc0.cz(qreg_0[0],qreg_3[0])
    
    subcirc1 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(3)
    subcirc1.add_register(qreg_0)
    qreg_3 = QuantumRegister(1)
    subcirc1.add_register(qreg_3)
    # Adding creg resources 
    subcirc1.y(qreg_0[2])
    subcirc1.s(qreg_3[0])
    subcirc1.y(qreg_0[0])
    subcirc1.y(qreg_0[1])
    subcirc1.s(qreg_0[1])
    
    subcirc2 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(3)
    subcirc2.add_register(qreg_0)
    qreg_3 = QuantumRegister(1)
    subcirc2.add_register(qreg_3)
    # Adding creg resources 
    subcirc2.rx(-0.387000, qreg_0[2])
    subcirc2.y(qreg_3[0])
    subcirc2.s(qreg_0[2])
    subcirc2.cz(qreg_0[1],qreg_3[0])
    subcirc2.rx(-0.509000, qreg_0[2])
    subcirc2 = subcirc2.to_gate().control(2)
    
    subcirc3 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(1)
    subcirc3.add_register(qreg_0)
    qreg_1 = QuantumRegister(1)
    subcirc3.add_register(qreg_1)
    qreg_2 = QuantumRegister(2)
    subcirc3.add_register(qreg_2)
    # Adding creg resources 
    subcirc3.s(qreg_1[0])
    subcirc3.rx(0.620000, qreg_2[1])
    subcirc3.rx(-0.709000, qreg_2[0])
    subcirc3.y(qreg_2[0])
    subcirc3.y(qreg_1[0])
    subcirc3 = subcirc3.to_gate().control(2)
    
    main_circ = QuantumCircuit(2)
    # Adding qregs 
    qreg_0 = QuantumRegister(2)
    main_circ.add_register(qreg_0)
    qreg_2 = QuantumRegister(1)
    main_circ.add_register(qreg_2)
    qreg_3 = QuantumRegister(1)
    main_circ.add_register(qreg_3)
    # Adding creg resources 
    creg_0 = ClassicalRegister(1)
    main_circ.add_register(creg_0)
    creg_1 = ClassicalRegister(1)
    main_circ.add_register(creg_1)
    # Adding symbols 
    param_0 = Parameter("param_0")
    param_1 = Parameter("param_1")
    param_2 = Parameter("param_2")
    
    main_circ.append(subcirc3,[qreg_0[0],0,1,qreg_2[0],qreg_0[1],qreg_3[0]])
    main_circ.append(subcirc0,[qreg_2[0],1,qreg_0[0],qreg_0[1]])
    main_circ.y(1)
    main_circ.append(subcirc0,[qreg_2[0],1,qreg_3[0],qreg_0[0]])
    main_circ.cz(qreg_0[1],qreg_2[0])
    main_circ.append(subcirc0,[0,qreg_2[0],qreg_0[0],qreg_0[1]])
    main_circ.s(qreg_0[1])
    main_circ.cz(qreg_0[0],0)
    main_circ.append(subcirc2,[1,0,qreg_3[0],qreg_0[0],qreg_2[0],qreg_0[1]])
    main_circ.s(qreg_2[0])
    main_circ.append(subcirc3,[qreg_0[0],1,qreg_0[1],qreg_2[0],qreg_3[0],0])
    main_circ.cz(qreg_3[0],0)
    main_circ.cz(1,qreg_2[0])
    main_circ.s(qreg_0[1])
    main_circ.cz(qreg_0[1],0)
    main_circ.append(subcirc3,[qreg_0[1],1,qreg_2[0],qreg_3[0],0,qreg_0[0]])
    main_circ.rx(param_1, qreg_3[0])
    main_circ.rx(0.563000, qreg_0[1])
    main_circ.s(qreg_0[1])
    main_circ.cz(0,qreg_0[0])
    bindings = {param_1: -0.182000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_routing_simulation(main_circ, "26")


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
