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



function __RandomFlag_ee01e536() : Bool {
    let b0 = false;
    let b1 = not true;
    let b2 = false;
    let b3 = not true;
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_6fb1d2f5() : Bool {
    let b0 = not true;
    let b1 = not false;
    let b2 = not false;
    let b3 = true;
    return Xor(Xor(b0, b1), Xor(b2, b3));
}
function __RandomFlag_7aaa23c7() : Bool {
    let b0 = not ResultAsBool(One);
    let b1 = ResultAsBool(One);
    let b2 = ResultAsBool(One);
    let b3 = ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}



    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Adj + Ctl {
        operation __InlineIfElseDeadcode_55c1ef67(q : Qubit[]) : Unit is Adj + Ctl {
            if __RandomFlag_7aaa23c7() {
                        operation __GenBlock_752a5948(q : Qubit[]) : Unit is Adj + Ctl {
                
                    IncByLEUsingAddLE(LookAheadDKRSAddLE, RippleCarryCGAddLE, [q[2], q[3]], [q[1], q[4]]);
                    ApplyQFT(q);
                    RippleCarryTTKIncByLE([q[4]], [q[2]]);
                    X(q[1]);
                    CCNOT(q[1], q[4], q[0]);
                    FourierTDIncByLE([q[1], q[3]], [q[2], q[5]]);
                    R1(3.28589, q[4]);
                    I(q[0]);
                }
                        __GenBlock_752a5948(q);
            } else {
                // --- DEADCODE START ---
                    operation __InlineApplyIfRelationLE_7e1406e0(q : Qubit[]) : Unit is Adj + Ctl {
                        operation __DeadBlock_1e2b8744(q : Qubit[]) : Unit is Adj + Ctl {
                                operation __InlineIfElseDeadcode_d2973fa2(q : Qubit[]) : Unit is Adj + Ctl {
                                    if __RandomFlag_6fb1d2f5() {
                                            operation __DeadBlock_50f171cf(q : Qubit[]) : Unit is Adj + Ctl {
                                                    // --- DEADCODE START ---
                                                    let target = [q[0]]; 
                                                    operation __InlineApplyIfRelation_2c3fd383(q : Qubit[]) : Unit is Adj + Ctl {
                                                        operation __ForLoopZeroBody_cece7827(q : Qubit[]) : Unit is Adj + Ctl {
                                                                operation __GenBlock_a709f804(q : Qubit[]) : Unit is Adj + Ctl {
                                                        
                                                            ApplyCNOTChain([q[0]]);
                                                        }
                                                                __GenBlock_a709f804(q);
                                                        }
                                                        // --- DEADCODE START ---
                                                        for i in 1..0 {
                                                            __ForLoopZeroBody_cece7827(q);
                                                        }
                                                        // --- DEADCODE END ---
                                                    }
                                                    use x = Qubit[2];
                                                    X(x[0]);
                                                    X(x[1]);
                                                    Controlled Adjoint ApplyIfEqualL([q[1]], (__InlineApplyIfRelation_2c3fd383, 0L, x, target));
                                                    X(x[0]);
                                                    X(x[1]);
                                                    // --- DEADCODE END ---
                                            }
                                            
                                            operation __InlineIfElseDeadcode_33bec301(q : Qubit[]) : Unit is Adj + Ctl {
                                                use ctrl = Qubit();
                                                within { } apply {
                                                    // --- DEADCODE START ---
                                                    Controlled __DeadBlock_50f171cf([ctrl], q);
                                                    // --- DEADCODE END ---
                                                }
                                                    operation __ControlledBody_bb266901(q : Qubit[]) : Unit is Adj + Ctl {
                                                            operation __GenBlock_b40acd54(q : Qubit[]) : Unit is Adj + Ctl {
                                                    
                                                        ApplyCNOTChain([q[0]]);
                                                    }
                                                            __GenBlock_b40acd54(q);
                                                    }
                                                    ApplyControlledOnBitString([false], __ControlledBody_bb266901, [q[1]], [q[0]]);
                                                    operation __GenBlock_f273f4e4(q : Qubit[]) : Unit is Adj + Ctl {
                                                
                                                    Rxx(1.125265, q[1], q[0]);
                                                }
                                                    __GenBlock_f273f4e4(q);
                                            }
                                            
                                            __InlineIfElseDeadcode_33bec301(q);
                                    } else {
                                        // --- DEADCODE START ---
                                            operation __InlineApplyIfRelationL_e3e2198b(q : Qubit[]) : Unit is Adj + Ctl {
                                                operation __ForLoopZeroBody_1b257052(q : Qubit[]) : Unit is Adj + Ctl {
                                                        operation __GenBlock_4f4e1f81(q : Qubit[]) : Unit is Adj + Ctl {
                                                
                                                    Y(q[0]);
                                                }
                                                        __GenBlock_4f4e1f81(q);
                                                }
                                                // --- DEADCODE START ---
                                                for i in 1..0 {
                                                    __ForLoopZeroBody_1b257052(q);
                                                }
                                                // --- DEADCODE END ---
                                            }
                                            let x = [q[1]];
                                            let target = [q[0]];
                                            ApplyIfGreaterOrEqualL(__InlineApplyIfRelationL_e3e2198b, 1L, x, target);
                                            operation __GenBlock_b865dfe8(q : Qubit[]) : Unit is Adj + Ctl {
                                        
                                            IncByL(IntAsBigInt(0), [q[0]]);
                                        }
                                            Controlled Adjoint __GenBlock_b865dfe8([q[1]], [q[0]]);
                                        // --- DEADCODE END ---
                                    }
                                }
                                
                                __InlineIfElseDeadcode_d2973fa2(q);
                        }
                        
                        operation __InlineIfElseDeadcode_afa72cd8(q : Qubit[]) : Unit is Adj + Ctl {
                            use ctrl = Qubit();
                            within { } apply {
                                // --- DEADCODE START ---
                                Controlled __DeadBlock_1e2b8744([ctrl], q);
                                // --- DEADCODE END ---
                            }
                                operation __InlineApplyIfRelationL_73a7de82(q : Qubit[]) : Unit is Adj + Ctl {
                                    operation __ForLoopBody_b1b3f17a(q : Qubit[]) : Unit is Adj + Ctl {
                                            operation __GenBlock_52d2a9ff(q : Qubit[]) : Unit is Adj + Ctl {
                                    
                                        IncByLUsingIncByLE(RippleCarryTTKIncByLE, IntAsBigInt(0), [q[0]]);
                                    }
                                            __GenBlock_52d2a9ff(q);
                                    }
                                    for i in 1..3 {
                                        __ForLoopBody_b1b3f17a(q);
                                    }
                                    operation __GenBlock_225b1671(q : Qubit[]) : Unit is Adj + Ctl {
                                
                                    I(q[0]);
                                }
                                    __GenBlock_225b1671(q);
                                }
                                let x = [q[1]];
                                let target = [q[0]];
                                ApplyIfEqualL(__InlineApplyIfRelationL_73a7de82, 0L, x, target);
                                operation __GenBlock_aea7fbb4(q : Qubit[]) : Unit is Adj + Ctl {
                            
                                H(q[1]);
                            }
                                __GenBlock_aea7fbb4(q);
                        }
                        
                        __InlineIfElseDeadcode_afa72cd8(q);
                    }
                    let x = [q[0], q[2]];
                    let y = [q[1], q[4]];
                    let target = [q[3], q[5]];
                    ApplyIfGreaterOrEqualLE(__InlineApplyIfRelationLE_7e1406e0, x, y, target);
                    operation __GenBlock_20512e41(q : Qubit[]) : Unit is Adj + Ctl {
                
                    CZ(q[3], q[4]);
                    Ry(5.574094, q[0]);
                }
                    Controlled Adjoint __GenBlock_20512e41([q[4]], [q[0], q[1], q[2], q[3], q[5]]);
                // --- DEADCODE END ---
            }
        }
        
        __InlineIfElseDeadcode_55c1ef67(q);
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj + Ctl {
        operation __InlineApplyIfRelationL_2c7a76cc(q : Qubit[]) : Unit is Adj + Ctl {
                operation __GenBlock_ce750fc3(q : Qubit[]) : Unit is Adj + Ctl {
        
            let n = 2;
        ApplyPauliFromInt(PauliY, true, n, [q[0], q[1], q[2]]);
        ApplyPauliFromInt(PauliX, false, n, [q[0], q[1], q[2]]);
            Z(q[2]);
            Ry(5.466971, q[2]);
            SWAP(q[0], q[2]);
            T(q[2]);
            IncByIUsingIncByLE(RippleCarryTTKIncByLE, 6, [q[0], q[1], q[2]]);
            ApplyP(PauliX, q[0]);
        }
                Controlled Adjoint __GenBlock_ce750fc3([q[3]], [q[0], q[1], q[2]]);
        }
        let x = [q[1], q[3]];
        let target = [q[0], q[2], q[5], q[6]];
        ApplyIfGreaterL(__InlineApplyIfRelationL_2c7a76cc, 2L, x, target);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit {
        operation __ControlledBody_4e4f50db(q : Qubit[]) : Unit is Adj + Ctl {
            operation __ControlledBody_825d0f9a(q : Qubit[]) : Unit is Adj + Ctl {
                operation __ForLoopBody_0e6ad8cb(q : Qubit[]) : Unit is Adj + Ctl {
                    operation __ForLoopBody_d8571a0a(q : Qubit[]) : Unit is Adj + Ctl {
                            operation __GenBlock_3a8a7ef5(q : Qubit[]) : Unit is Adj + Ctl {
                    
                        RFrac(PauliY, 6, 7, q[0]);
                    }
                            Controlled Adjoint __GenBlock_3a8a7ef5([q[0]], [q[1], q[2]]);
                    }
                    for i in 1..3 {
                        Controlled Adjoint __ForLoopBody_d8571a0a([q[2], q[3]], [q[0], q[1], q[4]]);
                    }
                    operation __GenBlock_4566fb33(q : Qubit[]) : Unit is Adj + Ctl {
                
                    Y(q[2]);
                }
                    Controlled Adjoint __GenBlock_4566fb33([q[3]], [q[0], q[1], q[2], q[4]]);
                }
                for i in 1..3 {
                    Controlled Adjoint __ForLoopBody_0e6ad8cb([q[1]], [q[0], q[2], q[3], q[4], q[5]]);
                }
                operation __GenBlock_5f5e131e(q : Qubit[]) : Unit is Adj + Ctl {
            
                Exp([PauliZ, PauliX, PauliY], 2.47021, [q[2], q[0], q[1]]);
            }
                Controlled Adjoint __GenBlock_5f5e131e([q[1], q[2], q[4]], [q[0], q[3], q[5]]);
            }
            ApplyControlledOnInt(1, __ControlledBody_825d0f9a, [q[2]], [q[0], q[1], q[3], q[4], q[5], q[6]]);
            operation __GenBlock_f96a7148(q : Qubit[]) : Unit is Adj + Ctl {
        
            Rz(2.70431, q[5]);
            CZ(q[0], q[2]);
        }
            __GenBlock_f96a7148(q);
        }
        ApplyControlledOnBitString([true], __ControlledBody_4e4f50db, [q[5]], [q[0], q[1], q[2], q[3], q[4], q[6], q[7]]);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[8] {
            X(q[1]);
            X(q[4]);
            X(q[7]);
            Controlled Adjoint ApplyRandomBlock0([q[1], q[7]], [q[0], q[2], q[3], q[4], q[5], q[6]]);
            Controlled Adjoint ApplyRandomBlock1([q[4]], [q[0], q[1], q[2], q[3], q[5], q[6], q[7]]);
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