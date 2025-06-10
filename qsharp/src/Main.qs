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



function __RandomFlag_6d24ef69() : Bool {
    let b0 = not ResultAsBool(Zero);
    let b1 = ResultAsBool(One);
    let b2 = not ResultAsBool(One);
    let b3 = not ResultAsBool(Zero);
    return Xor(Xor(b0, b1), Xor(b2, b3));
}
function __RandomFlag_a173ef94() : Bool {
    let b0 = not true;
    let b1 = not false;
    let b2 = not true;
    let b3 = not false;
    return (b0 and b1) or (b2 and not b3);
}



    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Ctl {
        // --- DEADCODE START ---
        let target = [q[1], q[2], q[3], q[4], q[5], q[6], q[7]]; 
        operation __InlineApplyIfRelation_0a176d8b(q : Qubit[]) : Unit is Adj + Ctl {
            operation __IfBody_1f7d1b37(q : Qubit[]) : Unit is Adj + Ctl {
                    operation __IfBody_413f521a(q : Qubit[]) : Unit is Adj + Ctl {
                                operation __GenBlock_b00b0ac2(q : Qubit[]) : Unit is Adj + Ctl {
                        
                            IncByLEUsingAddLE(LookAheadDKRSAddLE, RippleCarryCGAddLE, [q[0], q[3]], [q[1], q[2]]);
                            FourierTDIncByLE([q[0], q[3]], [q[1], q[2]]);
                            IncByI(2, [q[1], q[3]]);
                            IncByLEUsingAddLE(LookAheadDKRSAddLE, RippleCarryCGAddLE, [q[1]], [q[3]]);
                        }
                                Controlled Adjoint __GenBlock_b00b0ac2([q[0], q[1], q[3]], [q[2], q[4], q[5], q[6]]);
                    }
                    
                    operation __ElseBody_413f521a(q : Qubit[]) : Unit is Adj + Ctl {
                            operation __ForLoopBody_6e922f68(q : Qubit[]) : Unit is Adj + Ctl {
                                operation __InlineApplyIfRelationLE_d35baace(q : Qubit[]) : Unit is Adj + Ctl {
                                        operation __GenBlock_543b5e05(q : Qubit[]) : Unit is Adj + Ctl {
                                
                                    IncByIUsingIncByLE(RippleCarryTTKIncByLE, 0, [q[0]]);
                                }
                                        __GenBlock_543b5e05(q);
                                }
                                let x = [q[1], q[2]];
                                let y = [q[3], q[5]];
                                let target = [q[0], q[6]];
                                ApplyIfLessOrEqualLE(__InlineApplyIfRelationLE_d35baace, x, y, target);
                            }
                            for i in 1..3 {
                                __ForLoopBody_6e922f68(q);
                            }
                    }
                    
                    if __RandomFlag_6d24ef69() {
                        __IfBody_413f521a(q);
                    } else {
                        __ElseBody_413f521a(q);
                    }
            }
            
            operation __ElseBody_1f7d1b37(q : Qubit[]) : Unit is Adj + Ctl {
                        operation __GenBlock_2506e061(q : Qubit[]) : Unit is Adj + Ctl {
                
                    IncByL(IntAsBigInt(23), [q[0], q[1], q[2], q[3], q[4]]);
                    ReflectAboutInteger(6, [q[0], q[3], q[4]]);
                    FourierTDIncByLE([q[0], q[3]], [q[2], q[4]]);
                    FourierTDIncByLE([q[0]], [q[2]]);
                    MAJ(q[0], q[3], q[1]);
                    ReflectAboutInteger(0, [q[1]]);
                }
                        Controlled Adjoint __GenBlock_2506e061([q[1], q[3]], [q[0], q[2], q[4], q[5], q[6]]);
            }
            
            if __RandomFlag_a173ef94() {
                __IfBody_1f7d1b37(q);
            } else {
                __ElseBody_1f7d1b37(q);
            }
        }
        use x = Qubit[2];
        X(x[0]);
        X(x[1]);
        Controlled Adjoint ApplyIfGreaterOrEqualL([q[0], q[8]], (__InlineApplyIfRelation_0a176d8b, 0L, x, target));
        X(x[0]);
        X(x[1]);
        // --- DEADCODE END ---
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj {
        operation __InlineApplyIfRelationLE_d2b8c18d(q : Qubit[]) : Unit is Adj + Ctl {
                operation __GenBlock_4da8785f(q : Qubit[]) : Unit is Adj + Ctl {
        
            IncByLUsingIncByLE(RippleCarryTTKIncByLE, IntAsBigInt(7), [q[0], q[1], q[3]]);
            ReflectAboutInteger(1, [q[3], q[5], q[6]]);
            IncByLUsingIncByLE(RippleCarryTTKIncByLE, IntAsBigInt(0), [q[1], q[2], q[4]]);
            MAJ(q[1], q[6], q[4]);
            FourierTDIncByLE([q[3], q[4], q[6]], [q[0], q[1], q[5]]);
            IncByL(IntAsBigInt(5), [q[0], q[1], q[2], q[5]]);
            RippleCarryTTKIncByLE([q[1], q[2], q[6]], [q[3], q[4], q[5]]);
            IncByL(IntAsBigInt(113), [q[0], q[1], q[2], q[3], q[4], q[5], q[6]]);
        }
                __GenBlock_4da8785f(q);
        }
        let x = [q[7]];
        let y = [q[0]];
        let target = [q[2], q[3], q[4], q[5], q[9], q[10], q[11]];
        ApplyIfEqualLE(__InlineApplyIfRelationLE_d2b8c18d, x, y, target);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Ctl {
        operation __ForLoopBody_af994a33(q : Qubit[]) : Unit is Ctl {
                operation __GenBlock_e31cb310(q : Qubit[]) : Unit is Ctl {
        
            IncByL(IntAsBigInt(4), [q[1], q[2], q[6]]);
            IncByLEUsingAddLE(LookAheadDKRSAddLE, RippleCarryCGAddLE, [q[0], q[1], q[3]], [q[2], q[5], q[6]]);
            IncByI(0, [q[0], q[1], q[4], q[5], q[6]]);
            IncByLUsingIncByLE(RippleCarryTTKIncByLE, IntAsBigInt(1), [q[0], q[1], q[2], q[3], q[5]]);
            IncByLUsingIncByLE(RippleCarryTTKIncByLE, IntAsBigInt(19), [q[0], q[1], q[2], q[3], q[5]]);
            IncByLE([q[0]], [q[1], q[4]]);
            IncByLEUsingAddLE(LookAheadDKRSAddLE, RippleCarryCGAddLE, [q[3], q[5]], [q[2], q[6]]);
        }
                Controlled __GenBlock_e31cb310([q[3], q[4]], [q[0], q[1], q[2], q[5], q[6], q[7], q[8]]);
        }
        for i in 1..3 {
            __ForLoopBody_af994a33(q);
        }
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            Controlled ApplyRandomBlock0([q[3], q[5], q[11]], [q[0], q[1], q[2], q[4], q[6], q[7], q[8], q[9], q[10]]);
            Adjoint ApplyRandomBlock1(q);
            Controlled ApplyRandomBlock2([q[4], q[9], q[10]], [q[0], q[1], q[2], q[3], q[5], q[6], q[7], q[8], q[11]]);
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