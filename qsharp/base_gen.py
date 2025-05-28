import os
import random
import math
from qsharp_generator.functions import indent
from qsharp_generator.custom_blocks import (
    generate_single_qubit_block,
    generate_random_gate_block,
    make_apply_if_equalle_block,
)

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
                "controlled": False,
            }
        }
        self.builtin_block_names = [
            "ApplyQFT",
            "ApproximatelyPreparePureStateCP",
            "ApplyIfEqualLE",
        ]
        self.adj_ctl_block_counter = 0
        self.single_block_counter = 0

    def ensure_single_block(self):
        while True:
            idx = self.single_block_counter
            self.single_block_counter += 1
            block_name, op_text = generate_single_qubit_block(idx)
            if block_name not in self.generated_single_gate_block_names:
                self.generated_single_gate_block_names.add(block_name)
                self.generated_single_gate_blocks.append(op_text)
                return block_name, op_text

    def add_measure_all(self):
        self.measure_instructions.clear()
        for i in range(self.qubit_num):
            self.measure_instructions.append(f"let r{i} = M(q[{i}]);")

    def generate_qsharp_code(self):
        self.blocks.clear()
        self.add_measure_all()
        self.required_imports = set()
        call_types = random.choices(["plain", "adjoint", "controlled"], k=self.num_blocks)
        block_ops = []
        test_body = []
        extra_single_blocks = []

        for idx, call_type in enumerate(call_types):
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

            # 初始化包装器为 None
            make_if_block_adapter = None

            # 用闭包构造真正带递归能力的 adapter
            def make_if_block_adapter_closure():
                return lambda available_indices: make_apply_if_equalle_block(
                    available_indices=available_indices,
                    depth=self.depth_per_block,
                    builtin_block_names=self.builtin_block_names,
                    ensure_single_block=self.ensure_single_block,
                    required_imports=self.required_imports,
                    make_if_block_adapter=make_if_block_adapter  # 使用闭包外部变量
                )

            # 赋值闭包（可递归）
            make_if_block_adapter = make_if_block_adapter_closure()

            make_if_block_adapter = lambda available_indices: make_apply_if_equalle_block(
                available_indices=available_indices,
                depth=self.depth_per_block,
                builtin_block_names=self.builtin_block_names,
                ensure_single_block=self.ensure_single_block,
                required_imports=self.required_imports,
                make_if_block_adapter=make_if_block_adapter,
            )

            # ✅ 使用适配器调用
            used_indices, block, extra_ops = generate_random_gate_block(
                call_type=call_type,
                target_indices=target,
                depth=self.depth_per_block,
                builtin_block_names=self.builtin_block_names,
                ensure_single_block=self.ensure_single_block,
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
            f"    }}\n"  # ✅ 注意这里最后补上换行
        )
        return (
            f"namespace Main {{\n"
            f"{header}\n\n"
            f"{chr(10).join(self.generated_single_gate_blocks)}\n\n"
            f"{chr(10).join(block_ops)}\n\n"
            f"{test_circuit_op}"  # ✅ 不要额外拼接 }}，让 test_circuit_op 自带 }}
            f"}}"
        )

    def save_to_file(self, filename="src/Main.qs"):
        code = self.generate_qsharp_code()
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write(code)
        print(f"Q# code saved to {filename}")

if __name__ == "__main__":
    g = QSharpGenerator(qubit_num=12, num_blocks=3, depth_per_block=8)
    g.save_to_file()
