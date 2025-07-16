
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
    subcirc0.cz(qreg_0[2],qreg_0[0])
    subcirc0.u(-0.590000,0.000000,-0.096000, qreg_0[0])
    subcirc0.u(0.541000,0.430000,0.783000, qreg_3[0])
    subcirc0.u(0.418000,-0.056000,-0.698000, qreg_0[2])
    subcirc0.u(pi/2,0.797000,-0.767000, qreg_0[0])
    
    subcirc1 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(4)
    subcirc1.add_register(qreg_0)
    # Adding creg resources 
    subcirc1.s(qreg_0[1])
    subcirc1.u(pi/2,-0.946000,0.622000, qreg_0[0])
    subcirc1.u(pi/2,-0.176000,0.485000, qreg_0[1])
    subcirc1.s(qreg_0[2])
    subcirc1.u(-0.668000,0.443000,0.446000, qreg_0[2])
    subcirc1.u(pi/2,0.137000,0.507000, qreg_0[1])
    
    main_circ = QuantumCircuit(4)
    # Adding qregs 
    qreg_0 = QuantumRegister(1)
    main_circ.add_register(qreg_0)
    qreg_1 = QuantumRegister(1)
    main_circ.add_register(qreg_1)
    # Adding creg resources 
    creg_0 = ClassicalRegister(2)
    main_circ.add_register(creg_0)
    # Adding symbols 
    param_0 = Parameter("param_0")
    param_1 = Parameter("param_1")
    param_2 = Parameter("param_2")
    param_3 = Parameter("param_3")
    param_4 = Parameter("param_4")
    
    main_circ.u(0.009000,param_2,0.962000, 3)
    main_circ.u(param_3,param_2,0.970000, 2)
    main_circ.append(subcirc0,[0,qreg_0[0],3,2])
    main_circ.u(0.029000,0.231000,0.415000, qreg_0[0])
    main_circ.u(pi/2,0.186000,-0.051000, 0)
    main_circ.s(0)
    main_circ.append(subcirc1,[qreg_1[0],2,0,1])
    main_circ.append(subcirc0,[3,qreg_1[0],0,2])
    main_circ.cz(qreg_0[0],qreg_1[0])
    main_circ.u(-0.833000,0.724000,-0.957000, qreg_0[0])
    main_circ.s(1)
    main_circ.append(subcirc0,[0,1,qreg_0[0],3])
    main_circ.cz(0,qreg_0[0])
    main_circ.cz(2,qreg_1[0])
    main_circ.cz(0,qreg_0[0])
    main_circ.cz(2,3)
    main_circ.cz(1,qreg_1[0])
    main_circ.cz(0,2)
    main_circ.append(subcirc0,[1,2,qreg_0[0],qreg_1[0]])
    main_circ.cz(qreg_1[0],1)
    main_circ.u(param_0,0.065000,param_0, 2)
    bindings = {param_0: -0.975000, param_2: -0.969000, param_3: -0.801000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_routing_simulation(main_circ, "23")


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
