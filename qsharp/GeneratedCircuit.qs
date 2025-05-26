namespace QuantumFuzz {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;

    operation RunCircuit() : Result[] {
        using (q = Qubit[2]) {
            H(q[0]);
            CNOT(q[0], q[1]);
            let r0 = M(q[0]);
            let r1 = M(q[1]);
            return [r0, r1];
        }
    }
}