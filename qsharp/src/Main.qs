namespace Main {

    open Std.Arithmetic;
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Math;
    open Std.Measurement;
    open Std.StatePreparation;

    operation MySingleBlock_1e2a0fa5(q : Qubit) : Unit is Adj + Ctl {
        X(q);
        Y(q);
        Ry(1.618416, q);
    }
    operation MySingleBlock_e36119fb(q : Qubit) : Unit is Adj + Ctl {
        I(q);
        Rz(5.131016, q);
    }
    operation MySingleBlock_c6553a61(q : Qubit) : Unit is Adj + Ctl {
        R1(4.199411, q);
        Rx(4.52301, q);
        S(q);
    }
    operation MySingleBlock_2b4235f8(q : Qubit) : Unit is Adj + Ctl {
        Ry(0.176586, q);
        X(q);
        Y(q);
        Ry(1.934934, q);
    }
    operation MySingleBlock_d247b90f(q : Qubit) : Unit is Adj + Ctl {
        Y(q);
        T(q);
        I(q);
        Ry(0.945834, q);
    }
    operation MySingleBlock_3af8aa7e(q : Qubit) : Unit is Adj + Ctl {
        I(q);
        Y(q);
    }

    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Adj + Ctl {
        // --- DEADCODE START ---
        operation __InlineApplyIfEqualAction_c9c00508(q : Qubit[]) : Unit is Adj + Ctl {
                H(q[1]);
                T(q[3]);
                R1(4.687367, q[8]);
                operation __InlineApplyIfEqualAction_adcc0665(q : Qubit[]) : Unit is Adj + Ctl {
                I(q[2]);
                Y(q[3]);
                X(q[3]);
                ApplyToEachCA(MySingleBlock_1e2a0fa5, q);
                Ry(3.831918, q[2]);
                Rx(5.684788, q[3]);
                ApplyQFT(q);
                R1(6.264739, q[0]);
        }
        let x = [q[3]];
        let y = [q[4]];
        let target = [q[0], q[5], q[6], q[7]];
        ApplyIfEqualLE(__InlineApplyIfEqualAction_adcc0665, x, y, target);
                CNOT(q[8], q[6]);
                ApplyToEachCA(MySingleBlock_e36119fb, q);
                ApplyToEachCA(H, q);
                H(q[6]);
        }
        use x = Qubit[2];
        X(x[0]);
        X(x[1]);
        use y = Qubit[2];
        X(y[0]);
        let target = q;
        ApplyIfEqualLE(__InlineApplyIfEqualAction_c9c00508, x, y, target);
        X(x[0]);
        X(x[1]);
        X(y[0]);
        // --- DEADCODE END ---
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit {
        operation __InlineApplyIfEqualAction_13ef6b19(q : Qubit[]) : Unit is Adj + Ctl {
        CNOT(q[2], q[4]);
        Ry(3.272159, q[0]);
        H(q[2]);
        Rxx(0.392626, q[3], q[5]);
        ApplyToEachCA(MySingleBlock_c6553a61, q);
        S(q[4]);
        Z(q[4]);
        I(q[1]);
}
let x = [q[1], q[5], q[6]];
let y = [q[0], q[3], q[8]];
let target = [q[2], q[4], q[7], q[9], q[10], q[11]];
ApplyIfEqualLE(__InlineApplyIfEqualAction_13ef6b19, x, y, target);
        CCNOT(q[3], q[6], q[8]);
        ApplyQFT(q);
        ApplyToEach(MySingleBlock_2b4235f8, q);
        Rx(3.141877, q[4]);
        H(q[6]);
        T(q[2]);
        CNOT(q[2], q[3]);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Adj {
        CNOT(q[9], q[11]);
        ApplyToEachA(MySingleBlock_d247b90f, q);
        operation __InlineApplyIfEqualAction_20df24d9(q : Qubit[]) : Unit is Adj + Ctl {
        X(q[3]);
        S(q[3]);
        I(q[3]);
        Y(q[2]);
        Z(q[1]);
        H(q[3]);
        Rx(2.830081, q[0]);
        H(q[0]);
}
let x = [q[4], q[6], q[8]];
let y = [q[0], q[1], q[5]];
let target = [q[3], q[9], q[10], q[11]];
ApplyIfEqualLE(__InlineApplyIfEqualAction_20df24d9, x, y, target);
        Rx(3.594306, q[8]);
        ApplyQFT(q);
        operation __InlineApplyIfEqualAction_9f1a88b1(q : Qubit[]) : Unit is Adj + Ctl {
        ApplyToEachCA(MySingleBlock_3af8aa7e, q);
        Ryy(6.172973, q[4], q[2]);
        H(q[4]);
        Rz(2.949147, q[2]);
        Rz(3.22729, q[5]);
        I(q[3]);
        Ry(3.831557, q[2]);
        Y(q[8]);
}
let x = [q[8]];
let y = [q[1]];
let target = [q[0], q[2], q[3], q[5], q[6], q[7], q[9], q[10], q[11]];
ApplyIfEqualLE(__InlineApplyIfEqualAction_9f1a88b1, x, y, target);
        ApplyToEachA(H, q);
        Rx(5.786273, q[1]);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            Controlled ApplyRandomBlock0([q[2], q[5], q[9]], [q[0], q[1], q[3], q[4], q[6], q[7], q[8], q[10], q[11]]);
            ApplyRandomBlock1(q);
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