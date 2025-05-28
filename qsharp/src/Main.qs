namespace Main {
    open Std.Arithmetic;
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Math;
    open Std.Measurement;
    open Std.StatePreparation;

    operation MySingleBlock0(q : Qubit) : Unit is Adj + Ctl {
        T(q);
        X(q);
        Z(q);
        Z(q);
    }
    operation MySingleBlock1(q : Qubit) : Unit is Adj + Ctl {
        X(q);
        T(q);
    }
    operation MySingleBlock2(q : Qubit) : Unit is Adj + Ctl {
        Y(q);
        Z(q);
    }
    operation MySingleBlock3(q : Qubit) : Unit is Adj + Ctl {
        T(q);
        R1(4.931023, q);
    }
    operation MySingleBlock4(q : Qubit) : Unit is Adj + Ctl {
        H(q);
        Rx(3.989063, q);
        I(q);
    }
    operation MySingleBlock5(q : Qubit) : Unit is Adj + Ctl {
        Z(q);
        H(q);
        I(q);
        T(q);
    }

    operation ApplyRandomBlock0(q : Qubit[]) : Unit {
        operation __InlineApplyIfEqualAction_54f32651(q : Qubit[]) : Unit is Adj + Ctl {
                Ryy(3.654196, q[8], q[5]);
                H(q[2]);
                ApplyToEachCA(MySingleBlock0, q);
                Y(q[6]);
                X(q[5]);
                I(q[2]);
                CNOT(q[9], q[8]);
                ApplyToEachCA(MySingleBlock1, q);
        }
        use x = Qubit[2];
        X(x[0]);
        X(x[1]);
        use y = Qubit[2];
        X(y[0]);
        let target = q;
        ApplyIfEqualLE(__InlineApplyIfEqualAction_54f32651, x, y, target);
        X(x[0]);
        X(x[1]);
        X(y[0]);
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj + Ctl {
        ApplyQFT(q);
        ApplyQFT(q);
        ApplyQFT(q);
        CNOT(q[4], q[1]);
        SWAP(q[4], q[1]);
        Ry(2.722627, q[4]);
        operation __InlineApplyIfEqualAction_02d4d4f0(q : Qubit[]) : Unit is Adj + Ctl {
        Y(q[0]);
        ApplyQFT(q);
        Z(q[0]);
        Z(q[0]);
}
let x = [q[0], q[1]];
let y = [q[2], q[4]];
let target = [q[3]];
ApplyIfEqualLE(__InlineApplyIfEqualAction_02d4d4f0, x, y, target);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Adj {
        ApplyToEachA(H, q);
        ApplyToEachA(MySingleBlock2, q);
        Rx(4.404554, q[10]);
        CNOT(q[9], q[1]);
        ApplyQFT(q);
        operation __InlineApplyIfEqualAction_8a122f8e(q : Qubit[]) : Unit is Adj + Ctl {
        R1(2.525656, q[1]);
        ApproximatelyPreparePureStateCP(
    1e-6,
    [
        ComplexPolar(0.31909, 5.892467),
        ComplexPolar(0.638237, 5.060506),
        ComplexPolar(0.525251, 4.310815),
        ComplexPolar(0.463623, 2.425648)
    ],
    q
);
        ApplyToEachCA(MySingleBlock3, q);
        R1(4.650253, q[0]);
        I(q[0]);
        ApplyToEachCA(MySingleBlock4, q);
        Ry(0.892627, q[1]);
}
let x = [q[3], q[5]];
let y = [q[10], q[11]];
let target = [q[7], q[9]];
ApplyIfEqualLE(__InlineApplyIfEqualAction_8a122f8e, x, y, target);
        S(q[0]);
        ApplyToEachA(MySingleBlock5, q);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            ApplyRandomBlock0(q);
            Controlled ApplyRandomBlock1([q[1], q[2], q[4], q[5], q[7], q[9], q[10]], [q[0], q[3], q[6], q[8], q[11]]);
            Adjoint ApplyRandomBlock2(q);
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