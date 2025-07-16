
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
    subcirc0.u(-0.004000,0.223000,0.098000, qreg_0[0])
    subcirc0.ry(-0.476000, qreg_0[0])
    subcirc0.u(0.842000,0.394000,0.368000, qreg_2[0])
    subcirc0.ry(0.961000, qreg_0[0])
    
    subcirc1 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(4)
    subcirc1.add_register(qreg_0)
    # Adding creg resources 
    subcirc1.cz(qreg_0[1],qreg_0[2])
    subcirc1.u(0.402000,-0.433000,0.970000, qreg_0[1])
    subcirc1.cz(qreg_0[1],qreg_0[3])
    subcirc1.ry(-0.592000, qreg_0[0])
    subcirc1 = subcirc1.to_gate().control(1)
    
    subcirc2 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(3)
    subcirc2.add_register(qreg_0)
    qreg_3 = QuantumRegister(1)
    subcirc2.add_register(qreg_3)
    # Adding creg resources 
    subcirc2.ry(-0.194000, qreg_0[0])
    subcirc2.ry(-0.784000, qreg_3[0])
    subcirc2.cy(qreg_0[0],qreg_0[2])
    subcirc2.u(-0.332000,-0.318000,0.877000, qreg_0[0])
    
    subcirc3 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(3)
    subcirc3.add_register(qreg_0)
    qreg_3 = QuantumRegister(1)
    subcirc3.add_register(qreg_3)
    # Adding creg resources 
    subcirc3.cz(qreg_0[2],qreg_0[0])
    subcirc3.cy(qreg_0[0],qreg_0[1])
    subcirc3.cz(qreg_0[1],qreg_0[2])
    subcirc3.u(-0.283000,-0.853000,0.933000, qreg_0[1])
    
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
    
    main_circ.cy(qreg_0[0],qreg_0[2])
    main_circ.measure(qreg_0[3], creg_0[0])
    with main_circ.switch(creg_0[0]) as case_4:
    	with case_4(0):
    		main_circ.measure(qreg_0[1], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)):
    			main_circ.measure(qreg_0[1], creg_0[0])
    			with main_circ.if_test((creg_0[0],0)) as else_2:
    				main_circ.measure(qreg_0[3], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.cz(qreg_0[3],qreg_0[1])
    					main_circ.u(param_1,0.888000,param_0, qreg_0[0])
    					main_circ.cz(qreg_0[0],qreg_0[3])
    					main_circ.append(subcirc0,[qreg_0[3],qreg_0[2],qreg_0[0],qreg_0[1]])
    			with else_2:
    				main_circ.append(subcirc3,[qreg_0[2],qreg_0[1],qreg_0[0],qreg_0[3]])
    				main_circ.u(param_2,-0.048000,0.338000, qreg_0[3])
    	with case_4(1):
    		main_circ.measure(qreg_0[2], creg_0[0])
    		with main_circ.if_test((creg_0[0],0)) as else_3:
    			main_circ.measure(qreg_0[0], creg_1[0])
    			with main_circ.switch(creg_1[0]) as case_2:
    				with case_2(0):
    					main_circ.u(param_0,-0.780000,0.844000, qreg_0[2])
    					main_circ.measure(qreg_0[3], creg_0[0])
    					with main_circ.if_test((creg_0[0],0)) as else_1:
    						main_circ.u(0.948000,param_2,param_2, qreg_0[1])
    						main_circ.id(qreg_0[0])
    					with else_1:
    						main_circ.cz(qreg_0[2],qreg_0[3])
    					main_circ.measure(qreg_0[3], creg_1[0])
    					with main_circ.if_test((creg_1[0],0)) as else_1:
    						main_circ.append(subcirc2,[qreg_0[3],qreg_0[1],qreg_0[2],qreg_0[0]])
    					with else_1:
    						main_circ.barrier(qreg_0[2])
    				with case_2(1):
    					main_circ.append(subcirc2,[qreg_0[1],qreg_0[3],qreg_0[0],qreg_0[2]])
    		with else_3:
    			main_circ.measure(qreg_0[0], creg_0[0])
    			with main_circ.if_test((creg_0[0],0)):
    				main_circ.measure(qreg_0[1], creg_1[0])
    				with main_circ.if_test((creg_1[0],0)) as else_1:
    					main_circ.append(subcirc3,[qreg_0[1],qreg_0[0],qreg_0[2],qreg_0[3]])
    				with else_1:
    					main_circ.barrier(qreg_0[0])
    				main_circ.append(subcirc3,[qreg_0[3],qreg_0[2],qreg_0[0],qreg_0[1]])
    main_circ.append(subcirc0,[qreg_0[3],qreg_0[0],qreg_0[2],qreg_0[1]])
    main_circ.measure(qreg_0[3], creg_1[0])
    with main_circ.switch(creg_1[0]) as case_4:
    	with case_4(0):
    		main_circ.measure(qreg_0[1], creg_0[0])
    		with main_circ.if_test((creg_0[0],0)) as else_3:
    			main_circ.append(subcirc0,[qreg_0[1],qreg_0[2],qreg_0[0],qreg_0[3]])
    		with else_3:
    			main_circ.append(subcirc2,[qreg_0[2],qreg_0[0],qreg_0[1],qreg_0[3]])
    	with case_4(1):
    		main_circ.measure(qreg_0[3], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)) as else_3:
    			main_circ.measure(qreg_0[0], creg_0[0])
    			with main_circ.switch(creg_0[0]) as case_2:
    				with case_2(0):
    					main_circ.measure(qreg_0[2], creg_1[0])
    					with main_circ.switch(creg_1[0]) as case_1:
    						with case_1(0):
    							main_circ.cy(qreg_0[3],qreg_0[0])
    							main_circ.cz(qreg_0[3],qreg_0[0])
    							main_circ.u(-0.859000,-0.384000,0.840000, qreg_0[2])
    							main_circ.u(param_0,param_0,-0.876000, qreg_0[2])
    						with case_1(1):
    							main_circ.id(qreg_0[0])
    				with case_2(1):
    					main_circ.measure(qreg_0[1], creg_0[0])
    					with main_circ.if_test((creg_0[0],0)):
    						main_circ.id(qreg_0[3])
    					main_circ.measure(qreg_0[1], creg_0[0])
    					with main_circ.if_test((creg_0[0],0)) as else_1:
    						main_circ.ry(param_2, qreg_0[0])
    						main_circ.barrier(qreg_0[1])
    					with else_1:
    						main_circ.id(qreg_0[2])
    					main_circ.measure(qreg_0[0], creg_0[0])
    					with main_circ.switch(creg_0[0]) as case_1:
    						with case_1(0):
    							main_circ.id(qreg_0[3])
    						with case_1(1):
    							main_circ.barrier(qreg_0[3])
    					main_circ.measure(qreg_0[0], creg_1[0])
    					with main_circ.if_test((creg_1[0],0)):
    						main_circ.barrier(qreg_0[1])
    					main_circ.measure(qreg_0[2], creg_0[0])
    					with main_circ.if_test((creg_0[0],0)):
    						main_circ.barrier(qreg_0[2])
    					main_circ.barrier(qreg_0[1])
    		with else_3:
    			main_circ.measure(qreg_0[3], creg_1[0])
    			with main_circ.if_test((creg_1[0],0)) as else_2:
    				main_circ.measure(qreg_0[1], creg_1[0])
    				with main_circ.if_test((creg_1[0],0)) as else_1:
    					main_circ.id(qreg_0[0])
    				with else_1:
    					main_circ.id(qreg_0[2])
    				main_circ.measure(qreg_0[1], creg_1[0])
    				with main_circ.switch(creg_1[0]) as case_1:
    					with case_1(0):
    						main_circ.id(qreg_0[0])
    					with case_1(1):
    						main_circ.barrier(qreg_0[2])
    				main_circ.measure(qreg_0[3], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.barrier(qreg_0[0])
    				main_circ.measure(qreg_0[2], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.id(qreg_0[2])
    				with else_1:
    					main_circ.id(qreg_0[1])
    				main_circ.measure(qreg_0[0], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.barrier(qreg_0[3])
    				with else_1:
    					main_circ.id(qreg_0[1])
    				main_circ.measure(qreg_0[0], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.id(qreg_0[0])
    				main_circ.measure(qreg_0[3], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.barrier(qreg_0[2])
    				main_circ.barrier(qreg_0[2])
    			with else_2:
    				main_circ.measure(qreg_0[0], creg_1[0])
    				with main_circ.if_test((creg_1[0],0)) as else_1:
    					main_circ.barrier(qreg_0[3])
    				with else_1:
    					main_circ.id(qreg_0[0])
    				main_circ.measure(qreg_0[0], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.barrier(qreg_0[1])
    				main_circ.measure(qreg_0[2], creg_1[0])
    				with main_circ.if_test((creg_1[0],0)):
    					main_circ.barrier(qreg_0[0])
    				main_circ.barrier(qreg_0[0])
    			main_circ.measure(qreg_0[1], creg_0[0])
    			with main_circ.if_test((creg_0[0],0)):
    				main_circ.barrier(qreg_0[1])
    			main_circ.measure(qreg_0[2], creg_0[0])
    			with main_circ.switch(creg_0[0]) as case_2:
    				with case_2(0):
    					main_circ.measure(qreg_0[0], creg_0[0])
    					with main_circ.if_test((creg_0[0],0)):
    						main_circ.id(qreg_0[0])
    					main_circ.barrier(qreg_0[2])
    				with case_2(1):
    					main_circ.measure(qreg_0[3], creg_0[0])
    					with main_circ.if_test((creg_0[0],0)):
    						main_circ.id(qreg_0[2])
    					main_circ.measure(qreg_0[2], creg_1[0])
    					with main_circ.if_test((creg_1[0],0)) as else_1:
    						main_circ.id(qreg_0[0])
    					with else_1:
    						main_circ.id(qreg_0[2])
    					main_circ.measure(qreg_0[3], creg_1[0])
    					with main_circ.if_test((creg_1[0],0)) as else_1:
    						main_circ.barrier(qreg_0[2])
    					with else_1:
    						main_circ.barrier(qreg_0[2])
    					main_circ.measure(qreg_0[2], creg_1[0])
    					with main_circ.if_test((creg_1[0],0)) as else_1:
    						main_circ.barrier(qreg_0[3])
    					with else_1:
    						main_circ.id(qreg_0[2])
    					main_circ.measure(qreg_0[0], creg_1[0])
    					with main_circ.if_test((creg_1[0],0)) as else_1:
    						main_circ.id(qreg_0[1])
    					with else_1:
    						main_circ.id(qreg_0[1])
    					main_circ.measure(qreg_0[2], creg_1[0])
    					with main_circ.switch(creg_1[0]) as case_1:
    						with case_1(0):
    							main_circ.barrier(qreg_0[1])
    						with case_1(1):
    							main_circ.barrier(qreg_0[0])
    					main_circ.id(qreg_0[3])
    			main_circ.measure(qreg_0[3], creg_1[0])
    			with main_circ.if_test((creg_1[0],0)):
    				main_circ.measure(qreg_0[0], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.id(qreg_0[0])
    				main_circ.barrier(qreg_0[2])
    			main_circ.measure(qreg_0[2], creg_1[0])
    			with main_circ.if_test((creg_1[0],0)):
    				main_circ.measure(qreg_0[1], creg_1[0])
    				with main_circ.switch(creg_1[0]) as case_1:
    					with case_1(0):
    						main_circ.barrier(qreg_0[2])
    					with case_1(1):
    						main_circ.barrier(qreg_0[3])
    				main_circ.measure(qreg_0[0], creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.barrier(qreg_0[1])
    				with else_1:
    					main_circ.id(qreg_0[0])
    				main_circ.measure(qreg_0[0], creg_1[0])
    				with main_circ.switch(creg_1[0]) as case_1:
    					with case_1(0):
    						main_circ.id(qreg_0[3])
    					with case_1(1):
    						main_circ.id(qreg_0[2])
    				main_circ.id(qreg_0[1])
    			main_circ.id(qreg_0[1])
    bindings = {param_0: -0.919000, param_1: 0.887000, param_2: -0.279000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_on_simulator(main_circ, "62")


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
