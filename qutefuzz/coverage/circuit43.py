
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
    subcirc0.rz(-0.977000, qreg_0[0])
    subcirc0.u(0.175000,0.485000,-0.597000, qreg_0[1])
    subcirc0.u(0.921000,0.078000,0.406000, qreg_0[0])
    subcirc0.y(qreg_0[2])
    subcirc0.rz(-0.494000, qreg_0[1])
    subcirc0 = subcirc0.to_gate().control(3)
    
    subcirc1 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(2)
    subcirc1.add_register(qreg_0)
    qreg_2 = QuantumRegister(1)
    subcirc1.add_register(qreg_2)
    qreg_3 = QuantumRegister(1)
    subcirc1.add_register(qreg_3)
    # Adding creg resources 
    subcirc1.rz(-0.950000, qreg_3[0])
    subcirc1.rz(-0.801000, qreg_2[0])
    subcirc1.u(0,0,0.184000, qreg_3[0])
    subcirc1.y(qreg_0[0])
    subcirc1.u(-0.099000,0.457000,-0.287000, qreg_3[0])
    subcirc1 = subcirc1.to_gate().control(1)
    
    subcirc2 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(2)
    subcirc2.add_register(qreg_0)
    qreg_2 = QuantumRegister(2)
    subcirc2.add_register(qreg_2)
    # Adding creg resources 
    subcirc2.rz(0.724000, qreg_2[1])
    subcirc2.u(-0.577000,-0.104000,0.928000, qreg_2[0])
    subcirc2.rz(0.728000, qreg_0[0])
    subcirc2.rz(0.203000, qreg_2[0])
    subcirc2.rz(-0.428000, qreg_0[1])
    subcirc2 = subcirc2.to_gate().control(2)
    
    subcirc3 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(3)
    subcirc3.add_register(qreg_0)
    qreg_3 = QuantumRegister(1)
    subcirc3.add_register(qreg_3)
    # Adding creg resources 
    subcirc3.u(-0.477000,-0.955000,-0.006000, qreg_3[0])
    subcirc3.u(0,0,0.283000, qreg_0[0])
    subcirc3.y(qreg_0[0])
    subcirc3.y(qreg_3[0])
    subcirc3.u(0,0,0.423000, qreg_0[0])
    
    subcirc4 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(4)
    subcirc4.add_register(qreg_0)
    # Adding creg resources 
    subcirc4.rz(0.390000, qreg_0[3])
    subcirc4.u(-0.691000,-0.101000,-0.108000, qreg_0[3])
    subcirc4.rz(-0.462000, qreg_0[3])
    subcirc4.y(qreg_0[0])
    subcirc4.rz(0.719000, qreg_0[0])
    subcirc4 = subcirc4.to_gate().control(3)
    
    main_circ = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(4)
    main_circ.add_register(qreg_0)
    # Adding creg resources 
    creg_0 = ClassicalRegister(2)
    main_circ.add_register(creg_0)
    # Adding symbols 
    param_0 = Parameter("param_0")
    param_1 = Parameter("param_1")
    param_2 = Parameter("param_2")
    param_3 = Parameter("param_3")
    param_4 = Parameter("param_4")
    param_5 = Parameter("param_5")
    
    main_circ.measure(qreg_0[2], creg_0[0])
    with main_circ.if_test((creg_0[0],0)):
    	main_circ.u(0.255000,param_3,param_4, qreg_0[1])
    main_circ.measure(qreg_0[0], creg_0[0])
    with main_circ.if_test((creg_0[0],0)) as else_2:
    	main_circ.measure(qreg_0[3], creg_0[1])
    	with main_circ.switch(creg_0[1]) as case_1:
    		with case_1(0):
    			main_circ.id(qreg_0[2])
    		with case_1(1):
    			main_circ.barrier(qreg_0[0])
    	main_circ.measure(qreg_0[1], creg_0[0])
    	with main_circ.if_test((creg_0[0],0)):
    		main_circ.y(qreg_0[3])
    with else_2:
    	main_circ.id(qreg_0[1])
    main_circ.measure(qreg_0[3], creg_0[0])
    with main_circ.if_test((creg_0[0],0)):
    	main_circ.measure(qreg_0[2], creg_0[1])
    	with main_circ.if_test((creg_0[1],0)):
    		main_circ.id(qreg_0[3])
    	main_circ.measure(qreg_0[1], creg_0[0])
    	with main_circ.switch(creg_0[0]) as case_1:
    		with case_1(0):
    			main_circ.barrier(qreg_0[1])
    		with case_1(1):
    			main_circ.append(subcirc3,[qreg_0[2],qreg_0[3],qreg_0[0],qreg_0[1]])
    main_circ.append(subcirc3,[qreg_0[2],qreg_0[1],qreg_0[0],qreg_0[3]])
    main_circ.measure(qreg_0[2], creg_0[0])
    with main_circ.if_test((creg_0[0],0)):
    	main_circ.measure(qreg_0[1], creg_0[0])
    	with main_circ.if_test((creg_0[0],0)):
    		main_circ.id(qreg_0[3])
    	main_circ.rz(0.019000, qreg_0[0])
    	main_circ.measure(qreg_0[3], creg_0[1])
    	with main_circ.if_test((creg_0[1],0)) as else_1:
    		main_circ.id(qreg_0[0])
    	with else_1:
    		main_circ.append(subcirc3,[qreg_0[2],qreg_0[1],qreg_0[3],qreg_0[0]])
    main_circ.measure(qreg_0[2], creg_0[0])
    with main_circ.switch(creg_0[0]) as case_2:
    	with case_2(0):
    		main_circ.measure(qreg_0[2], creg_0[0])
    		with main_circ.if_test((creg_0[0],0)) as else_1:
    			main_circ.rz(param_4, qreg_0[1])
    			main_circ.id(qreg_0[3])
    		with else_1:
    			main_circ.u(param_2,param_4,param_1, qreg_0[2])
    			main_circ.barrier(qreg_0[2])
    		main_circ.measure(qreg_0[3], creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_1:
    			with case_1(0):
    				main_circ.barrier(qreg_0[3])
    			with case_1(1):
    				main_circ.u(param_2,param_5,-0.498000, qreg_0[2])
    				main_circ.u(0,0,-0.671000, qreg_0[3])
    				main_circ.append(subcirc3,[qreg_0[3],qreg_0[1],qreg_0[2],qreg_0[0]])
    	with case_2(1):
    		main_circ.y(qreg_0[1])
    		main_circ.measure(qreg_0[3], creg_0[0])
    		with main_circ.if_test((creg_0[0],0)) as else_1:
    			main_circ.id(qreg_0[3])
    		with else_1:
    			main_circ.id(qreg_0[3])
    		main_circ.measure(qreg_0[0], creg_0[0])
    		with main_circ.if_test((creg_0[0],0)) as else_1:
    			main_circ.u(param_5,0,0.078000, qreg_0[2])
    			main_circ.barrier(qreg_0[3])
    		with else_1:
    			main_circ.id(qreg_0[0])
    		main_circ.id(qreg_0[1])
    main_circ.measure(qreg_0[2], creg_0[0])
    with main_circ.switch(creg_0[0]) as case_2:
    	with case_2(0):
    		main_circ.rz(param_1, qreg_0[2])
    		main_circ.rz(-0.314000, qreg_0[1])
    		main_circ.append(subcirc3,[qreg_0[0],qreg_0[2],qreg_0[1],qreg_0[3]])
    	with case_2(1):
    		main_circ.measure(qreg_0[3], creg_0[1])
    		with main_circ.switch(creg_0[1]) as case_1:
    			with case_1(0):
    				main_circ.barrier(qreg_0[3])
    			with case_1(1):
    				main_circ.append(subcirc3,[qreg_0[0],qreg_0[3],qreg_0[1],qreg_0[2]])
    main_circ.measure(qreg_0[0], creg_0[1])
    with main_circ.if_test((creg_0[1],0)) as else_2:
    	main_circ.measure(qreg_0[1], creg_0[1])
    	with main_circ.switch(creg_0[1]) as case_1:
    		with case_1(0):
    			main_circ.u(0,param_5,-0.855000, qreg_0[2])
    			main_circ.u(0,param_5,param_4, qreg_0[3])
    			main_circ.u(param_4,0,0.769000, qreg_0[3])
    			main_circ.id(qreg_0[1])
    		with case_1(1):
    			main_circ.id(qreg_0[1])
    with else_2:
    	main_circ.measure(qreg_0[3], creg_0[1])
    	with main_circ.if_test((creg_0[1],0)) as else_1:
    		main_circ.id(qreg_0[1])
    	with else_1:
    		main_circ.id(qreg_0[2])
    	main_circ.barrier(qreg_0[1])
    main_circ.measure(qreg_0[1], creg_0[0])
    with main_circ.switch(creg_0[0]) as case_2:
    	with case_2(0):
    		main_circ.measure(qreg_0[1], creg_0[0])
    		with main_circ.if_test((creg_0[0],0)):
    			main_circ.barrier(qreg_0[3])
    		main_circ.measure(qreg_0[1], creg_0[1])
    		with main_circ.switch(creg_0[1]) as case_1:
    			with case_1(0):
    				main_circ.barrier(qreg_0[3])
    			with case_1(1):
    				main_circ.id(qreg_0[1])
    		main_circ.measure(qreg_0[1], creg_0[1])
    		with main_circ.switch(creg_0[1]) as case_1:
    			with case_1(0):
    				main_circ.id(qreg_0[2])
    			with case_1(1):
    				main_circ.id(qreg_0[1])
    		main_circ.rz(param_2, qreg_0[0])
    		main_circ.y(qreg_0[0])
    		main_circ.measure(qreg_0[0], creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_1:
    			with case_1(0):
    				main_circ.id(qreg_0[0])
    			with case_1(1):
    				main_circ.rz(param_1, qreg_0[2])
    				main_circ.id(qreg_0[0])
    		main_circ.measure(qreg_0[3], creg_0[0])
    		with main_circ.if_test((creg_0[0],0)):
    			main_circ.barrier(qreg_0[0])
    		main_circ.measure(qreg_0[0], creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_1:
    			with case_1(0):
    				main_circ.id(qreg_0[0])
    			with case_1(1):
    				main_circ.barrier(qreg_0[2])
    		main_circ.id(qreg_0[1])
    	with case_2(1):
    		main_circ.barrier(qreg_0[2])
    bindings = {param_1: -0.963000, param_2: 0.757000, param_3: 0.030000, param_4: 0.888000, param_5: -0.844000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_pass_on_simulator(main_circ, "43", "TemplateOptimization")


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
