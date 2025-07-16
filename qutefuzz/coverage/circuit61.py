
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
    subcirc0.x(qreg_0[1])
    subcirc0.ry(0.523000, qreg_0[1])
    subcirc0.u(0.875000,-0.971000,0.328000, qreg_0[0])
    subcirc0.x(qreg_0[3])
    subcirc0.x(qreg_0[3])
    
    main_circ = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(4)
    main_circ.add_register(qreg_0)
    # Adding creg resources 
    creg_0 = ClassicalRegister(2)
    main_circ.add_register(creg_0)
    # Adding symbols 
    param_0 = Parameter("param_0")
    param_1 = Parameter("param_1")
    
    main_circ.ry(param_1, qreg_0[2])
    main_circ.h(qreg_0[3])
    main_circ.ry(param_0, qreg_0[1])
    main_circ.x(qreg_0[0])
    main_circ.h(qreg_0[3])
    main_circ.append(subcirc0,[qreg_0[3],qreg_0[1],qreg_0[2],qreg_0[0]])
    main_circ.ry(0.373000, qreg_0[2])
    main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],qreg_0[0],qreg_0[3]])
    main_circ.x(qreg_0[3])
    main_circ.h(qreg_0[0])
    main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_0[3],qreg_0[2]])
    main_circ.x(qreg_0[1])
    main_circ.x(qreg_0[2])
    main_circ.u(0.510000,0.903000,0.829000, qreg_0[3])
    main_circ.h(qreg_0[0])
    main_circ.append(subcirc0,[qreg_0[3],qreg_0[0],qreg_0[1],qreg_0[2]])
    main_circ.u(0.776000,param_1,param_1, qreg_0[1])
    main_circ.x(qreg_0[2])
    main_circ.ry(param_1, qreg_0[3])
    main_circ.u(param_0,param_0,param_0, qreg_0[0])
    main_circ.x(qreg_0[2])
    main_circ.x(qreg_0[2])
    main_circ.x(qreg_0[1])
    main_circ.ry(0.786000, qreg_0[3])
    main_circ.x(qreg_0[2])
    main_circ.u(param_1,-0.115000,param_0, qreg_0[3])
    main_circ.append(subcirc0,[qreg_0[2],qreg_0[0],qreg_0[3],qreg_0[1]])
    main_circ.h(qreg_0[2])
    main_circ.h(qreg_0[2])
    main_circ.u(-0.962000,-0.305000,-0.542000, qreg_0[2])
    main_circ.x(qreg_0[0])
    main_circ.h(qreg_0[3])
    main_circ.ry(param_0, qreg_0[0])
    main_circ.u(0.856000,param_0,param_0, qreg_0[2])
    main_circ.ry(-0.697000, qreg_0[3])
    main_circ.h(qreg_0[2])
    main_circ.h(qreg_0[0])
    main_circ.u(0.713000,-0.292000,param_1, qreg_0[1])
    main_circ.h(qreg_0[3])
    bindings = {param_0: -0.010000, param_1: 0.892000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_routing_simulation(main_circ, "61")


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
