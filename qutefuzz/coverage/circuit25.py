
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
    subcirc0.rx(-0.470000, qreg_0[0])
    subcirc0.u(-0.258000,-0.214000,-0.680000, qreg_1[2])
    subcirc0.rx(0.803000, qreg_1[0])
    subcirc0.z(qreg_0[0])
    
    main_circ = QuantumCircuit(1)
    # Adding qregs 
    qreg_0 = QuantumRegister(2)
    main_circ.add_register(qreg_0)
    qreg_2 = QuantumRegister(2)
    main_circ.add_register(qreg_2)
    # Adding creg resources 
    creg_0 = ClassicalRegister(2)
    main_circ.add_register(creg_0)
    # Adding symbols 
    param_0 = Parameter("param_0")
    param_1 = Parameter("param_1")
    param_2 = Parameter("param_2")
    
    main_circ.measure(qreg_2[0], creg_0[0])
    with main_circ.switch(creg_0[0]) as case_1:
    	with case_1(0):
    		main_circ.rx(param_1, qreg_2[0])
    		main_circ.cy(qreg_0[0],0)
    		main_circ.u(-0.661000,param_1,-0.629000, qreg_0[0])
    		main_circ.u(0.153000,param_2,param_2, qreg_2[0])
    	with case_1(1):
    		main_circ.cy(0,qreg_2[0])
    		main_circ.rx(param_0, qreg_0[0])
    		main_circ.z(qreg_2[0])
    		main_circ.u(param_0,0.012000,param_2, qreg_2[0])
    main_circ.measure(0, creg_0[1])
    with main_circ.if_test((creg_0[1],0)):
    	main_circ.z(qreg_0[1])
    	main_circ.cy(qreg_2[0],qreg_0[1])
    	main_circ.cy(qreg_2[0],qreg_2[1])
    main_circ.cy(qreg_2[0],qreg_2[1])
    main_circ.rx(-0.538000, qreg_0[1])
    main_circ.measure(0, creg_0[0])
    with main_circ.if_test((creg_0[0],0)):
    	main_circ.z(0)
    main_circ.measure(qreg_2[0], creg_0[0])
    with main_circ.switch(creg_0[0]) as case_1:
    	with case_1(0):
    		main_circ.rx(param_2, 0)
    		main_circ.cy(qreg_2[0],qreg_0[1])
    		main_circ.z(0)
    		main_circ.cy(qreg_2[1],qreg_2[0])
    	with case_1(1):
    		main_circ.rx(param_1, qreg_0[1])
    		main_circ.u(param_1,param_0,0.241000, qreg_2[0])
    		main_circ.cy(0,qreg_0[0])
    		main_circ.rx(param_2, qreg_0[1])
    main_circ.z(0)
    main_circ.z(qreg_0[0])
    main_circ.measure(qreg_2[0], creg_0[0])
    with main_circ.if_test((creg_0[0],0)):
    	main_circ.rx(-0.965000, qreg_0[1])
    	main_circ.z(0)
    main_circ.measure(qreg_0[1], creg_0[1])
    with main_circ.if_test((creg_0[1],0)):
    	main_circ.z(qreg_2[1])
    main_circ.rx(param_1, qreg_2[0])
    main_circ.measure(qreg_0[0], creg_0[0])
    with main_circ.switch(creg_0[0]) as case_1:
    	with case_1(0):
    		main_circ.rx(-0.703000, qreg_2[0])
    		main_circ.rx(param_0, 0)
    		main_circ.append(subcirc0,[qreg_2[0],qreg_0[1],qreg_0[0],0])
    	with case_1(1):
    		main_circ.cy(0,qreg_2[1])
    		main_circ.cy(qreg_2[1],qreg_0[1])
    		main_circ.cy(0,qreg_0[0])
    		main_circ.cy(qreg_0[1],0)
    main_circ.measure(qreg_0[0], creg_0[0])
    with main_circ.if_test((creg_0[0],0)):
    	main_circ.cy(qreg_0[0],qreg_0[1])
    	main_circ.append(subcirc0,[qreg_0[1],0,qreg_2[0],qreg_2[1]])
    bindings = {param_0: -0.845000, param_1: 0.578000, param_2: 0.510000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_on_simulator(main_circ, "25")


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
