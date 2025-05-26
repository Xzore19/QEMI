class QSharpGenerator:
    def __init__(self, qubit_num=2):
        self.qubit_num = qubit_num
        self.gate_instructions = []
        self.measure_instructions = []

    def add_h(self, qubit):
        self.gate_instructions.append(f"H(q[{qubit}]);")

    def add_cnot(self, control, target):
        self.gate_instructions.append(f"CNOT(q[{control}], q[{target}]);")

    def add_measure(self, qubit, result_name):
        self.measure_instructions.append(f"let {result_name} = M(q[{qubit}]);")

    def generate_qsharp_code(self):
        def indent(lines, level=1, spaces_per_level=4):
            indent_str = " " * (level * spaces_per_level)
            return "\n".join(f"{indent_str}{line}" for line in lines)

        body_lines = self.gate_instructions + self.measure_instructions
        result_array = ", ".join([f"{{{r.split()[1]}}}" for r in self.measure_instructions])
        body_lines.append(f'Message($"Result: [{result_array}]");')
        body_lines.append("ResetAll(q);")

        body = indent(body_lines, level=3)

        return f"""namespace QuantumFuzz {{
        open Microsoft.Quantum.Intrinsic;
        open Microsoft.Quantum.Measurement;

        @EntryPoint()
        operation RunCircuit() : Unit {{
            use q = Qubit[{self.qubit_num}] {{
    {body}
            }}
        }}
    }}"""


    def save_to_file(self, filename="QuantumFuzzApp/Program.qs"):
        code = self.generate_qsharp_code()
        with open(filename, "w") as f:
            f.write(code)
        print(f"Q# code saved to {filename}")

if __name__ == "__main__":
    g = QSharpGenerator(qubit_num=2)
    g.add_h(0)
    g.add_cnot(0, 1)
    g.add_measure(0, "r0")
    g.add_measure(1, "r1")
    g.save_to_file()