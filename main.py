from qutefuzz.qiskit_gen import QiskitGenerator
from tqdm import tqdm

transpile_detail = {
    "optimization_level": 1,
    "routing_method": "basic",
    "layout_method": "trivial",
    "scheduling_method": "asap",
    "approximation_degree": 1,
    "basis_gates": None
}

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
               "OptimizeCliffords", "ElidePermutations", "NormalizeRXAngle", "OptimizeAnnotated"]


if __name__ == "__main__":
    for i in tqdm(range(1), desc="Processing"):
        a = QiskitGenerator(qubit_num = 3, measure_num = 1, gate_num_upper = 5, measure_times = 2000, transplie = None, backend="aer", use_pass= pass_option)
        a.run()
