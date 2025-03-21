# This module is some generators for random combination constraints
# with classical linear constraints and quantum constraints
import random
import math

quantum_constraint = ["check_state_eq", "check_state_gt", "check_state_lt"]


def quantum_constraint_generator(constraint_name, qubits_num):
    delta = random.choice([0.01, 0.005])
    if constraint_name == "check_state_eq":
        state_num = pow(2, qubits_num)
        prob_constraint = [random.uniform(0, 1) for i in range(state_num)]
        prob_constraint = [round(i / sum(prob_constraint), 4) for i in prob_constraint]
        return f"check_state_eq(qc, %s, %s)" % (str(prob_constraint), str(delta))
    elif constraint_name == "check_state_gt":
        state_index = [i for i in range(pow(2,qubits_num))]
        prob_num = math.ceil(qubits_num/2)
        cons_num = random.randint(1, prob_num)
        con_state = random.sample(state_index, cons_num)
        con_prob = [random.uniform(0.4, 0.7) for i in range(cons_num)]
        con_prob = [round(i/cons_num, 4) for i in con_prob]
        prob_list = [[con_state[i], con_prob[i]] for i in range(cons_num)]
        return f"check_state_gt(qc, %s, %s)" % (str(prob_list), str(delta))
    elif constraint_name == "check_state_lt":
        state_index = [i for i in range(pow(2,qubits_num))]
        prob_num = math.ceil(len(state_index)/2)
        cons_num = random.randint(1, prob_num)
        con_state = random.sample(state_index, cons_num)
        con_prob = [random.uniform(0.2, 0.5) for i in range(cons_num)]
        con_prob = [round(i/cons_num, 4) for i in con_prob]
        prob_list = [[con_state[i], con_prob[i]] for i in range(cons_num)]
        return f"check_state_lt(qc, %s, %s)" % (str(prob_list), str(delta))


def hybrid_two_constraint_generator(with_quantum, param, qubits_num=2):
    # with_quantum: a flag of whether the combination constraint has a quantum constraint
    # param: the target for building the classical constraint
    constraint = ""
    # build a flag to check whether we use and/or
    flag = random.uniform(0, 0.4)
    if flag < 0.5:
        # one constraint
        if with_quantum == 1:
            quantum = random.choice(quantum_constraint)
            return quantum_constraint_generator(quantum, qubits_num) ,quantum
        else:
            comparison_operator = random.choice(["<", ">", "==", "!=", "<=", ">="])
            value = str(random.randint(-20, 20))
            return f"{param} {comparison_operator} {value}", None
    else:
        # two constraint
        combine_str = random.choice(["and", "or"])
        comparison_operator = random.choice(["<", ">", "==", "!=", "<=", ">="])
        value = str(random.randint(-20, 20))
        first_constraint = f"%s {comparison_operator} {value}" % param
        if with_quantum == 1:
            quantum = random.choice(quantum_constraint)
            second_constraint = quantum_constraint_generator(quantum, qubits_num)
            return f"{first_constraint} {combine_str} {second_constraint}", quantum
        else:
            new_comparison_operator = random.choice(["<", ">", "==", "!=", "<=", ">="])
            new_value = str(random.randint(-20, 20))
            second_constraint = f"%s {new_comparison_operator} {new_value}" % param
            return f"{first_constraint} {combine_str} {second_constraint}", None




if __name__ == "__main__":
    prob = hybrid_two_constraint_generator(1,"x",2)
    print(prob)
