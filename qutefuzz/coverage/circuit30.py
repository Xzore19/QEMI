
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
    subcirc0.rx(0.995000, qreg_0[1])
    subcirc0.rz(-0.752000, qreg_0[0])
    subcirc0.u(-0.948000,-0.044000,-0.313000, qreg_0[2])
    subcirc0.s(qreg_0[0])
    subcirc0.s(qreg_0[1])
    
    subcirc1 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(3)
    subcirc1.add_register(qreg_0)
    qreg_3 = QuantumRegister(1)
    subcirc1.add_register(qreg_3)
    # Adding creg resources 
    subcirc1.rz(-0.329000, qreg_0[1])
    subcirc1.s(qreg_0[1])
    subcirc1.u(0.843000,0.140000,-0.745000, qreg_0[0])
    subcirc1.rz(0.820000, qreg_0[0])
    subcirc1.rz(0.033000, qreg_0[1])
    
    subcirc2 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(1)
    subcirc2.add_register(qreg_0)
    qreg_1 = QuantumRegister(3)
    subcirc2.add_register(qreg_1)
    # Adding creg resources 
    subcirc2.u(-0.750000,-0.316000,-0.003000, qreg_1[1])
    subcirc2.u(-0.871000,-0.720000,-0.422000, qreg_0[0])
    subcirc2.s(qreg_1[1])
    subcirc2.s(qreg_1[1])
    subcirc2.u(0.824000,-0.393000,0.315000, qreg_1[1])
    
    subcirc3 = QuantumCircuit(0)
    # Adding qregs 
    qreg_0 = QuantumRegister(4)
    subcirc3.add_register(qreg_0)
    # Adding creg resources 
    subcirc3.s(qreg_0[0])
    subcirc3.rz(-0.987000, qreg_0[2])
    subcirc3.s(qreg_0[1])
    subcirc3.s(qreg_0[1])
    subcirc3.u(-0.307000,-0.832000,-0.305000, qreg_0[2])
    subcirc3 = subcirc3.to_gate().control(2)
    
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
    
    main_circ.measure(0, creg_0[0])
    with main_circ.if_test((creg_0[0],0)) as else_4:
    	main_circ.s(2)
    	main_circ.measure(0, creg_0[1])
    	with main_circ.if_test((creg_0[1],0)):
    		main_circ.measure(3, creg_0[0])
    		with main_circ.switch(creg_0[0]) as case_2:
    			with case_2(0):
    				main_circ.measure(2, creg_0[1])
    				with main_circ.if_test((creg_0[1],0)):
    					main_circ.u(param_0,0.526000,param_2, 0)
    				main_circ.measure(2, creg_0[1])
    				with main_circ.switch(creg_0[1]) as case_1:
    					with case_1(0):
    						main_circ.rz(-0.907000, 3)
    						main_circ.rz(-0.004000, 0)
    						main_circ.append(subcirc1,[0,2,1,3])
    					with case_1(1):
    						main_circ.u(0.213000,param_0,0.370000, 1)
    						main_circ.id(0)
    			with case_2(1):
    				main_circ.append(subcirc1,[0,3,1,2])
    with else_4:
    	main_circ.measure(1, creg_0[1])
    	with main_circ.switch(creg_0[1]) as case_3:
    		with case_3(0):
    			main_circ.measure(1, creg_0[1])
    			with main_circ.switch(creg_0[1]) as case_2:
    				with case_2(0):
    					main_circ.measure(2, creg_0[0])
    					with main_circ.if_test((creg_0[0],0)) as else_1:
    						main_circ.barrier(2)
    					with else_1:
    						main_circ.rz(0.707000, 1)
    						main_circ.u(0.222000,0.604000,-0.787000, 1)
    					main_circ.measure(0, creg_0[1])
    					with main_circ.switch(creg_0[1]) as case_1:
    						with case_1(0):
    							main_circ.append(subcirc1,[2,1,0,3])
    						with case_1(1):
    							main_circ.rx(0.845000, 3)
    							main_circ.u(param_3,param_2,0.631000, 0)
    							main_circ.s(1)
    							main_circ.append(subcirc1,[1,3,2,0])
    				with case_2(1):
    					main_circ.measure(3, creg_0[1])
    					with main_circ.if_test((creg_0[1],0)) as else_1:
    						main_circ.u(param_2,-0.357000,param_3, 2)
    						main_circ.append(subcirc1,[0,1,3,2])
    					with else_1:
    						main_circ.barrier(1)
    		with case_3(1):
    			main_circ.measure(0, creg_0[0])
    			with main_circ.if_test((creg_0[0],0)) as else_2:
    				main_circ.measure(2, creg_0[1])
    				with main_circ.if_test((creg_0[1],0)) as else_1:
    					main_circ.append(subcirc1,[1,0,2,3])
    				with else_1:
    					main_circ.rx(param_1, 1)
    					main_circ.append(subcirc1,[2,3,0,1])
    			with else_2:
    				main_circ.measure(3, creg_0[1])
    				with main_circ.switch(creg_0[1]) as case_1:
    					with case_1(0):
    						main_circ.barrier(0)
    					with case_1(1):
    						main_circ.barrier(3)
    				main_circ.measure(2, creg_0[1])
    				with main_circ.switch(creg_0[1]) as case_1:
    					with case_1(0):
    						main_circ.id(2)
    					with case_1(1):
    						main_circ.id(2)
    				main_circ.id(1)
    bindings = {param_0: -0.106000, param_1: -0.505000, param_2: 0.164000, param_3: 0.347000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_on_simulator(main_circ, "30")


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
