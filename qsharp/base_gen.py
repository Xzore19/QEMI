# 完整更新后的 QSharpGenerator 类，支持内置预设电路封装类型自动判断

import random
import math

class QSharpGenerator:
    def __init__(self, qubit_num=3, num_blocks=3, depth_per_block=6):
        self.qubit_num = qubit_num
        self.num_blocks = num_blocks
        self.depth_per_block = depth_per_block
        self.blocks = []
        self.measure_instructions = []
        self.generated_single_gate_blocks = []
        self.generated_single_gate_block_names = set()
        self.required_imports = set()

        self.qsharp_builtin_blocks = {
            "ApplyQFT": {
                "import": "Std.Canon",
                "call": "ApplyQFT(q);",
                "adjoint": True,
                "controlled": False
            },
            "ApproximatelyPreparePureStateCP": self.make_random_stateprep_block()
        }

    def generate_random_complexpolar_vector(self, num_qubits):
        dim = 2 ** num_qubits
        squares = [random.uniform(0, 1) for _ in range(dim)]
        total = sum(squares)
        normed = [math.sqrt(x / total) for x in squares]
        phases = [random.uniform(0, 2 * math.pi) for _ in range(dim)]
        return [
            f"ComplexPolar({round(r, 6)}, {round(phi, 6)})"
            for r, phi in zip(normed, phases)
        ]

    def make_random_stateprep_block(self):
        vec = self.generate_random_complexpolar_vector(self.qubit_num)
        coeff_str = "[\n        " + ",\n        ".join(vec) + "\n    ]"
        return {
            "import": "Std.StatePreparation",
            "call": (
                "ApproximatelyPreparePureStateCP(\n"
                "    1e-6,\n"
                f"    {coeff_str},\n"
                "    q\n"
                ");"
            ),
            "adjoint": True,
            "controlled": False
        }

    def generate_single_qubit_block(self, idx):
        gates = ["H", "X", "Y", "Z", "S", "T", "I", "Rx", "Ry", "Rz", "R1"]
        instructions = []
        for _ in range(random.randint(2, 4)):
            gate = random.choice(gates)
            if gate in ["Rx", "Ry", "Rz", "R1"]:
                angle = round(random.uniform(0, 2 * math.pi), 6)
                instructions.append(f"    {gate}({angle}, q);")
            else:
                instructions.append(f"    {gate}(q);")
        body = "\n".join(instructions)
        name = f"MySingleBlock{idx}"
        return name, f"    operation {name}(q : Qubit) : Unit is Adj + Ctl {{\n{body}\n    }}"

    def ensure_single_block(self):
        idx = len(self.generated_single_gate_blocks)
        block_name, op_text = self.generate_single_qubit_block(idx)
        if block_name not in self.generated_single_gate_block_names:
            self.generated_single_gate_block_names.add(block_name)
            self.generated_single_gate_blocks.append(op_text)
        return block_name, op_text

    def generate_random_gate_block(self, call_type, idx, target_indices):
        single_no_param = ["H", "X", "Y", "Z", "S", "T", "I"]
        single_with_param = ["Rx", "Ry", "Rz", "R1"]
        two_no_param = ["CNOT", "SWAP"]
        two_with_param = ["Rxx", "Ryy", "Rzz"]
        three_qubit = ["CCNOT"]

        all_gates = single_no_param + single_with_param + two_no_param + two_with_param + three_qubit
        control_safe = set(single_no_param + single_with_param + two_no_param)

        instructions = []
        used_indices = set()
        extra_ops = []

        for _ in range(self.depth_per_block):
            # 20% chance to insert builtin Q# block
            if random.random() < 0.2:
                name, props = random.choice(list(self.qsharp_builtin_blocks.items()))
                if call_type == "controlled" and not props["controlled"]:
                    continue
                if call_type == "adjoint" and not props["adjoint"]:
                    continue

                q_expr = "q"

                call_text = props["call"].replace("{q_expr}", q_expr)
                instructions.append(call_text)
                self.required_imports.add(props["import"])
                used_indices.update(range(len(target_indices)))
                continue

            if random.random() < 0.2:
                block_name, op_text = self.ensure_single_block()
                instructions.append(f"ApplyToEachCA({block_name}, q);")
                used_indices.update(range(len(target_indices)))
                extra_ops.append(op_text)
                continue

            gate_type = random.choice(all_gates)
            if call_type == "controlled" and gate_type not in control_safe:
                continue
            max_index = len(target_indices) - 1
            if gate_type in single_no_param:
                q = random.randint(0, max_index)
                used_indices.add(q)
                instructions.append(f"{gate_type}(q[{q}]);")
            elif gate_type in single_with_param:
                q = random.randint(0, max_index)
                angle = round(random.uniform(0, 2 * math.pi), 6)
                used_indices.add(q)
                instructions.append(f"{gate_type}({angle}, q[{q}]);")
            elif gate_type in two_no_param and len(target_indices) >= 2:
                q1, q2 = random.sample(range(len(target_indices)), 2)
                used_indices.update([q1, q2])
                instructions.append(f"{gate_type}(q[{q1}], q[{q2}]);")
            elif gate_type in two_with_param and len(target_indices) >= 2:
                q1, q2 = random.sample(range(len(target_indices)), 2)
                angle = round(random.uniform(0, 2 * math.pi), 6)
                used_indices.update([q1, q2])
                instructions.append(f"{gate_type}({angle}, q[{q1}], q[{q2}]);")
            elif gate_type in three_qubit and len(target_indices) >= 3:
                q0, q1, q2 = random.sample(range(len(target_indices)), 3)
                used_indices.update([q0, q1, q2])
                instructions.append(f"{gate_type}(q[{q0}], q[{q1}], q[{q2}]);")

        return used_indices, instructions, extra_ops

    def add_measure_all(self):
        self.measure_instructions.clear()
        for i in range(self.qubit_num):
            self.measure_instructions.append(f"let r{i} = M(q[{i}]);")

    def indent(self, lines, level=1, spaces_per_level=4):
        indent_str = " " * (level * spaces_per_level)
        return "\n".join(f"{indent_str}{line}" for line in lines)

    def generate_qsharp_code(self):
        self.blocks.clear()
        self.add_measure_all()
        self.generated_single_gate_blocks = []
        self.generated_single_gate_block_names = set()
        self.required_imports = set()

        call_types = random.choices(["plain", "adjoint", "controlled"], k=self.num_blocks)
        block_ops = []
        test_body = []
        extra_single_blocks = []

        for idx, call_type in enumerate(call_types):
            qualifier = "Adj" if call_type in ["plain", "adjoint"] else "Adj + Ctl"

            if call_type == "controlled":
                available = list(range(self.qubit_num))
                num_ctrl = random.randint(1, self.qubit_num - 1)
                ctrl = sorted(random.sample(available, num_ctrl))
                target = sorted([i for i in available if i not in ctrl])
                if not target:
                    call_type = "plain"
                    target = list(range(self.qubit_num))
                    ctrl = []
            else:
                target = list(range(self.qubit_num))
                ctrl = []

            used_indices, block, extra_ops = self.generate_random_gate_block(call_type, idx, target)
            extra_single_blocks.extend(extra_ops)
            body = self.indent(block, level=2)
            block_ops.append(f"    operation ApplyRandomBlock{idx}(q : Qubit[]) : Unit is {qualifier} {{\n{body}\n    }}")

            if call_type == "plain":
                test_body.append(f"ApplyRandomBlock{idx}(q);")
            elif call_type == "adjoint":
                test_body.append(f"Adjoint ApplyRandomBlock{idx}(q);")
            elif call_type == "controlled":
                ctrl_str = ", ".join([f"q[{i}]" for i in ctrl])
                tgt_str = ", ".join([f"q[{i}]" for i in target])
                test_body.append(f"Controlled ApplyRandomBlock{idx}([{ctrl_str}], [{tgt_str}]);")

        test_body += self.measure_instructions
        test_body.append("ResetAll(q);")
        test_body.append("return [" + ", ".join([f"r{i}" for i in range(self.qubit_num)]) + "];")
        test_body_indented = self.indent(test_body, level=3)

        default_imports = [
            "Std.Intrinsic",
            "Std.Measurement",
            "Std.Math",
            "Std.Canon",
            "Std.Convert",
            "Std.Diagnostics"
        ]
        all_imports = sorted(set(default_imports).union(self.required_imports))
        header = "\n".join(f"    open {lib};" for lib in all_imports)

        test_circuit_op = f"    operation TestCircuit() : Result[] {{\n        use q = Qubit[{self.qubit_num}] {{\n{test_body_indented}\n        }}\n    }}"

        return (
            f"namespace Main {{\n"
            f"{header}\n\n"
            f"{chr(10).join(self.generated_single_gate_blocks)}\n\n"
            f"{chr(10).join(block_ops)}\n\n"
            f"{test_circuit_op}\n}}"
        )

    def save_to_file(self, filename="src/Main.qs"):
        code = self.generate_qsharp_code()
        with open(filename, "w") as f:
            f.write(code)
        print(f"Q# code saved to {filename}")

if __name__ == "__main__":
    g = QSharpGenerator(qubit_num=4, num_blocks=3, depth_per_block=8)
    g.save_to_file()
