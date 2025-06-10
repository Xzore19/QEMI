namespace Main_fuzzing {

    open Std.Arithmetic;
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Logical;
    open Std.Math;
    open Std.Measurement;
    open Std.StatePreparation;







    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Adj {
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Ctl {
        operation __ForLoopBody_368dbe33(q : Qubit[]) : Unit is Ctl {
                MAJ(q[1], q[6], q[8]);
                IncByI(334, [q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8]]);
                SwapReverseRegister([q[0], q[2]]);
                ReflectAboutInteger(6, [q[1], q[5], q[8]]);
                IncByLEUsingAddLE(LookAheadDKRSAddLE, RippleCarryCGAddLE, [q[3]], [q[8]]);
                IncByL(IntAsBigInt(0), [q[0], q[8]]);
                IncByLEUsingAddLE(LookAheadDKRSAddLE, RippleCarryCGAddLE, [q[1], q[4]], [q[0], q[3]]);
        }
        for i in 1..3 {
            __ForLoopBody_368dbe33(q);
        }
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit {
        operation __RepeatBody_6cf54c3f(q : Qubit[]) : Unit {
                IncByLUsingIncByLE(RippleCarryCGIncByLE, IntAsBigInt(21), [q[0], q[2], q[5], q[7], q[11]]);
                RippleCarryCGIncByLE([q[1], q[6], q[10]], [q[0], q[4], q[5], q[7], q[8], q[11]]);
                RippleCarryCGIncByLE([q[11]], [q[2], q[10]]);
                IncByI(75, [q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8]]);
                IncByIUsingIncByLE(RippleCarryCGIncByLE, 1917, [q[0], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9], q[10], q[11]]);
        }
        operation __FixupBody_db4f2c47(q : Qubit[]) : Unit {
            operation __ForLoopBody_7d5818df(q : Qubit[]) : Unit {
                    IncByLEUsingAddLE(LookAheadDKRSAddLE, RippleCarryCGAddLE, [q[0], q[8], q[10], q[11]], [q[1], q[2], q[5], q[9]]);
                    IncByI(162, [q[0], q[3], q[5], q[6], q[8], q[9], q[10], q[11]]);
                    IncByLE([q[2], q[3], q[5], q[9], q[10]], [q[0], q[4], q[6], q[7], q[8], q[11]]);
            }
            for i in 1..3 {
                __ForLoopBody_7d5818df(q);
            }
        }
        use flag = Qubit();
        mutable result = One;
        repeat {
            X(flag);
            __RepeatBody_6cf54c3f(q);
            set result = M(flag);
        } until (result == Zero) fixup {
            __FixupBody_db4f2c47(q);
        }
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            Adjoint ApplyRandomBlock0(q);
            Controlled ApplyRandomBlock1([q[4], q[10], q[11]], [q[0], q[1], q[2], q[3], q[5], q[6], q[7], q[8], q[9]]);
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