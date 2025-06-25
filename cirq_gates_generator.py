# This module is some random generators for cirq gates part.

import random
import math

complete_target_gates_lib = ["h", "x", "ccx", "ccz", "s", "z", "y", "sdg", "t", "tdg", "ch", "u",\
                    "cs", "cz", "csdg", "p", "cp", "rx", "crx", "ry", "cu", "cnot",\
                    "cry", "rz", "crz", "swap", "iswap", "cswap", "sx", "sxdg", "csx"]


# 根据门操作的qubit数量不同，将其区分为以下三种
single_qubit_gates = ["h", "x", "z", "y", "t", "rx", "ry", "rz", "xp", "yp", "zp", "pxp", "pxz", "s", "rotx", "roty", "rotz"]
double_qubit_gates = ["cz", "cx", "swap", "iswap", "fsim", "xxp","yyp","zzp"]
more_qubit_gates = ["ccx", "ccz"]

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
    "pxz": "cirq.PhasedXZGate",

    "rotx": "cirq.RotXGate",
    "roty": "cirq.RotYGate",
    "rotz": "cirq.RotZGate"
}

double_qubit_gate_map = {
    "cz": "cirq.CZ",
    "cx": "cirq.CNOT",
    "swap": "cirq.SWAP",
    "iswap": "cirq.ISWAP",
    "fsim": "cirq.FSimGate",

    "xxp": "cirq.XXPowGate",
    "yyp": "cirq.YYPowGate",
    "zzp": "cirq.ZZPowGate"
}

more_qubit_gate_map = {
    "ccx": "cirq.CCX",
    "ccz": "cirq.CCZ"
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

    if gate_name in {"h", "x","z","y","t","s"}:
        # These gates have only one parameter which is the index of target qubit.
        target = random.choice(qubits_index)
        if control_flag and qubits_num > 1:
            target = random.sample(qubits_index, qubits_num)
            control_statement = ",".join([f"{qubit_name}[{i}]" for i in target[1:]])
            return f"{cir_name}.append({single_qubit_gate_map[gate_name]}({qubit_name}[{target[0]}]).controlled_by({control_statement}))"
        else:
            return f"{cir_name}.append({single_qubit_gate_map[gate_name]}({qubit_name}[{target}]))"

    elif gate_name in {"rx", "ry", "rz", "xp", "yp", "zp", "rotx", "roty", "rotz"}:
        # These gates have two parameters which are (phase, index of qubit)
        target = random.choice(qubits_index)
        if pi_phase == 1:
            temp = 2**random.randint(1, 3)
            phase = math.pi/temp
        else:
            phase = random.uniform(0, 2*math.pi)

        if control_flag and qubits_num > 1:
            target = random.sample(qubits_index, qubits_num)
            control_statement = ",".join([f"{qubit_name}[{i}]" for i in target[1:]])
            return f"{cir_name}.append({single_qubit_gate_map[gate_name]}({phase}).on({qubit_name}[{target[0]}]).controlled_by({control_statement}))"
        else:
            return f"{cir_name}.append({single_qubit_gate_map[gate_name]}({phase}).on({qubit_name}[{target}]))"

    elif gate_name in {"cx", "cz", "swap", "iswap"}:
        # These gates have two parameters which are both the index of target qubit.
        index_list = random.sample(qubits_index, 2)
        if gate_name == "cz":
            index_list.sort()
        else:
            index_list.sort(reverse=True)
        [target1, target2] = index_list

        if control_flag and qubits_num > 2:
            target = random.sample(qubits_index, qubits_num)
            control_statement = ",".join([f"{qubit_name}[{i}]" for i in target[2:]])
            return f"{cir_name}.append({double_qubit_gate_map[gate_name]}({qubit_name}[{target[0]}], {qubit_name}[{target[1]}]).controlled_by({control_statement}))"
        else:
            return f"{cir_name}.append({double_qubit_gate_map[gate_name]}({qubit_name}[{target1}], {qubit_name}[{target2}]))"
    elif gate_name in {"ccx", "ccz"}:
        # These gates have three parameters which are all the index of target qubit.
        index_list = random.sample(qubits_index, 3)
        index_list.sort(reverse=True)
        [target1, target2, target3] = index_list

        if control_flag and qubits_num > 3:
            target = random.sample(qubits_index, qubits_num)
            control_statement = ",".join([f"{qubit_name}[{i}]" for i in target[3:]])
            return f"{cir_name}.append({more_qubit_gate_map[gate_name]}({qubit_name}[{target[0]}], {qubit_name}[{target[1]}], {qubit_name}[{target[2]}]).controlled_by({control_statement}))"
        else:
            return f"{cir_name}.append({more_qubit_gate_map[gate_name]}({qubit_name}[{target1}], {qubit_name}[{target2}], {qubit_name}[{target3}]))"

#============================================================================================================================================



if __name__ == "__main__":
    gate = gate_generator(qubits_num=4, pi_phase=1,cir_name = "qc", qubit_name = "q")
    print(gate)
