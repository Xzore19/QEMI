import random

from code_fuzzer.qiskit_gen import QiskitGenerator
from code_fuzzer.qasm_execution import QasmExecution
import qiskit.qasm3
from tqdm import tqdm
import gc
import argparse

# optimization_level = [1, 2, 3]
optimization_level = [3]
routing_method = ['none', 'stochastic', 'sabre', 'default']
layout_method = ["trivial", "dense", "noise_adaptive"]

transpile_detail_0 = {
    "optimization_level": 1,
    "routing_method": "none",
    "layout_method": "trivial",
    "approximation_degree": 1,
}


def generate_transpile():
    # 对于transpile函数的几个基本参数的遍历
    transpile_list = []
    transpile_detail = {"approximation_degree": 1}
    for opt in optimization_level:
        transpile_detail["optimization_level"] = opt
        for rou in routing_method:
            transpile_detail["routing_method"] = rou
            for lay in layout_method:
                transpile_detail["layout_method"] = lay
                transpile_list.append(transpile_detail)
    return transpile_list


# pass_option = ["Optimize1qGates", "Optimize1qGatesDecomposition", "Collect1qRuns",
#                "Collect2qBlocks", "CollectMultiQBlocks", "CollectLinearFunctions",
#                "CollectCliffords", "ConsolidateBlocks", "CXCancellation", "InverseCancellation",
#                "CommutationAnalysis", "CommutativeCancellation", "CommutativeInverseCancellation",
#                "Optimize1qGatesSimpleCommutation", "RemoveDiagonalGatesBeforeMeasure", "RemoveResetInZeroState",
#                "RemoveFinalReset", "HoareOptimizer", "TemplateOptimization", "ResetAfterMeasureSimplification",
#                "OptimizeCliffords", "ElidePermutations", "NormalizeRXAngle", "OptimizeAnnotated"]

# pass_option = [
#     "Optimize1qGates", "Optimize1qGatesDecomposition", "Optimize1qGatesSimpleCommutation",
#     "Collect1qRuns", "Collect2qBlocks", "CollectMultiQBlocks",
#     "CollectCliffords", "ConsolidateBlocks",
#     "CommutationAnalysis", "CommutativeCancellation", "CommutativeInverseCancellation",
#     "RemoveDiagonalGatesBeforeMeasure", "RemoveResetInZeroState", "RemoveFinalReset",
#     "RemoveFinalMeasurements", "RemoveIdentityEquivalent", "ResetAfterMeasureSimplification",
#     "HoareOptimizer", "TemplateOptimization", "OptimizeCliffords", "OptimizeAnnotated",
#     "ElidePermutations", "OptimizeSwapBeforeMeasure"
# ]

pass_option = [
    "Optimize1qGates", "Optimize1qGatesDecomposition", "Optimize1qGatesSimpleCommutation",
    "Collect1qRuns", "Collect2qBlocks", "CollectMultiQBlocks",
    "CommutationAnalysis", "CommutativeCancellation", "CommutativeInverseCancellation",
    "RemoveDiagonalGatesBeforeMeasure", "RemoveResetInZeroState", "RemoveFinalReset",
    "RemoveIdentityEquivalent", "ResetAfterMeasureSimplification",
    "HoareOptimizer", "TemplateOptimization", "OptimizeCliffords", "OptimizeAnnotated",
    "ElidePermutations", "OptimizeSwapBeforeMeasure"
]

# control = [
#     "for_break", "for_continue", "for_zero", "while_dead", "while_break", "if_test"
# ]

control = [
    "nest_dead", "nest"
]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Qiskit fuzzing tester")
    parser.add_argument("--qubits", type=int, default=4, help="Number of qubits for each generated circuit")
    parser.add_argument("--iter", type=int, default=1000, help="Number of iterations (default: 1000)")
    args = parser.parse_args()

    tran_list = generate_transpile()

    for tran in tran_list:
        for con in control:
            for i in tqdm(range(args.iter), desc="Processing"):
                a, b, c = random.sample(pass_option, 3)
                pas = [a, b, c]
                a = QiskitGenerator(qubit_num=args.qubits, measure_num=1, gate_num_upper=5, measure_times=10000, transplie=tran,
                                    backend="aer", use_pass=pas, fuzz_type=con)
                a.run()

                # a.qasm_convertor()
                # a.qasm_run()

                del a
                gc.collect()

    # a = QiskitGenerator(5, 1)
    # a.qasm_convertor()
    #
    # q = QasmExecution(file="qasm_code/code.qasm3", simulator="Qiskit")
    # fq = QasmExecution(file="qasm_code/fuzzing_code.qasm3", simulator="Qiskit")
    #
    # a = QiskitGenerator(5, 1)
    # a.run()
