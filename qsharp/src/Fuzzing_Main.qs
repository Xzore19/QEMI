namespace Main_fuzzing {

    open Std.Arithmetic;
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Math;
    open Std.Measurement;
    open Std.StatePreparation;

    operation MySingleBlock_13e16aab(q : Qubit) : Unit is Adj + Ctl {
        I(q);
        R1(5.210234, q);
        Rz(5.603679, q);
        X(q);
    }
    operation MySingleBlock_781d64ae(q : Qubit) : Unit is Adj + Ctl {
        R1(3.328709, q);
        Z(q);
        Ry(2.677822, q);
        H(q);
    }
    operation MySingleBlock_e406b308(q : Qubit) : Unit is Adj + Ctl {
        T(q);
        Y(q);
    }
    operation MySingleBlock_d45bc802(q : Qubit) : Unit is Adj + Ctl {
        H(q);
        Y(q);
        R1(5.557385, q);
    }
    operation MySingleBlock_fe0c6a74(q : Qubit) : Unit is Adj + Ctl {
        Y(q);
        Y(q);
        X(q);
    }
    operation MySingleBlock_cfd4aee5(q : Qubit) : Unit is Adj + Ctl {
        X(q);
        I(q);
        Rx(5.174124, q);
    }
    operation MySingleBlock_04c16f35(q : Qubit) : Unit is Adj + Ctl {
        Rz(3.378324, q);
        S(q);
    }

    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Adj + Ctl {
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj + Ctl {
        S(q[0]);
        ApplyToEachCA(MySingleBlock_cfd4aee5, q);
        I(q[0]);
        R1(1.989895, q[1]);
        I(q[0]);
        ApplyToEachCA(MySingleBlock_04c16f35, q);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Adj + Ctl {
        I(q[0]);
        S(q[0]);
        R1(4.354572, q[0]);
        R1(0.733273, q[0]);
        R1(1.338921, q[0]);
        T(q[0]);
        ApproximatelyPreparePureStateCP(
    1e-6,
    [
        ComplexPolar(0.756781, 6.270964),
        ComplexPolar(0.653668, 0.87321)
    ],
    q
);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            Controlled ApplyRandomBlock0([q[0], q[3]], [q[1], q[2], q[4], q[5], q[6], q[7], q[8], q[9], q[10], q[11]]);
            Controlled ApplyRandomBlock1([q[0], q[1], q[2], q[3], q[4], q[5], q[7], q[9], q[10], q[11]], [q[6], q[8]]);
            Controlled ApplyRandomBlock2([q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[10], q[11]], [q[9]]);
            let r0 = M(q[0]);
            let r1 = M(q[1]);
            let r2 = M(q[2]);
            let r3 = M(q[3]);
            let r4 = M(q[4]);
            let r5 = M(q[5]);
            let r6 = M(q[6]);
            let r7 = M(q[7]);
            let r8 = M(q[8]);
            let r9 = M(q[9]);
            let r10 = M(q[10]);
            let r11 = M(q[11]);
            ResetAll(q);
            return [r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11];
        }
    }
}