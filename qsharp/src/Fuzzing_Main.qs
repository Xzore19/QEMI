namespace Main_fuzzing {

    open Std.Arithmetic;
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Math;
    open Std.Measurement;
    open Std.StatePreparation;

    operation MySingleBlock_32d06c36(q : Qubit) : Unit is Adj + Ctl {
        X(q);
        S(q);
    }
    operation MySingleBlock_2ba3c4e3(q : Qubit) : Unit is Adj + Ctl {
        S(q);
        Z(q);
        H(q);
        T(q);
    }
    operation MySingleBlock_675b7b33(q : Qubit) : Unit is Adj + Ctl {
        Rx(1.949111, q);
        Z(q);
    }
    operation MySingleBlock_31f6d3fd(q : Qubit) : Unit is Adj + Ctl {
        Y(q);
        Y(q);
        Rz(3.048244, q);
    }
    operation MySingleBlock_20ffb053(q : Qubit) : Unit is Adj + Ctl {
        I(q);
        Z(q);
    }
    operation MySingleBlock_5f5b219f(q : Qubit) : Unit is Adj + Ctl {
        Rz(6.099335, q);
        Y(q);
        Z(q);
    }
    operation MySingleBlock_13d13fd4(q : Qubit) : Unit is Adj + Ctl {
        R1(1.446738, q);
        I(q);
        R1(5.094702, q);
        I(q);
    }
    operation MySingleBlock_2a40f65d(q : Qubit) : Unit is Adj + Ctl {
        Y(q);
        S(q);
        Ry(3.717576, q);
        Z(q);
    }

    operation ApplyRandomBlock0(q : Qubit[]) : Unit {
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit {
        T(q[2]);
        Rz(4.321442, q[2]);
        X(q[10]);
        ApplyToEach(MySingleBlock_31f6d3fd, q);
        CNOT(q[9], q[2]);
        operation __InlineApplyIfEqualAction_e4351d48(q : Qubit[]) : Unit is Adj + Ctl {
        SWAP(q[3], q[0]);
        Ry(5.910369, q[2]);
        ApplyToEachCA(MySingleBlock_20ffb053, q);
        Z(q[7]);
        SWAP(q[5], q[6]);
        ApplyToEachCA(MySingleBlock_5f5b219f, q);
        X(q[8]);
        SWAP(q[3], q[1]);
}
let x = [q[5]];
let y = [q[6]];
let target = [q[0], q[1], q[2], q[3], q[4], q[7], q[8], q[9], q[10], q[11]];
ApplyIfEqualLE(__InlineApplyIfEqualAction_e4351d48, x, y, target);
        Ryy(3.068634, q[7], q[2]);
        I(q[0]);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Adj {
        operation __InlineApplyIfEqualAction_e23732af(q : Qubit[]) : Unit is Adj + Ctl {
        Ryy(0.957286, q[2], q[0]);
        Y(q[2]);
        Y(q[1]);
        ApplyQFT(q);
        S(q[0]);
        ApplyToEachCA(MySingleBlock_13d13fd4, q);
        CCNOT(q[2], q[0], q[1]);
        H(q[2]);
}
let x = [q[2], q[10]];
let y = [q[1], q[6]];
let target = [q[0], q[3], q[5], q[8]];
ApplyIfEqualLE(__InlineApplyIfEqualAction_e23732af, x, y, target);
        ApplyToEachA(H, q);
        I(q[10]);
        H(q[1]);
        X(q[6]);
        Rx(2.464929, q[1]);
        ApplyToEachA(MySingleBlock_2a40f65d, q);
        operation __InlineApplyIfEqualAction_b35a2c22(q : Qubit[]) : Unit is Adj + Ctl {
        Rx(5.404898, q[1]);
        Ryy(2.147105, q[2], q[1]);
        CCNOT(q[0], q[2], q[1]);
        ApplyQFT(q);
        SWAP(q[1], q[2]);
        Y(q[0]);
        Y(q[2]);
        Rxx(5.625745, q[2], q[0]);
}
let x = [q[5]];
let y = [q[7]];
let target = [q[2], q[4], q[10]];
ApplyIfEqualLE(__InlineApplyIfEqualAction_b35a2c22, x, y, target);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            ApplyRandomBlock0(q);
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