namespace Main_fuzzing {

    open Std.Canon;
    open Std.Intrinsic;
    open Std.Measurement;

    operation SingleBlock(q : Qubit) : Unit is Adj + Ctl {
        Ry(5.67123, q);
        H(q);
        Rx(3.266496, q);
    }

    operation DeadBlock(q : Qubit[]) : Unit is Adj + Ctl {
        Rzz(5.86706, q[1], q[2]);
    }

    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Adj {
                
        ApplyToEachA(SingleBlock, q);
        CY(q[2], q[3]);
        Ry(2.016319, q[2]);
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit {

        Y(q[2]);
        SX(q[3]);
        SX(q[2]);

        use ctrl = Qubit[3];
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[8] {
            Adjoint ApplyRandomBlock0(q);
            ApplyRandomBlock1(q);
            let r0 = M(q[0]);
            let r1 = M(q[1]);
            let r2 = M(q[2]);
            let r3 = M(q[3]);
            ResetAll(q);
            return [r0, r1, r2, r3];
        }
    }
}