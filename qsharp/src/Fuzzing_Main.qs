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

    operation MySingleBlock_8ca4a547(q : Qubit) : Unit is Adj + Ctl {
        Rz(2.663366, q);
        H(q);
        Rx(0.642674, q);
    }

function __RandomFlag_f9d7279e() : Bool {
    let b0 = not ResultAsBool(One);
    let b1 = ResultAsBool(One);
    let b2 = ResultAsBool(Zero);
    let b3 = not ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_f6518811() : Bool {
    let b0 = true;
    let b1 = not true;
    let b2 = true;
    let b3 = false;
    return Xor(Xor(b0, b1), Xor(b2, b3));
}
function __RandomFlag_5827c898() : Bool {
    let b0 = not false;
    let b1 = true;
    let b2 = false;
    let b3 = true;
    return Xor(Xor(b0, b1), Xor(b2, b3));
}
function __RandomFlag_dbfb4060() : Bool {
    let b0 = ResultAsBool(One);
    let b1 = not ResultAsBool(Zero);
    let b2 = not ResultAsBool(One);
    let b3 = ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_cc2fb53f() : Bool {
    let b0 = true;
    let b1 = not false;
    let b2 = true;
    let b3 = not true;
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_aab8df29() : Bool {
    let b0 = not false;
    let b1 = false;
    let b2 = false;
    let b3 = false;
    return Xor(Xor(b0, b1), Xor(b2, b3));
}

operation __PowerOp_885e6372(q : Qubit[]) : Unit is Adj {
        operation __GenBlock_28eae5c3(q : Qubit[]) : Unit is Adj {

    IncByI(1, [q[0], q[1]]);
    SX(q[0]);
    Exp([PauliY, PauliX], 4.895806, [q[0], q[1]]);
    SWAP(q[1], q[0]);
    SX(q[1]);
}
        __GenBlock_28eae5c3(q);
}

    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Adj {
        operation __InlineIfElseDeadcode_0b8d22ad(q : Qubit[]) : Unit is Adj {
            if __RandomFlag_f9d7279e() {
            } else {
                    operation __ForLoopBody_50fd8deb(q : Qubit[]) : Unit is Adj {
                        operation __ControlledBody_ce38ee3f(q : Qubit[]) : Unit is Adj + Ctl {
                            operation __InlineApplyIfRelationLE_12418b41(q : Qubit[]) : Unit is Adj + Ctl {
                                operation __ForLoopZeroBody_09739a32(q : Qubit[]) : Unit is Adj + Ctl {
                                        operation __GenBlock_4bcc9b33(q : Qubit[]) : Unit is Adj + Ctl {
                                
                                    Y(q[0]);
                                }
                                        __GenBlock_4bcc9b33(q);
                                }
                            }
                            let x = [q[1], q[2], q[4]];
                            let y = [q[3], q[5], q[6]];
                            let target = [q[0]];
                            ApplyIfGreaterLE(__InlineApplyIfRelationLE_12418b41, x, y, target);
                            operation __GenBlock_f622fb52(q : Qubit[]) : Unit is Adj + Ctl {
                        
                            SX(q[2]);
                        }
                            Controlled Adjoint __GenBlock_f622fb52([q[4]], [q[0], q[1], q[2], q[3], q[5], q[6]]);
                        }
                        ApplyControlledOnInt(0, __ControlledBody_ce38ee3f, [q[1]], [q[0], q[2], q[3], q[4], q[5], q[6], q[7]]);
                        operation __GenBlock_3a7ffcd8(q : Qubit[]) : Unit is Adj {
                    
                        IncByIUsingIncByLE(RippleCarryCGIncByLE, 64, [q[0], q[2], q[3], q[4], q[5], q[6], q[7]]);
                        SwapReverseRegister([q[0], q[1], q[2], q[5]]);
                    }
                        __GenBlock_3a7ffcd8(q);
                    }
                    for i in 1..3 {
                        Adjoint __ForLoopBody_50fd8deb(q);
                    }
                    operation __GenBlock_20849bc7(q : Qubit[]) : Unit is Adj {
                
                    ReflectAboutInteger(16, [q[0], q[1], q[2], q[4], q[7]]);
                    IncByIUsingIncByLE(RippleCarryCGIncByLE, 47, [q[0], q[1], q[2], q[4], q[5], q[6], q[7]]);
                }
                    __GenBlock_20849bc7(q);
            }
        }
        
        __InlineIfElseDeadcode_0b8d22ad(q);
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Ctl {
        operation __ControlledBody_38b2223f(q : Qubit[]) : Unit is Adj + Ctl {
            operation __ControlledBody_1cc60c78(q : Qubit[]) : Unit is Adj + Ctl {
                    operation __GenBlock_e616fcd5(q : Qubit[]) : Unit is Adj + Ctl {
            
                RFrac(PauliY, 1, 9, q[0]);
                Rxx(3.420207, q[0], q[1]);
                Ry(2.355748, q[1]);
                IncByL(IntAsBigInt(3), [q[0], q[1]]);
                CY(q[1], q[0]);
            }
                    Controlled Adjoint __GenBlock_e616fcd5([q[2]], [q[0], q[1]]);
            }
            ApplyControlledOnBitString([true, true], __ControlledBody_1cc60c78, [q[0], q[1]], [q[2], q[3], q[4]]);
            operation __GenBlock_77fea4ce(q : Qubit[]) : Unit is Adj + Ctl {
        
            I(q[2]);
            ApplyCNOTChain([q[0], q[2]]);
        }
            Controlled Adjoint __GenBlock_77fea4ce([q[1], q[4]], [q[0], q[2], q[3]]);
        }
        ApplyControlledOnInt(2, __ControlledBody_38b2223f, [q[2], q[6]], [q[0], q[1], q[3], q[4], q[5]]);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit {
        operation __RepeatBody_9ad71f63(q : Qubit[]) : Unit {
            operation __RepeatBody_7f04439d(q : Qubit[]) : Unit {
                operation __InlineIfElseDeadcode_497d0a44(q : Qubit[]) : Unit {
                    if __RandomFlag_5827c898() {
                            operation __ForLoopZeroBody_533f369f(q : Qubit[]) : Unit {
                                operation __DeadBlock_4cda72ce(q : Qubit[]) : Unit is Adj + Ctl {
                                            operation __GenBlock_6a5b4af2(q : Qubit[]) : Unit is Adj + Ctl {
                                    
                                        I(q[4]);
                                    }
                                            __GenBlock_6a5b4af2(q);
                                }
                                
                                operation __InlineBitstringDeadcode_766d3e16(q : Qubit[]) : Unit {
                                    use ctrl = Qubit[3];
                                    within { } apply {
                                    }
                                    ResetAll(ctrl);
                                }
                                
                                __InlineBitstringDeadcode_766d3e16(q);
                            }
                    } else {
                    }
                }
                
                __InlineIfElseDeadcode_497d0a44(q);
            }
            repeat {
                __RepeatBody_7f04439d(q);
            } until (__RandomFlag_dbfb4060()) fixup {
            }
        }
        operation __FixupBody_fefc1f67(q : Qubit[]) : Unit {
            operation __InlineIfElseDeadcode_5c0d14ed(q : Qubit[]) : Unit {
                if __RandomFlag_aab8df29() {
                            operation __GenBlock_69fe9708(q : Qubit[]) : Unit {
                    
                        ApplyToEach(MySingleBlock_8ca4a547, q);
                        CZ(q[1], q[3]);
                        ReflectAboutInteger(2, [q[2], q[4], q[5], q[7]]);
                        Rx(5.766651, q[5]);
                    }
                            __GenBlock_69fe9708(q);
                } else {
                }
            }
            
            __InlineIfElseDeadcode_5c0d14ed(q);
        }
        use flag = Qubit();
        mutable result = One;
        repeat {
            X(flag);
            __RepeatBody_9ad71f63(q);
            set result = M(flag);
        } until (result == Zero) fixup {
            __FixupBody_fefc1f67(q);
        }
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[8] {
            X(q[5]);
            Adjoint ApplyRandomBlock0(q);
            Controlled ApplyRandomBlock1([q[5]], [q[0], q[1], q[2], q[3], q[4], q[6], q[7]]);
            ApplyRandomBlock2(q);
            let r0 = M(q[0]);
            let r1 = M(q[1]);
            let r2 = M(q[2]);
            let r3 = M(q[3]);
            let r4 = M(q[4]);
            let r5 = M(q[5]);
            let r6 = M(q[6]);
            let r7 = M(q[7]);
            ResetAll(q);
            return [r0, r1, r2, r3, r4, r5, r6, r7];
        }
    }
}