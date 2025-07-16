
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
    subcirc0.rx(-0.006000, qreg_0[0])
    subcirc0.rx(-0.135000, qreg_2[0])
    subcirc0.u(pi/2,0.389000,-0.758000, qreg_3[0])
    subcirc0.y(qreg_3[0])
    
    subcirc1 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(4)
    subcirc1.add_register(qreg_0)
    # Adding creg resources 
    subcirc1.cx(qreg_0[2],qreg_0[1])
    subcirc1.cx(qreg_0[2],qreg_0[0])
    subcirc1.cx(qreg_0[0],qreg_0[1])
    subcirc1.cx(qreg_0[2],qreg_0[1])
    
    subcirc2 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(3)
    subcirc2.add_register(qreg_0)
    qreg_3 = QuantumRegister(1)
    subcirc2.add_register(qreg_3)
    # Adding creg resources 
    subcirc2.cx(qreg_3[0],qreg_0[2])
    subcirc2.cx(qreg_0[1],qreg_3[0])
    subcirc2.cx(qreg_0[1],qreg_0[0])
    subcirc2.u(pi/2,-0.930000,-0.291000, qreg_0[1])
    
    subcirc3 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(3)
    subcirc3.add_register(qreg_0)
    qreg_3 = QuantumRegister(1)
    subcirc3.add_register(qreg_3)
    # Adding creg resources 
    subcirc3.rx(0.552000, qreg_0[1])
    subcirc3.cx(qreg_0[2],qreg_0[0])
    subcirc3.y(qreg_0[1])
    subcirc3.y(qreg_0[0])
    
    main_circ = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(4)
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
    
    main_circ.append(subcirc3,[qreg_0[0],qreg_0[2],qreg_0[1],qreg_0[3]])
    main_circ.measure(qreg_0[2], creg_0[0])
    with main_circ.if_test((creg_0[0],0)):
    	main_circ.rx(param_2, qreg_0[3])
    	main_circ.rx(param_0, qreg_0[3])
    	main_circ.u(param_0,param_1,param_1, qreg_0[1])
    	main_circ.measure(qreg_0[0], creg_0[0])
    	with main_circ.switch(creg_0[0]) as case_1:
    		with case_1(0):
    			main_circ.rx(-0.835000, qreg_0[2])
    			main_circ.u(pi/2,param_2,0.246000, qreg_0[2])
    			main_circ.cx(qreg_0[3],qreg_0[0])
    			main_circ.cx(qreg_0[1],qreg_0[2])
    		with case_1(1):
    			main_circ.append(subcirc1,[qreg_0[3],qreg_0[1],qreg_0[0],qreg_0[2]])
    main_circ.measure(qreg_0[1], creg_0[0])
    with main_circ.if_test((creg_0[0],0)):
    	main_circ.measure(qreg_0[3], creg_0[0])
    	with main_circ.switch(creg_0[0]) as case_1:
    		with case_1(0):
    			main_circ.append(subcirc0,[qreg_0[1],qreg_0[3],qreg_0[2],qreg_0[0]])
    		with case_1(1):
    			main_circ.append(subcirc2,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_0[3]])
    main_circ.measure(qreg_0[1], creg_0[0])
    with main_circ.switch(creg_0[0]) as case_2:
    	with case_2(0):
    		main_circ.rx(param_0, qreg_0[1])
    		main_circ.cx(qreg_0[3],qreg_0[1])
    		main_circ.append(subcirc3,[qreg_0[2],qreg_0[3],qreg_0[1],qreg_0[0]])
    	with case_2(1):
    		main_circ.cx(qreg_0[3],qreg_0[1])
    		main_circ.measure(qreg_0[3], creg_1[0])
    		with main_circ.switch(creg_1[0]) as case_1:
    			with case_1(0):
    				main_circ.rx(param_0, qreg_0[2])
    				main_circ.append(subcirc2,[qreg_0[3],qreg_0[0],qreg_0[2],qreg_0[1]])
    			with case_1(1):
    				main_circ.append(subcirc3,[qreg_0[2],qreg_0[3],qreg_0[0],qreg_0[1]])
    main_circ.measure(qreg_0[3], creg_1[0])
    with main_circ.if_test((creg_1[0],0)) as else_2:
    	main_circ.measure(qreg_0[3], creg_0[0])
    	with main_circ.if_test((creg_0[0],0)):
    		main_circ.u(param_1,-0.380000,0.958000, qreg_0[3])
    with else_2:
    	main_circ.append(subcirc0,[qreg_0[0],qreg_0[3],qreg_0[2],qreg_0[1]])
    	main_circ.measure(qreg_0[0], creg_0[0])
    	with main_circ.if_test((creg_0[0],0)):
    		main_circ.rx(param_0, qreg_0[3])
    		main_circ.append(subcirc0,[qreg_0[2],qreg_0[1],qreg_0[0],qreg_0[3]])
    main_circ.rx(-0.465000, qreg_0[2])
    main_circ.measure(qreg_0[3], creg_1[0])
    with main_circ.if_test((creg_1[0],0)):
    	main_circ.measure(qreg_0[3], creg_0[0])
    	with main_circ.if_test((creg_0[0],0)):
    		main_circ.rx(param_0, qreg_0[0])
    		main_circ.append(subcirc2,[qreg_0[3],qreg_0[0],qreg_0[2],qreg_0[1]])
    main_circ.measure(qreg_0[0], creg_1[0])
    with main_circ.if_test((creg_1[0],0)):
    	main_circ.measure(qreg_0[0], creg_1[0])
    	with main_circ.if_test((creg_1[0],0)):
    		main_circ.append(subcirc2,[qreg_0[2],qreg_0[3],qreg_0[1],qreg_0[0]])
    		main_circ.barrier(qreg_0[2])
    bindings = {param_0: -0.425000, param_1: -0.714000, param_2: -0.105000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_on_simulator(main_circ, "16")


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
