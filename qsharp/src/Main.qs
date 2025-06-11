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



function __RandomFlag_083d6004() : Bool {
    let b0 = not ResultAsBool(Zero);
    let b1 = ResultAsBool(One);
    let b2 = not ResultAsBool(Zero);
    let b3 = not ResultAsBool(One);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_768041d7() : Bool {
    let b0 = true;
    let b1 = false;
    let b2 = not false;
    let b3 = not true;
    return Xor(Xor(b0, b1), Xor(b2, b3));
}
function __RandomFlag_6de94fc2() : Bool {
    let b0 = not false;
    let b1 = true;
    let b2 = true;
    let b3 = false;
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_6740fb10() : Bool {
    let b0 = true;
    let b1 = not true;
    let b2 = not true;
    let b3 = true;
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_03e385b8() : Bool {
    let b0 = ResultAsBool(One);
    let b1 = ResultAsBool(One);
    let b2 = not ResultAsBool(One);
    let b3 = ResultAsBool(Zero);
    return Xor(Xor(b0, b1), Xor(b2, b3));
}
function __RandomFlag_e97d814a() : Bool {
    let b0 = not false;
    let b1 = not false;
    let b2 = not true;
    let b3 = not false;
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_433e9b10() : Bool {
    let b0 = not false;
    let b1 = false;
    let b2 = true;
    let b3 = true;
    return Xor(Xor(b0, b1), Xor(b2, b3));
}



    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Ctl {
        operation __InlineIfElseDeadcode_71ce7cdc(q : Qubit[]) : Unit is Ctl {
            if __RandomFlag_6de94fc2() {
                    operation __ForLoopZeroBody_ab9597ef(q : Qubit[]) : Unit is Ctl {
                        operation __ForLoopBody_5dc7cffb(q : Qubit[]) : Unit is Ctl {
                            // --- DEADCODE START ---
                            let target = [q[1], q[2], q[3], q[4], q[5], q[7], q[8], q[9]]; 
                            operation __InlineApplyIfRelation_cf44dd5b(q : Qubit[]) : Unit is Adj + Ctl {
                                operation __InlineApplyIfRelationLE_6b7adb21(q : Qubit[]) : Unit is Adj + Ctl {
                                        operation __GenBlock_e5e2b2ea(q : Qubit[]) : Unit is Adj + Ctl {
                                
                                    CY(q[1], q[3]);
                                    IncByIUsingIncByLE(RippleCarryTTKIncByLE, 21, [q[0], q[1], q[2], q[3], q[5]]);
                                    IncByLUsingIncByLE(RippleCarryTTKIncByLE, IntAsBigInt(1), [q[3]]);
                                }
                                        __GenBlock_e5e2b2ea(q);
                                }
                                let x = [q[0]];
                                let y = [q[4]];
                                let target = [q[1], q[2], q[3], q[5], q[6], q[7]];
                                ApplyIfEqualLE(__InlineApplyIfRelationLE_6b7adb21, x, y, target);
                            }
                            use x = Qubit[2];
                            Controlled Adjoint ApplyIfLessL([q[0], q[6]], (__InlineApplyIfRelation_cf44dd5b, 0L, x, target));
                            // --- DEADCODE END ---
                        }
                        for i in 1..3 {
                            Controlled __ForLoopBody_5dc7cffb([q[3]], [q[0], q[1], q[2], q[4], q[5], q[6], q[7], q[8], q[9], q[10]]);
                        }
                    }
                    // --- DEADCODE START ---
                    for i in 1..0 {
                        __ForLoopZeroBody_ab9597ef(q);
                    }
                    // --- DEADCODE END ---
            } else {
                // --- DEADCODE START ---
                    operation __DeadBlock_e254e52e(q : Qubit[]) : Unit is Ctl {
                            operation __InlineApplyIfRelationLE_fe08e369(q : Qubit[]) : Unit is Adj + Ctl {
                                    operation __GenBlock_8b39585c(q : Qubit[]) : Unit is Adj + Ctl {
                            
                                SWAP(q[0], q[4]);
                                CCNOT(q[4], q[1], q[0]);
                                Exp([PauliZ], 4.694337, [q[3]]);
                                Rxx(2.538838, q[0], q[4]);
                                CCNOT(q[0], q[3], q[2]);
                                Ryy(3.116426, q[1], q[2]);
                            }
                                    Controlled Adjoint __GenBlock_8b39585c([q[1], q[5], q[6]], [q[0], q[2], q[3], q[4], q[7]]);
                            }
                            let x = [q[5]];
                            let y = [q[6]];
                            let target = [q[0], q[1], q[2], q[3], q[4], q[7], q[8], q[10]];
                            ApplyIfEqualLE(__InlineApplyIfRelationLE_fe08e369, x, y, target);
                    }
                    
                    operation __InlineIfElseDeadcode_3c94db14(q : Qubit[]) : Unit is Ctl {
                        use ctrl = Qubit();
                        within { } apply {
                            // --- DEADCODE START ---
                            Controlled __DeadBlock_e254e52e([ctrl], q);
                            // --- DEADCODE END ---
                        }
                            operation __DeadBlock_4da5894a(q : Qubit[]) : Unit is Ctl {
                                    operation __DeadBlock_479eeecc(q : Qubit[]) : Unit is Ctl {
                                                operation __GenBlock_e2a9b3a5(q : Qubit[]) : Unit is Ctl {
                                        
                                            ApplyQFT(q);
                                            Rxx(0.849124, q[7], q[2]);
                                            IncByIUsingIncByLE(RippleCarryTTKIncByLE, 1, [q[0], q[4], q[6]]);
                                            Rx(0.894699, q[2]);
                                            SwapReverseRegister([q[0], q[1], q[3], q[4], q[5], q[6], q[8]]);
                                        }
                                                Controlled __GenBlock_e2a9b3a5([q[5], q[7]], [q[0], q[1], q[2], q[3], q[4], q[6], q[8], q[9], q[10]]);
                                    }
                                    
                                    operation __InlineIfElseDeadcode_f8278f84(q : Qubit[]) : Unit is Ctl {
                                        use ctrl = Qubit();
                                        within { } apply {
                                            // --- DEADCODE START ---
                                            Controlled __DeadBlock_479eeecc([ctrl], q);
                                            // --- DEADCODE END ---
                                        }
                                                operation __GenBlock_c6a02005(q : Qubit[]) : Unit is Ctl {
                                        
                                            R1Frac(4, 7, q[2]);
                                            X(q[0]);
                                            ApplyCNOTChain([q[5], q[3]]);
                                            IncByI(20, [q[1], q[2], q[3], q[9], q[10]]);
                                            CZ(q[8], q[1]);
                                        }
                                                __GenBlock_c6a02005(q);
                                    }
                                    
                                    __InlineIfElseDeadcode_f8278f84(q);
                            }
                            
                            operation __InlineIfElseDeadcode_cdb76474(q : Qubit[]) : Unit is Ctl {
                                use ctrl = Qubit();
                                within { } apply {
                                    // --- DEADCODE START ---
                                    Controlled __DeadBlock_4da5894a([ctrl], q);
                                    // --- DEADCODE END ---
                                }
                                    operation __InlineApplyIfRelationLE_3c848b02(q : Qubit[]) : Unit is Adj + Ctl {
                                        operation __IfBody_df08d78c(q : Qubit[]) : Unit is Adj + Ctl {
                                                    operation __GenBlock_517bebab(q : Qubit[]) : Unit is Adj + Ctl {
                                            
                                                Rz(5.073415, q[0]);
                                                SX(q[0]);
                                                IncByLUsingIncByLE(RippleCarryTTKIncByLE, IntAsBigInt(0), [q[0]]);
                                            }
                                                    __GenBlock_517bebab(q);
                                        }
                                        
                                        operation __ElseBody_df08d78c(q : Qubit[]) : Unit is Adj + Ctl {
                                                operation __ForLoopBody_84cb6411(q : Qubit[]) : Unit is Adj + Ctl {
                                                        operation __GenBlock_383cb48e(q : Qubit[]) : Unit is Adj + Ctl {
                                                
                                                    Exp([PauliY], 5.926709, [q[0]]);
                                                }
                                                        __GenBlock_383cb48e(q);
                                                }
                                                for i in 1..3 {
                                                    __ForLoopBody_84cb6411(q);
                                                }
                                        }
                                        
                                        if __RandomFlag_768041d7() {
                                            __IfBody_df08d78c(q);
                                        } else {
                                            __ElseBody_df08d78c(q);
                                        }
                                    }
                                    let x = [q[0], q[1], q[2]];
                                    let y = [q[3], q[5], q[6]];
                                    let target = [q[8]];
                                    ApplyIfGreaterLE(__InlineApplyIfRelationLE_3c848b02, x, y, target);
                            }
                            
                            __InlineIfElseDeadcode_cdb76474(q);
                    }
                    
                    __InlineIfElseDeadcode_3c94db14(q);
                // --- DEADCODE END ---
            }
        }
        
        __InlineIfElseDeadcode_71ce7cdc(q);
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj + Ctl {
        operation __ForLoopBody_0ff51398(q : Qubit[]) : Unit is Adj + Ctl {
            operation __ForLoopBody_df9024c8(q : Qubit[]) : Unit is Adj + Ctl {
                operation __InlineApplyIfRelationLE_5eabbfd1(q : Qubit[]) : Unit is Adj + Ctl {
                        operation __GenBlock_94bf5a6a(q : Qubit[]) : Unit is Adj + Ctl {
                
                    IncByL(IntAsBigInt(1), [q[1]]);
                    CNOT(q[1], q[0]);
                    Z(q[0]);
                    Ry(2.368628, q[1]);
                }
                        __GenBlock_94bf5a6a(q);
                }
                let x = [q[0], q[3], q[6]];
                let y = [q[1], q[2], q[7]];
                let target = [q[4], q[8]];
                ApplyIfGreaterOrEqualLE(__InlineApplyIfRelationLE_5eabbfd1, x, y, target);
            }
            for i in 1..3 {
                __ForLoopBody_df9024c8(q);
            }
        }
        for i in 1..3 {
            Controlled Adjoint __ForLoopBody_0ff51398([q[3], q[4]], [q[0], q[1], q[2], q[5], q[6], q[7], q[8], q[9], q[10]]);
        }
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Adj {
        operation __InlineApplyIfRelationL_a75ece1d(q : Qubit[]) : Unit is Adj + Ctl {
            // --- DEADCODE START ---
            let target = [q[0], q[1], q[2], q[3], q[4], q[5], q[6]]; 
            operation __InlineApplyIfRelation_dc29e28a(q : Qubit[]) : Unit is Adj + Ctl {
                operation __IfBody_d03b9073(q : Qubit[]) : Unit is Adj + Ctl {
                        operation __IfBody_b0985da2(q : Qubit[]) : Unit is Adj + Ctl {
                                operation __InlineIfElseDeadcode_9e1dcf9b(q : Qubit[]) : Unit is Adj + Ctl {
                                    if __RandomFlag_6740fb10() {
                                        // --- DEADCODE START ---
                                            operation __ControlledBody_c9d1a570(q : Qubit[]) : Unit is Adj + Ctl {
                                                operation __InlineApplyIfRelationL_efd1e3f9(q : Qubit[]) : Unit is Adj + Ctl {
                                                        operation __GenBlock_b230b045(q : Qubit[]) : Unit is Adj + Ctl {
                                                
                                                    
                                                }
                                                        __GenBlock_b230b045(q);
                                                }
                                                let x = [q[2], q[3], q[4]];
                                                let target = [q[0]];
                                                ApplyIfGreaterOrEqualL(__InlineApplyIfRelationL_efd1e3f9, 2L, x, target);
                                            }
                                            ApplyControlledOnInt(3, __ControlledBody_c9d1a570, [q[1], q[5]], [q[0], q[2], q[3], q[4], q[6]]);
                                        // --- DEADCODE END ---
                                    } else {
                                                operation __GenBlock_59ea8a74(q : Qubit[]) : Unit is Adj + Ctl {
                                        
                                            ApplyCNOTChain([q[5], q[3]]);
                                            Rxx(5.99331, q[4], q[2]);
                                        }
                                                Controlled Adjoint __GenBlock_59ea8a74([q[3]], [q[0], q[1], q[2], q[4], q[5], q[6]]);
                                    }
                                }
                                
                                __InlineIfElseDeadcode_9e1dcf9b(q);
                        }
                        
                        operation __ElseBody_b0985da2(q : Qubit[]) : Unit is Adj + Ctl {
                                // --- DEADCODE START ---
                                let target = [q[1], q[2], q[4], q[5], q[6]]; 
                                operation __InlineApplyIfRelation_34f02ef6(q : Qubit[]) : Unit is Adj + Ctl {
                                        operation __GenBlock_bbcc10fe(q : Qubit[]) : Unit is Adj + Ctl {
                                
                                    Ryy(3.321589, q[0], q[3]);
                                    SWAP(q[4], q[0]);
                                }
                                        __GenBlock_bbcc10fe(q);
                                }
                                use x = Qubit[2];
                                X(x[0]);
                                X(x[1]);
                                Controlled Adjoint ApplyIfGreaterOrEqualL([q[0], q[3]], (__InlineApplyIfRelation_34f02ef6, 0L, x, target));
                                X(x[0]);
                                X(x[1]);
                                // --- DEADCODE END ---
                        }
                        
                        if __RandomFlag_03e385b8() {
                            __IfBody_b0985da2(q);
                        } else {
                            __ElseBody_b0985da2(q);
                        }
                }
                
                operation __ElseBody_d03b9073(q : Qubit[]) : Unit is Adj + Ctl {
                        operation __ForLoopZeroBody_aa5b766f(q : Qubit[]) : Unit is Adj + Ctl {
                            operation __ControlledBody_e7e5c457(q : Qubit[]) : Unit is Adj + Ctl {
                                operation __IfBody_7f8314d6(q : Qubit[]) : Unit is Adj + Ctl {
                                            operation __GenBlock_6074ac81(q : Qubit[]) : Unit is Adj + Ctl {
                                    
                                        IncByIUsingIncByLE(RippleCarryTTKIncByLE, 0, [q[0], q[1], q[2]]);
                                    }
                                            Controlled Adjoint __GenBlock_6074ac81([q[0]], [q[1], q[2], q[3]]);
                                }
                                
                                operation __ElseBody_7f8314d6(q : Qubit[]) : Unit is Adj + Ctl {
                                            operation __GenBlock_928a290f(q : Qubit[]) : Unit is Adj + Ctl {
                                    
                                        IncByI(3, [q[0], q[1], q[3]]);
                                    }
                                            __GenBlock_928a290f(q);
                                }
                                
                                if __RandomFlag_e97d814a() {
                                    __IfBody_7f8314d6(q);
                                } else {
                                    __ElseBody_7f8314d6(q);
                                }
                            }
                            ApplyControlledOnInt(0, __ControlledBody_e7e5c457, [q[3]], [q[0], q[1], q[2], q[4]]);
                        }
                        // --- DEADCODE START ---
                        for i in 1..0 {
                            Controlled Adjoint __ForLoopZeroBody_aa5b766f([q[0], q[3]], [q[1], q[2], q[4], q[5], q[6]]);
                        }
                        // --- DEADCODE END ---
                }
                
                if __RandomFlag_433e9b10() {
                    __IfBody_d03b9073(q);
                } else {
                    __ElseBody_d03b9073(q);
                }
            }
            use x = Qubit[2];
            X(x[1]);
            use y = Qubit[2];
            X(y[0]);
            Controlled Adjoint ApplyIfLessLE([q[7]], (__InlineApplyIfRelation_dc29e28a, x, y, target));
            X(x[1]);
            X(y[0]);
            // --- DEADCODE END ---
        }
        let x = [q[0], q[5], q[6]];
        let target = [q[1], q[2], q[4], q[7], q[8], q[9], q[10], q[11]];
        ApplyIfGreaterL(__InlineApplyIfRelationL_a75ece1d, 5L, x, target);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            X(q[1]);
            Controlled ApplyRandomBlock0([q[1]], [q[0], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9], q[10], q[11]]);
            X(q[1]);
            Controlled Adjoint ApplyRandomBlock1([q[4]], [q[0], q[1], q[2], q[3], q[5], q[6], q[7], q[8], q[9], q[10], q[11]]);
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