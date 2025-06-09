namespace Main_fuzzing {

    open Std.Arithmetic;
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Math;
    open Std.Measurement;
    open Std.StatePreparation;

    operation MySingleBlock_3f47f687(q : Qubit) : Unit is Adj + Ctl {
        I(q);
        T(q);
        Rz(4.452677, q);
    }
    operation MySingleBlock_28c70887(q : Qubit) : Unit is Adj + Ctl {
        H(q);
        T(q);
    }



    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Ctl {
        operation __ForLoopZeroBody_d3e7b378(q : Qubit[]) : Unit is Ctl {
                Z(q[1]);
                Rx(1.060509, q[2]);
                CCNOT(q[8], q[1], q[4]);
                CCNOT(q[8], q[6], q[3]);
                Rz(2.049668, q[5]);
                Ryy(3.901787, q[8], q[2]);
                ApplyToEachC(H, q);
                Rzz(2.124982, q[3], q[8]);
        }
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Ctl {
        operation __InlineApplyIfRelationL_8d01be60(q : Qubit[]) : Unit is Adj + Ctl {
                I(q[0]);
                H(q[0]);
                I(q[0]);
                S(q[0]);
        }
        let x = [q[5]];
        let target = [q[0]];
        ApplyIfGreaterOrEqualL(__InlineApplyIfRelationL_8d01be60, 0L, x, target);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit {
        operation __RepeatBody_8290c3a6(q : Qubit[]) : Unit {
                Rz(5.398128, q[5]);
                R1(3.037001, q[4]);
                CCNOT(q[10], q[11], q[7]);
                ApplyToEach(MySingleBlock_3f47f687, q);
                CZ(q[10], q[9]);
        }
        operation __FixupBody_e014cdbd(q : Qubit[]) : Unit {
                X(q[3]);
                SWAP(q[1], q[3]);
                Rz(2.375044, q[7]);
                ApplyToEach(MySingleBlock_28c70887, q);
                Z(q[0]);
        }
        use flag = Qubit();
        mutable result = One;
        repeat {
            X(flag);
            __RepeatBody_8290c3a6(q);
            set result = M(flag);
        } until (result == Zero) fixup {
            __FixupBody_e014cdbd(q);
        }
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            Controlled ApplyRandomBlock0([q[2], q[6]], [q[0], q[1], q[3], q[4], q[5], q[7], q[8], q[9], q[10], q[11]]);
            Controlled ApplyRandomBlock1([q[0], q[1], q[3], q[4], q[5], q[11]], [q[2], q[6], q[7], q[8], q[9], q[10]]);
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