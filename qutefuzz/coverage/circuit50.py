
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
    subcirc0.cy(qreg_0[0],qreg_3[0])
    subcirc0.x(qreg_0[1])
    subcirc0.x(qreg_3[0])
    subcirc0.rx(-0.326000, qreg_0[1])
    subcirc0.cy(qreg_0[1],qreg_3[0])
    subcirc0.rx(-0.955000, qreg_3[0])
    
    subcirc1 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(1)
    subcirc1.add_register(qreg_0)
    qreg_1 = QuantumRegister(1)
    subcirc1.add_register(qreg_1)
    qreg_2 = QuantumRegister(1)
    subcirc1.add_register(qreg_2)
    qreg_3 = QuantumRegister(1)
    subcirc1.add_register(qreg_3)
    # Adding creg resources 
    subcirc1.z(qreg_0[0])
    subcirc1.rx(0.171000, qreg_1[0])
    subcirc1.cy(qreg_1[0],qreg_2[0])
    subcirc1.rx(-0.503000, qreg_1[0])
    subcirc1.rx(0.370000, qreg_3[0])
    subcirc1.x(qreg_3[0])
    subcirc1 = subcirc1.to_gate().control(2)
    
    subcirc2 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(2)
    subcirc2.add_register(qreg_0)
    qreg_2 = QuantumRegister(1)
    subcirc2.add_register(qreg_2)
    qreg_3 = QuantumRegister(1)
    subcirc2.add_register(qreg_3)
    # Adding creg resources 
    subcirc2.x(qreg_3[0])
    subcirc2.z(qreg_0[0])
    subcirc2.x(qreg_3[0])
    subcirc2.cy(qreg_2[0],qreg_3[0])
    subcirc2.cy(qreg_3[0],qreg_0[0])
    subcirc2.cy(qreg_0[1],qreg_3[0])
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
    subcirc3.x(qreg_3[0])
    subcirc3.x(qreg_0[0])
    subcirc3.x(qreg_1[1])
    subcirc3.cy(qreg_1[0],qreg_0[0])
    subcirc3.rx(-0.191000, qreg_0[0])
    subcirc3.cy(qreg_1[1],qreg_0[0])
    subcirc3 = subcirc3.to_gate().control(2)
    
    subcirc4 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(2)
    subcirc4.add_register(qreg_0)
    qreg_2 = QuantumRegister(2)
    subcirc4.add_register(qreg_2)
    # Adding creg resources 
    subcirc4.cy(qreg_2[1],qreg_0[0])
    subcirc4.rx(0.279000, qreg_0[1])
    subcirc4.z(qreg_2[0])
    subcirc4.rx(0.869000, qreg_0[1])
    subcirc4.x(qreg_2[1])
    subcirc4.x(qreg_2[1])
    
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
    
    main_circ.measure(qreg_0[1], creg_0[0])
    with main_circ.if_test((creg_0[0],0)):
    	main_circ.measure(0, creg_0[0])
    	with main_circ.if_test((creg_0[0],0)):
    		main_circ.measure(qreg_0[0], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)) as else_1:
    			main_circ.append(subcirc2,[0,qreg_0[0],qreg_0[1],1,qreg_2[0],qreg_3[0]])
    		with else_1:
    			main_circ.rx(param_2, 1)
    			main_circ.cy(qreg_0[0],qreg_3[0])
    main_circ.measure(qreg_0[1], creg_0[0])
    with main_circ.if_test((creg_0[0],0)) as else_3:
    	main_circ.x(qreg_0[0])
    	main_circ.measure(qreg_0[1], creg_1[0])
    	with main_circ.if_test((creg_1[0],0)):
    		main_circ.measure(qreg_3[0], creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_1:
    			with case_1(0):
    				main_circ.append(subcirc3,[qreg_2[0],qreg_3[0],0,qreg_0[0],qreg_0[1],1])
    			with case_1(1):
    				main_circ.append(subcirc4,[qreg_3[0],1,qreg_0[1],0])
    with else_3:
    	main_circ.append(subcirc1,[qreg_0[1],0,qreg_2[0],1,qreg_3[0],qreg_0[0]])
    main_circ.measure(qreg_3[0], creg_1[0])
    with main_circ.if_test((creg_1[0],0)):
    	main_circ.measure(qreg_3[0], creg_0[0])
    	with main_circ.if_test((creg_0[0],0)):
    		main_circ.measure(qreg_0[1], creg_1[0])
    		with main_circ.switch(creg_1[0]) as case_1:
    			with case_1(0):
    				main_circ.z(qreg_0[1])
    				main_circ.append(subcirc2,[qreg_3[0],qreg_0[1],qreg_0[0],qreg_2[0],0,1])
    			with case_1(1):
    				main_circ.append(subcirc0,[qreg_0[1],qreg_2[0],qreg_3[0],1])
    main_circ.cy(1,qreg_0[0])
    main_circ.append(subcirc2,[qreg_2[0],0,1,qreg_0[1],qreg_0[0],qreg_3[0]])
    main_circ.measure(1, creg_1[0])
    with main_circ.switch(creg_1[0]) as case_3:
    	with case_3(0):
    		main_circ.measure(1, creg_1[0])
    		with main_circ.switch(creg_1[0]) as case_2:
    			with case_2(0):
    				main_circ.measure(qreg_3[0], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.barrier(qreg_3[0])
    				with else_1:
    					main_circ.id(qreg_0[1])
    				main_circ.measure(0, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.rx(-0.929000, qreg_3[0])
    					main_circ.rx(-0.337000, qreg_0[1])
    				with else_1:
    					main_circ.barrier(qreg_2[0])
    				main_circ.measure(1, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.id(1)
    				with else_1:
    					main_circ.barrier(0)
    				main_circ.measure(qreg_2[0], creg_0[0])
    				with main_circ.switch(creg_0[0]) as case_1:
    					with case_1(0):
    						main_circ.id(qreg_3[0])
    					with case_1(1):
    						main_circ.id(1)
    				main_circ.measure(qreg_0[1], creg_1[0])
    				with main_circ.if_test((creg_1[0],0)) as else_1:
    					main_circ.barrier(qreg_0[1])
    				with else_1:
    					main_circ.barrier(qreg_3[0])
    				main_circ.measure(qreg_2[0], creg_0[0])
    				with main_circ.switch(creg_0[0]) as case_1:
    					with case_1(0):
    						main_circ.barrier(qreg_2[0])
    					with case_1(1):
    						main_circ.id(qreg_2[0])
    				main_circ.measure(0, creg_1[0])
    				with main_circ.if_test((creg_1[0],0)):
    					main_circ.barrier(qreg_2[0])
    				main_circ.measure(0, creg_1[0])
    				with main_circ.switch(creg_1[0]) as case_1:
    					with case_1(0):
    						main_circ.id(0)
    					with case_1(1):
    						main_circ.barrier(qreg_3[0])
    				main_circ.measure(qreg_3[0], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.barrier(1)
    				main_circ.measure(0, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.barrier(qreg_0[0])
    				main_circ.measure(0, creg_1[0])
    				with main_circ.if_test((creg_1[0],0)):
    					main_circ.barrier(qreg_3[0])
    				main_circ.id(qreg_0[0])
    			with case_2(1):
    				main_circ.measure(qreg_3[0], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.id(0)
    				with else_1:
    					main_circ.barrier(0)
    				main_circ.barrier(0)
    		main_circ.measure(0, creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_2:
    			with case_2(0):
    				main_circ.measure(qreg_3[0], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.id(qreg_0[0])
    				main_circ.barrier(1)
    			with case_2(1):
    				main_circ.measure(qreg_0[0], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.id(1)
    				with else_1:
    					main_circ.id(qreg_0[0])
    				main_circ.measure(qreg_0[1], creg_1[0])
    				with main_circ.if_test((creg_1[0],0)) as else_1:
    					main_circ.barrier(qreg_0[1])
    				with else_1:
    					main_circ.barrier(qreg_0[0])
    				main_circ.measure(qreg_2[0], creg_1[0])
    				with main_circ.if_test((creg_1[0],0)):
    					main_circ.barrier(qreg_0[1])
    				main_circ.measure(0, creg_0[0])
    				with main_circ.switch(creg_0[0]) as case_1:
    					with case_1(0):
    						main_circ.id(1)
    					with case_1(1):
    						main_circ.barrier(qreg_0[1])
    				main_circ.id(0)
    		main_circ.id(qreg_3[0])
    	with case_3(1):
    		main_circ.measure(qreg_2[0], creg_0[0])
    		with main_circ.if_test((creg_0[0],0)) as else_2:
    			main_circ.measure(1, creg_1[0])
    			with main_circ.if_test((creg_1[0],0)):
    				main_circ.id(1)
    			main_circ.measure(qreg_0[1], creg_1[0])
    			with main_circ.if_test((creg_1[0],0)) as else_1:
    				main_circ.id(qreg_2[0])
    			with else_1:
    				main_circ.barrier(qreg_2[0])
    			main_circ.measure(qreg_0[0], creg_1[0])
    			with main_circ.if_test((creg_1[0],0)):
    				main_circ.id(0)
    			main_circ.measure(qreg_0[1], creg_0[0])
    			with main_circ.if_test((creg_0[0],0)) as else_1:
    				main_circ.id(0)
    			with else_1:
    				main_circ.barrier(0)
    			main_circ.id(qreg_2[0])
    		with else_2:
    			main_circ.measure(qreg_0[1], creg_0[0])
    			with main_circ.switch(creg_0[0]) as case_1:
    				with case_1(0):
    					main_circ.barrier(qreg_2[0])
    				with case_1(1):
    					main_circ.id(qreg_0[1])
    			main_circ.barrier(qreg_3[0])
    		main_circ.measure(1, creg_1[0])
    		with main_circ.if_test((creg_1[0],0)):
    			main_circ.measure(0, creg_1[0])
    			with main_circ.switch(creg_1[0]) as case_1:
    				with case_1(0):
    					main_circ.barrier(qreg_2[0])
    				with case_1(1):
    					main_circ.barrier(qreg_0[1])
    			main_circ.id(qreg_2[0])
    		main_circ.measure(qreg_3[0], creg_0[0])
    		with main_circ.if_test((creg_0[0],0)):
    			main_circ.measure(qreg_3[0], creg_1[0])
    			with main_circ.if_test((creg_1[0],0)) as else_1:
    				main_circ.id(qreg_0[1])
    			with else_1:
    				main_circ.barrier(qreg_3[0])
    			main_circ.measure(qreg_0[1], creg_1[0])
    			with main_circ.if_test((creg_1[0],0)) as else_1:
    				main_circ.id(qreg_0[0])
    			with else_1:
    				main_circ.id(1)
    			main_circ.measure(qreg_3[0], creg_1[0])
    			with main_circ.if_test((creg_1[0],0)):
    				main_circ.barrier(qreg_3[0])
    			main_circ.measure(1, creg_1[0])
    			with main_circ.if_test((creg_1[0],0)) as else_1:
    				main_circ.barrier(1)
    			with else_1:
    				main_circ.id(1)
    			main_circ.id(qreg_0[0])
    		main_circ.measure(qreg_0[1], creg_0[0])
    		with main_circ.if_test((creg_0[0],0)):
    			main_circ.measure(qreg_0[0], creg_0[0])
    			with main_circ.switch(creg_0[0]) as case_1:
    				with case_1(0):
    					main_circ.barrier(qreg_0[1])
    				with case_1(1):
    					main_circ.id(0)
    			main_circ.id(qreg_0[1])
    		main_circ.measure(qreg_2[0], creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_2:
    			with case_2(0):
    				main_circ.barrier(1)
    			with case_2(1):
    				main_circ.id(0)
    		main_circ.measure(0, creg_1[0])
    		with main_circ.if_test((creg_1[0],0)) as else_2:
    			main_circ.measure(1, creg_0[0])
    			with main_circ.if_test((creg_0[0],0)) as else_1:
    				main_circ.barrier(1)
    			with else_1:
    				main_circ.barrier(qreg_0[1])
    			main_circ.id(qreg_3[0])
    		with else_2:
    			main_circ.measure(1, creg_0[0])
    			with main_circ.if_test((creg_0[0],0)) as else_1:
    				main_circ.id(0)
    			with else_1:
    				main_circ.id(qreg_3[0])
    			main_circ.measure(qreg_0[1], creg_0[0])
    			with main_circ.if_test((creg_0[0],0)):
    				main_circ.barrier(0)
    			main_circ.measure(qreg_3[0], creg_1[0])
    			with main_circ.switch(creg_1[0]) as case_1:
    				with case_1(0):
    					main_circ.barrier(1)
    				with case_1(1):
    					main_circ.barrier(qreg_3[0])
    			main_circ.measure(qreg_0[0], creg_0[0])
    			with main_circ.switch(creg_0[0]) as case_1:
    				with case_1(0):
    					main_circ.barrier(qreg_0[1])
    				with case_1(1):
    					main_circ.id(qreg_3[0])
    			main_circ.measure(qreg_0[0], creg_0[0])
    			with main_circ.if_test((creg_0[0],0)) as else_1:
    				main_circ.id(1)
    			with else_1:
    				main_circ.barrier(qreg_3[0])
    			main_circ.measure(qreg_2[0], creg_0[0])
    			with main_circ.if_test((creg_0[0],0)) as else_1:
    				main_circ.id(1)
    			with else_1:
    				main_circ.barrier(0)
    			main_circ.measure(qreg_0[1], creg_0[0])
    			with main_circ.switch(creg_0[0]) as case_1:
    				with case_1(0):
    					main_circ.id(1)
    				with case_1(1):
    					main_circ.barrier(qreg_2[0])
    			main_circ.measure(1, creg_1[0])
    			with main_circ.if_test((creg_1[0],0)) as else_1:
    				main_circ.barrier(qreg_0[1])
    			with else_1:
    				main_circ.barrier(qreg_0[1])
    			main_circ.measure(qreg_0[0], creg_0[0])
    			with main_circ.if_test((creg_0[0],0)):
    				main_circ.barrier(qreg_0[0])
    			main_circ.id(qreg_0[0])
    		main_circ.barrier(qreg_2[0])
    bindings = {param_2: 0.682000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_pass_on_simulator(main_circ, "50", "OptimizeAnnotated")


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
