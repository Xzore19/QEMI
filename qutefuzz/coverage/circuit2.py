
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi


def main():
    
    
    
    def main():
        
        
        
        def main():
            
            subcirc0 = QuantumCircuit(0)
            # Adding qregs 
            qreg_0 = QuantumRegister(4)
            subcirc0.add_register(qreg_0)
            # Adding creg resources 
            subcirc0.s(qreg_0[3])
            subcirc0.s(qreg_0[3])
            subcirc0.rz(-0.495000, qreg_0[3])
            subcirc0.rz(-0.394000, qreg_0[1])
            subcirc0.s(qreg_0[1])
            subcirc0 = subcirc0.to_gate().control(2)
            
            subcirc1 = QuantumCircuit(0)
            # Adding qregs 
            qreg_0 = QuantumRegister(1)
            subcirc1.add_register(qreg_0)
            qreg_1 = QuantumRegister(3)
            subcirc1.add_register(qreg_1)
            # Adding creg resources 
            subcirc1.ry(-0.837000, qreg_1[1])
            subcirc1.cy(qreg_0[0],qreg_1[2])
            subcirc1.ry(-0.556000, qreg_1[2])
            subcirc1.rz(-0.446000, qreg_0[0])
            subcirc1.rz(-0.082000, qreg_1[0])
            
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
            param_2 = Parameter("param_2")
            param_3 = Parameter("param_3")
            
            main_circ.cy(0,2)
            main_circ.ry(-0.399000, 1)
            main_circ.s(2)
            main_circ.append(subcirc1,[0,3,1,2])
            main_circ.cy(2,1)
            main_circ.rz(-0.733000, 0)
            main_circ.cy(3,2)
            main_circ.rz(-0.038000, 0)
            main_circ.s(2)
            main_circ.cy(0,2)
            main_circ.cy(0,1)
            main_circ.s(2)
            main_circ.ry(param_2, 0)
            main_circ.cy(2,0)
            main_circ.cy(1,0)
            main_circ.cy(3,1)
            main_circ.cy(2,1)
            main_circ.cy(3,1)
            main_circ.s(2)
            main_circ.ry(param_3, 2)
            main_circ.s(1)
            main_circ.ry(0.680000, 0)
            main_circ.ry(param_3, 1)
            main_circ.ry(0.151000, 2)
            main_circ.append(subcirc1,[0,1,3,2])
            main_circ.cy(2,1)
            main_circ.ry(-0.948000, 1)
            main_circ.append(subcirc1,[2,1,3,0])
            main_circ.append(subcirc1,[1,0,2,3])
            main_circ.ry(param_3, 3)
            bindings = {param_2: -0.903000, param_3: -0.115000, }
            main_circ = main_circ.assign_parameters(bindings)
            
            print(Path(__file__).name, " results:")
            main_circ.measure_active()
            run_routing_simulation(main_circ, "2")
        
        
        if __name__ == "__main__":
        
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
    
    
    if __name__ == "__main__":
    
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
