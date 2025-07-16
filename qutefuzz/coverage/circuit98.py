
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
    subcirc0.cz(qreg_0[1],qreg_0[3])
    subcirc0.x(qreg_0[3])
    subcirc0.z(qreg_0[0])
    subcirc0.x(qreg_0[3])
    subcirc0.cx(qreg_0[1],qreg_0[3])
    subcirc0.cx(qreg_0[2],qreg_0[1])
    
    subcirc1 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(3)
    subcirc1.add_register(qreg_0)
    qreg_3 = QuantumRegister(1)
    subcirc1.add_register(qreg_3)
    # Adding creg resources 
    subcirc1.x(qreg_0[2])
    subcirc1.z(qreg_3[0])
    subcirc1.z(qreg_0[2])
    subcirc1.x(qreg_0[0])
    subcirc1.cz(qreg_0[0],qreg_0[2])
    subcirc1.cz(qreg_0[2],qreg_3[0])
    subcirc1 = subcirc1.to_gate().control(1)
    
    main_circ = QuantumCircuit(2)
    # Adding qregs 
    qreg_0 = QuantumRegister(1)
    main_circ.add_register(qreg_0)
    qreg_1 = QuantumRegister(2)
    main_circ.add_register(qreg_1)
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
    param_2 = Parameter("param_2")
    
    main_circ.measure(0, creg_0[0])
    with main_circ.if_test((creg_0[0],0)):
    	main_circ.append(subcirc1,[qreg_3[0],qreg_1[1],0,qreg_0[0],qreg_1[0]])
    main_circ.measure(0, creg_0[0])
    with main_circ.switch(creg_0[0]) as case_3:
    	with case_3(0):
    		main_circ.measure(0, creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_2:
    			with case_2(0):
    				main_circ.measure(1, creg_1[0])
    				with main_circ.if_test((creg_1[0],0)) as else_1:
    					main_circ.append(subcirc0,[qreg_1[1],0,qreg_0[0],1])
    				with else_1:
    					main_circ.x(qreg_0[0])
    					main_circ.cz(qreg_1[1],qreg_3[0])
    					main_circ.append(subcirc1,[qreg_1[1],qreg_1[0],0,qreg_3[0],qreg_0[0]])
    			with case_2(1):
    				main_circ.measure(0, creg_1[0])
    				with main_circ.switch(creg_1[0]) as case_1:
    					with case_1(0):
    						main_circ.append(subcirc1,[qreg_3[0],qreg_0[0],qreg_1[0],qreg_1[1],1])
    					with case_1(1):
    						main_circ.append(subcirc0,[qreg_1[0],qreg_3[0],qreg_0[0],1])
    	with case_3(1):
    		main_circ.z(qreg_1[0])
    		main_circ.z(0)
    		main_circ.measure(1, creg_1[0])
    		with main_circ.switch(creg_1[0]) as case_2:
    			with case_2(0):
    				main_circ.measure(qreg_1[0], creg_1[0])
    				with main_circ.if_test((creg_1[0],0)) as else_1:
    					main_circ.z(qreg_0[0])
    					main_circ.append(subcirc0,[qreg_1[0],qreg_3[0],1,qreg_0[0]])
    				with else_1:
    					main_circ.cz(1,qreg_3[0])
    					main_circ.barrier(qreg_1[0])
    			with case_2(1):
    				main_circ.measure(1, creg_0[0])
    				with main_circ.if_test((creg_0[0],0)) as else_1:
    					main_circ.id(qreg_1[0])
    				with else_1:
    					main_circ.id(1)
    				main_circ.measure(qreg_3[0], creg_1[0])
    				with main_circ.if_test((creg_1[0],0)) as else_1:
    					main_circ.id(qreg_1[1])
    				with else_1:
    					main_circ.id(qreg_3[0])
    				main_circ.id(qreg_0[0])
    bindings = {}
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_on_simulator(main_circ, "98")


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
