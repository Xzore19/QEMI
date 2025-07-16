
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
    qreg_2 = QuantumRegister(2)
    subcirc0.add_register(qreg_2)
    # Adding creg resources 
    subcirc0.rz(0.535000, qreg_2[0])
    subcirc0.u(0.887000,-0.818000,-0.107000, qreg_0[0])
    subcirc0.rz(-0.892000, qreg_2[1])
    subcirc0.rz(-0.236000, qreg_2[0])
    subcirc0.cy(qreg_2[1],qreg_0[1])
    subcirc0 = subcirc0.to_gate().control(3)
    
    subcirc1 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(1)
    subcirc1.add_register(qreg_0)
    qreg_1 = QuantumRegister(2)
    subcirc1.add_register(qreg_1)
    qreg_3 = QuantumRegister(1)
    subcirc1.add_register(qreg_3)
    # Adding creg resources 
    subcirc1.x(qreg_1[1])
    subcirc1.cy(qreg_0[0],qreg_1[1])
    subcirc1.u(-0.766000,0.088000,-0.186000, qreg_1[1])
    subcirc1.u(-0.704000,-0.406000,0.427000, qreg_1[1])
    subcirc1.cy(qreg_3[0],qreg_1[1])
    
    subcirc2 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(1)
    subcirc2.add_register(qreg_0)
    qreg_1 = QuantumRegister(3)
    subcirc2.add_register(qreg_1)
    # Adding creg resources 
    subcirc2.cy(qreg_1[1],qreg_0[0])
    subcirc2.rz(0.512000, qreg_1[1])
    subcirc2.u(0.692000,0.627000,0.281000, qreg_1[1])
    subcirc2.u(-0.053000,0.367000,0.915000, qreg_1[1])
    subcirc2.x(qreg_1[2])
    
    subcirc3 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(1)
    subcirc3.add_register(qreg_0)
    qreg_1 = QuantumRegister(2)
    subcirc3.add_register(qreg_1)
    qreg_3 = QuantumRegister(1)
    subcirc3.add_register(qreg_3)
    # Adding creg resources 
    subcirc3.cy(qreg_1[1],qreg_0[0])
    subcirc3.x(qreg_3[0])
    subcirc3.u(0.151000,-0.435000,0.626000, qreg_1[1])
    subcirc3.cy(qreg_1[1],qreg_0[0])
    subcirc3.cy(qreg_1[0],qreg_1[1])
    
    subcirc4 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(2)
    subcirc4.add_register(qreg_0)
    qreg_2 = QuantumRegister(2)
    subcirc4.add_register(qreg_2)
    # Adding creg resources 
    subcirc4.rz(-0.305000, qreg_2[0])
    subcirc4.u(0.685000,0.579000,0.558000, qreg_0[0])
    subcirc4.rz(-0.765000, qreg_0[1])
    subcirc4.rz(0.668000, qreg_0[1])
    subcirc4.u(-0.063000,-0.450000,0.090000, qreg_2[1])
    subcirc4 = subcirc4.to_gate().control(3)
    
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
    param_6 = Parameter("param_6")
    param_7 = Parameter("param_7")
    
    main_circ.x(0)
    main_circ.u(-0.712000,-0.107000,param_0, 0)
    main_circ.append(subcirc1,[2,3,1,qreg_1[0]])
    main_circ.x(1)
    main_circ.append(subcirc2,[qreg_1[0],qreg_0[0],2,0])
    main_circ.append(subcirc2,[3,qreg_0[0],qreg_1[0],2])
    main_circ.append(subcirc2,[2,3,1,qreg_1[0]])
    main_circ.append(subcirc1,[qreg_0[0],3,2,0])
    main_circ.append(subcirc3,[qreg_1[0],1,2,3])
    main_circ.cy(1,0)
    main_circ.cy(qreg_0[0],1)
    main_circ.append(subcirc3,[qreg_1[0],qreg_0[0],1,0])
    main_circ.x(3)
    main_circ.x(2)
    main_circ.rz(param_0, 2)
    bindings = {param_0: -0.980000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_routing_simulation(main_circ, "70")


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
