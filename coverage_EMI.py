import random
import sys
import os

from tqdm import tqdm

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from code_fuzzer.qiskit_gen import QiskitGenerator
import time
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
    "Collect1qRuns", "Collect2qBlocks", "CollectMultiQBlocks",
    "CommutationAnalysis", "CommutativeCancellation", "CommutativeInverseCancellation",
    "RemoveDiagonalGatesBeforeMeasure", "RemoveResetInZeroState", "RemoveFinalReset",
    "RemoveIdentityEquivalent", "ResetAfterMeasureSimplification",
    "HoareOptimizer", "TemplateOptimization", "OptimizeCliffords", "OptimizeAnnotated",
    "ElidePermutations", "OptimizeSwapBeforeMeasure"
]

control = [
    "for_break", "for_continue", "for_zero", "while_dead", "while_break", "if_test","nest_dead", "nest"
]

if __name__ == "__main__":

    for i in tqdm(range(10), desc="Processing"):
        tran_list = generate_transpile()
        tran = random.choice(tran_list)
        con = random.choice(control)
        a, b, c = random.sample(pass_option, 3)
        pas = [a, b, c]
        a = QiskitGenerator(qubit_num=5, measure_num=1, gate_num_upper=4, measure_times=3200, transplie=tran,
                            backend="aer", use_pass=pas, fuzz_type=con, temp_measure=400)
        a.save_file(num=i)
        del a
        gc.collect()




