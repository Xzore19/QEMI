from string import Template
import random
from qiskit_gates_generator import gate_generator
import subprocess
import sys

class QiskitGenerator:
    def __init__(self, qubit_num, measure_num = 1, gate_num_upper = 5):
        self.qnum = qubit_num
        self.code = ""
        self.qreg = "qreg"
        self.creg = "creg"
        self.qc = "qc"
        self.measure_qubit_num = measure_num
        self.gate_num_upper = gate_num_upper
        self.measure_index = random.sample(range(self.qnum), self.measure_qubit_num)
        self.filename = "temp_test.py"
        self.combine()
        self.run()

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
        code_line += "from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, Aer, transpile, execute \n"
        code_line += "from qiskit.circuit import Parameter, ParameterVector \n"
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
        code_line = ""
        if show_type == "draw":
            circuit_draw = "mpl"
            code_line += "import matplotlib as plt \n"
            code_line += f"{self.qc}.draw(\"{circuit_draw}\") \n"
            code_line += "plt.pyplot.show() \n"
        elif show_type == "simulator":
            code_line += f"{self.qc}.measure({self.qreg}, {self.creg}) \n"
            code_line += f"simulator = Aer.get_backend(\"aer_simulator\") \n"
            code_line += f"compiled_circuit = transpile({self.qc}, simulator) \n"
            code_line += f"job = execute(compiled_circuit, simulator, shots=1024) \n"
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