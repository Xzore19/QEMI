
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
    subcirc0.u(pi/2,0.210000,0.382000, qreg_2[0])
    subcirc0.u(0,0,0.478000, qreg_3[0])
    subcirc0.u(pi/2,0.136000,0.447000, qreg_3[0])
    subcirc0.u(pi/2,0.313000,0.351000, qreg_2[0])
    subcirc0.u(0,0,-0.471000, qreg_0[0])
    subcirc0 = subcirc0.to_gate().control(1)
    
    main_circ = QuantumCircuit(4)
    # Adding qregs 
    # Adding creg resources 
    creg_0 = ClassicalRegister(2)
    main_circ.add_register(creg_0)
    # Adding symbols 
    param_0 = Parameter("param_0")
    
    main_circ.measure(3, creg_0[1])
    with main_circ.if_test((creg_0[1],0)) as else_4:
    	main_circ.measure(1, creg_0[0])
    	with main_circ.if_test((creg_0[0],0)) as else_3:
    		main_circ.measure(0, creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_2:
    			with case_2(0):
    				main_circ.measure(3, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.u(pi/2,param_0,0.698000, 3)
    					main_circ.rx(-0.750000, 3)
    					main_circ.id(2)
    				main_circ.measure(0, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.rx(0.238000, 1)
    				main_circ.barrier(0)
    			with case_2(1):
    				main_circ.measure(2, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.cx(3,1)
    				main_circ.measure(0, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.rx(0.104000, 1)
    				with else_1:
    					main_circ.rx(-0.743000, 1)
    					main_circ.u(param_0,param_0,-0.188000, 1)
    					main_circ.rx(param_0, 3)
    					main_circ.id(3)
    	with else_3:
    		main_circ.measure(2, creg_0[1])
    		with main_circ.switch(creg_0[1]) as case_2:
    			with case_2(0):
    				main_circ.id(0)
    			with case_2(1):
    				main_circ.measure(3, creg_0[1])
    				with main_circ.if_test((creg_0[1],0)) as else_1:
    					main_circ.u(param_0,param_0,-0.726000, 0)
    					main_circ.id(0)
    				with else_1:
    					main_circ.cx(3,2)
    					main_circ.rx(0.090000, 1)
    					main_circ.rx(0.650000, 2)
    					main_circ.rx(param_0, 3)
    with else_4:
    	main_circ.measure(1, creg_0[1])
    	with main_circ.if_test((creg_0[1],0)):
    		main_circ.measure(1, creg_0[1])
    		with main_circ.switch(creg_0[1]) as case_2:
    			with case_2(0):
    				main_circ.measure(1, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.id(2)
    				main_circ.measure(1, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.cx(0,1)
    					main_circ.id(2)
    				main_circ.measure(2, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.cx(1,2)
    					main_circ.rx(0.115000, 1)
    					main_circ.u(param_0,0.091000,0.892000, 0)
    					main_circ.u(param_0,0,param_0, 0)
    					main_circ.barrier(3)
    				with else_1:
    					main_circ.barrier(2)
    			with case_2(1):
    				main_circ.measure(2, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.cx(2,1)
    					main_circ.cx(1,3)
    				main_circ.measure(2, creg_0[0])
    				with main_circ.switch(creg_0[0]) as case_1:
    					with case_1(0):
    						main_circ.cx(0,2)
    						main_circ.u(pi/2,-0.776000,param_0, 3)
    						main_circ.u(param_0,param_0,param_0, 3)
    						main_circ.cx(0,3)
    					with case_1(1):
    						main_circ.u(param_0,param_0,0.310000, 3)
    						main_circ.u(0,0,0.437000, 3)
    						main_circ.u(pi/2,param_0,param_0, 3)
    						main_circ.u(param_0,param_0,param_0, 1)
    main_circ.measure(2, creg_0[1])
    with main_circ.if_test((creg_0[1],0)) as else_4:
    	main_circ.measure(0, creg_0[1])
    	with main_circ.switch(creg_0[1]) as case_3:
    		with case_3(0):
    			main_circ.measure(0, creg_0[0])
    			with main_circ.if_test((creg_0[0],0)) as else_2:
    				main_circ.measure(0, creg_0[1])
    				with main_circ.if_test((creg_0[1],0)):
    					main_circ.cx(1,0)
    					main_circ.cx(1,3)
    					main_circ.cx(0,3)
    					main_circ.cx(2,1)
    			with else_2:
    				main_circ.measure(1, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.u(0,param_0,0.357000, 0)
    					main_circ.u(0,0,-0.093000, 2)
    					main_circ.cx(0,3)
    				main_circ.measure(2, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.u(param_0,0.566000,param_0, 1)
    				with else_1:
    					main_circ.u(param_0,0.233000,0.008000, 0)
    					main_circ.u(param_0,param_0,param_0, 0)
    					main_circ.u(param_0,-0.151000,0.895000, 2)
    		with case_3(1):
    			main_circ.u(pi/2,param_0,param_0, 3)
    			main_circ.barrier(3)
    with else_4:
    	main_circ.measure(1, creg_0[1])
    	with main_circ.switch(creg_0[1]) as case_3:
    		with case_3(0):
    			main_circ.measure(3, creg_0[0])
    			with main_circ.if_test((creg_0[0],0)) as else_2:
    				main_circ.id(2)
    			with else_2:
    				main_circ.measure(3, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.barrier(3)
    				main_circ.measure(3, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.barrier(2)
    				with else_1:
    					main_circ.barrier(3)
    				main_circ.id(2)
    			main_circ.measure(2, creg_0[0])
    			with main_circ.switch(creg_0[0]) as case_2:
    				with case_2(0):
    					main_circ.id(1)
    				with case_2(1):
    					main_circ.measure(3, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)):
    						main_circ.id(2)
    					main_circ.measure(0, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)):
    						main_circ.id(3)
    					main_circ.barrier(0)
    			main_circ.measure(0, creg_0[0])
    			with main_circ.if_test((creg_0[0],0)) as else_2:
    				main_circ.measure(1, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.id(1)
    				with else_1:
    					main_circ.barrier(2)
    				main_circ.measure(0, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.id(3)
    				main_circ.measure(3, creg_0[1])
    				with main_circ.if_test((creg_0[1],0)):
    					main_circ.id(2)
    				main_circ.measure(2, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.id(3)
    				main_circ.measure(2, creg_0[0])
    				with main_circ.switch(creg_0[0]) as case_1:
    					with case_1(0):
    						main_circ.barrier(3)
    					with case_1(1):
    						main_circ.id(0)
    				main_circ.barrier(0)
    			with else_2:
    				main_circ.measure(0, creg_0[1])
    				with main_circ.if_test((creg_0[1],0)):
    					main_circ.barrier(3)
    				main_circ.measure(3, creg_0[1])
    				with main_circ.if_test((creg_0[1],0)) as else_1:
    					main_circ.barrier(2)
    				with else_1:
    					main_circ.barrier(3)
    				main_circ.measure(2, creg_0[1])
    				with main_circ.if_test((creg_0[1],0)):
    					main_circ.barrier(3)
    				main_circ.measure(2, creg_0[0])
    				with main_circ.switch(creg_0[0]) as case_1:
    					with case_1(0):
    						main_circ.id(0)
    					with case_1(1):
    						main_circ.barrier(3)
    				main_circ.measure(1, creg_0[1])
    				with main_circ.switch(creg_0[1]) as case_1:
    					with case_1(0):
    						main_circ.id(1)
    					with case_1(1):
    						main_circ.barrier(3)
    				main_circ.measure(2, creg_0[1])
    				with main_circ.if_test((creg_0[1],0)) as else_1:
    					main_circ.barrier(0)
    				with else_1:
    					main_circ.id(2)
    				main_circ.measure(0, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.id(2)
    				with else_1:
    					main_circ.barrier(0)
    				main_circ.measure(2, creg_0[1])
    				with main_circ.if_test((creg_0[1],0)):
    					main_circ.barrier(3)
    				main_circ.measure(3, creg_0[1])
    				with main_circ.if_test((creg_0[1],0)) as else_1:
    					main_circ.id(0)
    				with else_1:
    					main_circ.id(3)
    				main_circ.barrier(3)
    			main_circ.barrier(0)
    		with case_3(1):
    			main_circ.measure(3, creg_0[0])
    			with main_circ.if_test((creg_0[0],0)):
    				main_circ.measure(0, creg_0[1])
    				with main_circ.if_test((creg_0[1],0)) as else_1:
    					main_circ.id(3)
    				with else_1:
    					main_circ.id(2)
    				main_circ.measure(3, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.id(0)
    				with else_1:
    					main_circ.id(3)
    				main_circ.measure(2, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.id(0)
    				with else_1:
    					main_circ.id(2)
    				main_circ.measure(2, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.barrier(1)
    				with else_1:
    					main_circ.id(2)
    				main_circ.measure(3, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.id(3)
    				with else_1:
    					main_circ.id(1)
    				main_circ.measure(0, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.barrier(1)
    				with else_1:
    					main_circ.id(0)
    				main_circ.measure(0, creg_0[1])
    				with main_circ.switch(creg_0[1]) as case_1:
    					with case_1(0):
    						main_circ.barrier(1)
    					with case_1(1):
    						main_circ.barrier(2)
    				main_circ.measure(1, creg_0[1])
    				with main_circ.switch(creg_0[1]) as case_1:
    					with case_1(0):
    						main_circ.barrier(3)
    					with case_1(1):
    						main_circ.id(1)
    				main_circ.measure(2, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.id(0)
    				with else_1:
    					main_circ.id(3)
    				main_circ.measure(0, creg_0[1])
    				with main_circ.if_test((creg_0[1],0)) as else_1:
    					main_circ.id(3)
    				with else_1:
    					main_circ.id(1)
    				main_circ.measure(3, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.barrier(0)
    				with else_1:
    					main_circ.barrier(0)
    				main_circ.measure(3, creg_0[0])
    				with main_circ.switch(creg_0[0]) as case_1:
    					with case_1(0):
    						main_circ.id(0)
    					with case_1(1):
    						main_circ.id(3)
    				main_circ.barrier(3)
    			main_circ.measure(3, creg_0[0])
    			with main_circ.if_test((creg_0[0],0)) as else_2:
    				main_circ.measure(1, creg_0[1])
    				with main_circ.if_test((creg_0[1],0)) as else_1:
    					main_circ.id(2)
    				with else_1:
    					main_circ.id(1)
    				main_circ.measure(0, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.id(0)
    				with else_1:
    					main_circ.barrier(2)
    				main_circ.measure(0, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.barrier(0)
    				main_circ.measure(2, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.id(0)
    				main_circ.measure(2, creg_0[0])
    				with main_circ.switch(creg_0[0]) as case_1:
    					with case_1(0):
    						main_circ.id(3)
    					with case_1(1):
    						main_circ.id(2)
    				main_circ.measure(2, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.barrier(2)
    				with else_1:
    					main_circ.barrier(3)
    				main_circ.id(3)
    			with else_2:
    				main_circ.id(1)
    			main_circ.id(2)
    	main_circ.measure(3, creg_0[0])
    	with main_circ.switch(creg_0[0]) as case_3:
    		with case_3(0):
    			main_circ.barrier(0)
    		with case_3(1):
    			main_circ.id(2)
    	main_circ.measure(1, creg_0[1])
    	with main_circ.if_test((creg_0[1],0)):
    		main_circ.barrier(1)
    	main_circ.id(2)
    bindings = {param_0: -0.242000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_on_simulator(main_circ, "36")


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
