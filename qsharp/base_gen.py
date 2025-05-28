import os
import random
import math
from qsharp_generator.functions import indent
from qsharp_generator.custom_blocks import (
    generate_random_gate_block,
    make_apply_if_equalle_block,
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
        self.required_imports = set()
        self.builtin_block_names = [
            "ApplyQFT",
            "ApproximatelyPreparePureStateCP",
            "ApplyIfEqualLE",
        ]
        self.single_block_counter = 0

    def generate_qsharp_code(self, namespace_name="Main"):
        from qsharp_generator.functions import ensure_single_block, add_measure_all

        self.measure_instructions = add_measure_all(self.qubit_num)
        self.required_imports = set()
        call_types = random.choices(["plain", "adjoint", "controlled"], k=self.num_blocks)
        block_ops = []
        test_body = []
        extra_single_blocks = []

        start_idx = 0
        if not self.include_deadcode:
            start_idx = 1  # 跳过 idx == 0，避免插入 deadcode

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

            def make_if_block_adapter(available_indices):
                return make_apply_if_equalle_block(
                    available_indices=available_indices,
                    depth=self.depth_per_block,
                    builtin_block_names=self.builtin_block_names,
                    ensure_single_block=lambda: ensure_single_block(
                        self.single_block_counter,
                        self.generated_single_gate_block_names,
                        self.generated_single_gate_blocks
                    ),
                    required_imports=self.required_imports,
                    make_if_block_adapter=make_if_block_adapter,
                )

            if idx == 0 and self.include_deadcode:
                target_indices = target
                target_expr = "q"
                props = make_fixed_apply_if_equalle_block(
                    target_register=target_expr,
                    target_indices=target_indices,
                    depth=self.depth_per_block,
                    builtin_block_names=self.builtin_block_names,
                    ensure_single_block=lambda: ensure_single_block(
                        self.single_block_counter,
                        self.generated_single_gate_block_names,
                        self.generated_single_gate_blocks
                    ),
                    required_imports=self.required_imports,
                    make_if_block_adapter=make_if_block_adapter
                )
                block = (
                    "// --- DEADCODE START ---\n"
                    + props["call"] +
                    "\n// --- DEADCODE END ---"
                )
                self.required_imports.add(props["import"])
                body = indent(block.split("\n"), level=2)
                signature = f"    operation ApplyRandomBlock{idx}(q : Qubit[]) : Unit is Adj + Ctl {{\n{body}\n    }}"
                block_ops.append(signature)
                test_body.append(f"Controlled ApplyRandomBlock{idx}([], q);")  # deadcode 被视为可控模块
                continue

            used_indices, block, extra_ops = generate_random_gate_block(
                call_type=call_type,
                target_indices=target,
                depth=self.depth_per_block,
                builtin_block_names=self.builtin_block_names,
                ensure_single_block=lambda: ensure_single_block(
                    self.single_block_counter,
                    self.generated_single_gate_block_names,
                    self.generated_single_gate_blocks
                ),
                required_imports=self.required_imports,
                make_apply_if_equalle_block=make_if_block_adapter
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
        ]
        all_imports = sorted(set(default_imports).union(self.required_imports))
        header = "\n".join(f"    open {lib};" for lib in all_imports)

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
        # 生成代码（包含 deadcode）使用 namespace Main
        code = self.generate_qsharp_code(namespace_name="Main")

        os.makedirs(os.path.dirname(main_path), exist_ok=True)

        with open(main_path, "w") as f:
            f.write(code)

        # 移除 deadcode 并替换 namespace 为 Main_fuzzing
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