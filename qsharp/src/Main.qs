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



function __RandomFlag_f88c38ab() : Bool {
    let b0 = ResultAsBool(One);
    let b1 = not ResultAsBool(One);
    let b2 = not ResultAsBool(One);
    let b3 = ResultAsBool(One);
    return Xor(Xor(b0, b1), Xor(b2, b3));
}



    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Ctl {
        operation __ForLoopZeroBody_0656de08(q : Qubit[]) : Unit is Ctl {
            // --- DEADCODE START ---
            let target = q; 
            operation __InlineApplyIfRelation_26e32bfa(q : Qubit[]) : Unit is Adj + Ctl {
                operation __InlineApplyIfRelationLE_7c0a8d7f(q : Qubit[]) : Unit is Adj + Ctl {
                        operation __GenBlock_bbf67071(q : Qubit[]) : Unit is Adj + Ctl {
                
                    SX(q[0]);
                    ApplyPauli([PauliY], [q[0]]);
                    S(q[0]);
                    X(q[0]);
                    Exp([PauliY], 5.641287, [q[0]]);
                    let n = 1;
                ApplyPauliFromInt(PauliZ, true, n, [q[0]]);
                ApplyPauliFromInt(PauliY, false, n, [q[0]]);
                }
                        __GenBlock_bbf67071(q);
                }
                let x = [q[1], q[2]];
                let y = [q[0], q[3]];
                let target = [q[4]];
                ApplyIfLessOrEqualLE(__InlineApplyIfRelationLE_7c0a8d7f, x, y, target);
            }
            use x = Qubit[2];
            X(x[0]);
            X(x[1]);
            ApplyIfGreaterL(__InlineApplyIfRelation_26e32bfa, 0L, x, target);
            X(x[0]);
            X(x[1]);
            // --- DEADCODE END ---
        }
        // --- DEADCODE START ---
        for i in 1..0 {
            Controlled __ForLoopZeroBody_0656de08([q[1], q[2], q[4], q[8]], [q[0], q[3], q[5], q[6], q[7]]);
        }
        // --- DEADCODE END ---
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj {
        operation __InlineApplyIfRelationL_11783b42(q : Qubit[]) : Unit is Adj + Ctl {
            operation __InlineApplyIfRelationL_851045c6(q : Qubit[]) : Unit is Adj + Ctl {
                operation __ForLoopZeroBody_c60551d4(q : Qubit[]) : Unit is Adj + Ctl {
                    operation __DeadBlock_9b7217a9(q : Qubit[]) : Unit is Adj + Ctl {
                            operation __IfBody_2f2f9822(q : Qubit[]) : Unit is Adj + Ctl {
                                        operation __GenBlock_d489779c(q : Qubit[]) : Unit is Adj + Ctl {
                                
                                    ApplyCNOTChain([q[0]]);
                                    ApplyCNOTChain([q[0]]);
                                    IncByI(1, [q[0]]);
                                }
                                        __GenBlock_d489779c(q);
                            }
                            
                            operation __ElseBody_2f2f9822(q : Qubit[]) : Unit is Adj + Ctl {
                                        operation __GenBlock_4e3d7d43(q : Qubit[]) : Unit is Adj + Ctl {
                                
                                    ApplyQFT(q);
                                    ApplyPauli([PauliZ], [q[0]]);
                                    SX(q[0]);
                                }
                                        __GenBlock_4e3d7d43(q);
                            }
                            
                            if __RandomFlag_f88c38ab() {
                                __IfBody_2f2f9822(q);
                            } else {
                                __ElseBody_2f2f9822(q);
                            }
                    }
                    
                    operation __InlineIfElseDeadcode_8a0b4a59(q : Qubit[]) : Unit is Adj + Ctl {
                        use ctrl = Qubit();
                        within { } apply {
                            // --- DEADCODE START ---
                            Controlled __DeadBlock_9b7217a9([ctrl], q);
                            // --- DEADCODE END ---
                        }
                            // --- DEADCODE START ---
                            let target = q; 
                            operation __InlineApplyIfRelation_4e694c39(q : Qubit[]) : Unit is Adj + Ctl {
                                    operation __GenBlock_47ee12aa(q : Qubit[]) : Unit is Adj + Ctl {
                            
                                Z(q[0]);
                                ApplyPauli([PauliZ], [q[0]]);
                                H(q[0]);
                                Z(q[0]);
                            }
                                    __GenBlock_47ee12aa(q);
                            }
                            use x = Qubit[2];
                            X(x[0]);
                            X(x[1]);
                            ApplyIfGreaterOrEqualL(__InlineApplyIfRelation_4e694c39, 0L, x, target);
                            X(x[0]);
                            X(x[1]);
                            // --- DEADCODE END ---
                    }
                    
                    __InlineIfElseDeadcode_8a0b4a59(q);
                }
                // --- DEADCODE START ---
                for i in 1..0 {
                    __ForLoopZeroBody_c60551d4(q);
                }
                // --- DEADCODE END ---
            }
            let x = [q[1]];
            let target = [q[0]];
            ApplyIfLessOrEqualL(__InlineApplyIfRelationL_851045c6, 1L, x, target);
        }
        let x = [q[1], q[3], q[6]];
        let target = [q[4], q[10]];
        ApplyIfEqualL(__InlineApplyIfRelationL_11783b42, 6L, x, target);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit {
        operation __InlineApplyIfRelationLE_242b200f(q : Qubit[]) : Unit is Adj + Ctl {
                operation __GenBlock_0e45e6a2(q : Qubit[]) : Unit is Adj + Ctl {
        
            SWAP(q[0], q[4]);
            Rz(1.075059, q[4]);
            SX(q[1]);
            IncByLUsingIncByLE(RippleCarryTTKIncByLE, IntAsBigInt(6), [q[0], q[1], q[4]]);
            CZ(q[0], q[2]);
            Ry(0.450974, q[0]);
            Rz(5.024861, q[1]);
            H(q[4]);
        }
                __GenBlock_0e45e6a2(q);
        }
        let x = [q[2], q[5], q[7]];
        let y = [q[0], q[3], q[4]];
        let target = [q[1], q[6], q[8], q[9], q[10]];
        ApplyIfGreaterOrEqualLE(__InlineApplyIfRelationLE_242b200f, x, y, target);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            Controlled ApplyRandomBlock0([q[5], q[7], q[10]], [q[0], q[1], q[2], q[3], q[4], q[6], q[8], q[9], q[11]]);
            Adjoint ApplyRandomBlock1(q);
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