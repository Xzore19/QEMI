from qutefuzz.qiskit_gen import QiskitGenerator

transpile_detail = {
    "optimization_level": 1,
    "routing_method": 'basic',
    "layout_method": "trivial",
    "scheduling_method": "asap",
    "approximation_degree": 1,
    "basis_gates": None
}

if __name__ == "__main__":
    for i in range(100):
        a = QiskitGenerator(qubit_num = 3, measure_num = 1, gate_num_upper = 5, measure_times = 2000, transplie = None, backend="aer", use_pass= "HoareOptimizer")
        a.run()
