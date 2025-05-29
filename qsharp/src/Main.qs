namespace Main {

    open Std.Arithmetic;
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Math;
    open Std.Measurement;

    operation MySingleBlock_680f443f(q : Qubit) : Unit is Adj + Ctl {
        Z(q);
        S(q);
    }
    operation MySingleBlock_592d9e63(q : Qubit) : Unit is Adj + Ctl {
        X(q);
        Y(q);
        H(q);
        R1(5.74405, q);
    }
    operation MySingleBlock_9afdc7d2(q : Qubit) : Unit is Adj + Ctl {
        R1(1.982221, q);
        X(q);
    }
    operation MySingleBlock_f0986940(q : Qubit) : Unit is Adj + Ctl {
        H(q);
        S(q);
        Rz(0.533194, q);
        Z(q);
    }
    operation MySingleBlock_35a728f7(q : Qubit) : Unit is Adj + Ctl {
        H(q);
        X(q);
    }
    operation MySingleBlock_75acf1b4(q : Qubit) : Unit is Adj + Ctl {
        I(q);
        H(q);
        Ry(4.219457, q);
        S(q);
    }

    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Adj + Ctl {
        // --- DEADCODE START ---
        operation __InlineApplyIfEqualAction_78462200(q : Qubit[]) : Unit is Adj + Ctl {
                ApplyToEachCA(H, q);
                Rx(4.310572, q[8]);
                ApplyToEachCA(MySingleBlock_680f443f, q);
                I(q[6]);
                operation __InlineApplyIfEqualAction_25202e6a(q : Qubit[]) : Unit is Adj + Ctl {
                T(q[1]);
                I(q[0]);
                Rx(1.474411, q[0]);
                ApplyToEachCA(MySingleBlock_592d9e63, q);
                I(q[0]);
                T(q[0]);
                Rz(2.444802, q[0]);
                T(q[0]);
        }
        let x = [q[3], q[6]];
        let y = [q[0], q[4]];
        let target = [q[7], q[8]];
        ApplyIfEqualLE(__InlineApplyIfEqualAction_25202e6a, x, y, target);
                Rz(3.410249, q[9]);
                CNOT(q[3], q[5]);
                Ry(2.695482, q[5]);
        }
        use x = Qubit[2];
        X(x[0]);
        X(x[1]);
        use y = Qubit[2];
        X(y[0]);
        let target = q;
        ApplyIfEqualLE(__InlineApplyIfEqualAction_78462200, x, y, target);
        X(x[0]);
        X(x[1]);
        X(y[0]);
        // --- DEADCODE END ---
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj + Ctl {
        Ry(1.766329, q[0]);
        Rz(2.474117, q[3]);
        Ry(1.132424, q[3]);
        ApplyQFT(q);
        ApplyQFT(q);
        X(q[4]);
        SWAP(q[1], q[2]);
        ApplyToEachCA(MySingleBlock_9afdc7d2, q);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit {
        Y(q[4]);
        ApplyToEach(MySingleBlock_f0986940, q);
        Rzz(0.420355, q[3], q[2]);
        T(q[2]);
        X(q[9]);
        ApplyQFT(q);
        ApplyToEach(MySingleBlock_35a728f7, q);
        ApplyToEach(MySingleBlock_75acf1b4, q);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            Controlled ApplyRandomBlock0([q[0], q[2]], [q[1], q[3], q[4], q[5], q[6], q[7], q[8], q[9], q[10], q[11]]);
            Controlled ApplyRandomBlock1([q[1], q[6], q[9], q[10], q[11]], [q[0], q[2], q[3], q[4], q[5], q[7], q[8]]);
            ApplyRandomBlock2(q);
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