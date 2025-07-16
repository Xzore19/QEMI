
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
    qreg_2 = QuantumRegister(1)
    subcirc0.add_register(qreg_2)
    qreg_3 = QuantumRegister(1)
    subcirc0.add_register(qreg_3)
    # Adding creg resources 
    subcirc0.x(qreg_0[1])
    subcirc0.rz(-0.900000, qreg_3[0])
    subcirc0.x(qreg_0[0])
    subcirc0.y(qreg_0[0])
    subcirc0.x(qreg_3[0])
    
    subcirc1 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(2)
    subcirc1.add_register(qreg_0)
    qreg_2 = QuantumRegister(2)
    subcirc1.add_register(qreg_2)
    # Adding creg resources 
    subcirc1.y(qreg_0[1])
    subcirc1.rz(-0.011000, qreg_0[0])
    subcirc1.y(qreg_2[0])
    subcirc1.y(qreg_2[1])
    subcirc1.rz(-0.235000, qreg_0[0])
    
    subcirc2 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(4)
    subcirc2.add_register(qreg_0)
    # Adding creg resources 
    subcirc2.rz(0.956000, qreg_0[2])
    subcirc2.y(qreg_0[1])
    subcirc2.y(qreg_0[1])
    subcirc2.u(0.876000,-0.291000,-0.005000, qreg_0[2])
    subcirc2.x(qreg_0[1])
    subcirc2 = subcirc2.to_gate().control(1)
    
    subcirc3 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(3)
    subcirc3.add_register(qreg_0)
    qreg_3 = QuantumRegister(1)
    subcirc3.add_register(qreg_3)
    # Adding creg resources 
    subcirc3.x(qreg_3[0])
    subcirc3.y(qreg_0[0])
    subcirc3.rz(0.616000, qreg_0[2])
    subcirc3.rz(0.241000, qreg_0[0])
    subcirc3.rz(-0.396000, qreg_0[2])
    subcirc3 = subcirc3.to_gate().control(3)
    
    main_circ = QuantumCircuit(2)
    # Adding qregs 
    qreg_0 = QuantumRegister(2)
    main_circ.add_register(qreg_0)
    qreg_2 = QuantumRegister(2)
    main_circ.add_register(qreg_2)
    # Adding creg resources 
    creg_0 = ClassicalRegister(1)
    main_circ.add_register(creg_0)
    creg_1 = ClassicalRegister(1)
    main_circ.add_register(creg_1)
    # Adding symbols 
    param_0 = Parameter("param_0")
    param_1 = Parameter("param_1")
    param_2 = Parameter("param_2")
    
    main_circ.y(qreg_0[0])
    main_circ.measure(qreg_2[0], creg_0[0])
    with main_circ.switch(creg_0[0]) as case_2:
    	with case_2(0):
    		main_circ.measure(1, creg_0[0])
    		with main_circ.if_test((creg_0[0],0)) as else_1:
    			main_circ.x(qreg_0[1])
    			main_circ.append(subcirc2,[qreg_0[1],1,qreg_2[0],qreg_2[1],0])
    		with else_1:
    			main_circ.append(subcirc0,[0,qreg_2[1],qreg_0[0],qreg_0[1]])
    	with case_2(1):
    		main_circ.measure(qreg_0[1], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)) as else_1:
    			main_circ.append(subcirc1,[qreg_2[1],qreg_0[1],0,qreg_2[0]])
    		with else_1:
    			main_circ.y(qreg_0[1])
    main_circ.measure(1, creg_1[0])
    with main_circ.if_test((creg_1[0],0)) as else_2:
    	main_circ.u(param_1,-0.183000,param_0, qreg_0[0])
    	main_circ.y(qreg_2[0])
    with else_2:
    	main_circ.id(qreg_0[0])
    main_circ.measure(qreg_2[0], creg_0[0])
    with main_circ.if_test((creg_0[0],0)) as else_2:
    	main_circ.measure(0, creg_0[0])
    	with main_circ.if_test((creg_0[0],0)) as else_1:
    		main_circ.y(1)
    		main_circ.append(subcirc2,[qreg_2[0],qreg_0[0],qreg_0[1],1,qreg_2[1]])
    	with else_1:
    		main_circ.x(qreg_0[0])
    with else_2:
    	main_circ.measure(qreg_2[0], creg_1[0])
    	with main_circ.if_test((creg_1[0],0)) as else_1:
    		main_circ.append(subcirc0,[0,qreg_2[1],qreg_0[1],1])
    	with else_1:
    		main_circ.append(subcirc1,[1,qreg_0[0],0,qreg_2[0]])
    main_circ.append(subcirc2,[qreg_0[1],qreg_2[0],qreg_2[1],0,1])
    bindings = {param_0: -0.054000, param_1: 0.469000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_pass_on_simulator(main_circ, "79", "Optimize1qGatesSimpleCommutation")


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
