namespace EstimatorTest {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.ResourceEstimation;

    operation MyCircuit() : Unit {
        use q = Qubit[2];
        H(q[0]);
        CNOT(q[0], q[1]);
        ResetAll(q);
    }

    @EntryPoint()
    operation Main() : Unit {
        EstimateResources(MyCircuit);
    }
}
