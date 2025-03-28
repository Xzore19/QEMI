import random
from math import pi
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit_aer import Aer
from qiskit import transpile
import itertools

################################################################################
# 平衡函数 Oracle 构造方法（默认随机选择 dot_product 或 majority）
def balanced_oracle_dot_product(num_qubits, cir_name, qreg_name, dj_qubit_indices, aux_index):
    lines = [f"# === Oracle 主体部分（平衡函数：dot_product） ==="]
    active_bits = random.sample(dj_qubit_indices, k=random.randint(1, len(dj_qubit_indices)))
    for idx in active_bits:
        lines.append(f"{cir_name}.cx({qreg_name}[{idx}], {qreg_name}[{aux_index}])")
    return lines

def balanced_oracle_majority(num_qubits, cir_name, qreg_name, dj_qubit_indices, aux_index):
    lines = [f"# === Oracle 主体部分（平衡函数：majority） ==="]
    # 注意：确保 dj_qubit_indices 数量足够
    subset = random.sample(dj_qubit_indices, k=3)
    lines.append(f"{cir_name}.ccx({qreg_name}[{subset[0]}], {qreg_name}[{subset[1]}], {qreg_name}[{aux_index}])")
    lines.append(f"{cir_name}.cx({qreg_name}[{subset[2]}], {qreg_name}[{aux_index}])")
    return lines

# 预留后续 algebraic 构造接口
def balanced_oracle_algebraic(num_qubits, cir_name, qreg_name, dj_qubit_indices, aux_index):
    """
    生成基于 ANF 的 oracle，形式为 f(x)= ⊕_{i in L} x_i ⊕ (x_j & x_k)
    其中 L 是从 dj_qubit_indices 中随机选取的奇数个比特，x_j 和 x_k 为随机选取的两个比特。
    为确保生成的 f 为平衡函数（在 DJ 区上输入取值均匀分布），
    我们对所有 2^n 个输入进行验证（n 为 DJ 区比特数）。
    如果在 max_attempts 次尝试内没有找到满足条件的组合，则退化为仅使用一个线性项。
    """
    import random
    max_attempts = 100
    n = len(dj_qubit_indices)
    # 为了验证，先对 dj_qubit_indices 做排序，确保各个比特的赋值顺序固定
    ordered = sorted(dj_qubit_indices)
    
    for attempt in range(max_attempts):
        # 随机选择一个非空子集作为线性部分，并保证个数为奇数
        k = random.randint(1, n)
        candidate_linear = random.sample(ordered, k=k)
        if len(candidate_linear) % 2 == 0:
            candidate_linear.pop()  # 移除最后一个以保证奇数个

        # 随机选取一个二次项（保证两个比特不同）
        candidate_pair = random.sample(ordered, 2)
        
        # 检查该 ANF 构成的函数是否平衡
        # f(x)= (⊕_{q in candidate_linear} x_q) ⊕ (x_{candidate_pair[0]} & x_{candidate_pair[1]})
        total = 0
        for x in range(2**n):
            # 为 ordered 中的每个比特分配值：最低位对应 ordered[0]，依次上升
            bits = {}
            for i, q in enumerate(ordered):
                bits[q] = (x >> i) & 1
            linear_val = 0
            for q in candidate_linear:
                linear_val ^= bits[q]
            quad_val = bits[candidate_pair[0]] & bits[candidate_pair[1]]
            f_val = linear_val ^ quad_val
            # 累加 (-1)^f(x)
            total += (-1)**f_val
        
        # 对于平衡函数，理论上应有 total == 0
        if total == 0:
            lines = ["# === Oracle 主体部分（平衡函数：algebraic） ==="]
            for q in candidate_linear:
                lines.append(f"{cir_name}.cx({qreg_name}[{q}], {qreg_name}[{aux_index}])")
            lines.append(f"{cir_name}.ccx({qreg_name}[{candidate_pair[0]}], {qreg_name}[{candidate_pair[1]}], {qreg_name}[{aux_index}])")
            return lines

    # 若多次尝试未获得平衡函数，则退化为仅使用线性项（非零线性函数必然平衡）
    fallback = random.choice(ordered)
    lines = ["# === Oracle 主体部分（algebraic fallback，仅线性部分） ==="]
    lines.append(f"{cir_name}.cx({qreg_name}[{fallback}], {qreg_name}[{aux_index}])")
    return lines

def balanced_oracle_algebraic_complex(num_qubits, cir_name, qreg_name, dj_qubit_indices, aux_index, max_degree=3):
    """
    生成基于随机 ANF 的 oracle，其形式为：
       f(x) = ⊕_{term in candidate} (∏_{q in term} x_q)
    candidate 中每个 term 是一个单项式，term 为 () 表示常数项 1。
    
    max_degree 决定了允许的最高项次（例如 3 表示可以包含三次项）。
    
    该函数随机挑选候选项，并在所有 2^n 个输入上验证平衡性（1 的个数是否正好为 2^(n-1)）。
    验证通过后，生成对应量子门代码：
      - 空项 () 用 X 门作用于辅助比特；
      - 1 次项用 CX 门；
      - 多比特项用 mcx 门。
    """
    n = len(dj_qubit_indices)
    # 枚举所有可能的单项式：度从 0 到 max_degree（包括常数项）
    all_monomials = []
    for r in range(0, max_degree + 1):
        for combo in itertools.combinations(dj_qubit_indices, r):
            all_monomials.append(combo)
    
    max_attempts = 50
    p = 0.3  # 每个单项式被选中的概率
    candidate = None
    sorted_bits = sorted(dj_qubit_indices)
    
    for attempt in range(max_attempts):
        candidate_terms = []
        for monomial in all_monomials:
            if random.random() < p:
                candidate_terms.append(monomial)
        # 如果候选项为空或只有一个常数项，则重试
        if not candidate_terms or candidate_terms == [()]:
            continue
        
        # 检查 f(x) 在所有 2^n 个输入下是否平衡
        count_ones = 0
        for x in range(2**n):
            # 为确保顺序一致，按照 sorted_bits 分配比特值
            bits = {}
            for i, q in enumerate(sorted_bits):
                bits[q] = (x >> i) & 1
            f_val = 0
            for term in candidate_terms:
                if term == ():
                    term_val = 1  # 常数项
                else:
                    term_val = 1
                    for q in term:
                        term_val &= bits[q]
                f_val ^= term_val
            if f_val == 1:
                count_ones += 1
        if count_ones == 2**(n-1):
            candidate = candidate_terms
            break

    # 若多次尝试未生成平衡函数，则退化为使用全比特奇偶性（线性函数）
    if candidate is None:
        candidate = [tuple(sorted_bits)]
    
    # 根据 candidate 中的各项生成量子门操作代码
    lines = ["# === Oracle 主体部分（平衡函数：algebraic more complex） ==="]
    for term in candidate:
        if term == ():
            # 常数项，用 X 门作用于辅助比特
            lines.append(f"{cir_name}.x({qreg_name}[{aux_index}])")
        elif len(term) == 1:
            # 线性项，用 CX 门
            lines.append(f"{cir_name}.cx({qreg_name}[{term[0]}], {qreg_name}[{aux_index}])")
        else:
            # 多比特项，用 mcx 门实现（1 个控制比特时其实也就是 CX，但这里 term 长度至少为 2）
            controls_str = ", ".join(f"{qreg_name}[{q}]" for q in term)
            lines.append(f"{cir_name}.mcx([{controls_str}], {qreg_name}[{aux_index}])")
    return lines

def generate_balanced_oracle_code(num_qubits, cir_name="qc", qreg_name="dj_qreg", dj_qubit_indices=None, aux_index=None, method=None):
    if dj_qubit_indices is None or aux_index is None:
        raise ValueError("dj_qubit_indices and aux_index must be provided")

    methods = {
        # "dot_product": balanced_oracle_dot_product,
        # "majority": balanced_oracle_majority,
        "algebraic": balanced_oracle_algebraic_complex
    }

    if method is None:
        method = random.choice(list(methods.keys()))

    if method not in methods:
        raise ValueError(f"Unsupported balanced oracle method: {method}")

    return methods[method](num_qubits, cir_name, qreg_name, dj_qubit_indices, aux_index)

################################################################################
# 增强逻辑 Oracle 生成器（严格隔离 DJ 区）
def generate_enhanced_oracle_code(
    num_qubits,
    cir_name="qc",
    qreg_name="dj_qreg",
    dj_qubit_indices=None,
    enhanced_qubit_indices=None,
    aux_index=None,
    num_extra_gates=20
):
    if dj_qubit_indices is None or aux_index is None:
        raise ValueError("dj_qubit_indices and aux_index must be provided")
    if enhanced_qubit_indices is None:
        raise ValueError("enhanced_qubit_indices must be provided")

    # 可用的特殊角度值（float 极值、数学常数等）
    special_angles = [
        0.0,
        pi, -pi,                   # pi, -pi
        pi/2, -pi/2,               # pi/2, -pi/2
        1.0, -1.0,
        1.4142135623730951, -1.4142135623730951,  # sqrt(2)
        1.7976931348623157e+308, -1.7976931348623157e+308,  # float max
        2.2250738585072014e-308, -2.2250738585072014e-308      # float min positive
    ]

    def get_special_theta():
        return random.choice(special_angles)

    # 修正处：直接使用传入的 enhanced_qubit_indices（排除 aux_index）
    safe_indices = list(set(enhanced_qubit_indices) - {aux_index})
    if not safe_indices or len(safe_indices) < 2:
        return ["# ⚠️ 无可用增强 qubit，跳过增强 oracle"]

    lines = ["# === Oracle 增强部分（不影响 DJ 区） ==="]
    for _ in range(num_extra_gates):
        gate = random.choice(["cx", "crx", "crz", "iswap", "rz", "h"])

        if gate == "cx":
            ctrl, tgt = random.sample(safe_indices, 2)
            lines.append(f"{cir_name}.cx({qreg_name}[{ctrl}], {qreg_name}[{tgt}])")
        elif gate == "crx":
            theta = get_special_theta()
            ctrl, tgt = random.sample(safe_indices, 2)
            lines.append(f"{cir_name}.crx({theta}, {qreg_name}[{ctrl}], {qreg_name}[{tgt}])")
        elif gate == "crz":
            theta = get_special_theta()
            ctrl, tgt = random.sample(safe_indices, 2)
            lines.append(f"{cir_name}.crz({theta}, {qreg_name}[{ctrl}], {qreg_name}[{tgt}])")
        elif gate == "iswap":
            q1, q2 = random.sample(safe_indices, 2)
            lines.append(f"{cir_name}.iswap({qreg_name}[{q1}], {qreg_name}[{q2}])")
        elif gate == "rz":
            tgt = random.choice(safe_indices)
            theta = get_special_theta()
            lines.append(f"{cir_name}.rz({theta}, {qreg_name}[{tgt}])")
        elif gate == "h":
            tgt = random.choice(safe_indices)
            lines.append(f"{cir_name}.h({qreg_name}[{tgt}])")

    return lines

################################################################################
# 组合 Oracle
def generate_combined_oracle(num_qubits, cir_name="qc", qreg_name="dj_qreg", dj_qubit_indices=None, aux_index=None, method=None):
    if dj_qubit_indices is None or aux_index is None:
        raise ValueError("dj_qubit_indices and aux_index must be provided")

    # 先生成平衡部分 oracle
    oracle = generate_balanced_oracle_code(
        num_qubits=num_qubits,
        cir_name=cir_name,
        qreg_name=qreg_name,
        dj_qubit_indices=dj_qubit_indices,
        aux_index=aux_index,
        method=method
    )

    # 计算可用于增强逻辑的 qubit（注意：dj 区域之外的）
    enhanced_indices = list(set(range(num_qubits)) - set(dj_qubit_indices))
    if enhanced_indices:
        oracle += generate_enhanced_oracle_code(
            num_qubits=num_qubits + 1,  # 因为 quantum register 包含辅助比特
            cir_name=cir_name,
            qreg_name=qreg_name,
            dj_qubit_indices=dj_qubit_indices,
            enhanced_qubit_indices=enhanced_indices,
            aux_index=aux_index
        )
    else:
        oracle.append(f"# ⚠️ 无可用增强目标 qubit（num_qubits={num_qubits}），增强逻辑被跳过")

    return oracle

################################################################################
# 生成 DJ 算法子电路（可复用）
def generate_dj_subcircuit(num_qubits=8, dj_bits=4, method=None):
    aux_index = num_qubits
    total_qubits = num_qubits + 1
    dj_qubit_indices = list(range(dj_bits))

    qreg = QuantumRegister(total_qubits, name="dj_qreg")
    creg = ClassicalRegister(dj_bits, name="dj_creg")
    qc = QuantumCircuit(qreg, creg, name="dj_subcircuit")

    qc.x(qreg[aux_index])  # 将辅助比特初始化为 |1⟩
    qc.h(qreg)  # 所有量子比特 Hadamard

    # 注意：此处传入的 qreg_name 与电路中变量名对应
    oracle_lines = generate_combined_oracle(
        num_qubits=num_qubits,
        cir_name="qc",
        qreg_name="qreg",
        dj_qubit_indices=dj_qubit_indices,
        aux_index=aux_index,
        method=method
    )

    for line in oracle_lines:
        if line.startswith("#"):
            continue
        # 执行生成的 oracle 代码（此处假设生成的代码与当前变量名一致）
        exec(line)

    qc.h([qreg[i] for i in dj_qubit_indices])  # 再次 Hadamard
    for i in dj_qubit_indices:
        qc.measure(qreg[i], creg[i])

    return qc, creg

################################################################################
# 生成完整 Python 程序代码
def generate_dj_nonconstant_code(num_qubits=8, dj_bits=4, cir_name="qc", qreg_name="dj_qreg", creg_name="dj_creg"):
    aux_index = num_qubits
    dj_qubit_indices = list(range(dj_bits))

    header = [
        "from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile",
        "from qiskit_aer import Aer",
        "",
        f"{qreg_name} = QuantumRegister({num_qubits + 1})",
        f"{creg_name} = ClassicalRegister({dj_bits})",
        f"{cir_name} = QuantumCircuit({qreg_name}, {creg_name})",
        ""
    ]

    body = [
        f"{cir_name}.x({qreg_name}[{aux_index}])",
        f"{cir_name}.h([{', '.join(f'{qreg_name}[{i}]' for i in range(num_qubits + 1))}])"
    ]

    body += generate_combined_oracle(
        num_qubits=num_qubits,
        cir_name=cir_name,
        qreg_name=qreg_name,
        dj_qubit_indices=dj_qubit_indices,
        aux_index=aux_index
    )

    body.append(f"{cir_name}.h([{', '.join(f'{qreg_name}[{i}]' for i in dj_qubit_indices)}])")
    body += [f"{cir_name}.measure({qreg_name}[{i}], {creg_name}[{i}])" for i in dj_qubit_indices]

    footer = [
        "",
        "# 执行模拟器并获取测量结果",
        "backend = Aer.get_backend('aer_simulator')",
        f"compiled = transpile({cir_name}, backend)",
        f"job = backend.run(compiled, shots=1024)",
        "dj_result = job.result().get_counts()",
        "",
        "# 提取前 dj_bits 位作为 Deutsch-Jozsa 判定依据",
        f"dj_only_result = {{k[:{dj_bits}]: v for k, v in dj_result.items()}}",
        "print('Deutsch-Jozsa 结果 (前 dj_bits 位):', dj_only_result)",
        f"if any(key == '{'0'*dj_bits}' for key in dj_only_result.keys()):",
        "    print('❌ 出现全零字符串，错误')",
        "else:",
        "    print('✅ 未出现全零字符串')"
    ]

    return "\n".join(header + body + footer)

################################################################################
def write_dj_code_to_file(filename="dj_test.py", num_qubits=8, dj_bits=2):
    code = generate_dj_nonconstant_code(num_qubits, dj_bits)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"✅ 已生成代码文件：{filename}")

if __name__ == "__main__":
    write_dj_code_to_file("dj_test.py", num_qubits=16, dj_bits=8)
