# Re-import after kernel reset
import random
import math
import traceback
from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit import AncillaRegister
from qiskit.circuit.library import *
from numpy import identity
import numpy as np
from qiskit.circuit import Parameter
from qiskit.circuit import ParameterVector

MAX_DYNAMIC_QUBITS = 6

# Fixed, parametric, and dynamic gates
FIXED_GATES = [
    (XGate, 1, []), (HGate, 1, []), (CXGate, 2, []),
    (CCXGate, 3, []), (SwapGate, 2, []), (C3XGate, 4, [])
]

PARAM_GATES = [
    (RZGate, 1, ['theta']), (RXGate, 1, ['theta']),
    (CRXGate, 2, ['theta']),
    (U3Gate, 1, ['theta', 'phi', 'lambda']),
    (CUGate, 2, ['theta', 'phi', 'lambda', 'gamma'])
]

DYNAMIC_GATES = [
    (QFT, 1), (Diagonal, 1), (Permutation, 1), (MCXGate, 2), (MCPhaseGate, 2),
    (TwoLocal, 2), (RealAmplitudes, 2), (EfficientSU2, 2), (NLocal, 2),
    (ZZFeatureMap, 2), (ZFeatureMap, 1), (PauliFeatureMap, 2),
    (StatePreparation, 1), (Initialize, 1), (Isometry, 1),
    (WeightedAdder, 2), (DraperQFTAdder, 2),
    (OR, 2), (AND, 2), (XOR, 2),
]


def random_normalized_state_vector(size):
    vec = np.random.randn(size) + 1j * np.random.randn(size)
    vec /= np.linalg.norm(vec)
    return vec.tolist()


def random_unitary_matrix(size):
    # QR decomposition of random complex matrix → unitary
    z = np.random.randn(size, size) + 1j * np.random.randn(size, size)
    q, _ = np.linalg.qr(z)
    return q


# 工具函数：生成归一化复数向量（用于状态初始化）
def random_normalized_state_vector(dim):
    vec = np.random.randn(dim) + 1j * np.random.randn(dim)
    vec /= np.linalg.norm(vec)
    return vec.tolist()


# 修复后的 generate_dynamic_gate 函数，支持所有复杂门类型和自定义构造表达式
# 使用 parameter_prefix 修复 FeatureMap 门的参数冲突
# 更新 RealAmplitudes 等参数化门，添加 parameter_prefix 以防参数冲突
def generate_dynamic_gate(gate_cls, requested_qubits):
    if gate_cls == QFT:
        gate = gate_cls(requested_qubits)
        gate._custom_expr = f"QFT({requested_qubits})"
        return gate, requested_qubits

    elif gate_cls == Diagonal:
        diag_len = 2 ** requested_qubits
        entries = [np.exp(1j * theta) for theta in np.random.rand(diag_len) * 2 * np.pi]
        gate = Diagonal(entries)
        gate._custom_expr = f"Diagonal(np.array({repr(entries)}))"
        return gate, requested_qubits

    elif gate_cls == Permutation:
        pattern = list(range(requested_qubits))
        np.random.shuffle(pattern)
        gate = Permutation(requested_qubits, pattern=pattern)
        gate._custom_expr = f"Permutation({requested_qubits}, pattern={pattern})"
        return gate, requested_qubits

    elif gate_cls == MCXGate:
        ctrl = requested_qubits - 1
        gate = MCXGate(ctrl)
        gate._custom_expr = f"MCXGate({ctrl})"
        return gate, gate.num_qubits

    elif gate_cls == MCPhaseGate:
        ctrl = requested_qubits - 1
        gate = MCPhaseGate(1.0, num_ctrl_qubits=ctrl)
        gate._custom_expr = f"MCPhaseGate(1.0, num_ctrl_qubits={ctrl})"
        return gate, gate.num_qubits

    elif gate_cls in [TwoLocal, RealAmplitudes, EfficientSU2, NLocal]:
        prefix = f"theta_{uuid.uuid4().hex[:6]}"
        gate = gate_cls(requested_qubits, reps=1, parameter_prefix=prefix)
        gate._custom_expr = f"{gate_cls.__name__}({requested_qubits}, reps=1, parameter_prefix='{prefix}')"
        return gate, gate.num_qubits

    elif gate_cls in [ZZFeatureMap, ZFeatureMap, PauliFeatureMap]:
        prefix = f"x_{uuid.uuid4().hex[:6]}"
        gate = gate_cls(feature_dimension=requested_qubits, reps=1, parameter_prefix=prefix)
        gate._custom_expr = f"{gate_cls.__name__}({requested_qubits}, reps=1, parameter_prefix='{prefix}')"
        return gate, requested_qubits

    elif gate_cls == StatePreparation:
        vec = random_normalized_state_vector(2 ** requested_qubits)
        gate = StatePreparation(vec)
        gate._custom_expr = f"StatePreparation({repr(vec)})"
        return gate, requested_qubits

    elif gate_cls == Initialize:
        vec = random_normalized_state_vector(2 ** requested_qubits)
        gate = Initialize(vec)
        gate._custom_expr = f"Initialize({repr(vec)})"
        return gate, requested_qubits

    elif gate_cls == Isometry:
        dim = 2 ** requested_qubits
        matrix = np.eye(dim)
        gate = Isometry(matrix, 0, 0)
        gate._custom_expr = f"Isometry(np.array({repr(matrix.tolist())}), 0, 0)"
        return gate, requested_qubits

    elif gate_cls == WeightedAdder:
        weights = [np.random.randint(1, 4) for _ in range(requested_qubits)]
        gate = WeightedAdder(requested_qubits, weights=weights)
        gate._custom_expr = f"WeightedAdder({requested_qubits}, weights={weights})"
        return gate, gate.num_qubits

    elif gate_cls == DraperQFTAdder:
        gate = DraperQFTAdder(requested_qubits)
        gate._custom_expr = f"DraperQFTAdder({requested_qubits})"
        return gate, gate.num_qubits

    elif gate_cls in [OR, AND, XOR]:
        num_variable_qubits = requested_qubits - 1
        gate = gate_cls(num_variable_qubits)
        gate._custom_expr = f"{gate_cls.__name__}({num_variable_qubits})"
        return gate, gate.num_qubits

    else:
        raise ValueError(f"Unsupported dynamic gate: {gate_cls.__name__}")


def retry_with_same_category(category, max_qubits):
    try:
        if category == 'fixed':
            gate_cls, num_qubits, _ = random.choice(FIXED_GATES)
            return gate_cls(), num_qubits
        elif category == 'param':
            gate_cls, num_qubits, param_names = random.choice(PARAM_GATES)
            params = [round(random.uniform(0, 2 * math.pi), 3) for _ in param_names]
            return gate_cls(*params), num_qubits
        elif category == 'dynamic':
            gate_cls, min_qubits = random.choice(DYNAMIC_GATES)
            allowed_qubits = min(MAX_DYNAMIC_QUBITS, max_qubits)
            requested_qubits = random.randint(min_qubits, allowed_qubits)
            return generate_dynamic_gate(gate_cls, requested_qubits)
    except Exception as e:
        return None, f"# Retry failed: {e}"


def generate_random_gate_and_qubits(max_qubits=6):
    category = random.choice(['fixed', 'param', 'dynamic'])
    return retry_with_same_category(category, max_qubits)


def gate_to_code_expr(gate):
    if hasattr(gate, "_custom_expr"):
        return gate._custom_expr

    cls_name = gate.__class__.__name__

    # 修复 Singleton 情况
    singleton_aliases = {
        '_SingletonCXGate': 'CXGate',
        '_SingletonCCXGate': 'CCXGate',
        '_SingletonXGate': 'XGate',
        '_SingletonHGate': 'HGate',
        '_SingletonSwapGate': 'SwapGate',
        '_SingletonC3XGate': 'C3XGate',
    }
    if cls_name in singleton_aliases:
        return f"{singleton_aliases[cls_name]}()"

    # 带参数
    if hasattr(gate, 'params') and gate.params:
        args = ', '.join(repr(p) for p in gate.params)
        return f"{cls_name}({args})"

    # 默认情况
    if hasattr(gate, 'num_qubits'):
        return f"{cls_name}({gate.num_qubits})"

    return f"{cls_name}()"


# Safe qubit label formatter
def qubit_to_label(qc: QuantumCircuit, qubit) -> str:
    for reg in qc.qregs + qc.ancillas:
        if qubit in reg:
            return f"{reg.name}[{reg.index(qubit)}]"
    return "unknown"


import copy, uuid


def finalize_gate_binding(gate):
    """为参数化 gate 绑定随机参数值，避免 AerSimulator 报错"""
    if hasattr(gate, "is_parameterized") and gate.is_parameterized():
        rand_vals = np.random.uniform(0, 2 * np.pi, gate.num_parameters)
        gate = gate.assign_parameters(rand_vals)
    return gate


# 最终版 generate_random_append_statement，支持自动 gate deepcopy 以避免参数冲突
def generate_random_append_statement(max_qubits=6, qc_var='qc', qr_var='q', anc_var=None):
    gate_info = generate_random_gate_and_qubits(max_qubits)
    if gate_info[0] is None:
        return None, gate_info[1]

    gate, num_qubits = gate_info
    gate = finalize_gate_binding(copy.deepcopy(gate))  # 确保绑定参数并隔离副作用

    qr = QuantumRegister(max_qubits, qr_var)
    qc = QuantumCircuit(qr)
    code_lines = []

    if anc_var is None:
        anc_var = f"aux_{uuid.uuid4().hex[:6]}"

    if num_qubits > len(qc.qubits):
        ancilla_count = num_qubits - len(qc.qubits)
        ar = AncillaRegister(ancilla_count, anc_var)
        qc.add_register(ar)
        code_lines.append(f"{anc_var} = AncillaRegister({ancilla_count}, '{anc_var}')")
        code_lines.append(f"{qc_var}.add_register({anc_var})")

    try:
        selected = random.sample(qc.qubits, num_qubits)
        gate_expr = gate_to_code_expr(gate)
        qubit_expr = [qubit_to_label(qc, q) for q in selected]
        qubit_list_expr = "[" + ", ".join(qubit_expr) + "]"
        code_lines.append(f"{qc_var}.append({gate_expr}, {qubit_list_expr})")
        qc.append(gate, selected)
        return qc, "\n".join(code_lines)
    except Exception as e:
        return None, f"# Append failed: {e}"


# ------------------------------
# 主测试函数（写入txt）
# ------------------------------
def run_stress_test_with_log(iterations=100,
                             error_log_file="append_generation_errors.txt",
                             success_log_file="append_success_snippets.txt",
                             success_limit=1000):
    error_log = []
    success_log = []
    success_count = 0

    for i in range(iterations):
        try:
            qc, code = generate_random_append_statement(6)
            if qc is None:
                error_log.append(code)
            else:
                success_count += 1
                if len(success_log) < success_limit:
                    success_log.append(code)
        except Exception as e:
            tb = traceback.format_exc()
            error_log.append(f"[Exception] {str(e)}\n{tb}")

    # 写入失败日志
    with open(error_log_file, "w", encoding="utf-8") as f:
        f.write(f"✅ Success: {success_count}\n")
        f.write(f"❌ Failed: {len(error_log)}\n\n")
        for err in error_log:
            f.write(err + "\n")

    # 写入成功代码片段
    with open(success_log_file, "w", encoding="utf-8") as f:
        for block in success_log:
            f.write(block + "\n\n")

    print(f"测试完成。成功：{success_count}，失败：{len(error_log)}")
    print(f"错误日志已保存至：{error_log_file}")
    print(f"成功语句（最多 {success_limit} 条）已保存至：{success_log_file}")

    framework_header = """from qiskit import QuantumCircuit, QuantumRegister, AncillaRegister
from qiskit.circuit.library import *
import numpy as np

def build_circuit():
    q = QuantumRegister(6, 'q')
    qc = QuantumCircuit(q)
"""

    framework_footer = """
    qc.measure_all()
    from qiskit.circuit import Parameter
    qc = qc.assign_parameters({p: np.random.uniform(0, 2 * np.pi) for p in qc.parameters})
    qc = qc.decompose(reps=10)
    return qc

if __name__ == "__main__":
    from qiskit_aer import Aer
    circuit = build_circuit()
    backend = Aer.get_backend("aer_simulator")
    job = backend.run(circuit, shots=1024)
    result = job.result()
    print(result.get_counts())
"""

    with open("generated_script.py", "w", encoding="utf-8") as f:
        f.write(framework_header)
        for block in success_log:
            for line in block.strip().splitlines():
                f.write("    " + line + "\n")
        f.write(framework_footer)


# ✅ 调用入口
if __name__ == "__main__":

    qc, code = generate_random_append_statement(max_qubits=5, qc_var="qc", qr_var="qreg")
    gate_code = "\t" * 1 + code + "\n"
    print(gate_code)