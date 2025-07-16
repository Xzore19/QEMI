
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
    subcirc0.u(pi/2,-0.382000,-0.648000, qreg_0[0])
    subcirc0.u(pi/2,0.035000,0.927000, qreg_0[1])
    subcirc0.u(-0.722000,0.609000,-0.740000, qreg_0[2])
    subcirc0.u(pi/2,-0.126000,-0.602000, qreg_0[1])
    subcirc0.u(-0.143000,0.819000,-0.729000, qreg_0[1])
    subcirc0 = subcirc0.to_gate().control(1)
    
    subcirc1 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(2)
    subcirc1.add_register(qreg_0)
    qreg_2 = QuantumRegister(1)
    subcirc1.add_register(qreg_2)
    qreg_3 = QuantumRegister(1)
    subcirc1.add_register(qreg_3)
    # Adding creg resources 
    subcirc1.u(pi/2,-0.759000,0.313000, qreg_0[0])
    subcirc1.z(qreg_2[0])
    subcirc1.z(qreg_0[1])
    subcirc1.z(qreg_2[0])
    subcirc1.u(pi/2,-0.678000,-0.079000, qreg_3[0])
    
    subcirc2 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(2)
    subcirc2.add_register(qreg_0)
    qreg_2 = QuantumRegister(2)
    subcirc2.add_register(qreg_2)
    # Adding creg resources 
    subcirc2.u(0.555000,-0.893000,0.147000, qreg_0[0])
    subcirc2.u(-0.260000,-0.564000,-0.927000, qreg_2[1])
    subcirc2.u(pi/2,0.623000,-0.632000, qreg_0[1])
    subcirc2.u(pi/2,-0.492000,0.237000, qreg_0[0])
    subcirc2.u(0.565000,0.822000,-0.968000, qreg_0[1])
    subcirc2 = subcirc2.to_gate().control(2)
    
    subcirc3 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(1)
    subcirc3.add_register(qreg_0)
    qreg_1 = QuantumRegister(2)
    subcirc3.add_register(qreg_1)
    qreg_3 = QuantumRegister(1)
    subcirc3.add_register(qreg_3)
    # Adding creg resources 
    subcirc3.u(pi/2,-0.283000,0.951000, qreg_1[1])
    subcirc3.cy(qreg_3[0],qreg_1[0])
    subcirc3.u(pi/2,-0.404000,0.729000, qreg_1[0])
    subcirc3.z(qreg_3[0])
    subcirc3.z(qreg_1[1])
    subcirc3 = subcirc3.to_gate().control(2)
    
    subcirc4 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(3)
    subcirc4.add_register(qreg_0)
    qreg_3 = QuantumRegister(1)
    subcirc4.add_register(qreg_3)
    # Adding creg resources 
    subcirc4.z(qreg_0[0])
    subcirc4.z(qreg_0[1])
    subcirc4.cy(qreg_0[1],qreg_0[2])
    subcirc4.z(qreg_0[2])
    subcirc4.cy(qreg_0[1],qreg_0[0])
    subcirc4 = subcirc4.to_gate().control(3)
    
    main_circ = QuantumCircuit(4)
    # Adding qregs 
    qreg_0 = QuantumRegister(1)
    main_circ.add_register(qreg_0)
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
    
    main_circ.z(3)
    main_circ.u(pi/2,param_2,param_4, qreg_0[0])
    main_circ.cy(1,qreg_0[0])
    main_circ.z(3)
    main_circ.z(0)
    main_circ.u(param_4,param_1,param_2, 3)
    main_circ.append(subcirc0,[qreg_0[0],1,0,3,2])
    main_circ.u(-0.930000,-0.142000,-0.311000, 3)
    main_circ.append(subcirc0,[1,qreg_0[0],0,2,3])
    main_circ.append(subcirc0,[3,2,1,qreg_0[0],0])
    main_circ.u(param_4,param_2,0.950000, 2)
    main_circ.z(qreg_0[0])
    main_circ.u(param_6,-0.185000,param_3, 0)
    main_circ.append(subcirc1,[2,qreg_0[0],3,0])
    main_circ.u(param_6,param_4,param_5, 2)
    main_circ.append(subcirc1,[0,qreg_0[0],2,3])
    main_circ.cy(3,1)
    main_circ.cy(3,0)
    main_circ.cy(qreg_0[0],3)
    main_circ.cy(2,1)
    main_circ.cy(3,qreg_0[0])
    main_circ.cy(qreg_0[0],2)
    main_circ.cy(3,qreg_0[0])
    main_circ.cy(0,1)
    main_circ.cy(1,2)
    main_circ.cy(qreg_0[0],0)
    main_circ.cy(1,0)
    main_circ.cy(3,2)
    bindings = {param_1: -0.981000, param_2: 0.029000, param_3: -0.079000, param_4: -0.733000, param_5: -0.210000, param_6: 0.071000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_routing_simulation(main_circ, "9")


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
