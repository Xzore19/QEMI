# This module is some template generators of qiskit hybrid program.
# Program templates: outside_if, inside_if, if_elif
# Todo: add some more program templates


import random
from string import Template
from qiskit_constraint_generator import hybrid_two_constraint_generator
from qiskit_gates_generator import qiskit_generator

basic_template="""
from qiskit import Aer, transpile
import math
"""

template1 = """
def check_state_eq(qc, target_probability, delta):
    state_len = len(target_probability)
    qubits_num = int(math.log(state_len, 2))
    qubits_state = [bin(i)[2:].zfill(qubits_num) for i in range(state_len)]
    qc.measure_all()
    simulator = Aer.get_backend('aer_simulator')
    compiled_circuit = transpile(qc, simulator)
    job = simulator.run(compiled_circuit, shots=10000).result().get_counts()
    target = True
    for i in range(state_len):
        print(job.get(qubits_state[i], 0)/10000)
        if (job.get(qubits_state[i], 0)/10000) < target_probability[i]-delta or (job.get(qubits_state[i], 0) / 10000)> target_probability[i]+delta:
            target = False
    return target
"""

template2 = """
def check_state_gt(qc, target_probability, delta):
    qc.measure_all()
    simulator = Aer.get_backend('aer_simulator')
    compiled_circuit = transpile(qc, simulator)
    job = simulator.run(compiled_circuit, shots=10000).result().get_counts()
    new_job = {}
    for i in job.keys():
        new_job[int(i, 2)] = job[i]
    target = True
    for [target_state, prob] in target_probability:
        if (new_job.get(target_state, 0) / 10000) < prob - delta:
            target = False
    return target
"""

template3 = """
def check_state_lt(qc, target_probability, delta):
    qc.measure_all()
    simulator = Aer.get_backend('aer_simulator')
    compiled_circuit = transpile(qc, simulator)
    job = simulator.run(compiled_circuit, shots=10000).result().get_counts()
    new_job = {}
    for i in job.keys():
        new_job[int(i, 2)] = job[i]
    target = True
    for [target_state, prob] in target_probability:
        if (new_job.get(target_state, 0) / 10000) > prob + delta:
            target = False
    return target
"""

quantum_constraint = {"check_state_eq": template1, "check_state_gt": template2, "check_state_lt": template3}

def indent(strings, indent_num):
    new_strings = ""
    string_list = strings.split("\n")
    for string in string_list[:-1]:
        new_strings += "    "*indent_num
        new_strings += string
        new_strings += "\n"
    return new_strings

def outside_if_generator(qubits_num, gates_num, min =0):
    """ outside_if template:
    if():
    else:

    if():
    else:
    """
    random_program = ""

    # generate two constraints for two if-condition
    first_constraint, _ = hybrid_two_constraint_generator(0, "x", 0)
    second_constraint, constraint_flag = hybrid_two_constraint_generator(1, "x", qubits_num)

    # choice the number of gates in each module
    first_num, second_num, third_num = [random.randint(min,gates_num) for i in range(3)]

    # build the program modules of three areas
    first_part = qiskit_generator(qubits_num, first_num, "x")
    second_part = qiskit_generator(qubits_num, second_num, "x")
    third_part = qiskit_generator(qubits_num, third_num, "x")

    # Adjust indentation
    first_part = indent(first_part, 1)
    second_part = indent(second_part, 2)
    third_part = indent(third_part, 2)

    program_template = Template("""
def quantum_program(x, qc):
    a = 0
$first_part
    if $first_constraint:
        a += 1
$second_part
    else:
        a -=1
$third_part
    if $second_constraint:
        return a
    else:
        return a+1
        
def expected_result():
    return [-1, 0, 1, 2]
    """)

    random_program += basic_template
    random_program += quantum_constraint[constraint_flag]
    random_program += "\n"
    generated_code = program_template.substitute(first_part=first_part, second_part=second_part,third_part=third_part,\
                                                 first_constraint=first_constraint, second_constraint=second_constraint)
    random_program += generated_code
    return random_program


def inside_if_generator(qubits_num, gates_num, min=0):
    """ two_if template:
    if():
        if():
        else:
    else:
        if():
        else:
    """
    random_program = ""

    # generate two constraints for two if-condition
    first_constraint, _ = hybrid_two_constraint_generator(0, "x", 0)
    second_constraint, constraint_flag_1 = hybrid_two_constraint_generator(1, "x", qubits_num)
    third_constraint, constraint_flag_2 = hybrid_two_constraint_generator(1, "x", qubits_num)
    constraint = set([constraint_flag_1, constraint_flag_2])

    # choice the number of gates in each module
    first_num, second_num, third_num = [random.randint(min, gates_num) for i in range(3)]

    # build the program modules of three areas
    first_part = qiskit_generator(qubits_num, first_num, "x")
    second_part = qiskit_generator(qubits_num, second_num, "x")
    third_part = qiskit_generator(qubits_num, third_num, "x")

    # Adjust indentation
    first_part = indent(first_part, 1)
    second_part = indent(second_part, 2)
    third_part = indent(third_part, 2)

    program_template = Template("""
def quantum_program(x, qc):
$first_part
    if $first_constraint:
$second_part
        if $second_constraint:
            return 1
        else:
            return 2
    else:
$third_part
        if $third_constraint:
            return 3
        else:
            return 4

def expected_result():
    return [1, 2, 3, 4]
    """)

    random_program += basic_template
    for i in constraint:
        random_program += quantum_constraint[i]
    random_program += "\n"
    generated_code = program_template.substitute(first_part=first_part, second_part=second_part, third_part=third_part,\
                                                 first_constraint=first_constraint, second_constraint=second_constraint, third_constraint=third_constraint)
    random_program += generated_code
    return random_program

def if_elif_generator(qubits_num, gates_num, min =0):
    """ if_elif template:
    if():
    elif():
    else

    if():
    elif():
    else:
    """
    random_program = ""

    # generate two constraints for two if-condition
    first_constraint, _ = hybrid_two_constraint_generator(0, "x", 0)
    second_constraint, _ = hybrid_two_constraint_generator(0, "x", 0)
    third_constraint, constraint = hybrid_two_constraint_generator(1, "x", qubits_num)

    # choice the number of gates in each module
    first_num, second_num, third_num, fourth_num = [random.randint(min, gates_num) for i in range(4)]

    # build the program modules of three areas
    first_part = qiskit_generator(qubits_num, first_num, "x")
    second_part = qiskit_generator(qubits_num, second_num, "x")
    third_part = qiskit_generator(qubits_num, third_num, "x")
    fourth_part = qiskit_generator(qubits_num, fourth_num, "x")

    # Adjust indentation
    first_part = indent(first_part, 1)
    second_part = indent(second_part, 2)
    third_part = indent(third_part, 2)
    fourth_part = indent(fourth_part, 2)

    program_template = Template("""
def quantum_program(x, qc):
    a = 0
$first_part
    if $first_constraint:
        a = 1
$second_part
    elif $second_constraint:
        a = 2
$third_part
    else:
        a = 3
$fourth_part
    if $third_constraint:
        return a
    else:
        return a+3

def expected_result():
    return [1,2,3,4,5,6]
    """)

    random_program += basic_template
    random_program += quantum_constraint[constraint]
    random_program += "\n"
    generated_code = program_template.substitute(first_part=first_part, second_part=second_part, third_part=third_part, fourth_part=fourth_part,\
                                                 first_constraint=first_constraint, second_constraint=second_constraint,\
                                                 third_constraint=third_constraint)
    random_program += generated_code
    return random_program


def while_generator():
    pass

def multi_param_if_generator(qubits_num, gates_num, min = 0):
    """ inputs have three input params
    if(x):
    if(y):

    if():
    else:
    """
    random_program = ""

    # generate two constraints for two if-condition
    first_constraint, _ = hybrid_two_constraint_generator(0, "x", 0)
    second_constraint, _ = hybrid_two_constraint_generator(0, "y", 0)
    third_constraint, constraint_flag = hybrid_two_constraint_generator(1, "x", qubits_num)

    # choice the number of gates in each module
    first_num, second_num, third_num, fourth_num = [random.randint(min, gates_num) for i in range(4)]

    # build the program modules of three areas
    first_part = qiskit_generator(qubits_num, first_num, "x")
    second_part = qiskit_generator(qubits_num, second_num, "x")
    third_part = qiskit_generator(qubits_num, third_num, "x")


    # Adjust indentation
    first_part = indent(first_part, 1)
    second_part = indent(second_part, 2)
    third_part = indent(third_part, 2)

    program_template = Template("""
def quantum_program(x, y, qc):
    a = 0
$first_part
    if $first_constraint:
        a += 1
$second_part
    if $second_constraint:
        a += 2
$third_part
    if $third_constraint:
        return a
    else:
        return a+4

def expected_result():
    return [0,1,2,3,4,5,6,7]
    """)

    random_program += basic_template
    random_program += quantum_constraint[constraint_flag]
    random_program += "\n"
    generated_code = program_template.substitute(first_part=first_part, second_part=second_part, third_part=third_part,
                                                 first_constraint=first_constraint, second_constraint=second_constraint, \
                                                 third_constraint=third_constraint)
    random_program += generated_code
    return random_program


# Program templates: outside_if, inside_if, if_elif, multi_param_if
def benchmark_generator(qubits_num, gates_num, min, tests_num):
    basic_index = 0
    for test_num in range(tests_num):
        program_filename = "benchmark/exp_"+str(qubits_num)+"_"+str(gates_num)+"/quantum_program_"+str(basic_index+test_num)+".py"
        program = outside_if_generator(qubits_num, gates_num, min)
        with open(program_filename, "w+") as file:
            file.write(program)
    basic_index += tests_num
    for test_num in range(tests_num):
        program_filename = "benchmark/exp_"+str(qubits_num)+"_"+str(gates_num)+"/quantum_program_"+str(basic_index+test_num)+".py"
        program = inside_if_generator(qubits_num, gates_num, min)
        with open(program_filename, "w+") as file:
            file.write(program)
    basic_index += tests_num
    for test_num in range(tests_num):
        program_filename = "benchmark/exp_"+str(qubits_num)+"_"+str(gates_num)+"/quantum_program_"+str(basic_index+test_num)+".py"
        program = if_elif_generator(qubits_num, gates_num, min)
        with open(program_filename, "w+") as file:
            file.write(program)
    basic_index += tests_num
    for test_num in range(tests_num):
        program_filename = "benchmark/exp_"+str(qubits_num)+"_"+str(gates_num)+"/quantum_program_"+str(basic_index+test_num)+".py"
        program = multi_param_if_generator(qubits_num, gates_num, min)
        with open(program_filename, "w+") as file:
            file.write(program)
    print("Benchmark generation finished!")

def specific_generator(qubits_num, gates_num, min, index):
    if index in [i for i in range(10)]:
        program = outside_if_generator(qubits_num, gates_num, min)
    elif index in [i for i in range(10, 20)]:
        program = inside_if_generator(qubits_num,gates_num, min)
    elif index in [i for i in range(20, 30)]:
        program = if_elif_generator(qubits_num, gates_num, min)
    elif index in [i for i in range(30, 40)]:
        program = multi_param_if_generator(qubits_num, gates_num, min)

    print(program)

if __name__ == "__main__":

    specific_generator(3, 5,3, 15)

    # benchmark_generator(5,10, 5,10)