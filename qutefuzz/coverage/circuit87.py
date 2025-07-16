
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
    subcirc0.u(-0.109000,-0.771000,-0.734000, qreg_0[3])
    subcirc0.u(0,0,0.583000, qreg_0[0])
    subcirc0.u(0.537000,0.213000,0.991000, qreg_0[0])
    subcirc0.y(qreg_0[2])
    subcirc0.u(-0.881000,-0.843000,-0.505000, qreg_0[3])
    
    subcirc1 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(2)
    subcirc1.add_register(qreg_0)
    qreg_2 = QuantumRegister(1)
    subcirc1.add_register(qreg_2)
    qreg_3 = QuantumRegister(1)
    subcirc1.add_register(qreg_3)
    # Adding creg resources 
    subcirc1.y(qreg_2[0])
    subcirc1.u(0.010000,0.167000,-0.684000, qreg_0[0])
    subcirc1.u(0.338000,-0.409000,-0.585000, qreg_3[0])
    subcirc1.y(qreg_0[1])
    subcirc1.u(0.466000,-0.867000,0.198000, qreg_2[0])
    
    subcirc2 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(4)
    subcirc2.add_register(qreg_0)
    # Adding creg resources 
    subcirc2.u(0,0,-0.972000, qreg_0[2])
    subcirc2.ry(-0.056000, qreg_0[2])
    subcirc2.u(0,0,0.433000, qreg_0[2])
    subcirc2.y(qreg_0[0])
    subcirc2.y(qreg_0[3])
    subcirc2 = subcirc2.to_gate().control(1)
    
    main_circ = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(1)
    main_circ.add_register(qreg_0)
    qreg_1 = QuantumRegister(3)
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
    
    main_circ.ry(param_1, qreg_1[1])
    main_circ.ry(-0.443000, qreg_0[0])
    main_circ.u(param_2,param_0,-0.017000, qreg_0[0])
    main_circ.append(subcirc1,[qreg_1[0],qreg_0[0],qreg_1[1],qreg_1[2]])
    main_circ.append(subcirc1,[qreg_1[2],qreg_1[0],qreg_0[0],qreg_1[1]])
    main_circ.u(0,0,param_2, qreg_0[0])
    main_circ.append(subcirc1,[qreg_1[1],qreg_1[2],qreg_0[0],qreg_1[0]])
    main_circ.u(param_0,0.064000,param_1, qreg_0[0])
    main_circ.append(subcirc1,[qreg_1[1],qreg_1[0],qreg_1[2],qreg_0[0]])
    main_circ.y(qreg_1[0])
    main_circ.u(param_0,param_1,param_0, qreg_1[1])
    main_circ.append(subcirc1,[qreg_1[1],qreg_0[0],qreg_1[2],qreg_1[0]])
    main_circ.u(param_0,param_0,param_2, qreg_1[0])
    main_circ.u(param_1,param_0,param_0, qreg_1[1])
    main_circ.append(subcirc1,[qreg_1[0],qreg_0[0],qreg_1[1],qreg_1[2]])
    main_circ.ry(0.459000, qreg_1[0])
    main_circ.ry(param_0, qreg_1[2])
    main_circ.u(0,0,param_1, qreg_1[0])
    bindings = {param_0: 0.932000, param_1: -0.544000, param_2: 0.218000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_routing_simulation(main_circ, "87")


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
