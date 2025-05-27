namespace Main {
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Math;
    open Std.Measurement;

    operation MySingleBlock0(q : Qubit) : Unit is Adj + Ctl {
    S(q);
    Ry(5.241985, q);
    S(q);
    }
    operation MySingleBlock1(q : Qubit) : Unit is Adj + Ctl {
    I(q);
    Rx(4.124748, q);
    S(q);
    }
    operation MySingleBlock2(q : Qubit) : Unit is Adj + Ctl {
    S(q);
    I(q);
    Y(q);
    Rz(0.973171, q);
    }
    operation MySingleBlock3(q : Qubit) : Unit is Adj + Ctl {
    Rz(4.984404, q);
    X(q);
    }
    operation MySingleBlock4(q : Qubit) : Unit is Adj + Ctl {
    Rz(3.262536, q);
    Rz(2.464105, q);
    T(q);
    S(q);
    }
    operation MySingleBlock5(q : Qubit) : Unit is Adj + Ctl {
    Ry(2.041089, q);
    Rx(4.959105, q);
    }
    operation MySingleBlock6(q : Qubit) : Unit is Adj + Ctl {
    X(q);
    I(q);
    }

    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Adj {
        S(q[1]);
        H(q[1]);
        CCNOT(q[2], q[3], q[0]);
        ApplyToEachCA(MySingleBlock0, q);
        ApplyToEachCA(MySingleBlock1, q);
        Rz(6.268281, q[3]);
        H(q[1]);
        ApplyToEachCA(MySingleBlock2, q);
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj + Ctl {
        Rx(4.644623, q[2]);
        Ry(1.083081, q[1]);
        Rx(3.681661, q[0]);
        ApplyToEachCA(MySingleBlock3, q);
        S(q[2]);
        ApplyToEachCA(MySingleBlock4, q);
        T(q[0]);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Adj {
        I(q[0]);
        T(q[3]);
        X(q[2]);
        Rz(4.394303, q[3]);
        ApplyToEachCA(MySingleBlock5, q);
        ApplyToEachCA(MySingleBlock6, q);
        Rxx(2.310581, q[0], q[1]);
        R1(2.735991, q[0]);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[4] {
            Adjoint ApplyRandomBlock0(q);
            Controlled ApplyRandomBlock1([q[2]], [q[0], q[1], q[3]]);
            Adjoint ApplyRandomBlock2(q);
            let r0 = M(q[0]);
            let r1 = M(q[1]);
            let r2 = M(q[2]);
            let r3 = M(q[3]);
            ResetAll(q);
            return [r0, r1, r2, r3];
        }
    }
}