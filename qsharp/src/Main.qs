namespace Main {

    open Std.Arithmetic;
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Logical;
    open Std.Math;
    open Std.Measurement;
    open Std.StatePreparation;



operation __RandomFlag_104b42f8(q : Qubit[]) : Bool {
    return CheckZero(q[10]);
}
function __RandomFlag_7793eb59() : Bool {
    let b0 = true;
    let b1 = true;
    let b2 = not false;
    let b3 = false;
    return Xor(Xor(b0, b1), Xor(b2, b3));
}



    operation ApplyRandomBlock0(q : Qubit[]) : Unit {
        operation __InlineIfElseDeadcode_2d01a5b0(q : Qubit[]) : Unit {
            if __RandomFlag_7793eb59() {
                    operation __WhileBody_242f1413(q : Qubit[]) : Unit {
                        operation __InlineApplyIfRelationL_edcc1718(q : Qubit[]) : Unit is Adj + Ctl {
                            operation __InlineApplyIfRelationLE_ba6d3b99(q : Qubit[]) : Unit is Adj + Ctl {
                                    ApplyXorInPlaceL(IntAsBigInt(1), [q[0]]);
                                    ReflectAboutInteger(1, [q[0]]);
                            }
                            let x = [q[1], q[3]];
                            let y = [q[0], q[2]];
                            let target = [q[4]];
                            ApplyIfGreaterOrEqualLE(__InlineApplyIfRelationLE_ba6d3b99, x, y, target);
                        }
                        let x = [q[6]];
                        let target = [q[4], q[5], q[7], q[8], q[10]];
                        ApplyIfLessL(__InlineApplyIfRelationL_edcc1718, 0L, x, target);
                    }
                    use flag = Qubit();
                    mutable result = Zero;
                    X(flag);
                    set result = M(flag);
                    while (result == One) {
                        __WhileBody_242f1413(q);
                        X(flag);
                        set result = M(flag);
                    }
            } else {
                // --- DEADCODE START ---
                        SwapReverseRegister([q[0], q[2], q[4], q[5], q[6], q[7], q[9]]);
                        ReflectAboutInteger(72, [q[0], q[1], q[2], q[3], q[5], q[6], q[8], q[9], q[10], q[11]]);
                        IncByLUsingIncByLE(RippleCarryCGIncByLE, IntAsBigInt(0), [q[11]]);
                        FourierTDIncByLE([q[0], q[4]], [q[5], q[11]]);
                        IncByL(IntAsBigInt(165), [q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9], q[10], q[11]]);
                        IncByLUsingIncByLE(RippleCarryCGIncByLE, IntAsBigInt(2890), [q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9], q[10], q[11]]);
                        ResetAll([q[2], q[3], q[6]]);
                RippleCarryCGAddLE([q[4], q[7], q[8], q[10]], [q[0], q[5], q[9], q[11]], [q[1], q[2], q[3], q[6]]);
                        IncByLUsingIncByLE(RippleCarryCGIncByLE, IntAsBigInt(332), [q[1], q[2], q[3], q[4], q[5], q[7], q[8], q[9], q[10]]);
                // --- DEADCODE END ---
            }
        }
        
        __InlineIfElseDeadcode_2d01a5b0(q);
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit {
        operation __WhileBody_8ed1bb2a(q : Qubit[]) : Unit {
                MAJ(q[7], q[11], q[10]);
                IncByIUsingIncByLE(RippleCarryCGIncByLE, 0, [q[2]]);
                ResetAll([q[3], q[5]]);
        RippleCarryCGAddLE([q[4], q[7], q[10]], [q[2], q[9], q[11]], [q[1], q[3], q[5]]);
                MAJ(q[9], q[7], q[5]);
                IncByLEUsingAddLE(LookAheadDKRSAddLE, RippleCarryCGAddLE, [q[0], q[2], q[8], q[10]], [q[1], q[6], q[7], q[9]]);
        }
        use flag = Qubit();
        mutable result = Zero;
        X(flag);
        set result = M(flag);
        while (result == One) {
            __WhileBody_8ed1bb2a(q);
            X(flag);
            set result = M(flag);
        }
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit {
        operation __RepeatBody_9dcb5f9b(q : Qubit[]) : Unit {
                ApplyXorInPlace(1, [q[0]]);
                IncByIUsingIncByLE(RippleCarryCGIncByLE, 0, [q[1], q[3]]);
                RippleCarryCGIncByLE([q[5], q[6]], [q[4], q[11]]);
                IncByLUsingIncByLE(RippleCarryCGIncByLE, IntAsBigInt(0), [q[2]]);
                IncByLE([q[6]], [q[3], q[4], q[5], q[10]]);
        }
        operation __FixupBody_4f95045c(q : Qubit[]) : Unit {
                IncByI(277, [q[0], q[1], q[3], q[4], q[5], q[6], q[7], q[8], q[11]]);
                IncByI(2, [q[1], q[7]]);
                ApplyXorInPlace(2, [q[3], q[5], q[7]]);
                IncByL(IntAsBigInt(185), [q[1], q[2], q[4], q[5], q[6], q[7], q[9], q[11]]);
                IncByLUsingIncByLE(RippleCarryCGIncByLE, IntAsBigInt(12), [q[1], q[5], q[7], q[9]]);
        }
        use flag = Qubit();
        mutable result = One;
        repeat {
            X(flag);
            __RepeatBody_9dcb5f9b(q);
            set result = M(flag);
        } until (result == Zero) fixup {
            __FixupBody_4f95045c(q);
        }
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            ApplyRandomBlock0(q);
            ApplyRandomBlock1(q);
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