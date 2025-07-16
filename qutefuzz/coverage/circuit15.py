
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
    qreg_1 = QuantumRegister(3)
    subcirc0.add_register(qreg_1)
    # Adding creg resources 
    subcirc0.y(qreg_1[2])
    subcirc0.u(0,0,-0.236000, qreg_1[1])
    subcirc0.z(qreg_0[0])
    subcirc0.y(qreg_1[1])
    subcirc0.u(pi/2,-0.471000,0.848000, qreg_1[1])
    subcirc0.z(qreg_1[1])
    subcirc0 = subcirc0.to_gate().control(3)
    
    subcirc1 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(4)
    subcirc1.add_register(qreg_0)
    # Adding creg resources 
    subcirc1.y(qreg_0[0])
    subcirc1.y(qreg_0[2])
    subcirc1.u(0,0,0.919000, qreg_0[1])
    subcirc1.y(qreg_0[0])
    subcirc1.u(pi/2,0.362000,-0.515000, qreg_0[3])
    subcirc1.u(0,0,0.088000, qreg_0[1])
    subcirc1 = subcirc1.to_gate().control(3)
    
    subcirc2 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(4)
    subcirc2.add_register(qreg_0)
    # Adding creg resources 
    subcirc2.z(qreg_0[3])
    subcirc2.z(qreg_0[2])
    subcirc2.z(qreg_0[2])
    subcirc2.u(0,0,-0.071000, qreg_0[2])
    subcirc2.y(qreg_0[2])
    subcirc2.u(pi/2,0.949000,0.157000, qreg_0[3])
    
    subcirc3 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(1)
    subcirc3.add_register(qreg_0)
    qreg_1 = QuantumRegister(3)
    subcirc3.add_register(qreg_1)
    # Adding creg resources 
    subcirc3.u(0,0,0.747000, qreg_1[2])
    subcirc3.y(qreg_1[0])
    subcirc3.z(qreg_1[2])
    subcirc3.y(qreg_1[1])
    subcirc3.u(pi/2,-0.548000,0.546000, qreg_1[2])
    subcirc3.u(pi/2,0.950000,0.486000, qreg_1[2])
    subcirc3 = subcirc3.to_gate().control(2)
    
    main_circ = QuantumCircuit(4)
    # Adding qregs 
    qreg_0 = QuantumRegister(1)
    main_circ.add_register(qreg_0)
    # Adding creg resources 
    creg_0 = ClassicalRegister(2)
    main_circ.add_register(creg_0)
    # Adding symbols 
    param_0 = Parameter("param_0")
    param_1 = Parameter("param_1")
    param_2 = Parameter("param_2")
    
    main_circ.append(subcirc2,[2,1,3,0])
    main_circ.measure(qreg_0[0], creg_0[1])
    with main_circ.switch(creg_0[1]) as case_1:
    	with case_1(0):
    		main_circ.u(0,param_1,0.858000, qreg_0[0])
    		main_circ.u(param_0,0.156000,param_0, 0)
    		main_circ.id(qreg_0[0])
    	with case_1(1):
    		main_circ.u(param_0,param_0,-0.488000, qreg_0[0])
    		main_circ.append(subcirc2,[1,qreg_0[0],0,3])
    main_circ.measure(3, creg_0[1])
    with main_circ.if_test((creg_0[1],0)) as else_1:
    	main_circ.id(1)
    with else_1:
    	main_circ.u(param_1,-0.940000,-0.677000, 3)
    	main_circ.z(qreg_0[0])
    	main_circ.u(0,param_0,param_1, 0)
    	main_circ.id(3)
    main_circ.y(1)
    main_circ.u(param_1,0,param_2, 3)
    main_circ.append(subcirc2,[qreg_0[0],1,0,2])
    main_circ.measure(1, creg_0[1])
    with main_circ.switch(creg_0[1]) as case_1:
    	with case_1(0):
    		main_circ.u(0,0,param_0, 1)
    		main_circ.u(0,param_2,param_0, 3)
    		main_circ.append(subcirc2,[1,qreg_0[0],0,3])
    	with case_1(1):
    		main_circ.append(subcirc2,[1,3,qreg_0[0],2])
    main_circ.measure(qreg_0[0], creg_0[1])
    with main_circ.if_test((creg_0[1],0)):
    	main_circ.y(1)
    main_circ.measure(0, creg_0[1])
    with main_circ.switch(creg_0[1]) as case_1:
    	with case_1(0):
    		main_circ.u(0,0,param_1, 1)
    		main_circ.z(3)
    		main_circ.id(1)
    	with case_1(1):
    		main_circ.id(0)
    main_circ.measure(1, creg_0[0])
    with main_circ.if_test((creg_0[0],0)):
    	main_circ.barrier(qreg_0[0])
    main_circ.measure(0, creg_0[0])
    with main_circ.if_test((creg_0[0],0)):
    	main_circ.z(2)
    	main_circ.u(param_0,param_1,param_0, 1)
    	main_circ.z(2)
    	main_circ.u(param_1,param_0,-0.849000, qreg_0[0])
    main_circ.measure(3, creg_0[0])
    with main_circ.if_test((creg_0[0],0)):
    	main_circ.y(2)
    	main_circ.u(param_0,param_0,-0.530000, 0)
    main_circ.measure(1, creg_0[0])
    with main_circ.if_test((creg_0[0],0)) as else_1:
    	main_circ.u(param_1,param_0,-0.758000, 1)
    	main_circ.u(pi/2,param_0,-0.856000, 2)
    	main_circ.u(pi/2,0.929000,0.932000, 3)
    	main_circ.z(0)
    	main_circ.y(qreg_0[0])
    with else_1:
    	main_circ.id(0)
    main_circ.measure(3, creg_0[1])
    with main_circ.if_test((creg_0[1],0)):
    	main_circ.barrier(1)
    main_circ.measure(3, creg_0[0])
    with main_circ.if_test((creg_0[0],0)) as else_1:
    	main_circ.barrier(qreg_0[0])
    with else_1:
    	main_circ.u(param_0,0.432000,-0.611000, 2)
    	main_circ.u(param_0,param_2,param_0, qreg_0[0])
    	main_circ.barrier(1)
    main_circ.measure(1, creg_0[0])
    with main_circ.if_test((creg_0[0],0)):
    	main_circ.barrier(1)
    main_circ.measure(qreg_0[0], creg_0[0])
    with main_circ.if_test((creg_0[0],0)):
    	main_circ.id(qreg_0[0])
    main_circ.measure(0, creg_0[0])
    with main_circ.if_test((creg_0[0],0)) as else_1:
    	main_circ.id(1)
    with else_1:
    	main_circ.barrier(1)
    main_circ.u(param_1,param_1,0.403000, 0)
    bindings = {param_0: -0.468000, param_1: -0.577000, param_2: -0.148000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_pass_on_simulator(main_circ, "15", "ConsolidateBlocks")


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
