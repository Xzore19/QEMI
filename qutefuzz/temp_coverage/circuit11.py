
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
    subcirc0.u(0,0,0.642000, qreg_0[0])
    subcirc0.cz(qreg_0[0],qreg_3[0])
    subcirc0.cy(qreg_0[2],qreg_3[0])
    subcirc0.cz(qreg_0[1],qreg_3[0])
    subcirc0.cz(qreg_0[1],qreg_0[0])
    subcirc0 = subcirc0.to_gate().control(3)
    
    subcirc1 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(4)
    subcirc1.add_register(qreg_0)
    # Adding creg resources 
    subcirc1.cz(qreg_0[1],qreg_0[3])
    subcirc1.cz(qreg_0[3],qreg_0[2])
    subcirc1.cy(qreg_0[3],qreg_0[2])
    subcirc1.cy(qreg_0[0],qreg_0[3])
    subcirc1.u(pi/2,0.490000,-0.133000, qreg_0[2])
    subcirc1 = subcirc1.to_gate().control(3)
    
    subcirc2 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(2)
    subcirc2.add_register(qreg_0)
    qreg_2 = QuantumRegister(1)
    subcirc2.add_register(qreg_2)
    qreg_3 = QuantumRegister(1)
    subcirc2.add_register(qreg_3)
    # Adding creg resources 
    subcirc2.u(pi/2,0.335000,-0.039000, qreg_0[0])
    subcirc2.cz(qreg_0[1],qreg_0[0])
    subcirc2.cz(qreg_0[0],qreg_3[0])
    subcirc2.u(0,0,0.510000, qreg_2[0])
    subcirc2.u(0,0,-0.152000, qreg_0[0])
    
    main_circ = QuantumCircuit(4)
    # Adding qregs 
    qreg_0 = QuantumRegister(2)
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
    
    main_circ.measure(3, creg_0[0])
    with main_circ.if_test((creg_0[0],0)):
    	main_circ.cy(qreg_0[1],0)
    	main_circ.measure(3, creg_0[0])
    	with main_circ.if_test((creg_0[0],0)):
    		main_circ.measure(0, creg_1[0])
    		with main_circ.if_test((creg_1[0],0)) as else_2:
    			main_circ.measure(qreg_0[1], creg_1[0])
    			with main_circ.switch(creg_1[0]) as case_1:
    				with case_1(0):
    					main_circ.cy(0,qreg_0[1])
    					main_circ.cz(qreg_0[1],qreg_0[0])
    					main_circ.cy(0,qreg_0[0])
    					main_circ.cy(3,qreg_0[1])
    				with case_1(1):
    					main_circ.id(qreg_0[0])
    			main_circ.measure(qreg_0[1], creg_1[0])
    			with main_circ.if_test((creg_1[0],0)):
    				main_circ.cz(3,1)
    				main_circ.barrier(1)
    		with else_2:
    			main_circ.measure(3, creg_1[0])
    			with main_circ.if_test((creg_1[0],0)):
    				main_circ.barrier(0)
    			main_circ.measure(3, creg_1[0])
    			with main_circ.if_test((creg_1[0],0)) as else_1:
    				main_circ.u(param_0,param_1,param_1, qreg_0[0])
    				main_circ.id(0)
    			with else_1:
    				main_circ.append(subcirc2,[0,qreg_0[0],3,qreg_0[1]])
    main_circ.measure(0, creg_1[0])
    with main_circ.if_test((creg_1[0],0)) as else_4:
    	main_circ.measure(qreg_0[0], creg_1[0])
    	with main_circ.if_test((creg_1[0],0)):
    		main_circ.measure(qreg_0[0], creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_2:
    			with case_2(0):
    				main_circ.measure(3, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.barrier(1)
    				main_circ.measure(0, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.barrier(0)
    				main_circ.measure(1, creg_1[0])
    				with main_circ.if_test((creg_1[0],0)):
    					main_circ.u(0,param_2,param_0, 2)
    					main_circ.u(0,param_2,0.533000, 1)
    					main_circ.cy(qreg_0[0],0)
    					main_circ.u(param_0,-0.432000,param_1, qreg_0[1])
    					main_circ.id(3)
    			with case_2(1):
    				main_circ.append(subcirc2,[0,1,qreg_0[0],3])
    with else_4:
    	main_circ.measure(qreg_0[1], creg_0[0])
    	with main_circ.switch(creg_0[0]) as case_3:
    		with case_3(0):
    			main_circ.measure(3, creg_0[0])
    			with main_circ.switch(creg_0[0]) as case_2:
    				with case_2(0):
    					main_circ.measure(2, creg_1[0])
    					with main_circ.switch(creg_1[0]) as case_1:
    						with case_1(0):
    							main_circ.append(subcirc2,[qreg_0[1],1,0,qreg_0[0]])
    						with case_1(1):
    							main_circ.barrier(1)
    				with case_2(1):
    					main_circ.measure(qreg_0[0], creg_0[0])
    					with main_circ.switch(creg_0[0]) as case_1:
    						with case_1(0):
    							main_circ.cz(3,2)
    							main_circ.u(param_0,0.185000,-0.633000, 2)
    							main_circ.barrier(1)
    						with case_1(1):
    							main_circ.cz(qreg_0[1],3)
    							main_circ.u(param_2,param_0,-0.175000, qreg_0[0])
    							main_circ.u(pi/2,param_2,0.942000, qreg_0[0])
    							main_circ.u(pi/2,param_2,-0.189000, qreg_0[1])
    		with case_3(1):
    			main_circ.measure(qreg_0[1], creg_0[0])
    			with main_circ.if_test((creg_0[0],0)):
    				main_circ.barrier(qreg_0[1])
    			main_circ.measure(1, creg_1[0])
    			with main_circ.switch(creg_1[0]) as case_2:
    				with case_2(0):
    					main_circ.measure(1, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)):
    						main_circ.barrier(0)
    					main_circ.cz(3,qreg_0[0])
    					main_circ.barrier(2)
    				with case_2(1):
    					main_circ.append(subcirc2,[2,3,qreg_0[0],1])
    main_circ.measure(2, creg_1[0])
    with main_circ.if_test((creg_1[0],0)) as else_4:
    	main_circ.measure(qreg_0[1], creg_0[0])
    	with main_circ.if_test((creg_0[0],0)) as else_3:
    		main_circ.measure(3, creg_1[0])
    		with main_circ.if_test((creg_1[0],0)):
    			main_circ.id(2)
    		main_circ.measure(qreg_0[1], creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_2:
    			with case_2(0):
    				main_circ.measure(0, creg_1[0])
    				with main_circ.if_test((creg_1[0],0)) as else_1:
    					main_circ.u(0,0,0.124000, 3)
    					main_circ.barrier(3)
    				with else_1:
    					main_circ.cy(qreg_0[1],3)
    					main_circ.cy(qreg_0[0],2)
    					main_circ.append(subcirc2,[0,3,qreg_0[0],2])
    			with case_2(1):
    				main_circ.measure(3, creg_1[0])
    				with main_circ.if_test((creg_1[0],0)):
    					main_circ.append(subcirc2,[1,qreg_0[1],0,qreg_0[0]])
    	with else_3:
    		main_circ.measure(2, creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_2:
    			with case_2(0):
    				main_circ.measure(qreg_0[1], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.u(0,0,-0.343000, qreg_0[1])
    					main_circ.u(pi/2,-0.157000,-0.184000, 2)
    					main_circ.id(qreg_0[1])
    				with else_1:
    					main_circ.u(0,0,param_1, qreg_0[0])
    					main_circ.append(subcirc2,[0,1,3,2])
    			with case_2(1):
    				main_circ.measure(2, creg_1[0])
    				with main_circ.if_test((creg_1[0],0)):
    					main_circ.id(qreg_0[0])
    				main_circ.id(3)
    with else_4:
    	main_circ.barrier(2)
    bindings = {param_0: 0.634000, param_1: -0.908000, param_2: 0.793000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_on_simulator(main_circ, "11")


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
