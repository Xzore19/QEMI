from code_fuzzer.qiskit_gen import QiskitGenerator
from code_fuzzer.qasm_execution import QasmExecution
import qiskit.qasm3
from tqdm import tqdm
import gc

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
    "Collect1qRuns","Collect2qBlocks", "CollectMultiQBlocks",
    "ConsolidateBlocks",
    "CommutationAnalysis", "CommutativeCancellation", "CommutativeInverseCancellation",
    "RemoveDiagonalGatesBeforeMeasure", "RemoveResetInZeroState", "RemoveFinalReset",
    "RemoveFinalMeasurements", "RemoveIdentityEquivalent", "ResetAfterMeasureSimplification",
    "HoareOptimizer", "TemplateOptimization", "OptimizeCliffords", "OptimizeAnnotated",
    "ElidePermutations", "OptimizeSwapBeforeMeasure"
]

control = [
    "for_break", "for_continue", "for_zero", "while_dead", "while_break", "if_test"
]

if __name__ == "__main__":
    tran_list = generate_transpile()

    for tran in tran_list:
        for pas in pass_option:
            for con in control:
                for i in tqdm(range(100), desc="Processing"):
                    a = QiskitGenerator(qubit_num = 5, measure_num = 1, gate_num_upper = 10, measure_times = 10000, transplie = tran, backend="aer", use_pass= pas, fuzz_type=con)
                    a.run()

                    # 释放内存，防止因为循环的内存崩溃报错
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

