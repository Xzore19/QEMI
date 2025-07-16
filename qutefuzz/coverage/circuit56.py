
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi


def main():
    
    subcirc0 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(1)
    subcirc0.add_register(qreg_0)
    qreg_1 = QuantumRegister(2)
    subcirc0.add_register(qreg_1)
    qreg_3 = QuantumRegister(1)
    subcirc0.add_register(qreg_3)
    # Adding creg resources 
    subcirc0.rx(-0.562000, qreg_3[0])
    subcirc0.rx(-0.606000, qreg_0[0])
    subcirc0.u(0.320000,-0.502000,0.027000, qreg_1[0])
    subcirc0.u(0.674000,0.759000,-0.735000, qreg_1[1])
    subcirc0 = subcirc0.to_gate().control(2)
    
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
    param_3 = Parameter("param_3")
    
    main_circ.measure(1, creg_0[0])
    with main_circ.if_test((creg_0[0],0)) as else_2:
    	main_circ.measure(2, creg_0[0])
    	with main_circ.if_test((creg_0[0],0)):
    		main_circ.u(pi/2,param_1,0.214000, 1)
    		main_circ.u(pi/2,0.681000,param_0, 1)
    	main_circ.measure(qreg_0[0], creg_0[0])
    	with main_circ.if_test((creg_0[0],0)):
    		main_circ.u(param_2,param_1,param_1, 0)
    		main_circ.append(subcirc0,[2,1,qreg_0[1],3,0,qreg_0[0]])
    with else_2:
    	main_circ.measure(qreg_0[1], creg_1[0])
    	with main_circ.if_test((creg_1[0],0)) as else_1:
    		main_circ.rx(-0.242000, 3)
    		main_circ.cz(qreg_0[0],1)
    		main_circ.append(subcirc0,[1,2,qreg_0[0],qreg_0[1],0,3])
    	with else_1:
    		main_circ.u(param_1,param_2,param_3, 0)
    main_circ.u(-0.968000,param_2,param_3, 3)
    main_circ.measure(0, creg_1[0])
    with main_circ.switch(creg_1[0]) as case_2:
    	with case_2(0):
    		main_circ.measure(qreg_0[0], creg_1[0])
    		with main_circ.if_test((creg_1[0],0)):
    			main_circ.u(-0.357000,param_1,-0.235000, 2)
    			main_circ.u(param_1,param_2,0.966000, 1)
    			main_circ.cz(qreg_0[1],2)
    			main_circ.u(param_0,param_1,param_2, qreg_0[1])
    	with case_2(1):
    		main_circ.measure(3, creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_1:
    			with case_1(0):
    				main_circ.u(param_1,-0.732000,-0.869000, 0)
    				main_circ.u(param_2,0.638000,param_2, 1)
    				main_circ.rx(-0.583000, qreg_0[0])
    				main_circ.cz(3,2)
    			with case_1(1):
    				main_circ.cz(2,qreg_0[0])
    				main_circ.cz(qreg_0[1],2)
    				main_circ.u(param_1,param_0,-0.651000, 0)
    				main_circ.append(subcirc0,[3,1,qreg_0[1],2,qreg_0[0],0])
    main_circ.measure(0, creg_0[0])
    with main_circ.if_test((creg_0[0],0)) as else_2:
    	main_circ.measure(qreg_0[0], creg_1[0])
    	with main_circ.if_test((creg_1[0],0)):
    		main_circ.u(param_3,param_3,0.439000, 2)
    	main_circ.measure(0, creg_0[0])
    	with main_circ.if_test((creg_0[0],0)):
    		main_circ.cz(0,qreg_0[1])
    	main_circ.measure(0, creg_0[0])
    	with main_circ.if_test((creg_0[0],0)) as else_1:
    		main_circ.u(param_2,0.076000,0.477000, qreg_0[0])
    	with else_1:
    		main_circ.cz(2,0)
    with else_2:
    	main_circ.measure(3, creg_0[0])
    	with main_circ.switch(creg_0[0]) as case_1:
    		with case_1(0):
    			main_circ.append(subcirc0,[qreg_0[1],3,0,2,1,qreg_0[0]])
    		with case_1(1):
    			main_circ.cz(0,2)
    			main_circ.cz(qreg_0[1],0)
    			main_circ.cz(qreg_0[0],qreg_0[1])
    			main_circ.cz(1,3)
    main_circ.measure(qreg_0[1], creg_0[0])
    with main_circ.if_test((creg_0[0],0)):
    	main_circ.measure(0, creg_1[0])
    	with main_circ.if_test((creg_1[0],0)) as else_1:
    		main_circ.cz(2,0)
    		main_circ.cz(qreg_0[0],2)
    		main_circ.cz(1,qreg_0[0])
    	with else_1:
    		main_circ.append(subcirc0,[3,0,qreg_0[1],2,qreg_0[0],1])
    		main_circ.id(3)
    bindings = {param_0: -0.126000, param_1: -0.010000, param_2: -0.737000, param_3: -0.215000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_pass_on_simulator(main_circ, "56", "Collect2qBlocks")


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
