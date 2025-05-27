namespace QuantumFuzz {
        open Microsoft.Quantum.Intrinsic;
        open Microsoft.Quantum.Measurement;
        open Microsoft.Quantum.Canon;
        open Microsoft.Quantum.Convert;
        open Microsoft.Quantum.Diagnostics;

        @EntryPoint()
        operation TestCircuit() : Result[] {
            use q = Qubit[2] {
                H(q[0]);
            CNOT(q[0], q[1]);
            let r0 = M(q[0]);
            let r1 = M(q[1]);
            ResetAll(q);
            return [r0, r1];
            }
        }
    }