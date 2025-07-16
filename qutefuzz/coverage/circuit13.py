
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
    qreg_2 = QuantumRegister(2)
    subcirc0.add_register(qreg_2)
    # Adding creg resources 
    subcirc0.s(qreg_0[1])
    subcirc0.cy(qreg_0[0],qreg_2[1])
    subcirc0.x(qreg_0[1])
    subcirc0.s(qreg_2[1])
    
    main_circ = QuantumCircuit(2)
    # Adding qregs 
    qreg_0 = QuantumRegister(3)
    main_circ.add_register(qreg_0)
    qreg_3 = QuantumRegister(1)
    main_circ.add_register(qreg_3)
    # Adding creg resources 
    creg_0 = ClassicalRegister(2)
    main_circ.add_register(creg_0)
    # Adding symbols 
    param_0 = Parameter("param_0")
    param_1 = Parameter("param_1")
    param_2 = Parameter("param_2")
    param_3 = Parameter("param_3")
    
    main_circ.append(subcirc0,[0,qreg_0[2],qreg_0[0],1])
    main_circ.measure(qreg_3[0], creg_0[1])
    with main_circ.if_test((creg_0[1],0)) as else_2:
    	main_circ.measure(qreg_0[0], creg_0[0])
    	with main_circ.if_test((creg_0[0],0)) as else_1:
    		main_circ.cy(0,qreg_0[2])
    		main_circ.append(subcirc0,[1,qreg_0[2],qreg_0[0],qreg_0[1]])
    	with else_1:
    		main_circ.x(qreg_0[1])
    		main_circ.append(subcirc0,[qreg_0[0],qreg_0[2],qreg_0[1],1])
    with else_2:
    	main_circ.measure(1, creg_0[0])
    	with main_circ.switch(creg_0[0]) as case_1:
    		with case_1(0):
    			main_circ.append(subcirc0,[qreg_0[0],0,qreg_0[2],qreg_3[0]])
    		with case_1(1):
    			main_circ.append(subcirc0,[1,qreg_0[2],qreg_0[0],qreg_0[1]])
    main_circ.measure(0, creg_0[0])
    with main_circ.if_test((creg_0[0],0)) as else_2:
    	main_circ.measure(qreg_0[0], creg_0[0])
    	with main_circ.if_test((creg_0[0],0)):
    		main_circ.append(subcirc0,[qreg_0[2],qreg_0[0],qreg_3[0],qreg_0[1]])
    with else_2:
    	main_circ.measure(qreg_0[0], creg_0[1])
    	with main_circ.if_test((creg_0[1],0)):
    		main_circ.s(1)
    		main_circ.u(param_1,-0.569000,-0.052000, 0)
    		main_circ.x(qreg_0[1])
    	main_circ.measure(qreg_3[0], creg_0[1])
    	with main_circ.if_test((creg_0[1],0)) as else_1:
    		main_circ.u(pi/2,param_0,0.458000, qreg_3[0])
    		main_circ.s(qreg_0[2])
    	with else_1:
    		main_circ.u(param_1,param_3,-0.601000, 1)
    		main_circ.append(subcirc0,[qreg_3[0],qreg_0[1],qreg_0[2],1])
    main_circ.cy(1,qreg_0[1])
    main_circ.measure(qreg_3[0], creg_0[0])
    with main_circ.if_test((creg_0[0],0)):
    	main_circ.measure(qreg_3[0], creg_0[1])
    	with main_circ.switch(creg_0[1]) as case_1:
    		with case_1(0):
    			main_circ.cy(1,0)
    			main_circ.cy(qreg_0[0],qreg_0[1])
    			main_circ.cy(0,qreg_0[0])
    			main_circ.cy(qreg_3[0],qreg_0[0])
    		with case_1(1):
    			main_circ.cy(qreg_0[0],0)
    			main_circ.x(qreg_0[2])
    			main_circ.cy(0,1)
    			main_circ.id(qreg_0[2])
    main_circ.x(qreg_0[2])
    main_circ.u(param_3,-0.386000,param_1, qreg_0[2])
    main_circ.measure(0, creg_0[1])
    with main_circ.if_test((creg_0[1],0)) as else_2:
    	main_circ.measure(qreg_0[1], creg_0[1])
    	with main_circ.switch(creg_0[1]) as case_1:
    		with case_1(0):
    			main_circ.u(pi/2,param_0,-0.236000, 1)
    			main_circ.id(qreg_3[0])
    		with case_1(1):
    			main_circ.id(0)
    	main_circ.measure(qreg_0[2], creg_0[0])
    	with main_circ.switch(creg_0[0]) as case_1:
    		with case_1(0):
    			main_circ.id(qreg_0[0])
    		with case_1(1):
    			main_circ.id(qreg_0[1])
    	main_circ.measure(1, creg_0[0])
    	with main_circ.switch(creg_0[0]) as case_1:
    		with case_1(0):
    			main_circ.barrier(qreg_0[0])
    		with case_1(1):
    			main_circ.id(0)
    	main_circ.measure(qreg_3[0], creg_0[0])
    	with main_circ.if_test((creg_0[0],0)) as else_1:
    		main_circ.barrier(qreg_3[0])
    	with else_1:
    		main_circ.id(qreg_0[0])
    	main_circ.barrier(qreg_0[0])
    with else_2:
    	main_circ.measure(1, creg_0[1])
    	with main_circ.if_test((creg_0[1],0)):
    		main_circ.id(qreg_0[2])
    	main_circ.measure(qreg_0[0], creg_0[1])
    	with main_circ.if_test((creg_0[1],0)):
    		main_circ.id(qreg_0[2])
    	main_circ.barrier(qreg_0[2])
    bindings = {param_0: -0.845000, param_1: 0.249000, param_3: -0.631000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_on_simulator(main_circ, "13")


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
