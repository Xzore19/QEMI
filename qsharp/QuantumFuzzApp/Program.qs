namespace QuantumFuzz {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;
    open Microsoft.Quantum.ResourceEstimation;

    operation CircuitToEstimate() : Unit {
        use q = Qubit[2] {
            H(q[0]);
            CNOT(q[0], q[1]);
            let _ = M(q[0]);
            let _ = M(q[1]);
            ResetAll(q);
        }
    }

    @EntryPoint()
    operation RunCircuit() : Unit {
        EstimateResources(CircuitToEstimate);
    }
}