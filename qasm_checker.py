from code_fuzzer.qasm_execution import QasmExecution

qasm_truth = "qasm_code/code.qasm3"
qasm_fuzzing = "qasm_code/fuzzing_code.qasm3"


crash_index = 0
crash_truth = f"qasm_code/buggy_program/crash/truth_{crash_index}.py"
crash_fuzzing = f"qasm_code/buggy_program/crash/fuzzing_{crash_index}.py"

if __name__ == "__main__":
    # a = QasmExecution(qasm_truth)
    #
    # x = a.qasm_run(crash_truth)
    # print(x)

    b = QasmExecution(qasm_fuzzing)

    y = b.qasm_run(crash_fuzzing)
    print(y)

