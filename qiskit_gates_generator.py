# This module is some random generators for qiskit gates part.

import random
import math

# New version qiskit does not have gate-cnot!
complete_target_gates_lib = ["h", "x", "ccx", "ccz", "s", "z", "y", "sdg", "t", "tdg", "ch", "u",\
                    "cs", "cz", "csdg", "p", "cp", "rx", "crx", "ry", "cu", "cnot",\
                    "cry", "rz", "crz", "swap", "iswap", "cswap", "sx", "sxdg", "csx"]


# 根据门操作的qubit数量不同，将其区分为以下三种
# 先不考虑u
# single_qubit_gates = ["h", "x", "s", "z", "y", "sdg", "t", "tdg", "sx", "sxdg", "p", "rx", "ry", "rz"]
single_qubit_gates = ["h", "x", "z", "y", "t", "tdg", "p", "rx", "ry", "rz"]
# 先不加cu
# double_qubit_gates = ["ch", "cs", "cz", "csdg", "cx", "swap", "iswap", "csx", "cp", "crx", "cry", "crz"]
double_qubit_gates = ["ch", "cz", "cx", "swap", "iswap", "cp", "crx", "cry", "crz"]
more_qubit_gates = ["ccx", "ccz", "cswap"]

symqv_single_qubit_gates = ["h", "x", "z", "rx", "rz"]
symqv_double_qubit_gates = ["ch", "cx", "cz", "swap", "iswap", "crx", "crz"]


def weight_gate_generator(qubits_num, pi_phase = 1, cir_name = "qc"):
    # for given gate, return an effective gate with effective parameters
    qubits_index = [i for i in range(qubits_num)]
    weight = random.uniform(0, 0.75)
    if weight > 0.5:
        if qubits_num == 1:
            gate_name = random.choice(single_qubit_gates)
        elif qubits_num >= 2:
            gate_name = random.choice(single_qubit_gates+double_qubit_gates)
        # else:
        #     gate_name = random.choice(single_qubit_gates+double_qubit_gates+more_qubit_gates)
    else:
        if qubits_num == 1:
            gate_name = random.choice(symqv_single_qubit_gates)
        elif qubits_num >= 2:
            gate_name = random.choice(symqv_single_qubit_gates+symqv_double_qubit_gates)
        # else:
        #     gate_name = random.choice(symqv_single_qubit_gates+symqv_double_qubit_gates+more_qubit_gates)

    if gate_name in {"h", "x", "s", "z", "y", "sdg", "t", "tdg", "sx", "sxdg"}:
        # These gates have only one parameter which is the index of target qubit.
        target = random.choice(qubits_index)
        return f"{cir_name}.%s(%s)" % (gate_name, target)
    elif gate_name in {"ch", "cnot", "cs", "cz", "csdg", "cx", "swap", "iswap", "csx"}:
        # These gates have two parameters which are both the index of target qubit.
        index_list = random.sample(qubits_index, 2)
        if gate_name == "cz":
            index_list.sort()
        else:
            index_list.sort(reverse=True)
        [target1, target2] = index_list
        return f"{cir_name}.%s(%s, %s)" % (gate_name, target1, target2)
    elif gate_name in {"ccx", "ccz", "cswap"}:
        # These gates have three parameters which are all the index of target qubit.
        index_list = random.sample(qubits_index, 3)
        index_list.sort(reverse=True)
        [target1, target2, target3] = index_list
        return f"{cir_name}.%s(%s, %s, %s)" % (gate_name, target1, target2, target3)
    elif gate_name in {"p", "rx", "ry", "rz"}:
        # These gates have two parameters which are (phase, index of qubit)
        target = random.choice(qubits_index)
        if pi_phase == 1:
            temp = 2**random.randint(0, 2)
            phase = math.pi/temp
        else:
            phase = random.uniform(0, 2*math.pi)
        return f"{cir_name}.%s(%s, %s)" % (gate_name, phase, target)
    elif gate_name in {"cp", "crx", "cry", "crz"}:
        # These gates have three parameters which are (phase, index of qubit, index of qubit)
        target1, target2 = random.sample(qubits_index, 2)
        if pi_phase == 1:
            temp = 2**random.randint(0, 3)
            phase = math.pi / temp
        else:
            phase = random.uniform(0, 2 * math.pi)
        return f"{cir_name}.%s(%s, %s, %s)" % (gate_name, phase, target1, target2)
    elif gate_name in {"u"}:
        # These gates have four parameters which are (phase, phase, phase, index of qubit)
        target = random.choice(qubits_index)
        theta, phi, lamb = [random.uniform(0, 2*math.pi) for i in range(3)]
        return f"{cir_name}.%s(%s, %s, %s, %s)" % (gate_name, theta, phi, lamb, target)
    elif gate_name in {"cu"}:
        # These gates have five parameters which are (phase, phase, phase, index of qubit, index of qubit)
        target1, target2 = random.sample(qubits_index, 2)
        theta, phi, lamb = [random.uniform(0, 2 * math.pi) for i in range(3)]
        return f"{cir_name}.%s(%s, %s, %s, %s, %s)" % (gate_name, theta, phi, lamb, target1, target2)


def gate_generator(qubits_num, pi_phase = 1, cir_name = "qc"):
    # for given gate, return an effective gate with effective parameters
    qubits_index = [i for i in range(qubits_num)]
    if qubits_num == 1:
        gate_name = random.choice(single_qubit_gates)
    elif qubits_num == 2:
        gate_name = random.choice(single_qubit_gates+double_qubit_gates)
    else:
        gate_name = random.choice(single_qubit_gates+double_qubit_gates+more_qubit_gates)

    if gate_name in {"h", "x", "s", "z", "y", "sdg", "t", "tdg", "sx", "sxdg"}:
        # These gates have only one parameter which is the index of target qubit.
        target = random.choice(qubits_index)
        return f"{cir_name}.%s(%s)" % (gate_name, target)
    elif gate_name in {"ch", "cnot", "cs", "cz", "csdg", "cx", "swap", "iswap", "csx"}:
        # These gates have two parameters which are both the index of target qubit.
        index_list = random.sample(qubits_index, 2)
        if gate_name == "cz":
            index_list.sort()
        else:
            index_list.sort(reverse=True)
        [target1, target2] = index_list
        return f"{cir_name}.%s(%s, %s)" % (gate_name, target1, target2)
    elif gate_name in {"ccx", "ccz", "cswap"}:
        # These gates have three parameters which are all the index of target qubit.
        index_list = random.sample(qubits_index, 3)
        index_list.sort(reverse=True)
        [target1, target2, target3] = index_list
        return f"{cir_name}.%s(%s, %s, %s)" % (gate_name, target1, target2, target3)
    elif gate_name in {"p", "rx", "ry", "rz"}:
        # These gates have two parameters which are (phase, index of qubit)
        target = random.choice(qubits_index)
        if pi_phase == 1:
            temp = 2**random.randint(1, 3)
            phase = math.pi/temp
        else:
            phase = random.uniform(0, 2*math.pi)
        return f"{cir_name}.%s(%s, %s)" % (gate_name, phase, target)
    elif gate_name in {"cp", "crx", "cry", "crz"}:
        # These gates have three parameters which are (phase, index of qubit, index of qubit)
        target1, target2 = random.sample(qubits_index, 2)
        if pi_phase == 1:
            temp = 2**random.randint(1, 3)
            phase = math.pi / temp
        else:
            phase = random.uniform(0, 2 * math.pi)
        return f"{cir_name}.%s(%s, %s, %s)" % (gate_name, phase, target1, target2)
    elif gate_name in {"u"}:
        # These gates have four parameters which are (phase, phase, phase, index of qubit)
        target = random.choice(qubits_index)
        theta, phi, lamb = [random.uniform(0, 2*math.pi) for i in range(3)]
        return f"{cir_name}.%s(%s, %s, %s, %s)" % (gate_name, theta, phi, lamb, target)
    elif gate_name in {"cu"}:
        # These gates have five parameters which are (phase, phase, phase, index of qubit, index of qubit)
        target1, target2 = random.sample(qubits_index, 2)
        theta, phi, lamb = [random.uniform(0, 2 * math.pi) for i in range(3)]
        return f"{cir_name}.%s(%s, %s, %s, %s, %s)" % (gate_name, theta, phi, lamb, target1, target2)

def classcial_generator(param):
    operator = random.choice(["+=", "-=", "*=", "//="])
    value = str(round(random.randint(1, 10), 4))
    return f"{param} {operator} {value}"

def qiskit_generator(qubits_num, gates_num, param):
    # random choose gates from target_gates_lib
    # build the gates module for given qubits_num and given gates_num with QuantumCircuit.name == qc
    qiskit_program = ""
    flag_quantum = 0
    while flag_quantum < gates_num:
        a = random.uniform(0, 0.6)
        if a < 0.5:
            qiskit_program += weight_gate_generator(qubits_num)
            qiskit_program += "\n"
            flag_quantum += 1
        else:
            qiskit_program += classcial_generator(param)
            qiskit_program += "\n"
    return qiskit_program

# def qiskit_generator(qubits_num, gates_num, param):
#     # random choose gates from target_gates_lib
#     # build the gates module for given qubits_num and given gates_num with QuantumCircuit.name == qc
#     qiskit_program = ""
#     flag_quantum = 0
#     while flag_quantum < gates_num:
#         a = random.uniform(0, 0.7)
#         if a < 0.5:
#             qiskit_program += gate_generator(qubits_num)
#             qiskit_program += "\n"
#             flag_quantum += 1
#         else:
#             qiskit_program += classcial_generator(param)
#             qiskit_program += "\n"
#     return qiskit_program


if __name__ == "__main__":
    # program = qiskit_generator(2, 2, "x")
    program = qiskit_generator(2, 10, "x")
    print(program)
