from string import Template
import random
from qiskit_gates_generator import gate_generator
import subprocess
import sys
import numpy as np
from qiskit.circuit.library import XGate
from qiskit.transpiler.passes import *
from qiskit.transpiler import PassManager, generate_preset_pass_manager

opt_passes = {  "Optimize1qGates": Optimize1qGates(), "Optimize1qGatesDecomposition":Optimize1qGatesDecomposition(),
                "Collect1qRuns": Collect1qRuns(), "Collect2qBlocks": Collect2qBlocks(),
                "CollectMultiQBlocks":CollectMultiQBlocks(),"CollectLinearFunctions":CollectLinearFunctions(),
                "CollectCliffords":CollectCliffords(),"ConsolidateBlocks":ConsolidateBlocks(),
                "CXCancellation":CXCancellation(),"InverseCancellation":InverseCancellation([XGate()]),
                "CommutationAnalysis":CommutationAnalysis(),"CommutativeCancellation":CommutativeCancellation(),
                "CommutativeInverseCancellation":CommutativeInverseCancellation(),
                "Optimize1qGatesSimpleCommutation":Optimize1qGatesSimpleCommutation(),
                "RemoveDiagonalGatesBeforeMeasure":RemoveDiagonalGatesBeforeMeasure(),
                "RemoveResetInZeroState":RemoveResetInZeroState(),"RemoveFinalReset":RemoveFinalReset(),
                "HoareOptimizer":HoareOptimizer(),"TemplateOptimization":TemplateOptimization(),
                "ResetAfterMeasureSimplification":ResetAfterMeasureSimplification(), #"EchoRZXWeylDecomposition":EchoRZXWeylDecomposition(),
                "OptimizeCliffords":OptimizeCliffords(),"ElidePermutations":ElidePermutations(),
                "NormalizeRXAngle":NormalizeRXAngle(),"OptimizeAnnotated":OptimizeAnnotated()
            }

class QiskitGenerator:
    def __init__(self, qubit_num, measure_num = 1, gate_num_upper = 5, measure_times = 1024, transplie = None, backend = "aer", use_pass = None):
        self.qnum = qubit_num
        self.code = ""
        self.qreg = "qreg"
        self.creg = "creg"
        self.qc = "qc"
        self.transpile = transplie
        self.use_pass = use_pass
        self.backend = backend
        self.measure_times = measure_times
        self.measure_qubit_num = measure_num
        self.gate_num_upper = gate_num_upper
        self.measure_index = random.sample(range(self.qnum), self.measure_qubit_num)
        self.filename = "temp_test.py"
        self.combine()

    def simulator_option(self):
        code_line = "\n"
        if self.backend == "aer":
            code_line += f"simulator = Aer.get_backend(\"aer_simulator\") \n"
        elif self.backend == "GenericBackendV2":
            # 这个模拟器好像并不支持if_test语句
            code_line += f"simulator = GenericBackendV2(num_qubits={self.qnum}, seed=1234, noise_info=False) \n"
        return code_line

    def pass_option(self):
        code_line = "\n"
        if self.use_pass:
            code_line += f"p = PassManager({self.use_pass}()) \n"
            code_line += f"{self.qc} = p.run({self.qc}) \n"
        return code_line

    def transpile_option(self):
        optimization_level = [0, 1, 2, 3]
        routing_method = ['none', 'stochastic', 'sabre']
        layout_method = ["trivial", "dense", "noise_adaptive"]
        scheduling_method = ["asap", "alap"]
        basis_gates = []

        code_line = "\n"

        if self.transpile:
            optimization_level = self.transpile["optimization_level"]
            routing_method = self.transpile["routing_method"]
            layout_method = self.transpile["layout_method"]
            scheduling_method = self.transpile["scheduling_method"]
            approximation_degree = self.transpile["approximation_degree"]

        else:
            optimization_level = random.choice(optimization_level)
            routing_method = random.choice(routing_method)
            layout_method = random.choice(layout_method)
            scheduling_method = random.choice(scheduling_method)
            approximation_degree = random.choice(np.linspace(0, 1, num=100000))

        code_line += f"compiled_circuit = transpile({self.qc}, backend = simulator, optimization_level = {optimization_level}, routing_method = \"{routing_method}\", layout_method = \"{layout_method}\", approximation_degree = {approximation_degree} ) \n"
        return code_line


    def combine(self):
        self.code += self.write_import()
        self.code += self.basic_set()
        self.code += self.gate_generation(0)
        self.code += self.only_dynamic_if()
        self.code += self.gate_generation(0)
        self.code += self.final_part(show_type="simulator")

    def only_dynamic_if(self):
        result = random.choice(range(pow(2, len(self.measure_index))))
        code_line = ""
        for i in self.measure_index:
            code_line += f"{self.qc}.measure({self.qreg}[{i}], {self.creg}[{i}])\n"
        code_line += f"with {self.qc}.if_test(({self.creg}{self.measure_index}, {result})) as else_1: \n"
        code_line += self.gate_generation(1)
        code_line += f"with else_1: \n"
        code_line += self.gate_generation(1)
        code_line += "\n"
        return code_line


    def write_import(self):
        code_line = ""
        code_line += "from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile \n"
        code_line += "from qiskit_aer import Aer \n"
        code_line += "from qiskit.providers.fake_provider import GenericBackendV2 \n"
        code_line += "from qiskit.providers.fake_provider import GenericBackendV2 \n"
        code_line += "from qiskit.circuit import Parameter, ParameterVector \n"
        code_line += "from qiskit.circuit.library import XGate \n"
        code_line += "from qiskit.transpiler.passes import * \n"
        code_line += "import z3 \n"
        code_line += "from qiskit.transpiler import PassManager, generate_preset_pass_manager \n"
        # code_line += "from helpers.qiskit_helpers import compare_statevectors, run_on_simulator, run_routing_simulation, run_pass_on_simulator \n"
        # code_line += "from pathlib import Path \n"
        code_line += "from math import pi \n"
        code_line += "\n"
        return code_line

    def basic_set(self):
        code_line = ""
        code_line += f"{self.qreg} = QuantumRegister({self.qnum}) \n"
        code_line += f"{self.creg} = ClassicalRegister({self.qnum}) \n"
        code_line += f"{self.qc} = QuantumCircuit({self.qreg}, {self.creg}) \n"
        # q_mindx = ",".join([f"{self.qreg}[{i}]" for i in self.measure_index])
        # c_mindx = ",".join([f"{self.creg}[{i}]" for i in self.measure_index])
        # code_line += f"({q_mindx}) = {self.qreg} \n"
        # code_line += f"({c_mindx}) = {self.creg} \n"
        code_line += "\n"
        return code_line


    def gate_generation(self, indent):
        gate_code = ""
        for i in range(self.gate_num_upper):
            gate_code += "\t"* indent + gate_generator(qubits_num=self.qnum, cir_name=self.qc) + "\n"
        return gate_code

    def final_part(self, show_type):
        code_line = "\n"
        if show_type == "draw":
            circuit_draw = "mpl"
            code_line += "import matplotlib as plt \n"
            code_line += f"{self.qc}.draw(\"{circuit_draw}\") \n"
            code_line += "plt.pyplot.show() \n"
        elif show_type == "simulator":
            code_line += f"{self.qc}.measure({self.qreg}, {self.creg}) \n"
            code_line += self.simulator_option()
            code_line += self.pass_option()
            code_line += self.transpile_option()
            code_line += f"job = simulator.run(compiled_circuit, shots={self.measure_times}) \n"
            code_line += f"result = job.result().get_counts() \n"
            code_line += f"print(\"results:\", result)"
            code_line += "\n"
        return code_line

    def run(self):
        with open(self.filename, "w") as file:
            file.write(self.code)

        subprocess.run([sys.executable, self.filename])


    def check_code(self):
        print(self.code)

if __name__ == "__main__":
    a = QiskitGenerator(5,1)
    a.check_code()