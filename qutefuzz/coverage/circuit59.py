
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
    subcirc0.cz(qreg_3[0],qreg_0[1])
    subcirc0.ry(0.187000, qreg_0[0])
    subcirc0.ry(0.175000, qreg_0[2])
    subcirc0.cz(qreg_0[2],qreg_0[1])
    subcirc0.ry(-0.625000, qreg_0[1])
    subcirc0.cz(qreg_3[0],qreg_0[1])
    subcirc0 = subcirc0.to_gate().control(1)
    
    subcirc1 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(3)
    subcirc1.add_register(qreg_0)
    qreg_3 = QuantumRegister(1)
    subcirc1.add_register(qreg_3)
    # Adding creg resources 
    subcirc1.cz(qreg_3[0],qreg_0[2])
    subcirc1.ry(-0.269000, qreg_3[0])
    subcirc1.cy(qreg_0[2],qreg_0[1])
    subcirc1.ry(0.433000, qreg_0[1])
    subcirc1.u(0.854000,0.523000,0.821000, qreg_0[2])
    subcirc1.cz(qreg_3[0],qreg_0[1])
    subcirc1 = subcirc1.to_gate().control(2)
    
    subcirc2 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(1)
    subcirc2.add_register(qreg_0)
    qreg_1 = QuantumRegister(1)
    subcirc2.add_register(qreg_1)
    qreg_2 = QuantumRegister(2)
    subcirc2.add_register(qreg_2)
    # Adding creg resources 
    subcirc2.cy(qreg_1[0],qreg_2[0])
    subcirc2.cy(qreg_2[1],qreg_0[0])
    subcirc2.ry(0.010000, qreg_0[0])
    subcirc2.cz(qreg_2[0],qreg_0[0])
    subcirc2.cz(qreg_0[0],qreg_1[0])
    subcirc2.ry(0.943000, qreg_0[0])
    subcirc2 = subcirc2.to_gate().control(3)
    
    main_circ = QuantumCircuit(4)
    # Adding qregs 
    # Adding creg resources 
    creg_0 = ClassicalRegister(2)
    main_circ.add_register(creg_0)
    # Adding symbols 
    param_0 = Parameter("param_0")
    
    main_circ.cz(2,1)
    main_circ.u(param_0,-0.905000,0.124000, 1)
    main_circ.cz(0,3)
    main_circ.u(param_0,param_0,-0.866000, 1)
    main_circ.cy(3,2)
    main_circ.cy(0,1)
    main_circ.u(-0.746000,-0.731000,0.061000, 0)
    main_circ.ry(-0.040000, 3)
    main_circ.u(param_0,param_0,param_0, 1)
    main_circ.cy(0,1)
    main_circ.ry(param_0, 2)
    main_circ.ry(param_0, 1)
    main_circ.u(0.974000,param_0,param_0, 3)
    main_circ.cz(3,0)
    main_circ.ry(0.789000, 0)
    main_circ.u(param_0,0.019000,-0.163000, 0)
    main_circ.u(param_0,param_0,-0.830000, 1)
    main_circ.ry(0.580000, 1)
    main_circ.ry(param_0, 3)
    main_circ.cz(3,2)
    main_circ.cz(1,0)
    main_circ.ry(-0.548000, 2)
    main_circ.u(-0.833000,param_0,param_0, 2)
    main_circ.cy(3,2)
    main_circ.cy(3,1)
    main_circ.ry(-0.711000, 0)
    main_circ.cz(3,1)
    main_circ.ry(param_0, 3)
    main_circ.u(0.366000,param_0,0.723000, 2)
    main_circ.cy(0,2)
    main_circ.cz(0,2)
    main_circ.cy(1,0)
    main_circ.cz(3,0)
    main_circ.u(0.867000,0.997000,param_0, 0)
    main_circ.u(-0.667000,param_0,param_0, 1)
    main_circ.u(param_0,param_0,-0.075000, 0)
    main_circ.cz(3,2)
    main_circ.cz(3,2)
    main_circ.cy(0,2)
    main_circ.u(param_0,-0.524000,0.931000, 2)
    main_circ.cy(1,0)
    bindings = {param_0: -0.280000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_routing_simulation(main_circ, "59")


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
