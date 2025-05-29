namespace Main {

    open Std.Arithmetic;
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Math;
    open Std.Measurement;
    open Std.StatePreparation;

    operation MySingleBlock_869bfcd7(q : Qubit) : Unit is Adj + Ctl {
        Rz(0.39998, q);
        Z(q);
    }
    operation MySingleBlock_dc453efc(q : Qubit) : Unit is Adj + Ctl {
        Z(q);
        I(q);
        Ry(1.625766, q);
        Rx(5.032262, q);
    }

    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Adj {
        // --- DEADCODE START ---
        operation __InlineApplyIfEqualAction_ae51c419(q : Qubit[]) : Unit is Adj + Ctl {
                Z(q[11]);
                ApplyToEachCA(H, q);
                Ry(4.84528, q[10]);
                Rxx(0.853018, q[4], q[3]);
                Z(q[1]);
                I(q[4]);
                Ry(2.765436, q[2]);
                Ryy(4.330751, q[11], q[10]);
        }
        use x = Qubit[2];
        X(x[0]);
        X(x[1]);
        use y = Qubit[2];
        X(y[0]);
        let target = q;
        ApplyIfEqualLE(__InlineApplyIfEqualAction_ae51c419, x, y, target);
        X(x[0]);
        X(x[1]);
        X(y[0]);
        // --- DEADCODE END ---
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj + Ctl {
        H(q[0]);
        I(q[0]);
        ApplyToEachCA(MySingleBlock_869bfcd7, q);
        Ry(2.113124, q[0]);
        Ry(0.032832, q[0]);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Adj {
        operation __InlineApplyIfEqualAction_282e920f(q : Qubit[]) : Unit is Adj + Ctl {
                Z(q[0]);
                ApplyToEachCA(MySingleBlock_dc453efc, q);
                T(q[0]);
                Z(q[0]);
                Rzz(3.785594, q[0], q[1]);
                Z(q[0]);
                T(q[0]);
                Rx(4.900287, q[1]);
        }
        let x = [q[0], q[3], q[7]];
        let y = [q[4], q[8], q[9]];
        let target = [q[5], q[10]];
        ApplyIfEqualLE(__InlineApplyIfEqualAction_282e920f, x, y, target);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            Adjoint ApplyRandomBlock0(q);
            Controlled ApplyRandomBlock1([q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[8], q[9], q[10], q[11]], [q[7]]);
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