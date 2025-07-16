
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter, ParameterVector
from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator
from pathlib import Path
from math import pi


def main():
    
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
    param_4 = Parameter("param_4")
    
    main_circ.ry(param_4, 1)
    main_circ.y(2)
    main_circ.h(1)
    main_circ.ry(param_1, 3)
    main_circ.y(1)
    main_circ.ry(-0.421000, 1)
    main_circ.ry(-0.310000, 0)
    main_circ.s(3)
    main_circ.y(3)
    main_circ.y(3)
    main_circ.y(1)
    main_circ.ry(param_2, 2)
    main_circ.ry(-0.605000, 1)
    main_circ.h(3)
    main_circ.ry(param_4, 0)
    main_circ.ry(0.170000, 0)
    main_circ.ry(param_4, 1)
    main_circ.ry(0.365000, 3)
    main_circ.y(3)
    main_circ.h(1)
    main_circ.h(1)
    main_circ.h(3)
    main_circ.ry(-0.736000, 1)
    main_circ.h(0)
    main_circ.ry(0.541000, 0)
    main_circ.ry(0.357000, 2)
    main_circ.y(3)
    main_circ.y(0)
    main_circ.ry(param_4, 3)
    main_circ.s(2)
    main_circ.h(0)
    main_circ.ry(param_1, 2)
    main_circ.y(1)
    main_circ.h(3)
    main_circ.y(3)
    main_circ.y(1)
    main_circ.h(2)
    main_circ.ry(param_3, 0)
    main_circ.y(3)
    main_circ.y(1)
    main_circ.s(1)
    main_circ.y(2)
    bindings = {param_1: -0.340000, param_2: -0.028000, param_3: 0.985000, param_4: 0.506000, }
    main_circ = main_circ.assign_parameters(bindings)
    
    print(Path(__file__).name, " results:")
    main_circ.measure_active()
    run_routing_simulation(main_circ, "35")


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
