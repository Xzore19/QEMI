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
        Rx(3.541082, q);
        Ry(2.864049, q);
        T(q);
    }
    operation MySingleBlock1(q : Qubit) : Unit is Adj + Ctl {
        I(q);
        H(q);
    }
    operation MySingleBlock2(q : Qubit) : Unit is Adj + Ctl {
        Z(q);
        R1(0.925951, q);
    }
    operation MySingleBlock3(q : Qubit) : Unit is Adj + Ctl {
        X(q);
        Rz(4.763527, q);
        I(q);
        Rx(2.843202, q);
    }

    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Adj {
        T(q[3]);
        Z(q[7]);
        ApplyToEachA(MySingleBlock0, q);
        Y(q[6]);
        I(q[2]);
        Z(q[2]);
        Rxx(1.151889, q[10], q[2]);
        ApplyQFT(q);
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj + Ctl {
        ApplyToEachCA(H, q);
        ApplyToEachCA(MySingleBlock1, q);
        Rx(5.983075, q[0]);
        operation __InlineApplyIfEqualAction_7ee405d5(q : Qubit[]) : Unit is Adj + Ctl {
        Z(q[0]);
        I(q[0]);
        ApplyQFT(q);
        ApplyToEachCA(MySingleBlock2, q);
}
let x = [q[2], q[5]];
let y = [q[0], q[3]];
let target = [q[1]];
ApplyIfEqualLE(__InlineApplyIfEqualAction_7ee405d5, x, y, target);
        SWAP(q[0], q[2]);
        operation __InlineApplyIfEqualAction_db30804b(q : Qubit[]) : Unit is Adj + Ctl {
        Ry(0.511945, q[1]);
        X(q[1]);
        CNOT(q[1], q[0]);
        Rzz(3.571603, q[2], q[0]);
        Rz(0.810483, q[2]);
        Rxx(3.940471, q[2], q[0]);
        ApproximatelyPreparePureStateCP(
    1e-6,
    [
        ComplexPolar(0.183774, 0.094727),
        ComplexPolar(0.335143, 0.211985),
        ComplexPolar(0.385423, 3.73676),
        ComplexPolar(0.17467, 4.751043),
        ComplexPolar(0.32911, 3.781561),
        ComplexPolar(0.482104, 0.022044),
        ComplexPolar(0.494912, 5.961452),
        ComplexPolar(0.298615, 3.362773)
    ],
    q
);
        ApplyQFT(q);
}
let x = [q[4], q[6]];
let y = [q[3], q[5]];
let target = [q[0], q[1], q[2]];
ApplyIfEqualLE(__InlineApplyIfEqualAction_db30804b, x, y, target);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Adj {
        I(q[9]);
        ApplyToEachA(MySingleBlock3, q);
        Rxx(0.060994, q[7], q[9]);
        Rz(4.162136, q[10]);
        Rx(1.921403, q[5]);
        ApplyToEachA(H, q);
        Rzz(1.995917, q[1], q[3]);
        Ryy(3.471386, q[11], q[0]);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            Adjoint ApplyRandomBlock0(q);
            Controlled ApplyRandomBlock1([q[0], q[2], q[4], q[5], q[8]], [q[1], q[3], q[6], q[7], q[9], q[10], q[11]]);
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