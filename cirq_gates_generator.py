# This module is some random generators for cirq gates part.

import random
import math

complete_target_gates_lib = ["h", "x", "ccx", "ccz", "s", "z", "y", "sdg", "t", "tdg", "ch", "u",\
                    "cs", "cz", "csdg", "p", "cp", "rx", "crx", "ry", "cu", "cnot",\
                    "cry", "rz", "crz", "swap", "iswap", "cswap", "sx", "sxdg", "csx"]


# 根据门操作的qubit数量不同，将其区分为以下三种
single_qubit_gates = ["h", "x", "z", "y", "t", "rx", "ry", "rz", "xp", "yp", "zp", "pxp", "pxz", "s"]
double_qubit_gates = ["cz", "cx", "swap", "iswap", "fsim", "xxp","yyp","zzp", "ms", "pfs", "pisp","sqis", "inv_sqis"]
more_qubit_gates = ["ccx", "ccz", "cswap", "qft"]

single_qubit_gate_map = {
    "h": "cirq.H",
    "x": "cirq.X",
    "y": "cirq.Y",
    "z": "cirq.Z",
    "s": "cirq.S",
    "t": "cirq.T",

    # 参数化的门，保留占位参数
    "rx": "cirq.rx",
    "ry": "cirq.ry",
    "rz": "cirq.rz",

    "xp": "cirq.XPowGate",
    "yp": "cirq.YPowGate",
    "zp": "cirq.ZPowGate",

    "pxp": "cirq.PhasedXPowGate",
    "pxz": "cirq.PhasedXZGate"
}

double_qubit_gate_map = {
    "cz": "cirq.CZ",
    "cx": "cirq.CNOT",
    "swap": "cirq.SWAP",
    "iswap": "cirq.ISWAP",
    "fsim": "cirq.FSimGate",

    "xxp": "cirq.XXPowGate",
    "yyp": "cirq.YYPowGate",
    "zzp": "cirq.ZZPowGate",
    "ms" : "cirq.MSGate",
    "pfs" : "cirq.PhasedFSimGate",
    "pisp" : "cirq.PhasedISwapPowGate",
    "sqis" : "cirq.SQRT_ISWAP",
    "inv_sqis" : "cirq.SQRT_ISWAP_INV"
}

more_qubit_gate_map = {
    "ccx": "cirq.CCX",
    "ccz": "cirq.CCZ",
    "cswap": "cirq.CSwapGate",
    "qft" : "cirq.QuantumFourierTransformGate"
}



def gate_generator(qubits_num, pi_phase = 1, cir_name = "qc", qubit_name = "q"):
    # for given gate, return an effective gate with effective parameters
    qubits_index = [i for i in range(qubits_num)]

    control_flag = random.choice([True, False])

    if qubits_num == 1:
        gate_name = random.choice(single_qubit_gates)
    elif qubits_num == 2:
        gate_name = random.choice(single_qubit_gates + double_qubit_gates)
    else:
        gate_name = random.choice(single_qubit_gates + double_qubit_gates + more_qubit_gates)

    if gate_name in {"qft"}:
        # n qubit, 0 parameter
        qbit = random.randint(2, qubits_num)
        target = random.sample(qubits_index, qbit)
        if control_flag and qubits_num > 1:
            target = random.sample(qubits_index, qbit)
            control_statement = ",".join([f"{qubit_name}[{i}]" for i in target[0:1]])
            target_list = ",".join([f"{qubit_name}[{i}]" for i in target[1:]])
            return f"{cir_name}.append({more_qubit_gate_map[gate_name]}(num_qubits={qbit-1}).on({target_list}).controlled_by({control_statement}))"
        else:
            target = ",".join([f"{qubit_name}[{i}]" for i in target])
            return f"{cir_name}.append({more_qubit_gate_map[gate_name]}(num_qubits={qbit}).on({target}))"

    elif gate_name in {"h", "x","z","y","t","s"}:
        # 1 qubit, 0 parameter
        target = random.choice(qubits_index)
        if control_flag and qubits_num > 1:
            target = random.sample(qubits_index, qubits_num)
            control_statement = ",".join([f"{qubit_name}[{i}]" for i in target[1:2]])
            return f"{cir_name}.append({single_qubit_gate_map[gate_name]}({qubit_name}[{target[0]}]).controlled_by({control_statement}))"
        else:
            return f"{cir_name}.append({single_qubit_gate_map[gate_name]}({qubit_name}[{target}]))"

    elif gate_name in {"rx", "ry", "rz"}:
        # 1 qubit, 1 parameter
        target = random.choice(qubits_index)
        if pi_phase == 1:
            temp = 2**random.randint(1, 10)
            phase = math.pi/temp
        else:
            phase = random.uniform(0, 2*math.pi)

        if control_flag and qubits_num > 1:
            target = random.sample(qubits_index, qubits_num)
            control_statement = ",".join([f"{qubit_name}[{i}]" for i in target[1:2]])
            return f"{cir_name}.append({single_qubit_gate_map[gate_name]}({phase}).on({qubit_name}[{target[0]}]).controlled_by({control_statement}))"
        else:
            return f"{cir_name}.append({single_qubit_gate_map[gate_name]}({phase}).on({qubit_name}[{target}]))"

    elif gate_name in {"ms"}:
        # 2 qubit, 1 parameter
        index_list = random.sample(qubits_index, 2)
        [target1, target2] = index_list

        if pi_phase == 1:
            temp = 2 ** random.randint(1, 10)
            phase = math.pi / temp
        else:
            phase = random.uniform(0, 2 * math.pi)

        if control_flag and qubits_num > 2:
            target = random.sample(qubits_index, qubits_num)
            control_statement = ",".join([f"{qubit_name}[{i}]" for i in target[2:3]])
            return f"{cir_name}.append({double_qubit_gate_map[gate_name]}(rads={phase}).on({qubit_name}[{target[0]}], {qubit_name}[{target[1]}]).controlled_by({control_statement}))"
        else:
            return f"{cir_name}.append({double_qubit_gate_map[gate_name]}(rads={phase}).on({qubit_name}[{target1}], {qubit_name}[{target2}]))"

    elif gate_name in {"pfs"}:
        # 2 qubit, 5 parameter
        index_list = random.sample(qubits_index, 2)
        [target1, target2] = index_list

        if pi_phase == 1:
            temp = 2 ** random.randint(1, 10)
            phase = math.pi / temp
            temp = 2 ** random.randint(1, 10)
            phase_1 = math.pi / temp
            temp = 2 ** random.randint(1, 10)
            phase_2 = math.pi / temp
            temp = 2 ** random.randint(1, 10)
            phase_3 = math.pi / temp
            temp = 2 ** random.randint(1, 10)
            phase_4 = math.pi / temp
        else:
            phase = random.uniform(0, 2 * math.pi)
            phase_1 = random.uniform(0, 2 * math.pi)
            phase_2 = random.uniform(0, 2 * math.pi)
            phase_3 = random.uniform(0, 2 * math.pi)
            phase_4 = random.uniform(0, 2 * math.pi)

        if control_flag and qubits_num > 2:
            target = random.sample(qubits_index, qubits_num)
            control_statement = ",".join([f"{qubit_name}[{i}]" for i in target[2:3]])
            return f"{cir_name}.append({double_qubit_gate_map[gate_name]}(theta={phase}, zeta={phase_1}, chi={phase_2}, gamma={phase_3}, phi={phase_4}).on({qubit_name}[{target[0]}], {qubit_name}[{target[1]}]).controlled_by({control_statement}))"
        else:
            return f"{cir_name}.append({double_qubit_gate_map[gate_name]}(theta={phase}, zeta={phase_1}, chi={phase_2}, gamma={phase_3}, phi={phase_4}).on({qubit_name}[{target1}], {qubit_name}[{target2}]))"

    elif gate_name in {"xp", "yp", "zp"}:
        # 1 qubit, 1 parameter
        target = random.choice(qubits_index)
        if pi_phase == 1:
            temp = 2**random.randint(1, 10)
            phase = math.pi/temp
        else:
            phase = random.uniform(0, 2*math.pi)

        if control_flag and qubits_num > 1:
            target = random.sample(qubits_index, qubits_num)
            control_statement = ",".join([f"{qubit_name}[{i}]" for i in target[1:2]])
            return f"{cir_name}.append({single_qubit_gate_map[gate_name]}(exponent={phase}).on({qubit_name}[{target[0]}]).controlled_by({control_statement}))"
        else:
            return f"{cir_name}.append({single_qubit_gate_map[gate_name]}(exponent={phase}).on({qubit_name}[{target}]))"

    elif gate_name in {"pxp"}:
        # 1 qubit, 2 parameter
        target = random.choice(qubits_index)
        if pi_phase == 1:
            temp = 2**random.randint(1, 10)
            phase_1 = math.pi/temp
            temp = 2 ** random.randint(1, 10)
            phase_2 = math.pi / temp
        else:
            phase_1 = random.uniform(0, 2*math.pi)
            phase_2 = random.uniform(0, 2 * math.pi)

        if control_flag and qubits_num > 1:
            target = random.sample(qubits_index, qubits_num)
            control_statement = ",".join([f"{qubit_name}[{i}]" for i in target[1:2]])
            return f"{cir_name}.append({single_qubit_gate_map[gate_name]}(exponent={phase_1},phase_exponent={phase_2}).on({qubit_name}[{target[0]}]).controlled_by({control_statement}))"
        else:
            return f"{cir_name}.append({single_qubit_gate_map[gate_name]}(exponent={phase_1},phase_exponent={phase_2}).on({qubit_name}[{target}]))"

    elif gate_name in {"pxz"}:
        # 1 qubit, 3 parameter
        target = random.choice(qubits_index)
        if pi_phase == 1:
            temp = 2**random.randint(1, 10)
            phase_1 = math.pi/temp
            temp = 2 ** random.randint(1, 10)
            phase_2 = math.pi / temp
            temp = 2 ** random.randint(1, 10)
            phase_3 = math.pi / temp
        else:
            phase_1 = random.uniform(0, 2*math.pi)
            phase_2 = random.uniform(0, 2 * math.pi)
            phase_3 = random.uniform(0, 2 * math.pi)

        if control_flag and qubits_num > 1:
            target = random.sample(qubits_index, qubits_num)
            control_statement = ",".join([f"{qubit_name}[{i}]" for i in target[1:2]])
            return f"{cir_name}.append({single_qubit_gate_map[gate_name]}(x_exponent={phase_1},z_exponent={phase_2}, axis_phase_exponent={phase_3}).on({qubit_name}[{target[0]}]).controlled_by({control_statement}))"
        else:
            return f"{cir_name}.append({single_qubit_gate_map[gate_name]}(x_exponent={phase_1},z_exponent={phase_2}, axis_phase_exponent={phase_3}).on({qubit_name}[{target}]))"

    elif gate_name in {"xxp", "yyp", "zzp"}:
        # 2 qubit, 1 parameter
        index_list = random.sample(qubits_index, 2)
        [target1, target2] = index_list

        if pi_phase == 1:
            temp = 2**random.randint(1, 10)
            phase = math.pi/temp
        else:
            phase = random.uniform(0, 2*math.pi)

        if control_flag and qubits_num > 2:
            target = random.sample(qubits_index, qubits_num)
            control_statement = ",".join([f"{qubit_name}[{i}]" for i in target[2:3]])
            return f"{cir_name}.append({double_qubit_gate_map[gate_name]}(exponent={phase}).on({qubit_name}[{target[0]}], {qubit_name}[{target[1]}]).controlled_by({control_statement}))"
        else:
            return f"{cir_name}.append({double_qubit_gate_map[gate_name]}(exponent={phase}).on({qubit_name}[{target1}], {qubit_name}[{target2}]))"

    elif gate_name in {"fsim"}:
        # 2 qubit, 2 parameter
        index_list = random.sample(qubits_index, 2)
        [target1, target2] = index_list

        if pi_phase == 1:
            temp = 2 ** random.randint(1, 10)
            phase = math.pi / temp
            temp = 2 ** random.randint(1, 10)
            phase_1 = math.pi / temp
        else:
            phase = random.uniform(0, 2 * math.pi)
            phase_1 = random.uniform(0, 2 * math.pi)

        if control_flag and qubits_num > 2:
            target = random.sample(qubits_index, qubits_num)
            control_statement = ",".join([f"{qubit_name}[{i}]" for i in target[2:3]])
            return f"{cir_name}.append({double_qubit_gate_map[gate_name]}(theta={phase},phi={phase_1}).on({qubit_name}[{target[0]}], {qubit_name}[{target[1]}]).controlled_by({control_statement}))"
        else:
            return f"{cir_name}.append({double_qubit_gate_map[gate_name]}(theta={phase},phi={phase_1}).on({qubit_name}[{target1}], {qubit_name}[{target2}]))"

    elif gate_name in {"pisp"}:
        # 2 qubit, 2 parameter
        index_list = random.sample(qubits_index, 2)
        [target1, target2] = index_list

        if pi_phase == 1:
            temp = 2 ** random.randint(1, 10)
            phase = math.pi / temp
            temp = 2 ** random.randint(1, 10)
            phase_1 = math.pi / temp
        else:
            phase = random.uniform(0, 2 * math.pi)
            phase_1 = random.uniform(0, 2 * math.pi)

        if control_flag and qubits_num > 2:
            target = random.sample(qubits_index, qubits_num)
            control_statement = ",".join([f"{qubit_name}[{i}]" for i in target[2:3]])
            return f"{cir_name}.append({double_qubit_gate_map[gate_name]}(phase_exponent={phase},exponent={phase_1}).on({qubit_name}[{target[0]}], {qubit_name}[{target[1]}]).controlled_by({control_statement}))"
        else:
            return f"{cir_name}.append({double_qubit_gate_map[gate_name]}(phase_exponent={phase},exponent={phase_1}).on({qubit_name}[{target1}], {qubit_name}[{target2}]))"

    elif gate_name in {"cx", "cz", "swap", "iswap", "sqis", "inv_sqis"}:
        # 2 qubit, 0 parameter
        index_list = random.sample(qubits_index, 2)
        if gate_name == "cz":
            index_list.sort()
        else:
            index_list.sort(reverse=True)
        [target1, target2] = index_list

        if control_flag and qubits_num > 2:
            target = random.sample(qubits_index, qubits_num)
            control_statement = ",".join([f"{qubit_name}[{i}]" for i in target[2:3]])
            return f"{cir_name}.append({double_qubit_gate_map[gate_name]}({qubit_name}[{target[0]}], {qubit_name}[{target[1]}]).controlled_by({control_statement}))"
        else:
            return f"{cir_name}.append({double_qubit_gate_map[gate_name]}({qubit_name}[{target1}], {qubit_name}[{target2}]))"

    elif gate_name in {"ccx", "ccz"}:
        # 3 qubit, 0 parameter
        index_list = random.sample(qubits_index, 3)
        index_list.sort(reverse=True)
        [target1, target2, target3] = index_list

        if control_flag and qubits_num > 3:
            target = random.sample(qubits_index, qubits_num)
            control_statement = ",".join([f"{qubit_name}[{i}]" for i in target[3:4]])
            return f"{cir_name}.append({more_qubit_gate_map[gate_name]}({qubit_name}[{target[0]}], {qubit_name}[{target[1]}], {qubit_name}[{target[2]}]).controlled_by({control_statement}))"
        else:
            return f"{cir_name}.append({more_qubit_gate_map[gate_name]}({qubit_name}[{target1}], {qubit_name}[{target2}], {qubit_name}[{target3}]))"

    elif gate_name in {"cswap"}:
        # 3 qubit, 0 parameter
        index_list = random.sample(qubits_index, 3)
        index_list.sort(reverse=True)
        [target1, target2, target3] = index_list

        if control_flag and qubits_num > 3:
            target = random.sample(qubits_index, qubits_num)
            control_statement = ",".join([f"{qubit_name}[{i}]" for i in target[3:4]])
            return f"{cir_name}.append({more_qubit_gate_map[gate_name]}().on({qubit_name}[{target[0]}], {qubit_name}[{target[1]}], {qubit_name}[{target[2]}]).controlled_by({control_statement}))"
        else:
            return f"{cir_name}.append({more_qubit_gate_map[gate_name]}().on({qubit_name}[{target1}], {qubit_name}[{target2}], {qubit_name}[{target3}]))"



if __name__ == "__main__":
    gate = gate_generator(qubits_num=4, pi_phase=1,cir_name = "qc", qubit_name = "q")
    print(gate)
