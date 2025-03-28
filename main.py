from qutefuzz.qiskit_gen import QiskitGenerator
from tqdm import tqdm
import gc

optimization_level = [1, 2, 3]
routing_method = ['none', 'stochastic', 'sabre']
layout_method = ["trivial", "dense", "noise_adaptive"]

transpile_detail_0 = {
    "optimization_level": 1,
    "routing_method": "none",
    "layout_method": "trivial",
    "approximation_degree": 1,
}

def generate_transpile():
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
pass_option = ["Optimize1qGates", "Optimize1qGatesDecomposition", "Collect1qRuns",
               "Collect2qBlocks", "CollectMultiQBlocks", "CollectLinearFunctions",
               "CollectCliffords", "ConsolidateBlocks", "CXCancellation",
               "CommutationAnalysis", "CommutativeCancellation", "CommutativeInverseCancellation",
               "Optimize1qGatesSimpleCommutation", "RemoveDiagonalGatesBeforeMeasure", "RemoveResetInZeroState",
               "RemoveFinalReset", "HoareOptimizer", "TemplateOptimization", "ResetAfterMeasureSimplification",
               "OptimizeCliffords", "ElidePermutations", "OptimizeAnnotated"]


if __name__ == "__main__":
    tran_list = generate_transpile()

    for tran in tran_list:
        for pas in pass_option:
            for i in tqdm(range(100), desc="Processing"):
                a = QiskitGenerator(qubit_num = 5, measure_num = 1, gate_num_upper = 50, measure_times = 10000, transplie = tran, backend="aer", use_pass= pas)
                a.run()

                # 释放内存，防止因为循环的内存崩溃报错
                del a
                gc.collect()
