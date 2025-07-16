namespace Main{
    open Std.Intrinsic;
    open Std.Measurement;

    operation Main() : Result[] {
        use q = Qubit[2];
        SX(q[0]);
        X(q[1]);
        let r0 = M(q[0]);
        let r1 = M(q[1]);
        ResetAll(q);
        return [r0, r1];
    }
}

