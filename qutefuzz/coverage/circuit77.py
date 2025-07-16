
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
    subcirc0.u(0.728000,-0.051000,-0.622000, qreg_0[1])
    subcirc0.u(0,0,0.099000, qreg_0[0])
    subcirc0.u(-0.592000,0.547000,0.534000, qreg_0[2])
    subcirc0.u(0.821000,0.893000,-0.089000, qreg_0[2])
    subcirc0.ry(0.062000, qreg_3[0])
    subcirc0.h(qreg_0[2])
    
    subcirc1 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(4)
    subcirc1.add_register(qreg_0)
    # Adding creg resources 
    subcirc1.u(0,0,-0.030000, qreg_0[1])
    subcirc1.u(-0.649000,0.408000,0.956000, qreg_0[1])
    subcirc1.u(-0.687000,0.552000,0.873000, qreg_0[1])
    subcirc1.ry(0.384000, qreg_0[0])
    subcirc1.ry(-0.445000, qreg_0[3])
    subcirc1.u(-0.526000,-0.071000,-0.950000, qreg_0[2])
    
    subcirc2 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(4)
    subcirc2.add_register(qreg_0)
    # Adding creg resources 
    subcirc2.ry(0.599000, qreg_0[1])
    subcirc2.u(-0.917000,-0.797000,-0.603000, qreg_0[0])
    subcirc2.ry(0.638000, qreg_0[2])
    subcirc2.h(qreg_0[2])
    subcirc2.u(-0.583000,0.066000,0.449000, qreg_0[2])
    subcirc2.h(qreg_0[0])
    subcirc2 = subcirc2.to_gate().control(2)
    
    subcirc3 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(2)
    subcirc3.add_register(qreg_0)
    qreg_2 = QuantumRegister(2)
    subcirc3.add_register(qreg_2)
    # Adding creg resources 
    subcirc3.ry(0.056000, qreg_2[0])
    subcirc3.u(0.735000,0.889000,-0.660000, qreg_0[0])
    subcirc3.u(-0.888000,0.521000,0.499000, qreg_0[1])
    subcirc3.ry(-0.425000, qreg_0[0])
    subcirc3.u(-0.073000,-0.393000,-0.070000, qreg_0[1])
    subcirc3.h(qreg_0[0])
    subcirc3 = subcirc3.to_gate().control(3)
    
    subcirc4 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(2)
    subcirc4.add_register(qreg_0)
    qreg_2 = QuantumRegister(2)
    subcirc4.add_register(qreg_2)
    # Adding creg resources 
    subcirc4.u(-0.228000,-0.116000,0.319000, qreg_0[0])
    subcirc4.u(-0.264000,-0.171000,0.765000, qreg_2[1])
    subcirc4.u(0.997000,0.965000,0.870000, qreg_2[0])
    subcirc4.ry(0.881000, qreg_2[1])
    subcirc4.ry(-0.449000, qreg_2[1])
    subcirc4.u(-0.636000,-0.068000,-0.396000, qreg_2[0])
    
    main_circ = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(3)
    main_circ.add_register(qreg_0)
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
    
    main_circ.measure(qreg_0[2], creg_0[0])
    with main_circ.if_test((creg_0[0],0)):
    	main_circ.measure(qreg_0[2], creg_0[0])
    	with main_circ.if_test((creg_0[0],0)):
    		main_circ.measure(qreg_3[0], creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_1:
    			with case_1(0):
    				main_circ.u(param_1,0,param_1, qreg_0[2])
    				main_circ.u(0,param_1,-0.739000, qreg_0[2])
    				main_circ.append(subcirc4,[qreg_0[2],qreg_0[1],qreg_3[0],qreg_0[0]])
    			with case_1(1):
    				main_circ.ry(0.699000, qreg_0[2])
    				main_circ.u(param_0,0.120000,0.818000, qreg_0[2])
    				main_circ.id(qreg_0[0])
    main_circ.measure(qreg_0[0], creg_0[0])
    with main_circ.switch(creg_0[0]) as case_3:
    	with case_3(0):
    		main_circ.measure(qreg_3[0], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)) as else_2:
    			main_circ.append(subcirc4,[qreg_3[0],qreg_0[0],qreg_0[1],qreg_0[2]])
    		with else_2:
    			main_circ.ry(param_0, qreg_0[2])
    			main_circ.h(qreg_0[0])
    			main_circ.measure(qreg_0[1], creg_1[0])
    			with main_circ.if_test((creg_1[0],0)):
    				main_circ.u(param_1,0,param_0, qreg_0[2])
    				main_circ.ry(param_1, qreg_3[0])
    	with case_3(1):
    		main_circ.measure(qreg_3[0], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)) as else_2:
    			main_circ.measure(qreg_0[0], creg_1[0])
    			with main_circ.switch(creg_1[0]) as case_1:
    				with case_1(0):
    					main_circ.u(param_1,param_0,param_1, qreg_0[2])
    					main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],qreg_3[0],qreg_0[1]])
    				with case_1(1):
    					main_circ.barrier(qreg_0[2])
    		with else_2:
    			main_circ.measure(qreg_0[2], creg_0[0])
    			with main_circ.if_test((creg_0[0],0)) as else_1:
    				main_circ.append(subcirc1,[qreg_0[1],qreg_0[0],qreg_3[0],qreg_0[2]])
    			with else_1:
    				main_circ.u(0.159000,-0.600000,param_0, qreg_0[2])
    				main_circ.u(param_1,-0.297000,0.533000, qreg_3[0])
    				main_circ.h(qreg_3[0])
    main_circ.measure(qreg_0[2], creg_1[0])
    with main_circ.if_test((creg_1[0],0)) as else_3:
    	main_circ.measure(qreg_3[0], creg_1[0])
    	with main_circ.if_test((creg_1[0],0)):
    		main_circ.measure(qreg_0[2], creg_0[0])
    		with main_circ.if_test((creg_0[0],0)) as else_1:
    			main_circ.id(qreg_0[2])
    		with else_1:
    			main_circ.h(qreg_0[1])
    			main_circ.h(qreg_3[0])
    			main_circ.id(qreg_0[0])
    		main_circ.measure(qreg_3[0], creg_1[0])
    		with main_circ.switch(creg_1[0]) as case_1:
    			with case_1(0):
    				main_circ.u(-0.378000,param_0,param_0, qreg_3[0])
    				main_circ.barrier(qreg_0[0])
    			with case_1(1):
    				main_circ.u(0.497000,0.548000,param_0, qreg_0[1])
    				main_circ.barrier(qreg_3[0])
    	main_circ.measure(qreg_0[0], creg_1[0])
    	with main_circ.if_test((creg_1[0],0)) as else_2:
    		main_circ.measure(qreg_0[1], creg_1[0])
    		with main_circ.switch(creg_1[0]) as case_1:
    			with case_1(0):
    				main_circ.u(0.477000,0.656000,param_1, qreg_0[2])
    				main_circ.barrier(qreg_0[0])
    			with case_1(1):
    				main_circ.barrier(qreg_0[2])
    		main_circ.measure(qreg_3[0], creg_0[0])
    		with main_circ.if_test((creg_0[0],0)) as else_1:
    			main_circ.id(qreg_3[0])
    		with else_1:
    			main_circ.ry(-0.857000, qreg_0[0])
    		main_circ.measure(qreg_0[1], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)):
    			main_circ.id(qreg_0[0])
    		main_circ.measure(qreg_0[0], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)) as else_1:
    			main_circ.barrier(qreg_3[0])
    		with else_1:
    			main_circ.barrier(qreg_3[0])
    		main_circ.measure(qreg_3[0], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)):
    			main_circ.barrier(qreg_0[2])
    		main_circ.measure(qreg_0[1], creg_0[0])
    		with main_circ.if_test((creg_0[0],0)) as else_1:
    			main_circ.barrier(qreg_0[0])
    		with else_1:
    			main_circ.id(qreg_0[1])
    		main_circ.measure(qreg_3[0], creg_1[0])
    		with main_circ.switch(creg_1[0]) as case_1:
    			with case_1(0):
    				main_circ.barrier(qreg_0[0])
    			with case_1(1):
    				main_circ.id(qreg_0[2])
    		main_circ.barrier(qreg_3[0])
    	with else_2:
    		main_circ.measure(qreg_0[0], creg_0[0])
    		with main_circ.if_test((creg_0[0],0)):
    			main_circ.barrier(qreg_0[2])
    		main_circ.measure(qreg_0[1], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)):
    			main_circ.barrier(qreg_3[0])
    		main_circ.barrier(qreg_0[1])
    with else_3:
    	main_circ.measure(qreg_3[0], creg_0[0])
    	with main_circ.if_test((creg_0[0],0)):
    		main_circ.id(qreg_0[0])
    	main_circ.measure(qreg_0[2], creg_1[0])
    	with main_circ.if_test((creg_1[0],0)) as else_2:
    		main_circ.measure(qreg_3[0], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)) as else_1:
    			main_circ.barrier(qreg_3[0])
    		with else_1:
    			main_circ.barrier(qreg_3[0])
    		main_circ.measure(qreg_3[0], creg_1[0])
    		with main_circ.switch(creg_1[0]) as case_1:
    			with case_1(0):
    				main_circ.barrier(qreg_0[0])
    			with case_1(1):
    				main_circ.id(qreg_0[0])
    		main_circ.measure(qreg_0[1], creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_1:
    			with case_1(0):
    				main_circ.id(qreg_0[1])
    			with case_1(1):
    				main_circ.id(qreg_0[2])
    		main_circ.measure(qreg_0[0], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)) as else_1:
    			main_circ.barrier(qreg_0[1])
    		with else_1:
    			main_circ.id(qreg_3[0])
    		main_circ.measure(qreg_3[0], creg_0[0])
    		with main_circ.if_test((creg_0[0],0)):
    			main_circ.id(qreg_3[0])
    		main_circ.measure(qreg_0[0], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)):
    			main_circ.id(qreg_0[1])
    		main_circ.measure(qreg_0[1], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)):
    			main_circ.barrier(qreg_0[1])
    		main_circ.measure(qreg_0[2], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)) as else_1:
    			main_circ.id(qreg_0[0])
    		with else_1:
    			main_circ.barrier(qreg_3[0])
    		main_circ.measure(qreg_0[2], creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_1:
    			with case_1(0):
    				main_circ.barrier(qreg_0[1])
    			with case_1(1):
    				main_circ.barrier(qreg_3[0])
    		main_circ.measure(qreg_3[0], creg_0[0])
    		with main_circ.if_test((creg_0[0],0)) as else_1:
    			main_circ.barrier(qreg_3[0])
    		with else_1:
    			main_circ.barrier(qreg_0[0])
    		main_circ.barrier(qreg_0[0])
    	with else_2:
    		main_circ.measure(qreg_0[0], creg_0[0])
    		with main_circ.if_test((creg_0[0],0)) as else_1:
    			main_circ.barrier(qreg_0[2])
    		with else_1:
    			main_circ.barrier(qreg_0[1])
    		main_circ.measure(qreg_3[0], creg_1[0])
    		with main_circ.switch(creg_1[0]) as case_1:
    			with case_1(0):
    				main_circ.id(qreg_0[0])
    			with case_1(1):
    				main_circ.id(qreg_3[0])
    		main_circ.measure(qreg_0[2], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)):
    			main_circ.id(qreg_0[1])
    		main_circ.measure(qreg_0[2], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)):
    			main_circ.id(qreg_0[1])
    		main_circ.measure(qreg_0[1], creg_0[0])
    		with main_circ.if_test((creg_0[0],0)):
    			main_circ.barrier(qreg_3[0])
    		main_circ.measure(qreg_0[2], creg_0[0])
    		with main_circ.if_test((creg_0[0],0)):
    			main_circ.id(qreg_0[1])
    		main_circ.measure(qreg_3[0], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)) as else_1:
    			main_circ.barrier(qreg_3[0])
    		with else_1:
    			main_circ.barrier(qreg_3[0])
    		main_circ.measure(qreg_0[0], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)):
    			main_circ.id(qreg_0[0])
    		main_circ.measure(qreg_0[1], creg_0[0])
    		with main_circ.if_test((creg_0[0],0)):
    			main_circ.barrier(qreg_0[1])
    		main_circ.measure(qreg_0[0], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)) as else_1:
    			main_circ.id(qreg_3[0])
    		with else_1:
    			main_circ.id(qreg_0[1])
    		main_circ.measure(qreg_0[1], creg_1[0])
    		with main_circ.switch(creg_1[0]) as case_1:
    			with case_1(0):
    				main_circ.id(qreg_3[0])
    			with case_1(1):
    				main_circ.barrier(qreg_0[1])
    		main_circ.measure(qreg_0[1], creg_1[0])
    		with main_circ.switch(creg_1[0]) as case_1:
    			with case_1(0):
    				main_circ.barrier(qreg_0[0])
    			with case_1(1):
    				main_circ.barrier(qreg_0[0])
    		main_circ.measure(qreg_3[0], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)):
    			main_circ.barrier(qreg_0[0])
    		main_circ.measure(qreg_0[0], creg_0[0])
    		with main_circ.if_test((creg_0[0],0)):
    			main_circ.id(qreg_0[0])
    		main_circ.measure(qreg_0[0], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)) as else_1:
    			main_circ.barrier(qreg_0[1])
    		with else_1:
    			main_circ.id(qreg_0[2])
    		main_circ.measure(qreg_0[2], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)) as else_1:
    			main_circ.id(qreg_0[0])
    		with else_1:
    			main_circ.barrier(qreg_0[0])
    		main_circ.measure(qreg_0[2], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)) as else_1:
    			main_circ.id(qreg_0[2])
    		with else_1:
    			main_circ.barrier(qreg_3[0])
    		main_circ.measure(qreg_0[0], creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_1:
    			with case_1(0):
    				main_circ.id(qreg_0[0])
    			with case_1(1):
    				main_circ.id(qreg_0[0])
    		main_circ.measure(qreg_3[0], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)):
    			main_circ.barrier(qreg_3[0])
    		main_circ.measure(qreg_0[1], creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_1:
    			with case_1(0):
    				main_circ.id(qreg_0[1])
    			with case_1(1):
    				main_circ.id(qreg_0[0])
    		main_circ.measure(qreg_0[0], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)) as else_1:
    			main_circ.id(qreg_0[0])
    		with else_1:
    			main_circ.barrier(qreg_3[0])
    		main_circ.measure(qreg_0[1], creg_1[0])
    		with main_circ.switch(creg_1[0]) as case_1:
    			with case_1(0):
    				main_circ.id(qreg_0[1])
    			with case_1(1):
    				main_circ.id(qreg_0[2])
    		main_circ.measure(qreg_0[1], creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_1:
    			with case_1(0):
    				main_circ.barrier(qreg_0[1])
    			with case_1(1):
    				main_circ.id(qreg_3[0])
    		main_circ.barrier(qreg_0[0])
    	main_circ.measure(qreg_3[0], creg_1[0])
    	with main_circ.if_test((creg_1[0],0)) as else_2:
    		main_circ.id(qreg_0[2])
    	with else_2:
    		main_circ.measure(qreg_0[2], creg_0[0])
    		with main_circ.if_test((creg_0[0],0)) as else_1:
    			main_circ.barrier(qreg_0[1])
    		with else_1:
    			main_circ.id(qreg_0[0])
    		main_circ.measure(qreg_0[2], creg_0[0])
    		with main_circ.if_test((creg_0[0],0)) as else_1:
    			main_circ.barrier(qreg_0[0])
    		with else_1:
    			main_circ.id(qreg_3[0])
    		main_circ.measure(qreg_0[2], creg_0[0])
    		with main_circ.if_test((creg_0[0],0)) as else_1:
    			main_circ.barrier(qreg_0[0])
    		with else_1:
    			main_circ.id(qreg_0[2])
    		main_circ.measure(qreg_0[1], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)):
    			main_circ.id(qreg_0[2])
    		main_circ.measure(qreg_0[2], creg_1[0])
    		with main_circ.switch(creg_1[0]) as case_1:
    			with case_1(0):
    				main_circ.barrier(qreg_0[0])
    			with case_1(1):
    				main_circ.barrier(qreg_3[0])
    		main_circ.measure(qreg_0[1], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)):
    			main_circ.id(qreg_0[1])
    		main_circ.measure(qreg_0[0], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)) as else_1:
    			main_circ.barrier(qreg_0[0])
    		with else_1:
    			main_circ.id(qreg_3[0])
    		main_circ.measure(qreg_0[1], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)):
    			main_circ.barrier(qreg_0[2])
    		main_circ.id(qreg_0[0])
    	main_circ.measure(qreg_0[1], creg_1[0])
    	with main_circ.if_test((creg_1[0],0)):
    		main_circ.id(qreg_0[2])
    	main_circ.measure(qreg_0[1], creg_1[0])
    	with main_circ.if_test((creg_1[0],0)) as else_2:
    		main_circ.barrier(qreg_0[0])
    	with else_2:
    		main_circ.measure(qreg_0[1], creg_1[0])
    		with main_circ.switch(creg_1[0]) as case_1:
    			with case_1(0):
    				main_circ.id(qreg_0[1])
    			with case_1(1):
    				main_circ.id(qreg_0[2])
    		main_circ.measure(qreg_0[2], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)):
    			main_circ.barrier(qreg_3[0])
    		main_circ.barrier(qreg_0[2])
    	main_circ.measure(qreg_0[0], creg_0[0])
    	with main_circ.if_test((creg_0[0],0)):
    		main_circ.measure(qreg_0[0], creg_0[0])
    		with main_circ.if_test((creg_0[0],0)):
    			main_circ.id(qreg_0[0])
    		main_circ.measure(qreg_3[0], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)):
    			main_circ.id(qreg_0[1])
    		main_circ.measure(qreg_0[0], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)):
    			main_circ.id(qreg_0[0])
    		main_circ.measure(qreg_3[0], creg_0[0])
    		with main_circ.if_test((creg_0[0],0)) as else_1:
    			main_circ.id(qreg_0[1])
    		with else_1:
    			main_circ.id(qreg_3[0])
    		main_circ.measure(qreg_0[1], creg_1[0])
    		with main_circ.switch(creg_1[0]) as case_1:
    			with case_1(0):
    				main_circ.barrier(qreg_0[0])
    			with case_1(1):
    				main_circ.id(qreg_0[0])
    		main_circ.measure(qreg_0[0], creg_1[0])
    		with main_circ.switch(creg_1[0]) as case_1:
    			with case_1(0):
    				main_circ.barrier(qreg_3[0])
    			with case_1(1):
    				main_circ.barrier(qreg_3[0])
    		main_circ.barrier(qreg_0[1])
    	main_circ.barrier(qreg_0[0])
    bindings = {param_0: 0.054000, param_1: 0.497000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_pass_on_simulator(main_circ, "77", "CommutativeInverseCancellation")


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
