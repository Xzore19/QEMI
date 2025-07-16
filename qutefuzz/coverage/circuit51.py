
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi


def main():
    
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
    
    main_circ.measure(0, creg_0[0])
    with main_circ.if_test((creg_0[0],0)):
    	main_circ.z(0)
    	main_circ.measure(2, creg_0[0])
    	with main_circ.if_test((creg_0[0],0)):
    		main_circ.measure(qreg_0[0], creg_0[1])
    		with main_circ.if_test((creg_0[1],0)) as else_2:
    			main_circ.measure(qreg_1[0], creg_0[0])
    			with main_circ.if_test((creg_0[0],0)) as else_1:
    				main_circ.rx(param_2, 1)
    			with else_1:
    				main_circ.z(2)
    				main_circ.ry(param_2, qreg_1[0])
    		with else_2:
    			main_circ.measure(1, creg_0[1])
    			with main_circ.switch(creg_0[1]) as case_1:
    				with case_1(0):
    					main_circ.rz(param_0, 1)
    					main_circ.ry(0.805000, 0)
    					main_circ.rx(0.277000, 3)
    					main_circ.rx(-0.393000, 0)
    				with case_1(1):
    					main_circ.z(1)
    					main_circ.z(qreg_1[0])
    					main_circ.rx(-0.143000, qreg_1[0])
    					main_circ.ry(param_0, 3)
    main_circ.measure(3, creg_0[0])
    with main_circ.if_test((creg_0[0],0)) as else_4:
    	main_circ.measure(qreg_1[0], creg_0[1])
    	with main_circ.if_test((creg_0[1],0)):
    		main_circ.measure(0, creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_2:
    			with case_2(0):
    				main_circ.measure(qreg_0[0], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.z(qreg_1[0])
    					main_circ.ry(-0.810000, 1)
    				with else_1:
    					main_circ.z(0)
    				main_circ.measure(3, creg_0[0])
    				with main_circ.switch(creg_0[0]) as case_1:
    					with case_1(0):
    						main_circ.rz(param_1, qreg_1[0])
    						main_circ.rx(param_0, qreg_0[0])
    						main_circ.rx(param_1, 2)
    						main_circ.rx(-0.668000, qreg_0[0])
    					with case_1(1):
    						main_circ.rz(-0.474000, 2)
    						main_circ.rz(0.178000, qreg_0[0])
    						main_circ.ry(-0.429000, 1)
    						main_circ.z(2)
    			with case_2(1):
    				main_circ.measure(0, creg_0[1])
    				with main_circ.if_test((creg_0[1],0)) as else_1:
    					main_circ.rz(0.643000, 3)
    					main_circ.ry(param_2, 2)
    					main_circ.z(2)
    					main_circ.ry(0.536000, qreg_1[0])
    					main_circ.ry(0.469000, qreg_1[0])
    				with else_1:
    					main_circ.ry(param_1, 0)
    					main_circ.rx(param_2, 0)
    with else_4:
    	main_circ.measure(3, creg_0[0])
    	with main_circ.if_test((creg_0[0],0)) as else_3:
    		main_circ.measure(2, creg_0[0])
    		with main_circ.if_test((creg_0[0],0)):
    			main_circ.measure(1, creg_0[0])
    			with main_circ.switch(creg_0[0]) as case_1:
    				with case_1(0):
    					main_circ.rx(0.049000, 2)
    					main_circ.z(qreg_0[0])
    					main_circ.rx(-0.896000, qreg_0[0])
    					main_circ.ry(param_2, 2)
    				with case_1(1):
    					main_circ.z(qreg_0[0])
    					main_circ.rz(param_0, qreg_0[0])
    					main_circ.rx(-0.140000, qreg_1[0])
    					main_circ.rz(param_0, 3)
    	with else_3:
    		main_circ.measure(qreg_0[0], creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_2:
    			with case_2(0):
    				main_circ.measure(1, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.rx(param_0, 0)
    					main_circ.rz(param_1, qreg_1[0])
    				main_circ.measure(3, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.rx(param_2, qreg_1[0])
    				with else_1:
    					main_circ.rz(param_1, 1)
    			with case_2(1):
    				main_circ.measure(1, creg_0[1])
    				with main_circ.if_test((creg_0[1],0)):
    					main_circ.z(2)
    					main_circ.rz(-0.141000, qreg_0[0])
    					main_circ.z(3)
    					main_circ.rz(param_2, 2)
    main_circ.measure(qreg_1[0], creg_0[0])
    with main_circ.switch(creg_0[0]) as case_4:
    	with case_4(0):
    		main_circ.measure(qreg_0[0], creg_0[1])
    		with main_circ.if_test((creg_0[1],0)) as else_3:
    			main_circ.measure(2, creg_0[1])
    			with main_circ.if_test((creg_0[1],0)) as else_2:
    				main_circ.ry(param_1, qreg_1[0])
    				main_circ.measure(3, creg_0[1])
    				with main_circ.if_test((creg_0[1],0)) as else_1:
    					main_circ.ry(param_2, qreg_0[0])
    					main_circ.rz(0.129000, 3)
    					main_circ.ry(0.401000, qreg_1[0])
    					main_circ.ry(0.559000, 2)
    					main_circ.rx(-0.996000, qreg_1[0])
    				with else_1:
    					main_circ.rz(0.512000, 1)
    					main_circ.rx(0.305000, qreg_0[0])
    			with else_2:
    				main_circ.measure(qreg_1[0], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.ry(param_1, 3)
    					main_circ.ry(param_2, qreg_0[0])
    					main_circ.rx(-0.731000, qreg_0[0])
    					main_circ.id(1)
    		with else_3:
    			main_circ.measure(2, creg_0[0])
    			with main_circ.switch(creg_0[0]) as case_2:
    				with case_2(0):
    					main_circ.id(3)
    				with case_2(1):
    					main_circ.measure(1, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)) as else_1:
    						main_circ.barrier(1)
    					with else_1:
    						main_circ.barrier(qreg_0[0])
    					main_circ.measure(3, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)) as else_1:
    						main_circ.barrier(2)
    					with else_1:
    						main_circ.barrier(2)
    					main_circ.measure(qreg_0[0], creg_0[1])
    					with main_circ.switch(creg_0[1]) as case_1:
    						with case_1(0):
    							main_circ.id(1)
    						with case_1(1):
    							main_circ.barrier(1)
    					main_circ.measure(qreg_0[0], creg_0[0])
    					with main_circ.switch(creg_0[0]) as case_1:
    						with case_1(0):
    							main_circ.barrier(2)
    						with case_1(1):
    							main_circ.id(1)
    					main_circ.measure(qreg_0[0], creg_0[0])
    					with main_circ.if_test((creg_0[0],0)) as else_1:
    						main_circ.barrier(3)
    					with else_1:
    						main_circ.id(3)
    					main_circ.barrier(qreg_0[0])
    			main_circ.measure(2, creg_0[0])
    			with main_circ.if_test((creg_0[0],0)):
    				main_circ.measure(3, creg_0[1])
    				with main_circ.if_test((creg_0[1],0)) as else_1:
    					main_circ.id(2)
    				with else_1:
    					main_circ.barrier(qreg_1[0])
    				main_circ.measure(3, creg_0[1])
    				with main_circ.if_test((creg_0[1],0)) as else_1:
    					main_circ.id(1)
    				with else_1:
    					main_circ.id(1)
    				main_circ.measure(qreg_1[0], creg_0[1])
    				with main_circ.switch(creg_0[1]) as case_1:
    					with case_1(0):
    						main_circ.barrier(2)
    					with case_1(1):
    						main_circ.id(3)
    				main_circ.measure(qreg_0[0], creg_0[1])
    				with main_circ.switch(creg_0[1]) as case_1:
    					with case_1(0):
    						main_circ.id(qreg_1[0])
    					with case_1(1):
    						main_circ.barrier(qreg_0[0])
    				main_circ.measure(1, creg_0[1])
    				with main_circ.switch(creg_0[1]) as case_1:
    					with case_1(0):
    						main_circ.barrier(qreg_1[0])
    					with case_1(1):
    						main_circ.barrier(qreg_0[0])
    				main_circ.measure(1, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.id(3)
    				with else_1:
    					main_circ.barrier(0)
    				main_circ.measure(0, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.barrier(1)
    				main_circ.id(1)
    			main_circ.measure(0, creg_0[1])
    			with main_circ.if_test((creg_0[1],0)):
    				main_circ.measure(qreg_0[0], creg_0[1])
    				with main_circ.switch(creg_0[1]) as case_1:
    					with case_1(0):
    						main_circ.barrier(1)
    					with case_1(1):
    						main_circ.id(qreg_1[0])
    				main_circ.measure(3, creg_0[1])
    				with main_circ.if_test((creg_0[1],0)):
    					main_circ.barrier(qreg_1[0])
    				main_circ.measure(2, creg_0[1])
    				with main_circ.if_test((creg_0[1],0)):
    					main_circ.barrier(2)
    				main_circ.measure(0, creg_0[0])
    				with main_circ.switch(creg_0[0]) as case_1:
    					with case_1(0):
    						main_circ.id(2)
    					with case_1(1):
    						main_circ.barrier(1)
    				main_circ.measure(2, creg_0[1])
    				with main_circ.if_test((creg_0[1],0)) as else_1:
    					main_circ.barrier(qreg_0[0])
    				with else_1:
    					main_circ.id(3)
    				main_circ.barrier(qreg_0[0])
    			main_circ.barrier(3)
    	with case_4(1):
    		main_circ.measure(qreg_1[0], creg_0[1])
    		with main_circ.switch(creg_0[1]) as case_3:
    			with case_3(0):
    				main_circ.measure(qreg_1[0], creg_0[1])
    				with main_circ.switch(creg_0[1]) as case_2:
    					with case_2(0):
    						main_circ.measure(0, creg_0[0])
    						with main_circ.switch(creg_0[0]) as case_1:
    							with case_1(0):
    								main_circ.id(2)
    							with case_1(1):
    								main_circ.id(3)
    						main_circ.barrier(3)
    					with case_2(1):
    						main_circ.measure(1, creg_0[1])
    						with main_circ.if_test((creg_0[1],0)) as else_1:
    							main_circ.id(qreg_1[0])
    						with else_1:
    							main_circ.id(2)
    						main_circ.barrier(3)
    				main_circ.measure(3, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_2:
    					main_circ.measure(0, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)):
    						main_circ.barrier(2)
    					main_circ.measure(qreg_0[0], creg_0[0])
    					with main_circ.if_test((creg_0[0],0)):
    						main_circ.id(2)
    					main_circ.measure(qreg_1[0], creg_0[1])
    					with main_circ.if_test((creg_0[1],0)):
    						main_circ.id(1)
    					main_circ.measure(qreg_0[0], creg_0[1])
    					with main_circ.if_test((creg_0[1],0)):
    						main_circ.id(2)
    					main_circ.measure(3, creg_0[1])
    					with main_circ.switch(creg_0[1]) as case_1:
    						with case_1(0):
    							main_circ.id(2)
    						with case_1(1):
    							main_circ.id(qreg_0[0])
    					main_circ.measure(2, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)) as else_1:
    						main_circ.id(qreg_0[0])
    					with else_1:
    						main_circ.id(3)
    					main_circ.measure(qreg_0[0], creg_0[0])
    					with main_circ.if_test((creg_0[0],0)) as else_1:
    						main_circ.id(2)
    					with else_1:
    						main_circ.barrier(qreg_0[0])
    					main_circ.measure(2, creg_0[0])
    					with main_circ.switch(creg_0[0]) as case_1:
    						with case_1(0):
    							main_circ.id(3)
    						with case_1(1):
    							main_circ.barrier(1)
    					main_circ.measure(3, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)) as else_1:
    						main_circ.barrier(2)
    					with else_1:
    						main_circ.barrier(0)
    					main_circ.measure(qreg_1[0], creg_0[1])
    					with main_circ.if_test((creg_0[1],0)) as else_1:
    						main_circ.barrier(qreg_0[0])
    					with else_1:
    						main_circ.id(2)
    					main_circ.measure(3, creg_0[0])
    					with main_circ.switch(creg_0[0]) as case_1:
    						with case_1(0):
    							main_circ.id(2)
    						with case_1(1):
    							main_circ.id(qreg_0[0])
    					main_circ.barrier(1)
    				with else_2:
    					main_circ.id(qreg_0[0])
    				main_circ.measure(qreg_1[0], creg_0[0])
    				with main_circ.switch(creg_0[0]) as case_2:
    					with case_2(0):
    						main_circ.measure(0, creg_0[1])
    						with main_circ.if_test((creg_0[1],0)) as else_1:
    							main_circ.barrier(3)
    						with else_1:
    							main_circ.barrier(qreg_1[0])
    						main_circ.measure(0, creg_0[0])
    						with main_circ.if_test((creg_0[0],0)) as else_1:
    							main_circ.id(qreg_1[0])
    						with else_1:
    							main_circ.barrier(0)
    						main_circ.measure(qreg_0[0], creg_0[1])
    						with main_circ.if_test((creg_0[1],0)) as else_1:
    							main_circ.id(1)
    						with else_1:
    							main_circ.id(1)
    						main_circ.measure(3, creg_0[0])
    						with main_circ.if_test((creg_0[0],0)):
    							main_circ.barrier(qreg_1[0])
    						main_circ.measure(3, creg_0[0])
    						with main_circ.switch(creg_0[0]) as case_1:
    							with case_1(0):
    								main_circ.barrier(qreg_1[0])
    							with case_1(1):
    								main_circ.id(3)
    						main_circ.id(2)
    					with case_2(1):
    						main_circ.measure(3, creg_0[0])
    						with main_circ.if_test((creg_0[0],0)) as else_1:
    							main_circ.barrier(0)
    						with else_1:
    							main_circ.barrier(2)
    						main_circ.measure(qreg_1[0], creg_0[0])
    						with main_circ.if_test((creg_0[0],0)):
    							main_circ.barrier(1)
    						main_circ.measure(1, creg_0[0])
    						with main_circ.if_test((creg_0[0],0)):
    							main_circ.barrier(1)
    						main_circ.measure(qreg_1[0], creg_0[1])
    						with main_circ.if_test((creg_0[1],0)) as else_1:
    							main_circ.barrier(3)
    						with else_1:
    							main_circ.id(0)
    						main_circ.measure(0, creg_0[0])
    						with main_circ.if_test((creg_0[0],0)):
    							main_circ.barrier(qreg_1[0])
    						main_circ.measure(qreg_0[0], creg_0[0])
    						with main_circ.switch(creg_0[0]) as case_1:
    							with case_1(0):
    								main_circ.barrier(qreg_1[0])
    							with case_1(1):
    								main_circ.id(1)
    						main_circ.measure(qreg_1[0], creg_0[0])
    						with main_circ.if_test((creg_0[0],0)):
    							main_circ.barrier(qreg_0[0])
    						main_circ.measure(2, creg_0[0])
    						with main_circ.if_test((creg_0[0],0)):
    							main_circ.barrier(qreg_0[0])
    						main_circ.id(2)
    				main_circ.measure(1, creg_0[0])
    				with main_circ.switch(creg_0[0]) as case_2:
    					with case_2(0):
    						main_circ.measure(0, creg_0[1])
    						with main_circ.if_test((creg_0[1],0)) as else_1:
    							main_circ.barrier(3)
    						with else_1:
    							main_circ.barrier(0)
    						main_circ.measure(3, creg_0[1])
    						with main_circ.if_test((creg_0[1],0)) as else_1:
    							main_circ.id(0)
    						with else_1:
    							main_circ.barrier(2)
    						main_circ.measure(1, creg_0[1])
    						with main_circ.if_test((creg_0[1],0)) as else_1:
    							main_circ.id(0)
    						with else_1:
    							main_circ.id(3)
    						main_circ.measure(qreg_0[0], creg_0[0])
    						with main_circ.switch(creg_0[0]) as case_1:
    							with case_1(0):
    								main_circ.barrier(qreg_1[0])
    							with case_1(1):
    								main_circ.barrier(qreg_0[0])
    						main_circ.measure(0, creg_0[0])
    						with main_circ.switch(creg_0[0]) as case_1:
    							with case_1(0):
    								main_circ.barrier(qreg_0[0])
    							with case_1(1):
    								main_circ.barrier(qreg_1[0])
    						main_circ.measure(qreg_1[0], creg_0[1])
    						with main_circ.if_test((creg_0[1],0)) as else_1:
    							main_circ.barrier(1)
    						with else_1:
    							main_circ.id(1)
    						main_circ.measure(qreg_1[0], creg_0[1])
    						with main_circ.if_test((creg_0[1],0)):
    							main_circ.barrier(qreg_1[0])
    						main_circ.barrier(3)
    					with case_2(1):
    						main_circ.id(1)
    				main_circ.measure(1, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_2:
    					main_circ.measure(3, creg_0[1])
    					with main_circ.switch(creg_0[1]) as case_1:
    						with case_1(0):
    							main_circ.id(0)
    						with case_1(1):
    							main_circ.id(qreg_0[0])
    					main_circ.measure(qreg_0[0], creg_0[1])
    					with main_circ.if_test((creg_0[1],0)) as else_1:
    						main_circ.barrier(qreg_1[0])
    					with else_1:
    						main_circ.barrier(1)
    					main_circ.measure(0, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)):
    						main_circ.id(0)
    					main_circ.measure(qreg_1[0], creg_0[0])
    					with main_circ.switch(creg_0[0]) as case_1:
    						with case_1(0):
    							main_circ.barrier(3)
    						with case_1(1):
    							main_circ.id(qreg_0[0])
    					main_circ.barrier(2)
    				with else_2:
    					main_circ.id(2)
    				main_circ.measure(2, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_2:
    					main_circ.id(2)
    				with else_2:
    					main_circ.measure(qreg_1[0], creg_0[0])
    					with main_circ.if_test((creg_0[0],0)):
    						main_circ.id(1)
    					main_circ.measure(0, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)):
    						main_circ.id(1)
    					main_circ.id(2)
    				main_circ.id(qreg_1[0])
    			with case_3(1):
    				main_circ.id(2)
    		main_circ.measure(2, creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_3:
    			with case_3(0):
    				main_circ.measure(1, creg_0[1])
    				with main_circ.if_test((creg_0[1],0)):
    					main_circ.measure(0, creg_0[0])
    					with main_circ.switch(creg_0[0]) as case_1:
    						with case_1(0):
    							main_circ.barrier(2)
    						with case_1(1):
    							main_circ.barrier(0)
    					main_circ.measure(3, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)) as else_1:
    						main_circ.barrier(3)
    					with else_1:
    						main_circ.barrier(qreg_0[0])
    					main_circ.measure(qreg_1[0], creg_0[1])
    					with main_circ.switch(creg_0[1]) as case_1:
    						with case_1(0):
    							main_circ.barrier(3)
    						with case_1(1):
    							main_circ.id(qreg_1[0])
    					main_circ.barrier(1)
    				main_circ.measure(qreg_0[0], creg_0[1])
    				with main_circ.if_test((creg_0[1],0)):
    					main_circ.measure(qreg_0[0], creg_0[1])
    					with main_circ.if_test((creg_0[1],0)) as else_1:
    						main_circ.barrier(0)
    					with else_1:
    						main_circ.id(3)
    					main_circ.measure(1, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)) as else_1:
    						main_circ.id(qreg_1[0])
    					with else_1:
    						main_circ.id(3)
    					main_circ.measure(qreg_1[0], creg_0[1])
    					with main_circ.if_test((creg_0[1],0)) as else_1:
    						main_circ.barrier(qreg_1[0])
    					with else_1:
    						main_circ.id(3)
    					main_circ.measure(2, creg_0[0])
    					with main_circ.switch(creg_0[0]) as case_1:
    						with case_1(0):
    							main_circ.barrier(qreg_0[0])
    						with case_1(1):
    							main_circ.barrier(1)
    					main_circ.measure(3, creg_0[1])
    					with main_circ.switch(creg_0[1]) as case_1:
    						with case_1(0):
    							main_circ.id(qreg_1[0])
    						with case_1(1):
    							main_circ.barrier(2)
    					main_circ.measure(0, creg_0[1])
    					with main_circ.switch(creg_0[1]) as case_1:
    						with case_1(0):
    							main_circ.id(3)
    						with case_1(1):
    							main_circ.barrier(qreg_1[0])
    					main_circ.measure(qreg_0[0], creg_0[1])
    					with main_circ.if_test((creg_0[1],0)) as else_1:
    						main_circ.id(0)
    					with else_1:
    						main_circ.barrier(0)
    					main_circ.barrier(0)
    				main_circ.measure(0, creg_0[0])
    				with main_circ.switch(creg_0[0]) as case_2:
    					with case_2(0):
    						main_circ.measure(2, creg_0[1])
    						with main_circ.if_test((creg_0[1],0)) as else_1:
    							main_circ.id(1)
    						with else_1:
    							main_circ.id(qreg_0[0])
    						main_circ.measure(1, creg_0[1])
    						with main_circ.switch(creg_0[1]) as case_1:
    							with case_1(0):
    								main_circ.barrier(qreg_1[0])
    							with case_1(1):
    								main_circ.barrier(1)
    						main_circ.measure(2, creg_0[0])
    						with main_circ.switch(creg_0[0]) as case_1:
    							with case_1(0):
    								main_circ.id(1)
    							with case_1(1):
    								main_circ.id(1)
    						main_circ.measure(qreg_0[0], creg_0[0])
    						with main_circ.if_test((creg_0[0],0)) as else_1:
    							main_circ.id(3)
    						with else_1:
    							main_circ.barrier(qreg_0[0])
    						main_circ.measure(1, creg_0[1])
    						with main_circ.if_test((creg_0[1],0)) as else_1:
    							main_circ.barrier(2)
    						with else_1:
    							main_circ.id(1)
    						main_circ.measure(qreg_1[0], creg_0[1])
    						with main_circ.if_test((creg_0[1],0)):
    							main_circ.barrier(1)
    						main_circ.barrier(3)
    					with case_2(1):
    						main_circ.measure(3, creg_0[0])
    						with main_circ.switch(creg_0[0]) as case_1:
    							with case_1(0):
    								main_circ.id(qreg_0[0])
    							with case_1(1):
    								main_circ.barrier(qreg_0[0])
    						main_circ.barrier(0)
    				main_circ.measure(qreg_0[0], creg_0[1])
    				with main_circ.switch(creg_0[1]) as case_2:
    					with case_2(0):
    						main_circ.measure(qreg_0[0], creg_0[1])
    						with main_circ.if_test((creg_0[1],0)) as else_1:
    							main_circ.id(3)
    						with else_1:
    							main_circ.barrier(0)
    						main_circ.id(qreg_1[0])
    					with case_2(1):
    						main_circ.measure(0, creg_0[0])
    						with main_circ.switch(creg_0[0]) as case_1:
    							with case_1(0):
    								main_circ.barrier(qreg_1[0])
    							with case_1(1):
    								main_circ.barrier(qreg_0[0])
    						main_circ.measure(0, creg_0[0])
    						with main_circ.if_test((creg_0[0],0)) as else_1:
    							main_circ.barrier(qreg_0[0])
    						with else_1:
    							main_circ.id(3)
    						main_circ.measure(2, creg_0[0])
    						with main_circ.if_test((creg_0[0],0)):
    							main_circ.barrier(qreg_1[0])
    						main_circ.measure(2, creg_0[0])
    						with main_circ.switch(creg_0[0]) as case_1:
    							with case_1(0):
    								main_circ.id(qreg_1[0])
    							with case_1(1):
    								main_circ.id(0)
    						main_circ.measure(2, creg_0[1])
    						with main_circ.switch(creg_0[1]) as case_1:
    							with case_1(0):
    								main_circ.id(1)
    							with case_1(1):
    								main_circ.id(3)
    						main_circ.measure(qreg_1[0], creg_0[0])
    						with main_circ.if_test((creg_0[0],0)):
    							main_circ.barrier(2)
    						main_circ.measure(3, creg_0[0])
    						with main_circ.if_test((creg_0[0],0)) as else_1:
    							main_circ.barrier(qreg_1[0])
    						with else_1:
    							main_circ.barrier(3)
    						main_circ.id(qreg_1[0])
    				main_circ.measure(qreg_1[0], creg_0[1])
    				with main_circ.if_test((creg_0[1],0)):
    					main_circ.id(qreg_1[0])
    				main_circ.id(qreg_0[0])
    			with case_3(1):
    				main_circ.measure(3, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_2:
    					main_circ.measure(qreg_1[0], creg_0[0])
    					with main_circ.if_test((creg_0[0],0)) as else_1:
    						main_circ.id(qreg_1[0])
    					with else_1:
    						main_circ.barrier(3)
    					main_circ.measure(3, creg_0[1])
    					with main_circ.switch(creg_0[1]) as case_1:
    						with case_1(0):
    							main_circ.id(3)
    						with case_1(1):
    							main_circ.barrier(3)
    					main_circ.measure(qreg_0[0], creg_0[1])
    					with main_circ.switch(creg_0[1]) as case_1:
    						with case_1(0):
    							main_circ.id(0)
    						with case_1(1):
    							main_circ.id(2)
    					main_circ.barrier(3)
    				with else_2:
    					main_circ.measure(3, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)) as else_1:
    						main_circ.id(0)
    					with else_1:
    						main_circ.barrier(0)
    					main_circ.measure(qreg_1[0], creg_0[0])
    					with main_circ.switch(creg_0[0]) as case_1:
    						with case_1(0):
    							main_circ.id(1)
    						with case_1(1):
    							main_circ.id(qreg_0[0])
    					main_circ.measure(3, creg_0[0])
    					with main_circ.switch(creg_0[0]) as case_1:
    						with case_1(0):
    							main_circ.id(3)
    						with case_1(1):
    							main_circ.barrier(0)
    					main_circ.measure(1, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)):
    						main_circ.barrier(0)
    					main_circ.measure(3, creg_0[1])
    					with main_circ.switch(creg_0[1]) as case_1:
    						with case_1(0):
    							main_circ.barrier(1)
    						with case_1(1):
    							main_circ.barrier(3)
    					main_circ.measure(1, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)):
    						main_circ.id(1)
    					main_circ.measure(qreg_1[0], creg_0[0])
    					with main_circ.switch(creg_0[0]) as case_1:
    						with case_1(0):
    							main_circ.barrier(qreg_1[0])
    						with case_1(1):
    							main_circ.id(3)
    					main_circ.measure(2, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)) as else_1:
    						main_circ.id(qreg_1[0])
    					with else_1:
    						main_circ.id(qreg_1[0])
    					main_circ.measure(1, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)) as else_1:
    						main_circ.id(1)
    					with else_1:
    						main_circ.barrier(1)
    					main_circ.measure(1, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)):
    						main_circ.id(1)
    					main_circ.measure(1, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)):
    						main_circ.id(qreg_1[0])
    					main_circ.measure(3, creg_0[1])
    					with main_circ.switch(creg_0[1]) as case_1:
    						with case_1(0):
    							main_circ.barrier(1)
    						with case_1(1):
    							main_circ.id(0)
    					main_circ.measure(qreg_0[0], creg_0[0])
    					with main_circ.switch(creg_0[0]) as case_1:
    						with case_1(0):
    							main_circ.barrier(3)
    						with case_1(1):
    							main_circ.barrier(2)
    					main_circ.measure(1, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)) as else_1:
    						main_circ.barrier(qreg_0[0])
    					with else_1:
    						main_circ.barrier(qreg_0[0])
    					main_circ.measure(1, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)):
    						main_circ.barrier(qreg_0[0])
    					main_circ.measure(qreg_1[0], creg_0[1])
    					with main_circ.if_test((creg_0[1],0)):
    						main_circ.id(3)
    					main_circ.measure(qreg_1[0], creg_0[0])
    					with main_circ.switch(creg_0[0]) as case_1:
    						with case_1(0):
    							main_circ.id(2)
    						with case_1(1):
    							main_circ.id(2)
    					main_circ.measure(1, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)):
    						main_circ.id(2)
    					main_circ.barrier(qreg_0[0])
    				main_circ.measure(0, creg_0[0])
    				with main_circ.switch(creg_0[0]) as case_2:
    					with case_2(0):
    						main_circ.measure(qreg_1[0], creg_0[0])
    						with main_circ.if_test((creg_0[0],0)):
    							main_circ.barrier(1)
    						main_circ.id(0)
    					with case_2(1):
    						main_circ.measure(2, creg_0[1])
    						with main_circ.switch(creg_0[1]) as case_1:
    							with case_1(0):
    								main_circ.barrier(0)
    							with case_1(1):
    								main_circ.barrier(2)
    						main_circ.measure(qreg_1[0], creg_0[0])
    						with main_circ.if_test((creg_0[0],0)) as else_1:
    							main_circ.barrier(qreg_1[0])
    						with else_1:
    							main_circ.id(3)
    						main_circ.id(2)
    				main_circ.measure(qreg_0[0], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_2:
    					main_circ.measure(3, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)):
    						main_circ.id(3)
    					main_circ.measure(1, creg_0[1])
    					with main_circ.switch(creg_0[1]) as case_1:
    						with case_1(0):
    							main_circ.barrier(0)
    						with case_1(1):
    							main_circ.id(3)
    					main_circ.measure(0, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)) as else_1:
    						main_circ.id(qreg_1[0])
    					with else_1:
    						main_circ.id(1)
    					main_circ.measure(qreg_0[0], creg_0[0])
    					with main_circ.switch(creg_0[0]) as case_1:
    						with case_1(0):
    							main_circ.id(qreg_0[0])
    						with case_1(1):
    							main_circ.barrier(qreg_1[0])
    					main_circ.measure(2, creg_0[0])
    					with main_circ.switch(creg_0[0]) as case_1:
    						with case_1(0):
    							main_circ.id(qreg_1[0])
    						with case_1(1):
    							main_circ.id(1)
    					main_circ.barrier(2)
    				with else_2:
    					main_circ.measure(qreg_0[0], creg_0[0])
    					with main_circ.switch(creg_0[0]) as case_1:
    						with case_1(0):
    							main_circ.id(2)
    						with case_1(1):
    							main_circ.id(qreg_1[0])
    					main_circ.measure(0, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)) as else_1:
    						main_circ.barrier(qreg_1[0])
    					with else_1:
    						main_circ.id(2)
    					main_circ.measure(1, creg_0[0])
    					with main_circ.switch(creg_0[0]) as case_1:
    						with case_1(0):
    							main_circ.barrier(0)
    						with case_1(1):
    							main_circ.barrier(qreg_1[0])
    					main_circ.id(qreg_1[0])
    				main_circ.measure(1, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.measure(1, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)) as else_1:
    						main_circ.barrier(qreg_1[0])
    					with else_1:
    						main_circ.barrier(qreg_0[0])
    					main_circ.id(0)
    				main_circ.measure(qreg_0[0], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_2:
    					main_circ.measure(3, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)) as else_1:
    						main_circ.id(0)
    					with else_1:
    						main_circ.id(2)
    					main_circ.measure(2, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)) as else_1:
    						main_circ.barrier(0)
    					with else_1:
    						main_circ.barrier(qreg_1[0])
    					main_circ.measure(3, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)):
    						main_circ.id(1)
    					main_circ.barrier(2)
    				with else_2:
    					main_circ.measure(0, creg_0[1])
    					with main_circ.switch(creg_0[1]) as case_1:
    						with case_1(0):
    							main_circ.id(qreg_0[0])
    						with case_1(1):
    							main_circ.barrier(qreg_1[0])
    					main_circ.barrier(qreg_1[0])
    				main_circ.measure(2, creg_0[1])
    				with main_circ.if_test((creg_0[1],0)) as else_2:
    					main_circ.measure(qreg_1[0], creg_0[1])
    					with main_circ.if_test((creg_0[1],0)) as else_1:
    						main_circ.barrier(qreg_0[0])
    					with else_1:
    						main_circ.barrier(2)
    					main_circ.measure(qreg_0[0], creg_0[0])
    					with main_circ.switch(creg_0[0]) as case_1:
    						with case_1(0):
    							main_circ.barrier(qreg_0[0])
    						with case_1(1):
    							main_circ.barrier(0)
    					main_circ.measure(qreg_1[0], creg_0[1])
    					with main_circ.if_test((creg_0[1],0)):
    						main_circ.barrier(0)
    					main_circ.measure(qreg_1[0], creg_0[1])
    					with main_circ.if_test((creg_0[1],0)) as else_1:
    						main_circ.barrier(0)
    					with else_1:
    						main_circ.id(qreg_0[0])
    					main_circ.id(2)
    				with else_2:
    					main_circ.measure(1, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)) as else_1:
    						main_circ.barrier(qreg_1[0])
    					with else_1:
    						main_circ.id(2)
    					main_circ.measure(qreg_1[0], creg_0[1])
    					with main_circ.switch(creg_0[1]) as case_1:
    						with case_1(0):
    							main_circ.barrier(0)
    						with case_1(1):
    							main_circ.barrier(qreg_1[0])
    					main_circ.measure(2, creg_0[0])
    					with main_circ.switch(creg_0[0]) as case_1:
    						with case_1(0):
    							main_circ.barrier(qreg_1[0])
    						with case_1(1):
    							main_circ.barrier(3)
    					main_circ.id(qreg_0[0])
    				main_circ.measure(1, creg_0[1])
    				with main_circ.switch(creg_0[1]) as case_2:
    					with case_2(0):
    						main_circ.barrier(3)
    					with case_2(1):
    						main_circ.measure(qreg_0[0], creg_0[0])
    						with main_circ.if_test((creg_0[0],0)) as else_1:
    							main_circ.id(0)
    						with else_1:
    							main_circ.id(2)
    						main_circ.id(qreg_0[0])
    				main_circ.measure(0, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.measure(qreg_1[0], creg_0[0])
    					with main_circ.if_test((creg_0[0],0)) as else_1:
    						main_circ.id(0)
    					with else_1:
    						main_circ.id(qreg_0[0])
    					main_circ.measure(0, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)):
    						main_circ.barrier(3)
    					main_circ.measure(3, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)) as else_1:
    						main_circ.id(qreg_0[0])
    					with else_1:
    						main_circ.id(1)
    					main_circ.measure(qreg_1[0], creg_0[1])
    					with main_circ.if_test((creg_0[1],0)):
    						main_circ.id(1)
    					main_circ.measure(3, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)) as else_1:
    						main_circ.id(1)
    					with else_1:
    						main_circ.barrier(1)
    					main_circ.barrier(1)
    				main_circ.measure(3, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.measure(qreg_0[0], creg_0[1])
    					with main_circ.if_test((creg_0[1],0)):
    						main_circ.barrier(2)
    					main_circ.measure(qreg_0[0], creg_0[0])
    					with main_circ.if_test((creg_0[0],0)):
    						main_circ.barrier(0)
    					main_circ.barrier(qreg_1[0])
    				main_circ.measure(3, creg_0[0])
    				with main_circ.switch(creg_0[0]) as case_2:
    					with case_2(0):
    						main_circ.id(qreg_1[0])
    					with case_2(1):
    						main_circ.measure(qreg_1[0], creg_0[0])
    						with main_circ.if_test((creg_0[0],0)):
    							main_circ.barrier(1)
    						main_circ.measure(qreg_0[0], creg_0[0])
    						with main_circ.if_test((creg_0[0],0)) as else_1:
    							main_circ.barrier(1)
    						with else_1:
    							main_circ.barrier(qreg_0[0])
    						main_circ.measure(2, creg_0[1])
    						with main_circ.switch(creg_0[1]) as case_1:
    							with case_1(0):
    								main_circ.barrier(3)
    							with case_1(1):
    								main_circ.id(qreg_0[0])
    						main_circ.barrier(qreg_1[0])
    				main_circ.measure(0, creg_0[1])
    				with main_circ.if_test((creg_0[1],0)):
    					main_circ.measure(0, creg_0[0])
    					with main_circ.switch(creg_0[0]) as case_1:
    						with case_1(0):
    							main_circ.id(qreg_1[0])
    						with case_1(1):
    							main_circ.id(0)
    					main_circ.measure(3, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)):
    						main_circ.barrier(0)
    					main_circ.measure(1, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)) as else_1:
    						main_circ.id(2)
    					with else_1:
    						main_circ.id(qreg_0[0])
    					main_circ.measure(1, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)) as else_1:
    						main_circ.id(2)
    					with else_1:
    						main_circ.barrier(0)
    					main_circ.measure(0, creg_0[0])
    					with main_circ.switch(creg_0[0]) as case_1:
    						with case_1(0):
    							main_circ.barrier(2)
    						with case_1(1):
    							main_circ.id(qreg_1[0])
    					main_circ.barrier(0)
    				main_circ.measure(2, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_2:
    					main_circ.measure(3, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)) as else_1:
    						main_circ.id(3)
    					with else_1:
    						main_circ.id(qreg_0[0])
    					main_circ.measure(2, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)):
    						main_circ.id(0)
    					main_circ.measure(qreg_1[0], creg_0[0])
    					with main_circ.if_test((creg_0[0],0)):
    						main_circ.barrier(qreg_0[0])
    					main_circ.measure(2, creg_0[0])
    					with main_circ.switch(creg_0[0]) as case_1:
    						with case_1(0):
    							main_circ.barrier(3)
    						with case_1(1):
    							main_circ.id(qreg_0[0])
    					main_circ.measure(3, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)):
    						main_circ.id(3)
    					main_circ.measure(1, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)):
    						main_circ.barrier(0)
    					main_circ.measure(0, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)):
    						main_circ.barrier(3)
    					main_circ.measure(1, creg_0[1])
    					with main_circ.switch(creg_0[1]) as case_1:
    						with case_1(0):
    							main_circ.barrier(qreg_0[0])
    						with case_1(1):
    							main_circ.barrier(1)
    					main_circ.measure(3, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)) as else_1:
    						main_circ.id(qreg_1[0])
    					with else_1:
    						main_circ.id(qreg_1[0])
    					main_circ.measure(qreg_1[0], creg_0[0])
    					with main_circ.if_test((creg_0[0],0)):
    						main_circ.barrier(1)
    					main_circ.measure(1, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)):
    						main_circ.barrier(qreg_1[0])
    					main_circ.measure(1, creg_0[1])
    					with main_circ.switch(creg_0[1]) as case_1:
    						with case_1(0):
    							main_circ.id(qreg_1[0])
    						with case_1(1):
    							main_circ.id(qreg_0[0])
    					main_circ.measure(3, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)) as else_1:
    						main_circ.barrier(3)
    					with else_1:
    						main_circ.id(3)
    					main_circ.measure(qreg_0[0], creg_0[1])
    					with main_circ.switch(creg_0[1]) as case_1:
    						with case_1(0):
    							main_circ.barrier(1)
    						with case_1(1):
    							main_circ.id(qreg_0[0])
    					main_circ.measure(2, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)):
    						main_circ.barrier(1)
    					main_circ.id(0)
    				with else_2:
    					main_circ.measure(qreg_0[0], creg_0[1])
    					with main_circ.if_test((creg_0[1],0)):
    						main_circ.id(qreg_1[0])
    					main_circ.barrier(3)
    				main_circ.measure(3, creg_0[1])
    				with main_circ.if_test((creg_0[1],0)) as else_2:
    					main_circ.measure(2, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)):
    						main_circ.barrier(1)
    					main_circ.measure(3, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)) as else_1:
    						main_circ.barrier(0)
    					with else_1:
    						main_circ.barrier(qreg_1[0])
    					main_circ.measure(qreg_0[0], creg_0[1])
    					with main_circ.switch(creg_0[1]) as case_1:
    						with case_1(0):
    							main_circ.id(qreg_0[0])
    						with case_1(1):
    							main_circ.barrier(2)
    					main_circ.id(qreg_1[0])
    				with else_2:
    					main_circ.barrier(1)
    				main_circ.measure(3, creg_0[1])
    				with main_circ.if_test((creg_0[1],0)) as else_2:
    					main_circ.measure(2, creg_0[1])
    					with main_circ.switch(creg_0[1]) as case_1:
    						with case_1(0):
    							main_circ.id(0)
    						with case_1(1):
    							main_circ.barrier(qreg_1[0])
    					main_circ.measure(0, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)) as else_1:
    						main_circ.id(0)
    					with else_1:
    						main_circ.id(3)
    					main_circ.measure(1, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)):
    						main_circ.id(qreg_1[0])
    					main_circ.id(0)
    				with else_2:
    					main_circ.id(qreg_1[0])
    				main_circ.id(3)
    		main_circ.measure(1, creg_0[0])
    		with main_circ.if_test((creg_0[0],0)) as else_3:
    			main_circ.barrier(1)
    		with else_3:
    			main_circ.measure(qreg_0[0], creg_0[1])
    			with main_circ.switch(creg_0[1]) as case_2:
    				with case_2(0):
    					main_circ.measure(qreg_0[0], creg_0[1])
    					with main_circ.switch(creg_0[1]) as case_1:
    						with case_1(0):
    							main_circ.barrier(2)
    						with case_1(1):
    							main_circ.id(qreg_0[0])
    					main_circ.measure(qreg_1[0], creg_0[0])
    					with main_circ.if_test((creg_0[0],0)) as else_1:
    						main_circ.barrier(qreg_0[0])
    					with else_1:
    						main_circ.id(0)
    					main_circ.measure(qreg_0[0], creg_0[0])
    					with main_circ.if_test((creg_0[0],0)):
    						main_circ.barrier(qreg_0[0])
    					main_circ.measure(1, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)):
    						main_circ.barrier(qreg_0[0])
    					main_circ.id(1)
    				with case_2(1):
    					main_circ.measure(1, creg_0[0])
    					with main_circ.switch(creg_0[0]) as case_1:
    						with case_1(0):
    							main_circ.barrier(0)
    						with case_1(1):
    							main_circ.barrier(qreg_0[0])
    					main_circ.measure(qreg_1[0], creg_0[0])
    					with main_circ.if_test((creg_0[0],0)) as else_1:
    						main_circ.id(0)
    					with else_1:
    						main_circ.id(3)
    					main_circ.measure(3, creg_0[0])
    					with main_circ.switch(creg_0[0]) as case_1:
    						with case_1(0):
    							main_circ.id(2)
    						with case_1(1):
    							main_circ.barrier(2)
    					main_circ.measure(0, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)) as else_1:
    						main_circ.barrier(qreg_1[0])
    					with else_1:
    						main_circ.barrier(2)
    					main_circ.measure(0, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)) as else_1:
    						main_circ.id(qreg_0[0])
    					with else_1:
    						main_circ.barrier(1)
    					main_circ.measure(0, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)):
    						main_circ.id(1)
    					main_circ.measure(0, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)):
    						main_circ.barrier(3)
    					main_circ.id(1)
    			main_circ.measure(3, creg_0[0])
    			with main_circ.if_test((creg_0[0],0)):
    				main_circ.barrier(3)
    			main_circ.measure(qreg_1[0], creg_0[0])
    			with main_circ.if_test((creg_0[0],0)) as else_2:
    				main_circ.measure(1, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.barrier(qreg_0[0])
    				with else_1:
    					main_circ.id(1)
    				main_circ.id(qreg_1[0])
    			with else_2:
    				main_circ.measure(qreg_0[0], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.barrier(qreg_0[0])
    				main_circ.measure(3, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.id(1)
    				with else_1:
    					main_circ.id(qreg_1[0])
    				main_circ.measure(3, creg_0[0])
    				with main_circ.switch(creg_0[0]) as case_1:
    					with case_1(0):
    						main_circ.barrier(3)
    					with case_1(1):
    						main_circ.id(2)
    				main_circ.measure(3, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.barrier(2)
    				main_circ.measure(2, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.barrier(0)
    				main_circ.measure(1, creg_0[1])
    				with main_circ.switch(creg_0[1]) as case_1:
    					with case_1(0):
    						main_circ.barrier(qreg_1[0])
    					with case_1(1):
    						main_circ.barrier(3)
    				main_circ.measure(1, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.id(qreg_0[0])
    				with else_1:
    					main_circ.id(0)
    				main_circ.measure(qreg_1[0], creg_0[1])
    				with main_circ.if_test((creg_0[1],0)):
    					main_circ.id(3)
    				main_circ.id(qreg_0[0])
    			main_circ.measure(qreg_0[0], creg_0[1])
    			with main_circ.if_test((creg_0[1],0)):
    				main_circ.measure(0, creg_0[1])
    				with main_circ.switch(creg_0[1]) as case_1:
    					with case_1(0):
    						main_circ.id(3)
    					with case_1(1):
    						main_circ.barrier(3)
    				main_circ.id(qreg_0[0])
    			main_circ.id(qreg_1[0])
    		main_circ.measure(2, creg_0[0])
    		with main_circ.if_test((creg_0[0],0)):
    			main_circ.measure(1, creg_0[1])
    			with main_circ.if_test((creg_0[1],0)):
    				main_circ.id(3)
    			main_circ.barrier(1)
    		main_circ.measure(1, creg_0[0])
    		with main_circ.if_test((creg_0[0],0)):
    			main_circ.measure(3, creg_0[1])
    			with main_circ.if_test((creg_0[1],0)):
    				main_circ.id(0)
    			main_circ.measure(2, creg_0[1])
    			with main_circ.switch(creg_0[1]) as case_2:
    				with case_2(0):
    					main_circ.measure(qreg_0[0], creg_0[1])
    					with main_circ.switch(creg_0[1]) as case_1:
    						with case_1(0):
    							main_circ.id(qreg_1[0])
    						with case_1(1):
    							main_circ.id(qreg_0[0])
    					main_circ.measure(qreg_0[0], creg_0[0])
    					with main_circ.if_test((creg_0[0],0)):
    						main_circ.barrier(0)
    					main_circ.measure(1, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)):
    						main_circ.barrier(3)
    					main_circ.measure(qreg_0[0], creg_0[1])
    					with main_circ.if_test((creg_0[1],0)) as else_1:
    						main_circ.barrier(3)
    					with else_1:
    						main_circ.barrier(0)
    					main_circ.measure(2, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)):
    						main_circ.id(3)
    					main_circ.measure(3, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)) as else_1:
    						main_circ.barrier(3)
    					with else_1:
    						main_circ.id(qreg_1[0])
    					main_circ.barrier(1)
    				with case_2(1):
    					main_circ.id(3)
    			main_circ.barrier(3)
    		main_circ.id(3)
    bindings = {param_0: -0.997000, param_1: -0.766000, param_2: -0.705000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_pass_on_simulator(main_circ, "51", "Optimize1qGates")


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
