namespace Main_fuzzing {
    open Std.Arithmetic;
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Math;
    open Std.Measurement;

    operation MySingleBlock0(q : Qubit) : Unit is Adj + Ctl {
        Z(q);
        X(q);
    }
    operation MySingleBlock1(q : Qubit) : Unit is Adj + Ctl {
        X(q);
        X(q);
        Rz(3.554153, q);
    }
    operation MySingleBlock2(q : Qubit) : Unit is Adj + Ctl {
        X(q);
        T(q);
    }
    operation MySingleBlock3(q : Qubit) : Unit is Adj + Ctl {
        T(q);
        Rz(4.102214, q);
        Rz(4.339647, q);
        Y(q);
    }
    operation MySingleBlock4(q : Qubit) : Unit is Adj + Ctl {
        R1(5.971955, q);
        R1(0.919645, q);
        I(q);
        H(q);
    }

    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Adj + Ctl {
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj + Ctl {
        Z(q[0]);
        ApplyToEachCA(MySingleBlock2, q);
        R1(3.539547, q[0]);
        ApplyQFT(q);
        H(q[0]);
        I(q[0]);
        I(q[1]);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Adj {
        Rxx(4.697685, q[8], q[10]);
        Rz(0.598734, q[5]);
        ApplyQFT(q);
        CCNOT(q[10], q[0], q[4]);
        ApplyToEachA(MySingleBlock3, q);
        X(q[6]);
        ApplyQFT(q);
        operation __InlineApplyIfEqualAction_5fdab434(q : Qubit[]) : Unit is Adj + Ctl {
        Rzz(1.135698, q[3], q[2]);
        ApplyQFT(q);
        Y(q[3]);
        CNOT(q[2], q[0]);
        ApplyQFT(q);
        Rz(4.226311, q[1]);
        Ryy(3.075486, q[1], q[2]);
        operation __InlineApplyIfEqualAction_01a6aac7(q : Qubit[]) : Unit is Adj + Ctl {
        ApplyQFT(q);
        R1(4.903472, q[1]);
        I(q[0]);
        Ryy(5.996557, q[1], q[0]);
        Z(q[1]);
        Ry(0.673845, q[0]);
        ApplyToEachCA(MySingleBlock4, q);
        X(q[0]);
}
let x = [q[0]];
let y = [q[3]];
let target = [q[1], q[2]];
ApplyIfEqualLE(__InlineApplyIfEqualAction_01a6aac7, x, y, target);
}
let x = [q[1]];
let y = [q[0]];
let target = [q[2], q[4], q[7], q[11]];
ApplyIfEqualLE(__InlineApplyIfEqualAction_5fdab434, x, y, target);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            Controlled ApplyRandomBlock0([], q);
            Controlled ApplyRandomBlock1([q[0], q[1], q[2], q[4], q[5], q[6], q[7], q[9], q[10], q[11]], [q[3], q[8]]);
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