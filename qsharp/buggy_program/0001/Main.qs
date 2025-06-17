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

    operation MySingleBlock_6f043b5a(q : Qubit) : Unit is Adj + Ctl {
        Ry(5.67123, q);
        H(q);
        Rx(3.266496, q);
    }

function __RandomFlag_5ed6c0be() : Bool {
    let b0 = not ResultAsBool(One);
    let b1 = not ResultAsBool(One);
    let b2 = ResultAsBool(Zero);
    let b3 = ResultAsBool(One);
    return Xor(Xor(b0, b1), Xor(b2, b3));
}
function __RandomFlag_5a6b31ff() : Bool {
    let b0 = ResultAsBool(One);
    let b1 = not ResultAsBool(Zero);
    let b2 = not ResultAsBool(One);
    let b3 = ResultAsBool(One);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_87930607() : Bool {
    let b0 = not true;
    let b1 = not false;
    let b2 = not true;
    let b3 = true;
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_d1d0a21d() : Bool {
    let b0 = not ResultAsBool(One);
    let b1 = not ResultAsBool(One);
    let b2 = ResultAsBool(One);
    let b3 = ResultAsBool(One);
    return Xor(Xor(b0, b1), Xor(b2, b3));
}
function __RandomFlag_1d9e9c93() : Bool {
    let b0 = true;
    let b1 = false;
    let b2 = not true;
    let b3 = true;
    return Xor(Xor(b0, b1), Xor(b2, b3));
}
function __RandomFlag_e4e0785e() : Bool {
    let b0 = ResultAsBool(One);
    let b1 = ResultAsBool(One);
    let b2 = ResultAsBool(One);
    let b3 = ResultAsBool(Zero);
    return Xor(Xor(b0, b1), Xor(b2, b3));
}

operation __PowerOp_afa89fd2(q : Qubit[]) : Unit is Adj {
    operation __InlineIfElseDeadcode_4e10a3dc(q : Qubit[]) : Unit is Adj {
        if __RandomFlag_d1d0a21d() {
            // --- DEADCODE START ---
                    operation __GenBlock_340b053d(q : Qubit[]) : Unit is Adj {
            
                Ry(0.353347, q[0]);
                H(q[0]);
                Rz(5.331091, q[0]);
                Rz(4.050887, q[0]);
            }
                    __GenBlock_340b053d(q);
            // --- DEADCODE END ---
        } else {
                operation __IfBody_dcb8fc58(q : Qubit[]) : Unit is Adj {
                        operation __InlineIfElseDeadcode_744b5e2e(q : Qubit[]) : Unit is Adj {
                            if __RandomFlag_5a6b31ff() {
                                        operation __GenBlock_50cc209e(q : Qubit[]) : Unit is Adj {
                                
                                    Exp([PauliZ], 1.68195, [q[0]]);
                                }
                                        __GenBlock_50cc209e(q);
                            } else {
                                // --- DEADCODE START ---
                                        operation __GenBlock_05b85a09(q : Qubit[]) : Unit is Adj {
                                
                                    T(q[0]);
                                }
                                        __GenBlock_05b85a09(q);
                                // --- DEADCODE END ---
                            }
                        }
                        
                        __InlineIfElseDeadcode_744b5e2e(q);
                }
                
                operation __ElseBody_dcb8fc58(q : Qubit[]) : Unit is Adj {
                        operation __ForLoopZeroBody_aaa367d4(q : Qubit[]) : Unit is Adj {
                                operation __GenBlock_b14e437f(q : Qubit[]) : Unit is Adj {
                        
                            let n = 1;
                        ApplyPauliFromInt(PauliY, true, n, [q[0]]);
                        ApplyPauliFromInt(PauliZ, false, n, [q[0]]);
                        }
                                __GenBlock_b14e437f(q);
                        }
                        // --- DEADCODE START ---
                        for i in 1..0 {
                            Adjoint __ForLoopZeroBody_aaa367d4(q);
                        }
                        // --- DEADCODE END ---
                }
                
                if __RandomFlag_87930607() {
                    Adjoint __IfBody_dcb8fc58(q);
                } else {
                    Adjoint __ElseBody_dcb8fc58(q);
                }
                operation __GenBlock_18ed06ba(q : Qubit[]) : Unit is Adj {
            
                ApplyCNOTChain([q[0]]);
            }
                __GenBlock_18ed06ba(q);
        }
    }
    
    __InlineIfElseDeadcode_4e10a3dc(q);
}

    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Adj {
        operation __InlineIfElseDeadcode_5fb0241b(q : Qubit[]) : Unit is Adj {
            if __RandomFlag_5ed6c0be() {
                        operation __GenBlock_b374611d(q : Qubit[]) : Unit is Adj {
                
                    Rzz(0.472803, q[2], q[6]);
                    ApplyP(PauliZ, q[3]);
                    ApplyToEachA(MySingleBlock_6f043b5a, q);
                    H(q[3]);
                    Z(q[0]);
                    CY(q[2], q[7]);
                    Ry(2.016319, q[2]);
                    H(q[0]);
                }
                        __GenBlock_b374611d(q);
            } else {
                // --- DEADCODE START ---
                        operation __GenBlock_4851d70e(q : Qubit[]) : Unit is Adj {
                
                    Exp([PauliY], 0.604408, [q[7]]);
                    IncByI(9, [q[0], q[1], q[4], q[5]]);
                    ApplyPauli([PauliY, PauliX, PauliZ], [q[3], q[2], q[4]]);
                    Rz(5.524669, q[2]);
                    Relabel([q[1], q[2], q[3], q[4], q[5], q[7]], [q[4], q[5], q[1], q[3], q[2], q[7]]);
                    H(q[7]);
                    CNOT(q[0], q[6]);
                    ApplyCNOTChain([q[1], q[5], q[6], q[2], q[7], q[0], q[3], q[4]]);
                }
                        __GenBlock_4851d70e(q);
                // --- DEADCODE END ---
            }
        }
        
        __InlineIfElseDeadcode_5fb0241b(q);
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit {
        operation __RepeatBody_72609a84(q : Qubit[]) : Unit {
                operation __GenBlock_3435b5d8(q : Qubit[]) : Unit {
        
            ApplyOperationPowerA(-1, __PowerOp_afa89fd2, q);
            IncByIUsingIncByLE(RippleCarryCGIncByLE, 15, [q[0], q[3], q[4], q[5], q[6]]);
            Y(q[2]);
            SX(q[6]);
            SX(q[2]);
        }
                __GenBlock_3435b5d8(q);
        }
        operation __FixupBody_aaec9f59(q : Qubit[]) : Unit {
            operation __DeadBlock_31d9ad92(q : Qubit[]) : Unit is Adj + Ctl {
                    // --- DEADCODE START ---
                    let target = q; 
                    operation __InlineApplyIfRelation_b009790f(q : Qubit[]) : Unit is Adj + Ctl {
                        operation __InlineIfElseDeadcode_c708e3aa(q : Qubit[]) : Unit is Adj + Ctl {
                            if __RandomFlag_1d9e9c93() {
                                // --- DEADCODE START ---
                                    operation __DeadBlock_d19bb406(q : Qubit[]) : Unit is Adj + Ctl {
                                                operation __GenBlock_8bab67a7(q : Qubit[]) : Unit is Adj + Ctl {
                                        
                                            CCNOT(q[7], q[2], q[6]);
                                        }
                                                __GenBlock_8bab67a7(q);
                                    }
                                    
                                    operation __InlineIfElseDeadcode_99d4dec5(q : Qubit[]) : Unit is Adj + Ctl {
                                        use ctrl = Qubit();
                                        within { } apply {
                                            // --- DEADCODE START ---
                                            Controlled __DeadBlock_d19bb406([ctrl], q);
                                            // --- DEADCODE END ---
                                        }
                                                operation __GenBlock_8417b95f(q : Qubit[]) : Unit is Adj + Ctl {
                                        
                                            Rxx(0.183399, q[0], q[6]);
                                        }
                                                Controlled Adjoint __GenBlock_8417b95f([q[0]], [q[1], q[2], q[3], q[4], q[5], q[6], q[7]]);
                                    }
                                    
                                    __InlineIfElseDeadcode_99d4dec5(q);
                                // --- DEADCODE END ---
                            } else {
                                        operation __GenBlock_33e83d21(q : Qubit[]) : Unit is Adj + Ctl {
                                
                                    Rzz(5.86706, q[1], q[2]);
                                    let n = 1;
                                ApplyPauliFromInt(PauliZ, true, n, [q[0]]);
                                ApplyPauliFromInt(PauliX, false, n, [q[0]]);
                                }
                                        Controlled Adjoint __GenBlock_33e83d21([q[4], q[5], q[6], q[7]], [q[0], q[1], q[2], q[3]]);
                            }
                        }
                        
                        __InlineIfElseDeadcode_c708e3aa(q);
                    }
                    use x = Qubit[2];
                    X(x[0]);
                    X(x[1]);
                    use y = Qubit[2];
                    X(y[0]);
                    ApplyIfEqualLE(__InlineApplyIfRelation_b009790f, x, y, target);
                    X(x[0]);
                    X(x[1]);
                    X(y[0]);
                    // --- DEADCODE END ---
            }
            
            operation __InlineBitstringDeadcode_b899fd35(q : Qubit[]) : Unit {
                use ctrl = Qubit[3];
                within { } apply {
                    // --- DEADCODE START ---
                    // ctrl actual = |001⟩ (int 4), condition = 7
                    X(ctrl[2]);
                    ApplyControlledOnInt(7, __DeadBlock_31d9ad92, ctrl, q);
                    // --- DEADCODE END ---
                }
                ResetAll(ctrl);
            }
            
            __InlineBitstringDeadcode_b899fd35(q);
        }
        use flag = Qubit();
        mutable result = One;
        repeat {
            X(flag);
            __RepeatBody_72609a84(q);
            set result = M(flag);
        } until (result == Zero) fixup {
            __FixupBody_aaec9f59(q);
        }
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Ctl {
        operation __IfBody_ff38881a(q : Qubit[]) : Unit is Ctl {
                    operation __GenBlock_707a9db3(q : Qubit[]) : Unit is Ctl {
            
                SX(q[2]);
                Ry(4.960988, q[0]);
                RFrac(PauliX, 6, 7, q[1]);
                S(q[2]);
                IncByI(0, [q[2]]);
                CNOT(q[5], q[3]);
                IncByLUsingIncByLE(RippleCarryTTKIncByLE, IntAsBigInt(2), [q[0], q[1], q[4], q[5]]);
            }
                    Controlled __GenBlock_707a9db3([q[4]], [q[0], q[1], q[2], q[3], q[5], q[6]]);
        }
        
        operation __ElseBody_ff38881a(q : Qubit[]) : Unit is Ctl {
                operation __ForLoopBody_d5eb5a5b(q : Qubit[]) : Unit is Ctl {
                        operation __GenBlock_2b58d9c8(q : Qubit[]) : Unit is Ctl {
                
                    IncByI(14, [q[0], q[1], q[2], q[3]]);
                    Rzz(1.335787, q[2], q[1]);
                    X(q[1]);
                    CZ(q[1], q[2]);
                    Rxx(2.870271, q[3], q[2]);
                }
                        Controlled __GenBlock_2b58d9c8([q[0], q[1]], [q[2], q[3], q[4], q[5]]);
                }
                for i in 1..3 {
                    Controlled __ForLoopBody_d5eb5a5b([q[2]], [q[0], q[1], q[3], q[4], q[5], q[6]]);
                }
                operation __GenBlock_aec799bf(q : Qubit[]) : Unit is Ctl {
            
                MAJ(q[3], q[2], q[0]);
                CX(q[0], q[5]);
            }
                __GenBlock_aec799bf(q);
        }
        
        if __RandomFlag_e4e0785e() {
            __IfBody_ff38881a(q);
        } else {
            __ElseBody_ff38881a(q);
        }
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[8] {
            Adjoint ApplyRandomBlock0(q);
            ApplyRandomBlock1(q);
            Controlled ApplyRandomBlock2([q[2]], [q[0], q[1], q[3], q[4], q[5], q[6], q[7]]);
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