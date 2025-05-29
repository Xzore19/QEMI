import os
import random
import math
from qsharp_generator.functions import indent
from qsharp_generator.custom_blocks import (
    generate_random_gate_block,
)
from qsharp_generator.deadcode import make_fixed_apply_if_equalle_block

class QSharpGenerator:
    def __init__(self, qubit_num=3, num_blocks=3, depth_per_block=6, include_deadcode=True):
        self.qubit_num = qubit_num
        self.num_blocks = num_blocks
        self.depth_per_block = depth_per_block
        self.include_deadcode = include_deadcode
        self.measure_instructions = []
        self.generated_single_gate_blocks = []
        self.generated_single_gate_block_names = set()
        self.single_block_counter = 0

    def register_single_qubit_block(self) -> str:
        from qsharp_generator.functions import generate_single_qubit_block

        while True:
            name, text = generate_single_qubit_block()
            if name not in self.generated_single_gate_block_names:
                self.generated_single_gate_block_names.add(name)
                self.generated_single_gate_blocks.append(text)
                return name

    def generate_qsharp_code(self, namespace_name="Main"):
        from qsharp_generator.functions import add_measure_all

        self.measure_instructions = add_measure_all(self.qubit_num)
        call_types = random.choices(["plain", "adjoint", "controlled"], k=self.num_blocks)
        block_ops = []
        test_body = []
        extra_single_blocks = []

        start_idx = 0
        if not self.include_deadcode:
            start_idx = 1

        for idx in range(start_idx, self.num_blocks):
            call_type = call_types[idx]

            qualifier = {
                "plain": "",
                "adjoint": "is Adj",
                "controlled": "is Adj + Ctl",
            }.get(call_type, "is Adj + Ctl")

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

            if idx == 0 and self.include_deadcode:
                target_indices = target
                target_expr = "q"
                props = make_fixed_apply_if_equalle_block(
                    target_register=target_expr,
                    target_indices=target_indices,
                    depth=self.depth_per_block,
                    register_block=lambda: self.register_single_qubit_block(),
                )
                block = props["call"]
                body = indent(block.split("\n"), level=2)
            else:
                used_indices, block, extra_ops = generate_random_gate_block(
                    call_type=call_type,
                    target_indices=target,
                    depth=self.depth_per_block,
                    register_block=lambda: self.register_single_qubit_block(),
                )
                extra_single_blocks.extend(extra_ops)
                body = indent(block, level=2)

            signature = f"    operation ApplyRandomBlock{idx}(q : Qubit[]) : Unit"
            if qualifier:
                signature += f" {qualifier}"
            signature += " {\n" + body + "\n    }"
            block_ops.append(signature)

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
        test_body_indented = indent(test_body, level=3)

        default_imports = [
            "Std.Intrinsic",
            "Std.Measurement",
            "Std.Math",
            "Std.Canon",
            "Std.Convert",
            "Std.Diagnostics",
            "Std.Arithmetic",
            "Std.StatePreparation",
        ]
        all_imports = sorted(set(default_imports))
        header = "\n" + "\n".join(f"    open {lib};" for lib in all_imports)

        test_circuit_op = (
            f"    operation TestCircuit() : Result[] {{\n"
            f"        use q = Qubit[{self.qubit_num}] {{\n"
            f"{test_body_indented}\n"
            f"        }}\n"
            f"    }}\n"
        )
        return (
            f"namespace {namespace_name} {{\n"
            f"{header}\n\n"
            f"{chr(10).join(self.generated_single_gate_blocks)}\n\n"
            f"{chr(10).join(block_ops)}\n\n"
            f"{test_circuit_op}"
            f"}}"
        )

    def save_to_file(self, filename="src/Main.qs"):
        code = self.generate_qsharp_code()
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write(code)
        print(f"Q# code saved to {filename}")

    def save_dual_versions(self, main_path="src/Main.qs", fuzzing_path="src/Fuzzing_Main.qs"):
        code = self.generate_qsharp_code(namespace_name="Main")
        os.makedirs(os.path.dirname(main_path), exist_ok=True)
        with open(main_path, "w") as f:
            f.write(code)

        fuzzing_code_lines = []
        inside_deadcode = False
        for line in code.splitlines():
            if "// --- DEADCODE START ---" in line:
                inside_deadcode = True
                continue
            if "// --- DEADCODE END ---" in line:
                inside_deadcode = False
                continue
            if not inside_deadcode:
                if line.strip().startswith("namespace Main"):
                    line = line.replace("namespace Main", "namespace Main_fuzzing")
                fuzzing_code_lines.append(line)

        with open(fuzzing_path, "w") as f:
            f.write("\n".join(fuzzing_code_lines))

        print(f"Q# main saved to {main_path}")
        print(f"Q# fuzzing version (no deadcode) saved to {fuzzing_path}")

if __name__ == "__main__":
    g = QSharpGenerator(qubit_num=12, num_blocks=3, depth_per_block=8)
    g.save_dual_versions()