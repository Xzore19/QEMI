
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile, AncillaRegister
from qiskit_aer import Aer
from qiskit.providers.fake_provider import GenericBackendV2
from qiskit.providers.fake_provider import GenericBackendV2
from qiskit.circuit import Parameter, ParameterVector
from qiskit.circuit.library import XGate
from qiskit.transpiler.passes import *
from qiskit.circuit.library import *
from qiskit.transpiler import PassManager, generate_preset_pass_manager
from math import pi
import numpy as np


def main():
    np.random.seed(42) 
    
    qreg = QuantumRegister(5) 
    creg = ClassicalRegister(5) 
    qc = QuantumCircuit(qreg, creg) 
    
    qc.append(CRXGate(1.782), [qreg[3], qreg[4]])
    qc.append(RXGate(1.441), [qreg[2]])
    qc.append(CCXGate(), [qreg[0], qreg[1], qreg[2]])
    qc.append(RZGate(0.767), [qreg[3]])
    pass
    qc.append(Initialize([(0.2694853035629431+0.014949236408824491j), (-0.046775677747789686-0.18873749289337116j), (0.04028387565288663+0.1442040597675446j), (-0.4130832226173611-0.560174768610463j), (0.263774533640571+0.1403325551419323j), (0.38943389273142603+0.3385973125731004j), (-0.028899786370958563-0.13248210167223506j), (-0.0886931183514135+0.02574806549690836j)]), [qreg[1], qreg[2], qreg[3]])
    qc.append(XGate(), [qreg[0]])
    qc.append(StatePreparation([(-0.1542812402467593+0.21766643886417805j), (0.22000669245931637-0.18949953554162652j), (0.060805566083752635-0.060740057192639446j), (0.20565763560502373-0.21996792962807168j), (-0.18728055790148787+0.022926600123380252j), (0.16098337168470245-0.10983806621104994j), (-0.14832508267927555+0.005820102986464329j), (0.21220244143683606-0.3043139418037914j), (0.2800231344807551-0.24170909346822805j), (0.03631690303758327-0.32396620132253595j), (-0.004128716519069285-0.09229828943709346j), (0.02245120267461556+0.2097202224930633j), (-0.2819261597071135-0.044463945463096524j), (-0.025819226046101932+0.06453282764966628j), (0.06737515976137669-0.2984069994663233j), (0.009816274086402487+0.19256765660137953j)]), [qreg[1], qreg[2], qreg[0], qreg[4]])
    qc.append(CXGate(), [qreg[2], qreg[0]])
    qc.measure(qreg[0], creg[0]) 
    qc.measure(qreg[1], creg[1]) 
    qc.measure(qreg[2], creg[2]) 
    qc.measure(qreg[3], creg[3]) 
    qc.measure(qreg[4], creg[4]) 
    
    qc = qc.assign_parameters({p: 0.5 for p in qc.parameters})
    
    
    simulator = Aer.get_backend("aer_simulator") 
    
    p = PassManager([ElidePermutations(),CommutationAnalysis(),CollectMultiQBlocks()]) 
    qc = p.run(qc) 
    
    compiled_circuit = transpile(qc, backend = simulator, optimization_level = 3, routing_method = "default", layout_method = "noise_adaptive", approximation_degree = 1) 
    
    qc = qc.decompose(reps=10)
    
    job = simulator.run(compiled_circuit, shots=400) 
    result = job.result().get_counts() 
    print(result)


if __name__ == "__main__":
    from coverage import Coverage

    cov = Coverage(
        source=["qiskit"],
        branch=False,
        data_suffix=True
    )
    cov.start()

    main()

    cov.stop()
    cov.save()
    cov.combine()
    cov.report()
