
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
    qreg_1 = QuantumRegister(3)
    subcirc0.add_register(qreg_1)
    # Adding creg resources 
    subcirc0.u(pi/2,0.675000,0.256000, qreg_1[0])
    subcirc0.u(pi/2,-0.854000,0.739000, qreg_0[0])
    subcirc0.s(qreg_1[2])
    subcirc0.s(qreg_1[1])
    subcirc0.u(0,0,-0.581000, qreg_1[1])
    subcirc0.u(0,0,0.362000, qreg_1[2])
    subcirc0 = subcirc0.to_gate().control(2)
    
    subcirc1 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(3)
    subcirc1.add_register(qreg_0)
    qreg_3 = QuantumRegister(1)
    subcirc1.add_register(qreg_3)
    # Adding creg resources 
    subcirc1.u(pi/2,-0.776000,0.639000, qreg_0[2])
    subcirc1.s(qreg_3[0])
    subcirc1.u(pi/2,-0.616000,0.792000, qreg_0[0])
    subcirc1.s(qreg_3[0])
    subcirc1.u(-0.581000,-0.443000,0.353000, qreg_3[0])
    subcirc1.u(pi/2,0.738000,-0.175000, qreg_0[2])
    
    subcirc2 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(3)
    subcirc2.add_register(qreg_0)
    qreg_3 = QuantumRegister(1)
    subcirc2.add_register(qreg_3)
    # Adding creg resources 
    subcirc2.u(0.283000,0.439000,-0.740000, qreg_3[0])
    subcirc2.s(qreg_3[0])
    subcirc2.u(pi/2,-0.424000,0.446000, qreg_0[1])
    subcirc2.u(0.590000,0.749000,-0.870000, qreg_0[2])
    subcirc2.u(0,0,-0.114000, qreg_3[0])
    subcirc2.s(qreg_0[2])
    
    main_circ = QuantumCircuit(4)
    # Adding qregs 
    # Adding creg resources 
    creg_0 = ClassicalRegister(2)
    main_circ.add_register(creg_0)
    # Adding symbols 
    param_0 = Parameter("param_0")
    param_1 = Parameter("param_1")
    param_2 = Parameter("param_2")
    param_3 = Parameter("param_3")
    
    main_circ.u(param_3,0.751000,param_1, 0)
    main_circ.measure(0, creg_0[1])
    with main_circ.switch(creg_0[1]) as case_4:
    	with case_4(0):
    		main_circ.measure(3, creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_3:
    			with case_3(0):
    				main_circ.measure(1, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)):
    					main_circ.measure(3, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)):
    						main_circ.u(param_3,param_3,param_0, 1)
    					main_circ.measure(1, creg_0[0])
    					with main_circ.switch(creg_0[0]) as case_1:
    						with case_1(0):
    							main_circ.u(0,param_3,0.446000, 3)
    							main_circ.u(param_3,param_1,0.325000, 1)
    							main_circ.u(0.600000,param_2,param_1, 3)
    							main_circ.u(0,0,0.658000, 0)
    						with case_1(1):
    							main_circ.u(param_1,param_2,param_3, 0)
    							main_circ.u(param_0,param_0,param_2, 1)
    							main_circ.id(2)
    			with case_3(1):
    				main_circ.u(0,param_0,param_1, 1)
    				main_circ.measure(3, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_2:
    					main_circ.measure(3, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)):
    						main_circ.u(param_1,0,param_3, 0)
    						main_circ.u(pi/2,param_0,param_2, 2)
    						main_circ.u(param_0,param_2,param_2, 1)
    						main_circ.u(param_0,0.377000,-0.260000, 1)
    						main_circ.append(subcirc1,[0,2,1,3])
    				with else_2:
    					main_circ.measure(1, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)):
    						main_circ.barrier(3)
    					main_circ.u(0,0,param_0, 0)
    					main_circ.id(3)
    	with case_4(1):
    		main_circ.u(0,0,param_0, 2)
    		main_circ.measure(3, creg_0[1])
    		with main_circ.if_test((creg_0[1],0)) as else_3:
    			main_circ.measure(3, creg_0[1])
    			with main_circ.if_test((creg_0[1],0)) as else_2:
    				main_circ.measure(2, creg_0[0])
    				with main_circ.switch(creg_0[0]) as case_1:
    					with case_1(0):
    						main_circ.append(subcirc2,[0,2,1,3])
    					with case_1(1):
    						main_circ.id(1)
    			with else_2:
    				main_circ.measure(3, creg_0[0])
    				with main_circ.switch(creg_0[0]) as case_1:
    					with case_1(0):
    						main_circ.u(-0.068000,0.082000,param_1, 0)
    						main_circ.u(param_1,param_1,-0.686000, 3)
    						main_circ.id(3)
    					with case_1(1):
    						main_circ.s(1)
    						main_circ.u(param_0,0.892000,0.270000, 0)
    						main_circ.u(param_3,-0.384000,param_0, 3)
    						main_circ.u(param_1,param_0,param_1, 1)
    		with else_3:
    			main_circ.measure(3, creg_0[1])
    			with main_circ.switch(creg_0[1]) as case_2:
    				with case_2(0):
    					main_circ.measure(0, creg_0[0])
    					with main_circ.switch(creg_0[0]) as case_1:
    						with case_1(0):
    							main_circ.append(subcirc2,[1,3,0,2])
    						with case_1(1):
    							main_circ.u(param_3,param_1,param_3, 1)
    							main_circ.id(2)
    				with case_2(1):
    					main_circ.u(0,param_1,param_2, 2)
    					main_circ.measure(1, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)):
    						main_circ.u(param_2,0,-0.260000, 2)
    						main_circ.barrier(2)
    					main_circ.measure(3, creg_0[0])
    					with main_circ.switch(creg_0[0]) as case_1:
    						with case_1(0):
    							main_circ.barrier(3)
    						with case_1(1):
    							main_circ.id(2)
    					main_circ.measure(1, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)) as else_1:
    						main_circ.u(pi/2,param_2,0.045000, 0)
    						main_circ.u(0,0,param_3, 2)
    						main_circ.id(3)
    					with else_1:
    						main_circ.id(3)
    bindings = {param_0: 0.223000, param_1: -0.863000, param_2: 0.780000, param_3: -0.851000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_on_simulator(main_circ, "78")


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
