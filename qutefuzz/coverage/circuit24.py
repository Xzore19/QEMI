
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi


def main():
    
    subcirc0 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(4)
    subcirc0.add_register(qreg_0)
    # Adding creg resources 
    subcirc0.u(pi/2,0.658000,0.402000, qreg_0[2])
    subcirc0.z(qreg_0[0])
    subcirc0.u(-0.200000,-0.175000,-0.894000, qreg_0[1])
    subcirc0.z(qreg_0[1])
    subcirc0.u(pi/2,-0.837000,-0.164000, qreg_0[1])
    subcirc0.z(qreg_0[2])
    
    main_circ = QuantumCircuit(4)
    # Adding qregs 
    # Adding creg resources 
    creg_0 = ClassicalRegister(1)
    main_circ.add_register(creg_0)
    creg_1 = ClassicalRegister(1)
    main_circ.add_register(creg_1)
    # Adding symbols 
    param_0 = Parameter("param_0")
    param_1 = Parameter("param_1")
    
    main_circ.measure(0, creg_0[0])
    with main_circ.if_test((creg_0[0],0)) as else_3:
    	main_circ.append(subcirc0,[1,3,0,2])
    with else_3:
    	main_circ.measure(2, creg_1[0])
    	with main_circ.if_test((creg_1[0],0)) as else_2:
    		main_circ.measure(3, creg_1[0])
    		with main_circ.switch(creg_1[0]) as case_1:
    			with case_1(0):
    				main_circ.u(-0.944000,param_0,-0.407000, 1)
    				main_circ.append(subcirc0,[2,1,0,3])
    			with case_1(1):
    				main_circ.rx(param_0, 2)
    				main_circ.rx(0.158000, 1)
    				main_circ.rx(0.370000, 0)
    				main_circ.z(2)
    	with else_2:
    		main_circ.append(subcirc0,[3,0,2,1])
    main_circ.measure(2, creg_0[0])
    with main_circ.if_test((creg_0[0],0)):
    	main_circ.measure(3, creg_0[0])
    	with main_circ.if_test((creg_0[0],0)):
    		main_circ.measure(1, creg_1[0])
    		with main_circ.if_test((creg_1[0],0)):
    			main_circ.rx(0.991000, 3)
    			main_circ.u(pi/2,param_0,param_0, 0)
    			main_circ.rx(-0.664000, 1)
    	main_circ.measure(1, creg_1[0])
    	with main_circ.switch(creg_1[0]) as case_2:
    		with case_2(0):
    			main_circ.measure(0, creg_0[0])
    			with main_circ.switch(creg_0[0]) as case_1:
    				with case_1(0):
    					main_circ.u(param_1,param_1,-0.550000, 3)
    					main_circ.z(2)
    					main_circ.z(0)
    					main_circ.u(param_1,param_0,param_0, 1)
    				with case_1(1):
    					main_circ.append(subcirc0,[1,3,2,0])
    		with case_2(1):
    			main_circ.measure(2, creg_1[0])
    			with main_circ.if_test((creg_1[0],0)):
    				main_circ.rx(param_0, 3)
    			main_circ.measure(3, creg_1[0])
    			with main_circ.if_test((creg_1[0],0)):
    				main_circ.z(2)
    			main_circ.measure(0, creg_0[0])
    			with main_circ.if_test((creg_0[0],0)):
    				main_circ.rx(-0.184000, 1)
    				main_circ.u(param_1,param_0,param_1, 3)
    				main_circ.id(1)
    main_circ.u(param_1,-0.814000,-0.329000, 1)
    main_circ.z(0)
    main_circ.z(3)
    main_circ.measure(2, creg_1[0])
    with main_circ.if_test((creg_1[0],0)) as else_3:
    	main_circ.measure(3, creg_1[0])
    	with main_circ.switch(creg_1[0]) as case_2:
    		with case_2(0):
    			main_circ.measure(2, creg_1[0])
    			with main_circ.switch(creg_1[0]) as case_1:
    				with case_1(0):
    					main_circ.u(param_0,param_0,0.505000, 3)
    					main_circ.id(2)
    				with case_1(1):
    					main_circ.id(0)
    			main_circ.measure(0, creg_1[0])
    			with main_circ.if_test((creg_1[0],0)):
    				main_circ.id(3)
    			main_circ.id(3)
    		with case_2(1):
    			main_circ.measure(1, creg_1[0])
    			with main_circ.if_test((creg_1[0],0)):
    				main_circ.id(3)
    			main_circ.measure(1, creg_0[0])
    			with main_circ.if_test((creg_0[0],0)) as else_1:
    				main_circ.barrier(3)
    			with else_1:
    				main_circ.id(3)
    			main_circ.barrier(3)
    	main_circ.measure(1, creg_0[0])
    	with main_circ.if_test((creg_0[0],0)):
    		main_circ.measure(0, creg_0[0])
    		with main_circ.if_test((creg_0[0],0)):
    			main_circ.id(0)
    		main_circ.barrier(0)
    	main_circ.measure(3, creg_0[0])
    	with main_circ.if_test((creg_0[0],0)):
    		main_circ.id(3)
    	main_circ.measure(1, creg_1[0])
    	with main_circ.switch(creg_1[0]) as case_2:
    		with case_2(0):
    			main_circ.barrier(2)
    		with case_2(1):
    			main_circ.barrier(1)
    	main_circ.measure(1, creg_0[0])
    	with main_circ.if_test((creg_0[0],0)) as else_2:
    		main_circ.barrier(1)
    	with else_2:
    		main_circ.id(2)
    	main_circ.measure(2, creg_1[0])
    	with main_circ.if_test((creg_1[0],0)) as else_2:
    		main_circ.measure(3, creg_1[0])
    		with main_circ.if_test((creg_1[0],0)):
    			main_circ.barrier(3)
    		main_circ.measure(2, creg_1[0])
    		with main_circ.switch(creg_1[0]) as case_1:
    			with case_1(0):
    				main_circ.id(3)
    			with case_1(1):
    				main_circ.id(1)
    		main_circ.measure(2, creg_1[0])
    		with main_circ.switch(creg_1[0]) as case_1:
    			with case_1(0):
    				main_circ.barrier(1)
    			with case_1(1):
    				main_circ.barrier(3)
    		main_circ.measure(2, creg_1[0])
    		with main_circ.if_test((creg_1[0],0)) as else_1:
    			main_circ.id(0)
    		with else_1:
    			main_circ.id(2)
    		main_circ.measure(1, creg_1[0])
    		with main_circ.if_test((creg_1[0],0)) as else_1:
    			main_circ.id(1)
    		with else_1:
    			main_circ.barrier(0)
    		main_circ.measure(3, creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_1:
    			with case_1(0):
    				main_circ.barrier(3)
    			with case_1(1):
    				main_circ.id(3)
    		main_circ.id(1)
    	with else_2:
    		main_circ.measure(1, creg_0[0])
    		with main_circ.if_test((creg_0[0],0)) as else_1:
    			main_circ.id(3)
    		with else_1:
    			main_circ.id(1)
    		main_circ.id(0)
    	main_circ.measure(3, creg_1[0])
    	with main_circ.if_test((creg_1[0],0)):
    		main_circ.measure(2, creg_1[0])
    		with main_circ.if_test((creg_1[0],0)) as else_1:
    			main_circ.barrier(0)
    		with else_1:
    			main_circ.barrier(0)
    		main_circ.measure(2, creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_1:
    			with case_1(0):
    				main_circ.id(1)
    			with case_1(1):
    				main_circ.id(2)
    		main_circ.id(3)
    	main_circ.measure(1, creg_1[0])
    	with main_circ.if_test((creg_1[0],0)) as else_2:
    		main_circ.barrier(1)
    	with else_2:
    		main_circ.measure(0, creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_1:
    			with case_1(0):
    				main_circ.barrier(1)
    			with case_1(1):
    				main_circ.id(0)
    		main_circ.measure(2, creg_0[0])
    		with main_circ.if_test((creg_0[0],0)) as else_1:
    			main_circ.id(0)
    		with else_1:
    			main_circ.barrier(3)
    		main_circ.measure(1, creg_1[0])
    		with main_circ.if_test((creg_1[0],0)):
    			main_circ.id(0)
    		main_circ.measure(1, creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_1:
    			with case_1(0):
    				main_circ.barrier(0)
    			with case_1(1):
    				main_circ.id(0)
    		main_circ.id(0)
    	main_circ.measure(1, creg_0[0])
    	with main_circ.switch(creg_0[0]) as case_2:
    		with case_2(0):
    			main_circ.measure(1, creg_1[0])
    			with main_circ.if_test((creg_1[0],0)) as else_1:
    				main_circ.barrier(3)
    			with else_1:
    				main_circ.id(0)
    			main_circ.measure(2, creg_1[0])
    			with main_circ.if_test((creg_1[0],0)) as else_1:
    				main_circ.barrier(3)
    			with else_1:
    				main_circ.id(0)
    			main_circ.barrier(1)
    		with case_2(1):
    			main_circ.measure(3, creg_1[0])
    			with main_circ.switch(creg_1[0]) as case_1:
    				with case_1(0):
    					main_circ.id(3)
    				with case_1(1):
    					main_circ.barrier(2)
    			main_circ.measure(0, creg_0[0])
    			with main_circ.if_test((creg_0[0],0)):
    				main_circ.id(0)
    			main_circ.measure(1, creg_0[0])
    			with main_circ.switch(creg_0[0]) as case_1:
    				with case_1(0):
    					main_circ.barrier(3)
    				with case_1(1):
    					main_circ.id(2)
    			main_circ.measure(2, creg_1[0])
    			with main_circ.switch(creg_1[0]) as case_1:
    				with case_1(0):
    					main_circ.barrier(0)
    				with case_1(1):
    					main_circ.id(3)
    			main_circ.measure(3, creg_0[0])
    			with main_circ.switch(creg_0[0]) as case_1:
    				with case_1(0):
    					main_circ.id(2)
    				with case_1(1):
    					main_circ.id(3)
    			main_circ.measure(0, creg_0[0])
    			with main_circ.if_test((creg_0[0],0)):
    				main_circ.barrier(3)
    			main_circ.measure(1, creg_0[0])
    			with main_circ.if_test((creg_0[0],0)):
    				main_circ.barrier(1)
    			main_circ.measure(2, creg_0[0])
    			with main_circ.if_test((creg_0[0],0)):
    				main_circ.barrier(0)
    			main_circ.measure(2, creg_0[0])
    			with main_circ.if_test((creg_0[0],0)):
    				main_circ.id(0)
    			main_circ.measure(2, creg_0[0])
    			with main_circ.if_test((creg_0[0],0)):
    				main_circ.id(2)
    			main_circ.measure(3, creg_0[0])
    			with main_circ.switch(creg_0[0]) as case_1:
    				with case_1(0):
    					main_circ.id(1)
    				with case_1(1):
    					main_circ.barrier(0)
    			main_circ.barrier(0)
    	main_circ.measure(1, creg_1[0])
    	with main_circ.switch(creg_1[0]) as case_2:
    		with case_2(0):
    			main_circ.barrier(3)
    		with case_2(1):
    			main_circ.measure(0, creg_0[0])
    			with main_circ.switch(creg_0[0]) as case_1:
    				with case_1(0):
    					main_circ.id(0)
    				with case_1(1):
    					main_circ.id(3)
    			main_circ.id(1)
    	main_circ.measure(1, creg_0[0])
    	with main_circ.if_test((creg_0[0],0)) as else_2:
    		main_circ.measure(0, creg_1[0])
    		with main_circ.if_test((creg_1[0],0)):
    			main_circ.barrier(0)
    		main_circ.measure(2, creg_0[0])
    		with main_circ.if_test((creg_0[0],0)) as else_1:
    			main_circ.barrier(2)
    		with else_1:
    			main_circ.barrier(2)
    		main_circ.measure(2, creg_0[0])
    		with main_circ.if_test((creg_0[0],0)) as else_1:
    			main_circ.barrier(2)
    		with else_1:
    			main_circ.id(0)
    		main_circ.id(0)
    	with else_2:
    		main_circ.measure(2, creg_1[0])
    		with main_circ.switch(creg_1[0]) as case_1:
    			with case_1(0):
    				main_circ.barrier(3)
    			with case_1(1):
    				main_circ.id(1)
    		main_circ.measure(3, creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_1:
    			with case_1(0):
    				main_circ.id(3)
    			with case_1(1):
    				main_circ.id(0)
    		main_circ.measure(1, creg_1[0])
    		with main_circ.if_test((creg_1[0],0)) as else_1:
    			main_circ.barrier(1)
    		with else_1:
    			main_circ.id(2)
    		main_circ.measure(3, creg_0[0])
    		with main_circ.if_test((creg_0[0],0)):
    			main_circ.barrier(1)
    		main_circ.measure(3, creg_1[0])
    		with main_circ.switch(creg_1[0]) as case_1:
    			with case_1(0):
    				main_circ.id(2)
    			with case_1(1):
    				main_circ.id(0)
    		main_circ.measure(3, creg_1[0])
    		with main_circ.if_test((creg_1[0],0)) as else_1:
    			main_circ.barrier(3)
    		with else_1:
    			main_circ.id(1)
    		main_circ.measure(3, creg_0[0])
    		with main_circ.if_test((creg_0[0],0)):
    			main_circ.barrier(0)
    		main_circ.measure(1, creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_1:
    			with case_1(0):
    				main_circ.id(0)
    			with case_1(1):
    				main_circ.id(1)
    		main_circ.measure(1, creg_1[0])
    		with main_circ.if_test((creg_1[0],0)):
    			main_circ.barrier(3)
    		main_circ.barrier(1)
    	main_circ.barrier(3)
    with else_3:
    	main_circ.measure(3, creg_0[0])
    	with main_circ.if_test((creg_0[0],0)) as else_2:
    		main_circ.measure(2, creg_1[0])
    		with main_circ.if_test((creg_1[0],0)) as else_1:
    			main_circ.barrier(0)
    		with else_1:
    			main_circ.barrier(3)
    		main_circ.measure(2, creg_1[0])
    		with main_circ.if_test((creg_1[0],0)) as else_1:
    			main_circ.id(0)
    		with else_1:
    			main_circ.id(3)
    		main_circ.measure(0, creg_1[0])
    		with main_circ.if_test((creg_1[0],0)):
    			main_circ.barrier(1)
    		main_circ.measure(2, creg_0[0])
    		with main_circ.if_test((creg_0[0],0)) as else_1:
    			main_circ.id(0)
    		with else_1:
    			main_circ.barrier(2)
    		main_circ.measure(1, creg_0[0])
    		with main_circ.if_test((creg_0[0],0)) as else_1:
    			main_circ.id(0)
    		with else_1:
    			main_circ.barrier(2)
    		main_circ.barrier(3)
    	with else_2:
    		main_circ.measure(2, creg_1[0])
    		with main_circ.if_test((creg_1[0],0)) as else_1:
    			main_circ.id(2)
    		with else_1:
    			main_circ.barrier(0)
    		main_circ.measure(0, creg_0[0])
    		with main_circ.if_test((creg_0[0],0)):
    			main_circ.id(2)
    		main_circ.measure(2, creg_1[0])
    		with main_circ.switch(creg_1[0]) as case_1:
    			with case_1(0):
    				main_circ.id(3)
    			with case_1(1):
    				main_circ.barrier(2)
    		main_circ.id(3)
    	main_circ.measure(0, creg_0[0])
    	with main_circ.if_test((creg_0[0],0)):
    		main_circ.measure(0, creg_1[0])
    		with main_circ.if_test((creg_1[0],0)) as else_1:
    			main_circ.id(0)
    		with else_1:
    			main_circ.id(3)
    		main_circ.id(3)
    	main_circ.measure(1, creg_1[0])
    	with main_circ.if_test((creg_1[0],0)):
    		main_circ.measure(2, creg_0[0])
    		with main_circ.if_test((creg_0[0],0)):
    			main_circ.barrier(1)
    		main_circ.measure(3, creg_1[0])
    		with main_circ.if_test((creg_1[0],0)):
    			main_circ.barrier(3)
    		main_circ.barrier(1)
    	main_circ.id(1)
    bindings = {param_0: -0.044000, param_1: 0.052000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_on_simulator(main_circ, "24")


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
