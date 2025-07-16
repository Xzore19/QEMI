
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
    subcirc0.h(qreg_0[1])
    subcirc0.h(qreg_0[0])
    subcirc0.u(0.292000,0.443000,-0.473000, qreg_0[0])
    subcirc0.u(0.948000,0.081000,0.713000, qreg_0[0])
    subcirc0.cy(qreg_0[0],qreg_3[0])
    subcirc0.ry(-0.067000, qreg_3[0])
    
    subcirc1 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(4)
    subcirc1.add_register(qreg_0)
    # Adding creg resources 
    subcirc1.ry(-0.742000, qreg_0[1])
    subcirc1.cy(qreg_0[0],qreg_0[2])
    subcirc1.u(-0.751000,-0.093000,-0.939000, qreg_0[3])
    subcirc1.u(-0.337000,-0.727000,-0.770000, qreg_0[2])
    subcirc1.ry(-0.670000, qreg_0[2])
    subcirc1.cy(qreg_0[2],qreg_0[1])
    subcirc1 = subcirc1.to_gate().control(3)
    
    subcirc2 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(3)
    subcirc2.add_register(qreg_0)
    qreg_3 = QuantumRegister(1)
    subcirc2.add_register(qreg_3)
    # Adding creg resources 
    subcirc2.u(0.930000,0.479000,-0.477000, qreg_0[1])
    subcirc2.cy(qreg_3[0],qreg_0[0])
    subcirc2.ry(0.608000, qreg_0[1])
    subcirc2.cy(qreg_0[0],qreg_0[1])
    subcirc2.cy(qreg_0[1],qreg_3[0])
    subcirc2.ry(-0.778000, qreg_0[1])
    
    subcirc3 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(2)
    subcirc3.add_register(qreg_0)
    qreg_2 = QuantumRegister(1)
    subcirc3.add_register(qreg_2)
    qreg_3 = QuantumRegister(1)
    subcirc3.add_register(qreg_3)
    # Adding creg resources 
    subcirc3.u(0.127000,0.951000,0.310000, qreg_0[1])
    subcirc3.h(qreg_2[0])
    subcirc3.ry(-0.194000, qreg_0[0])
    subcirc3.u(-0.205000,-0.913000,-0.972000, qreg_2[0])
    subcirc3.cy(qreg_2[0],qreg_0[0])
    subcirc3.u(0.803000,-0.971000,-0.522000, qreg_3[0])
    subcirc3 = subcirc3.to_gate().control(2)
    
    subcirc4 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(1)
    subcirc4.add_register(qreg_0)
    qreg_1 = QuantumRegister(3)
    subcirc4.add_register(qreg_1)
    # Adding creg resources 
    subcirc4.ry(-0.153000, qreg_1[0])
    subcirc4.cy(qreg_1[1],qreg_0[0])
    subcirc4.ry(0.664000, qreg_1[1])
    subcirc4.ry(0.691000, qreg_0[0])
    subcirc4.u(-0.367000,-0.676000,0.006000, qreg_1[2])
    subcirc4.cy(qreg_1[2],qreg_1[1])
    
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
    
    main_circ.append(subcirc4,[qreg_0[2],qreg_0[1],qreg_0[0],qreg_3[0]])
    main_circ.measure(qreg_0[1], creg_0[0])
    with main_circ.switch(creg_0[0]) as case_3:
    	with case_3(0):
    		main_circ.measure(qreg_0[0], creg_1[0])
    		with main_circ.switch(creg_1[0]) as case_2:
    			with case_2(0):
    				main_circ.measure(qreg_0[1], creg_1[0])
    				with main_circ.if_test((creg_1[0],0)):
    					main_circ.cy(qreg_0[1],qreg_3[0])
    					main_circ.ry(0.021000, qreg_0[0])
    					main_circ.u(param_1,param_0,param_1, qreg_0[2])
    				main_circ.measure(qreg_3[0], creg_0[0])
    				with main_circ.switch(creg_0[0]) as case_1:
    					with case_1(0):
    						main_circ.append(subcirc0,[qreg_0[0],qreg_0[1],qreg_3[0],qreg_0[2]])
    					with case_1(1):
    						main_circ.append(subcirc2,[qreg_0[2],qreg_0[0],qreg_3[0],qreg_0[1]])
    			with case_2(1):
    				main_circ.measure(qreg_0[0], creg_1[0])
    				with main_circ.if_test((creg_1[0],0)):
    					main_circ.h(qreg_0[0])
    				main_circ.id(qreg_0[2])
    	with case_3(1):
    		main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],qreg_3[0],qreg_0[1]])
    main_circ.measure(qreg_0[1], creg_1[0])
    with main_circ.if_test((creg_1[0],0)):
    	main_circ.measure(qreg_3[0], creg_0[0])
    	with main_circ.switch(creg_0[0]) as case_2:
    		with case_2(0):
    			main_circ.measure(qreg_3[0], creg_1[0])
    			with main_circ.if_test((creg_1[0],0)):
    				main_circ.id(qreg_0[0])
    			main_circ.measure(qreg_0[2], creg_0[0])
    			with main_circ.switch(creg_0[0]) as case_1:
    				with case_1(0):
    					main_circ.id(qreg_0[1])
    				with case_1(1):
    					main_circ.ry(param_0, qreg_0[0])
    					main_circ.barrier(qreg_0[1])
    			main_circ.measure(qreg_0[2], creg_0[0])
    			with main_circ.switch(creg_0[0]) as case_1:
    				with case_1(0):
    					main_circ.append(subcirc4,[qreg_0[1],qreg_0[0],qreg_0[2],qreg_3[0]])
    				with case_1(1):
    					main_circ.barrier(qreg_3[0])
    		with case_2(1):
    			main_circ.measure(qreg_0[0], creg_1[0])
    			with main_circ.switch(creg_1[0]) as case_1:
    				with case_1(0):
    					main_circ.append(subcirc2,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_3[0]])
    				with case_1(1):
    					main_circ.cy(qreg_3[0],qreg_0[0])
    					main_circ.cy(qreg_0[1],qreg_0[0])
    					main_circ.cy(qreg_0[0],qreg_0[2])
    					main_circ.append(subcirc4,[qreg_0[2],qreg_3[0],qreg_0[0],qreg_0[1]])
    main_circ.measure(qreg_0[0], creg_1[0])
    with main_circ.switch(creg_1[0]) as case_3:
    	with case_3(0):
    		main_circ.measure(qreg_3[0], creg_1[0])
    		with main_circ.switch(creg_1[0]) as case_2:
    			with case_2(0):
    				main_circ.measure(qreg_0[1], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.ry(0.503000, qreg_3[0])
    					main_circ.barrier(qreg_3[0])
    				with else_1:
    					main_circ.barrier(qreg_3[0])
    				main_circ.measure(qreg_0[1], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.cy(qreg_3[0],qreg_0[0])
    					main_circ.h(qreg_0[1])
    					main_circ.u(param_0,param_1,param_0, qreg_0[2])
    					main_circ.id(qreg_0[1])
    				with else_1:
    					main_circ.id(qreg_3[0])
    			with case_2(1):
    				main_circ.measure(qreg_0[0], creg_0[0])
    				with main_circ.switch(creg_0[0]) as case_1:
    					with case_1(0):
    						main_circ.id(qreg_0[2])
    					with case_1(1):
    						main_circ.id(qreg_0[1])
    				main_circ.measure(qreg_0[0], creg_1[0])
    				with main_circ.if_test((creg_1[0],0)) as else_1:
    					main_circ.barrier(qreg_0[0])
    				with else_1:
    					main_circ.id(qreg_0[0])
    				main_circ.measure(qreg_3[0], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.id(qreg_0[2])
    				with else_1:
    					main_circ.barrier(qreg_0[2])
    				main_circ.measure(qreg_0[2], creg_0[0])
    				with main_circ.switch(creg_0[0]) as case_1:
    					with case_1(0):
    						main_circ.id(qreg_0[0])
    					with case_1(1):
    						main_circ.barrier(qreg_0[1])
    				main_circ.measure(qreg_0[2], creg_1[0])
    				with main_circ.switch(creg_1[0]) as case_1:
    					with case_1(0):
    						main_circ.barrier(qreg_0[0])
    					with case_1(1):
    						main_circ.id(qreg_0[2])
    				main_circ.measure(qreg_0[2], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.barrier(qreg_0[2])
    				with else_1:
    					main_circ.barrier(qreg_0[2])
    				main_circ.barrier(qreg_0[0])
    	with case_3(1):
    		main_circ.measure(qreg_0[1], creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_2:
    			with case_2(0):
    				main_circ.measure(qreg_0[0], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.id(qreg_0[0])
    				with else_1:
    					main_circ.barrier(qreg_0[0])
    				main_circ.measure(qreg_3[0], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.id(qreg_0[2])
    				main_circ.id(qreg_0[0])
    			with case_2(1):
    				main_circ.measure(qreg_0[2], creg_1[0])
    				with main_circ.if_test((creg_1[0],0)) as else_1:
    					main_circ.barrier(qreg_0[0])
    				with else_1:
    					main_circ.barrier(qreg_0[1])
    				main_circ.measure(qreg_3[0], creg_0[0])
    				with main_circ.switch(creg_0[0]) as case_1:
    					with case_1(0):
    						main_circ.barrier(qreg_0[1])
    					with case_1(1):
    						main_circ.barrier(qreg_0[2])
    				main_circ.measure(qreg_0[1], creg_0[0])
    				with main_circ.switch(creg_0[0]) as case_1:
    					with case_1(0):
    						main_circ.id(qreg_0[2])
    					with case_1(1):
    						main_circ.barrier(qreg_0[2])
    				main_circ.measure(qreg_0[2], creg_1[0])
    				with main_circ.switch(creg_1[0]) as case_1:
    					with case_1(0):
    						main_circ.id(qreg_3[0])
    					with case_1(1):
    						main_circ.barrier(qreg_0[2])
    				main_circ.measure(qreg_0[2], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.id(qreg_3[0])
    				with else_1:
    					main_circ.id(qreg_0[0])
    				main_circ.measure(qreg_0[2], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.id(qreg_0[1])
    				main_circ.measure(qreg_3[0], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.barrier(qreg_3[0])
    				main_circ.measure(qreg_3[0], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.barrier(qreg_0[1])
    				main_circ.measure(qreg_0[0], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.id(qreg_3[0])
    				main_circ.measure(qreg_0[0], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.id(qreg_0[2])
    				main_circ.measure(qreg_0[0], creg_1[0])
    				with main_circ.switch(creg_1[0]) as case_1:
    					with case_1(0):
    						main_circ.barrier(qreg_0[2])
    					with case_1(1):
    						main_circ.barrier(qreg_3[0])
    				main_circ.measure(qreg_0[1], creg_1[0])
    				with main_circ.switch(creg_1[0]) as case_1:
    					with case_1(0):
    						main_circ.barrier(qreg_0[2])
    					with case_1(1):
    						main_circ.barrier(qreg_0[1])
    				main_circ.measure(qreg_0[0], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.id(qreg_3[0])
    				with else_1:
    					main_circ.id(qreg_3[0])
    				main_circ.id(qreg_0[0])
    		main_circ.measure(qreg_0[1], creg_0[0])
    		with main_circ.if_test((creg_0[0],0)):
    			main_circ.measure(qreg_0[2], creg_0[0])
    			with main_circ.switch(creg_0[0]) as case_1:
    				with case_1(0):
    					main_circ.id(qreg_3[0])
    				with case_1(1):
    					main_circ.barrier(qreg_0[1])
    			main_circ.barrier(qreg_0[1])
    		main_circ.id(qreg_3[0])
    bindings = {param_0: -0.200000, param_1: -0.689000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_on_simulator(main_circ, "67")


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
