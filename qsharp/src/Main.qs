namespace Main {

    open Std.Arithmetic;
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Math;
    open Std.Measurement;
    open Std.StatePreparation;

    operation MySingleBlock_61b8ed47(q : Qubit) : Unit is Adj + Ctl {
        I(q);
        H(q);
    }
    operation MySingleBlock_d0e5b5ce(q : Qubit) : Unit is Adj + Ctl {
        Z(q);
        X(q);
        Ry(4.815127, q);
    }
    operation MySingleBlock_96a2f43b(q : Qubit) : Unit is Adj + Ctl {
        I(q);
        X(q);
    }
    operation MySingleBlock_a0212a57(q : Qubit) : Unit is Adj + Ctl {
        R1(5.647057, q);
        H(q);
        X(q);
        T(q);
    }
    operation MySingleBlock_327fb10d(q : Qubit) : Unit is Adj + Ctl {
        T(q);
        Y(q);
        Rz(5.990739, q);
        T(q);
    }

function __RandomFlag_2abe4308() : Bool {
    let b0 = ResultAsBool(Zero);
    let b1 = not ResultAsBool(Zero);
    let b2 = ResultAsBool(One);
    let b3 = ResultAsBool(One);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_6b965fbd() : Bool {
    let b0 = not ResultAsBool(Zero);
    let b1 = not ResultAsBool(Zero);
    let b2 = ResultAsBool(One);
    let b3 = not ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_8448b1f3() : Bool {
    let b0 = ResultAsBool(Zero);
    let b1 = ResultAsBool(Zero);
    let b2 = ResultAsBool(Zero);
    let b3 = not ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_aa011093() : Bool {
    let b0 = ResultAsBool(One);
    let b1 = not ResultAsBool(One);
    let b2 = ResultAsBool(Zero);
    let b3 = not ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_d954b003() : Bool {
    let b0 = not ResultAsBool(Zero);
    let b1 = ResultAsBool(One);
    let b2 = ResultAsBool(One);
    let b3 = not ResultAsBool(One);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_cb7523f6() : Bool {
    let b0 = not ResultAsBool(Zero);
    let b1 = ResultAsBool(One);
    let b2 = ResultAsBool(One);
    let b3 = not ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_c6e6fe94() : Bool {
    let b0 = ResultAsBool(One);
    let b1 = ResultAsBool(Zero);
    let b2 = ResultAsBool(Zero);
    let b3 = not ResultAsBool(One);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_327ff316() : Bool {
    let b0 = not ResultAsBool(One);
    let b1 = ResultAsBool(Zero);
    let b2 = ResultAsBool(Zero);
    let b3 = ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_cde47b72() : Bool {
    let b0 = ResultAsBool(Zero);
    let b1 = not ResultAsBool(Zero);
    let b2 = not ResultAsBool(Zero);
    let b3 = ResultAsBool(One);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_9c942f7e() : Bool {
    let b0 = not ResultAsBool(One);
    let b1 = not ResultAsBool(One);
    let b2 = ResultAsBool(One);
    let b3 = not ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_dbff1b93() : Bool {
    let b0 = not ResultAsBool(One);
    let b1 = not ResultAsBool(One);
    let b2 = not ResultAsBool(Zero);
    let b3 = not ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_6d547bd4() : Bool {
    let b0 = not ResultAsBool(One);
    let b1 = ResultAsBool(Zero);
    let b2 = ResultAsBool(One);
    let b3 = ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_f5d92fff() : Bool {
    let b0 = ResultAsBool(One);
    let b1 = ResultAsBool(One);
    let b2 = not ResultAsBool(One);
    let b3 = ResultAsBool(One);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_1df1d2f6() : Bool {
    let b0 = not ResultAsBool(One);
    let b1 = ResultAsBool(Zero);
    let b2 = not ResultAsBool(One);
    let b3 = not ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_78cfa5b2() : Bool {
    let b0 = ResultAsBool(Zero);
    let b1 = not ResultAsBool(One);
    let b2 = ResultAsBool(One);
    let b3 = ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_477e2483() : Bool {
    let b0 = not ResultAsBool(One);
    let b1 = ResultAsBool(One);
    let b2 = ResultAsBool(One);
    let b3 = ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_a4846af1() : Bool {
    let b0 = ResultAsBool(One);
    let b1 = ResultAsBool(Zero);
    let b2 = not ResultAsBool(Zero);
    let b3 = ResultAsBool(One);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_5509f8e1() : Bool {
    let b0 = ResultAsBool(Zero);
    let b1 = ResultAsBool(One);
    let b2 = not ResultAsBool(Zero);
    let b3 = ResultAsBool(One);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_820e31bb() : Bool {
    let b0 = not ResultAsBool(Zero);
    let b1 = ResultAsBool(One);
    let b2 = ResultAsBool(Zero);
    let b3 = ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_2974df1d() : Bool {
    let b0 = not ResultAsBool(Zero);
    let b1 = not ResultAsBool(One);
    let b2 = ResultAsBool(Zero);
    let b3 = not ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_e78e5e12() : Bool {
    let b0 = not ResultAsBool(Zero);
    let b1 = ResultAsBool(Zero);
    let b2 = ResultAsBool(One);
    let b3 = not ResultAsBool(One);
    return (b0 and b1) or (b2 and not b3);
}

    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Ctl {
        operation __InlineIfElseDeadcode_2ac507b8(q : Qubit[]) : Unit is Ctl {
            if __RandomFlag_cb7523f6() {
                    operation __IfBody_222e960e(q : Qubit[]) : Unit is Ctl {
                            operation __InlineApplyIfRelationL_8bbb82c7(q : Qubit[]) : Unit is Adj + Ctl {
                                    ApplyQFT(q);
                                    Rz(0.36701, q[0]);
                                    Rx(2.511567, q[0]);
                                    ApproximatelyPreparePureStateCP(
                                1e-6,
                                [
                                    ComplexPolar(0.780207, 0.450584),
                                    ComplexPolar(0.625522, 6.041097)
                                ],
                                q
                            );
                            }
                            let x = [q[0], q[5], q[6]];
                            let target = [q[4]];
                            ApplyIfLessL(__InlineApplyIfRelationL_8bbb82c7, 4L, x, target);
                    }
                    
                    operation __ElseBody_222e960e(q : Qubit[]) : Unit is Ctl {
                            operation __IfBody_372f6b28(q : Qubit[]) : Unit is Ctl {
                                    operation __InlineApplyIfRelationL_9e3913b8(q : Qubit[]) : Unit is Adj + Ctl {
                                        operation __InlineApplyIfRelationLE_dc1190b4(q : Qubit[]) : Unit is Adj + Ctl {
                                            operation __ForLoopBody_009a067b(q : Qubit[]) : Unit is Adj + Ctl {
                                                    I(q[0]);
                                                    Y(q[0]);
                                                    ApproximatelyPreparePureStateCP(
                                                1e-6,
                                                [
                                                    ComplexPolar(0.842177, 2.358967),
                                                    ComplexPolar(0.539201, 3.575745)
                                                ],
                                                q
                                            );
                                                    ApproximatelyPreparePureStateCP(
                                                1e-6,
                                                [
                                                    ComplexPolar(0.68532, 6.202818),
                                                    ComplexPolar(0.728242, 4.626518)
                                                ],
                                                q
                                            );
                                            }
                                            for i in 1..3 {
                                                __ForLoopBody_009a067b(q);
                                            }
                                        }
                                        let x = [q[1]];
                                        let y = [q[2]];
                                        let target = [q[0]];
                                        ApplyIfLessOrEqualLE(__InlineApplyIfRelationLE_dc1190b4, x, y, target);
                                    }
                                    let x = [q[1], q[2], q[5]];
                                    let target = [q[0], q[3], q[6]];
                                    ApplyIfGreaterL(__InlineApplyIfRelationL_9e3913b8, 4L, x, target);
                            }
                            
                            operation __ElseBody_372f6b28(q : Qubit[]) : Unit is Ctl {
                                    operation __InlineApplyIfRelationLE_f04c84a3(q : Qubit[]) : Unit is Adj + Ctl {
                                        operation __InlineApplyIfRelationL_af5e19a1(q : Qubit[]) : Unit is Adj + Ctl {
                                            operation __IfBody_d86ab2bf(q : Qubit[]) : Unit is Adj + Ctl {
                                                        ApplyToEachCA(MySingleBlock_d0e5b5ce, q);
                                                        H(q[0]);
                                            }
                                            
                                            operation __ElseBody_d86ab2bf(q : Qubit[]) : Unit is Adj + Ctl {
                                                    operation __ForLoopBody_f848165a(q : Qubit[]) : Unit is Adj + Ctl {
                                                        operation __IfBody_6e8bb946(q : Qubit[]) : Unit is Adj + Ctl {
                                                                operation __IfBody_665ab3a5(q : Qubit[]) : Unit is Adj + Ctl {
                                                                        operation __ForLoopBody_b0f96a42(q : Qubit[]) : Unit is Adj + Ctl {
                                                                                Y(q[0]);
                                                                        }
                                                                        for i in 1..3 {
                                                                            __ForLoopBody_b0f96a42(q);
                                                                        }
                                                                }
                                                                
                                                                operation __ElseBody_665ab3a5(q : Qubit[]) : Unit is Adj + Ctl {
                                                                            I(q[0]);
                                                                }
                                                                
                                                                if __RandomFlag_2abe4308() {
                                                                    __IfBody_665ab3a5(q);
                                                                } else {
                                                                    __ElseBody_665ab3a5(q);
                                                                }
                                                        }
                                                        
                                                        operation __ElseBody_6e8bb946(q : Qubit[]) : Unit is Adj + Ctl {
                                                                    ApproximatelyPreparePureStateCP(
                                                                1e-6,
                                                                [
                                                                    ComplexPolar(0.653871, 2.639653),
                                                                    ComplexPolar(0.756606, 1.310191)
                                                                ],
                                                                q
                                                            );
                                                                    S(q[0]);
                                                                    T(q[0]);
                                                        }
                                                        
                                                        if __RandomFlag_6b965fbd() {
                                                            __IfBody_6e8bb946(q);
                                                        } else {
                                                            __ElseBody_6e8bb946(q);
                                                        }
                                                    }
                                                    for i in 1..3 {
                                                        __ForLoopBody_f848165a(q);
                                                    }
                                            }
                                            
                                            if __RandomFlag_8448b1f3() {
                                                __IfBody_d86ab2bf(q);
                                            } else {
                                                __ElseBody_d86ab2bf(q);
                                            }
                                        }
                                        let x = [q[1]];
                                        let target = [q[0]];
                                        ApplyIfEqualL(__InlineApplyIfRelationL_af5e19a1, 1L, x, target);
                                    }
                                    let x = [q[2], q[6]];
                                    let y = [q[0], q[4]];
                                    let target = [q[3], q[5]];
                                    ApplyIfEqualLE(__InlineApplyIfRelationLE_f04c84a3, x, y, target);
                            }
                            
                            if __RandomFlag_aa011093() {
                                __IfBody_372f6b28(q);
                            } else {
                                __ElseBody_372f6b28(q);
                            }
                    }
                    
                    if __RandomFlag_d954b003() {
                        __IfBody_222e960e(q);
                    } else {
                        __ElseBody_222e960e(q);
                    }
            } else {
                // --- DEADCODE START ---
                    operation __InlineApplyIfRelationL_d5050e56(q : Qubit[]) : Unit is Adj + Ctl {
                            T(q[0]);
                            ApplyToEachCA(MySingleBlock_61b8ed47, q);
                            Rz(1.43805, q[0]);
                            R1(3.084198, q[0]);
                            S(q[0]);
                    }
                    let x = [q[2]];
                    let target = [q[5]];
                    ApplyIfGreaterL(__InlineApplyIfRelationL_d5050e56, 1L, x, target);
                // --- DEADCODE END ---
            }
        }
        
        __InlineIfElseDeadcode_2ac507b8(q);
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj {
        operation __ForLoopBody_c6e9d146(q : Qubit[]) : Unit is Adj {
            operation __IfBody_fbb8b005(q : Qubit[]) : Unit is Adj {
                    operation __InlineApplyIfRelationLE_e681060e(q : Qubit[]) : Unit is Adj + Ctl {
                        operation __InlineApplyIfRelationL_e7c8d2ce(q : Qubit[]) : Unit is Adj + Ctl {
                            operation __InlineApplyIfRelationLE_683799cd(q : Qubit[]) : Unit is Adj + Ctl {
                                operation __ForLoopBody_c21c1403(q : Qubit[]) : Unit is Adj + Ctl {
                                    operation __IfBody_45554479(q : Qubit[]) : Unit is Adj + Ctl {
                                            operation __ForLoopBody_750cdffe(q : Qubit[]) : Unit is Adj + Ctl {
                                                operation __IfBody_ba45590b(q : Qubit[]) : Unit is Adj + Ctl {
                                                        operation __IfBody_7a763976(q : Qubit[]) : Unit is Adj + Ctl {
                                                                    Z(q[0]);
                                                        }
                                                        
                                                        operation __ElseBody_7a763976(q : Qubit[]) : Unit is Adj + Ctl {
                                                                    T(q[0]);
                                                        }
                                                        
                                                        if __RandomFlag_c6e6fe94() {
                                                            __IfBody_7a763976(q);
                                                        } else {
                                                            __ElseBody_7a763976(q);
                                                        }
                                                }
                                                
                                                operation __ElseBody_ba45590b(q : Qubit[]) : Unit is Adj + Ctl {
                                                        operation __ForLoopBody_cea43638(q : Qubit[]) : Unit is Adj + Ctl {
                                                                ApplyQFT(q);
                                                        }
                                                        for i in 1..3 {
                                                            __ForLoopBody_cea43638(q);
                                                        }
                                                }
                                                
                                                if __RandomFlag_327ff316() {
                                                    __IfBody_ba45590b(q);
                                                } else {
                                                    __ElseBody_ba45590b(q);
                                                }
                                            }
                                            for i in 1..3 {
                                                __ForLoopBody_750cdffe(q);
                                            }
                                    }
                                    
                                    operation __ElseBody_45554479(q : Qubit[]) : Unit is Adj + Ctl {
                                            operation __ForLoopBody_fc0238c7(q : Qubit[]) : Unit is Adj + Ctl {
                                                    X(q[0]);
                                                    T(q[0]);
                                            }
                                            for i in 1..3 {
                                                __ForLoopBody_fc0238c7(q);
                                            }
                                    }
                                    
                                    if __RandomFlag_cde47b72() {
                                        __IfBody_45554479(q);
                                    } else {
                                        __ElseBody_45554479(q);
                                    }
                                }
                                for i in 1..3 {
                                    __ForLoopBody_c21c1403(q);
                                }
                            }
                            let x = [q[1]];
                            let y = [q[0]];
                            let target = [q[3]];
                            ApplyIfGreaterOrEqualLE(__InlineApplyIfRelationLE_683799cd, x, y, target);
                        }
                        let x = [q[2]];
                        let target = [q[0], q[1], q[3], q[5]];
                        ApplyIfEqualL(__InlineApplyIfRelationL_e7c8d2ce, 0L, x, target);
                    }
                    let x = [q[0], q[3], q[11]];
                    let y = [q[6], q[7], q[10]];
                    let target = [q[1], q[2], q[4], q[5], q[8], q[9]];
                    ApplyIfGreaterLE(__InlineApplyIfRelationLE_e681060e, x, y, target);
            }
            
            operation __ElseBody_fbb8b005(q : Qubit[]) : Unit is Adj {
                    operation __IfBody_96b6cd84(q : Qubit[]) : Unit is Adj {
                            operation __InlineApplyIfRelationL_6207b61d(q : Qubit[]) : Unit is Adj + Ctl {
                                operation __InlineApplyIfRelationLE_294c212a(q : Qubit[]) : Unit is Adj + Ctl {
                                    operation __IfBody_519b3f8f(q : Qubit[]) : Unit is Adj + Ctl {
                                            operation __ForLoopBody_68263ee0(q : Qubit[]) : Unit is Adj + Ctl {
                                                    I(q[0]);
                                                    Rx(5.351459, q[0]);
                                                    SWAP(q[0], q[1]);
                                            }
                                            for i in 1..3 {
                                                Controlled Adjoint __ForLoopBody_68263ee0([q[0], q[2]], [q[1], q[3]]);
                                            }
                                    }
                                    
                                    operation __ElseBody_519b3f8f(q : Qubit[]) : Unit is Adj + Ctl {
                                            operation __ForLoopBody_b9ac159e(q : Qubit[]) : Unit is Adj + Ctl {
                                                operation __InlineApplyIfRelationL_1d6afe24(q : Qubit[]) : Unit is Adj + Ctl {
                                                    operation __ForLoopBody_9c179b4a(q : Qubit[]) : Unit is Adj + Ctl {
                                                    
                                                    }
                                                    for i in 1..3 {
                                                        __ForLoopBody_9c179b4a(q);
                                                    }
                                                }
                                                let x = [q[0], q[2], q[3]];
                                                let target = [q[1]];
                                                ApplyIfEqualL(__InlineApplyIfRelationL_1d6afe24, 1L, x, target);
                                            }
                                            for i in 1..3 {
                                                __ForLoopBody_b9ac159e(q);
                                            }
                                    }
                                    
                                    if __RandomFlag_9c942f7e() {
                                        __IfBody_519b3f8f(q);
                                    } else {
                                        __ElseBody_519b3f8f(q);
                                    }
                                }
                                let x = [q[5]];
                                let y = [q[1]];
                                let target = [q[0], q[2], q[3], q[4]];
                                ApplyIfGreaterLE(__InlineApplyIfRelationLE_294c212a, x, y, target);
                            }
                            let x = [q[11]];
                            let target = [q[0], q[3], q[6], q[8], q[9], q[10]];
                            ApplyIfGreaterL(__InlineApplyIfRelationL_6207b61d, 0L, x, target);
                    }
                    
                    operation __ElseBody_96b6cd84(q : Qubit[]) : Unit is Adj {
                            operation __InlineApplyIfRelationLE_f3f55857(q : Qubit[]) : Unit is Adj + Ctl {
                                operation __ForLoopBody_987f002a(q : Qubit[]) : Unit is Adj + Ctl {
                                    operation __InlineApplyIfRelationLE_629a11d2(q : Qubit[]) : Unit is Adj + Ctl {
                                        operation __IfBody_827605fe(q : Qubit[]) : Unit is Adj + Ctl {
                                                operation __ForLoopBody_0b47e461(q : Qubit[]) : Unit is Adj + Ctl {
                                                        X(q[0]);
                                                }
                                                for i in 1..3 {
                                                    Controlled Adjoint __ForLoopBody_0b47e461([q[1]], [q[0]]);
                                                }
                                        }
                                        
                                        operation __ElseBody_827605fe(q : Qubit[]) : Unit is Adj + Ctl {
                                                operation __InlineApplyIfRelationL_40f97797(q : Qubit[]) : Unit is Adj + Ctl {
                                                    operation __IfBody_34e1f72d(q : Qubit[]) : Unit is Adj + Ctl {
                                                            operation __ForLoopBody_60151b19(q : Qubit[]) : Unit is Adj + Ctl {
                                                            
                                                            }
                                                            for i in 1..3 {
                                                                __ForLoopBody_60151b19(q);
                                                            }
                                                    }
                                                    
                                                    operation __ElseBody_34e1f72d(q : Qubit[]) : Unit is Adj + Ctl {
                                                            operation __IfBody_99eeaa12(q : Qubit[]) : Unit is Adj + Ctl {
                                                                        ApplyToEachCA(MySingleBlock_96a2f43b, q);
                                                            }
                                                            
                                                            operation __ElseBody_99eeaa12(q : Qubit[]) : Unit is Adj + Ctl {
                                                                        ApproximatelyPreparePureStateCP(
                                                                    1e-6,
                                                                    [
                                                                        ComplexPolar(0.145649, 4.556058),
                                                                        ComplexPolar(0.989336, 4.644598)
                                                                    ],
                                                                    q
                                                                );
                                                            }
                                                            
                                                            if __RandomFlag_dbff1b93() {
                                                                __IfBody_99eeaa12(q);
                                                            } else {
                                                                __ElseBody_99eeaa12(q);
                                                            }
                                                    }
                                                    
                                                    if __RandomFlag_6d547bd4() {
                                                        __IfBody_34e1f72d(q);
                                                    } else {
                                                        __ElseBody_34e1f72d(q);
                                                    }
                                                }
                                                let x = [q[1]];
                                                let target = [q[0]];
                                                ApplyIfGreaterOrEqualL(__InlineApplyIfRelationL_40f97797, 0L, x, target);
                                        }
                                        
                                        if __RandomFlag_f5d92fff() {
                                            __IfBody_827605fe(q);
                                        } else {
                                            __ElseBody_827605fe(q);
                                        }
                                    }
                                    let x = [q[1], q[2]];
                                    let y = [q[0], q[4]];
                                    let target = [q[3], q[5]];
                                    ApplyIfGreaterOrEqualLE(__InlineApplyIfRelationLE_629a11d2, x, y, target);
                                }
                                for i in 1..3 {
                                    __ForLoopBody_987f002a(q);
                                }
                            }
                            let x = [q[4]];
                            let y = [q[3]];
                            let target = [q[2], q[5], q[6], q[9], q[10], q[11]];
                            ApplyIfLessOrEqualLE(__InlineApplyIfRelationLE_f3f55857, x, y, target);
                    }
                    
                    if __RandomFlag_1df1d2f6() {
                        Adjoint __IfBody_96b6cd84(q);
                    } else {
                        Adjoint __ElseBody_96b6cd84(q);
                    }
            }
            
            if __RandomFlag_78cfa5b2() {
                Adjoint __IfBody_fbb8b005(q);
            } else {
                Adjoint __ElseBody_fbb8b005(q);
            }
        }
        for i in 1..3 {
            Adjoint __ForLoopBody_c6e9d146(q);
        }
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Adj {
        operation __ForLoopBody_5bf9baa3(q : Qubit[]) : Unit is Adj {
            operation __InlineApplyIfRelationL_96de5a70(q : Qubit[]) : Unit is Adj + Ctl {
                operation __InlineApplyIfRelationL_9c76475a(q : Qubit[]) : Unit is Adj + Ctl {
                    operation __IfBody_3d38a90e(q : Qubit[]) : Unit is Adj + Ctl {
                                Ryy(3.304445, q[0], q[1]);
                                S(q[1]);
                                ApplyToEachCA(MySingleBlock_a0212a57, q);
                                Z(q[0]);
                                Y(q[0]);
                                Ry(1.236401, q[1]);
                    }
                    
                    operation __ElseBody_3d38a90e(q : Qubit[]) : Unit is Adj + Ctl {
                            operation __IfBody_cba5d10a(q : Qubit[]) : Unit is Adj + Ctl {
                                    operation __ForLoopBody_cf5ded59(q : Qubit[]) : Unit is Adj + Ctl {
                                            I(q[0]);
                                            ApproximatelyPreparePureStateCP(
                                        1e-6,
                                        [
                                            ComplexPolar(0.874473, 4.227966),
                                            ComplexPolar(0.485075, 5.190749)
                                        ],
                                        q
                                    );
                                            Rx(4.937343, q[0]);
                                    }
                                    for i in 1..3 {
                                        Controlled Adjoint __ForLoopBody_cf5ded59([q[1]], [q[0]]);
                                    }
                            }
                            
                            operation __ElseBody_cba5d10a(q : Qubit[]) : Unit is Adj + Ctl {
                                    operation __InlineApplyIfRelationL_9f95a430(q : Qubit[]) : Unit is Adj + Ctl {
                                        operation __IfBody_c6a59789(q : Qubit[]) : Unit is Adj + Ctl {
                                                    X(q[0]);
                                                    Ry(1.988457, q[0]);
                                        }
                                        
                                        operation __ElseBody_c6a59789(q : Qubit[]) : Unit is Adj + Ctl {
                                                operation __IfBody_4a52f53c(q : Qubit[]) : Unit is Adj + Ctl {
                                                            Ry(5.022834, q[0]);
                                                            ApplyToEachCA(MySingleBlock_327fb10d, q);
                                                }
                                                
                                                operation __ElseBody_4a52f53c(q : Qubit[]) : Unit is Adj + Ctl {
                                                        operation __IfBody_83f7023d(q : Qubit[]) : Unit is Adj + Ctl {
                                                                operation __IfBody_db5f369c(q : Qubit[]) : Unit is Adj + Ctl {
                                                                            X(q[0]);
                                                                }
                                                                
                                                                operation __ElseBody_db5f369c(q : Qubit[]) : Unit is Adj + Ctl {
                                                                            S(q[0]);
                                                                }
                                                                
                                                                if __RandomFlag_477e2483() {
                                                                    __IfBody_db5f369c(q);
                                                                } else {
                                                                    __ElseBody_db5f369c(q);
                                                                }
                                                        }
                                                        
                                                        operation __ElseBody_83f7023d(q : Qubit[]) : Unit is Adj + Ctl {
                                                                operation __ForLoopBody_b433826d(q : Qubit[]) : Unit is Adj + Ctl {
                                                                
                                                                }
                                                                for i in 1..3 {
                                                                    __ForLoopBody_b433826d(q);
                                                                }
                                                        }
                                                        
                                                        if __RandomFlag_a4846af1() {
                                                            __IfBody_83f7023d(q);
                                                        } else {
                                                            __ElseBody_83f7023d(q);
                                                        }
                                                }
                                                
                                                if __RandomFlag_5509f8e1() {
                                                    __IfBody_4a52f53c(q);
                                                } else {
                                                    __ElseBody_4a52f53c(q);
                                                }
                                        }
                                        
                                        if __RandomFlag_820e31bb() {
                                            __IfBody_c6a59789(q);
                                        } else {
                                            __ElseBody_c6a59789(q);
                                        }
                                    }
                                    let x = [q[1]];
                                    let target = [q[0]];
                                    ApplyIfGreaterOrEqualL(__InlineApplyIfRelationL_9f95a430, 1L, x, target);
                            }
                            
                            if __RandomFlag_2974df1d() {
                                __IfBody_cba5d10a(q);
                            } else {
                                __ElseBody_cba5d10a(q);
                            }
                    }
                    
                    if __RandomFlag_e78e5e12() {
                        __IfBody_3d38a90e(q);
                    } else {
                        __ElseBody_3d38a90e(q);
                    }
                }
                let x = [q[0]];
                let target = [q[1], q[2]];
                ApplyIfGreaterL(__InlineApplyIfRelationL_9c76475a, 1L, x, target);
            }
            let x = [q[4], q[6]];
            let target = [q[0], q[9], q[11]];
            ApplyIfLessOrEqualL(__InlineApplyIfRelationL_96de5a70, 1L, x, target);
        }
        for i in 1..3 {
            Adjoint __ForLoopBody_5bf9baa3(q);
        }
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            Controlled ApplyRandomBlock0([q[3], q[4], q[6], q[8], q[9]], [q[0], q[1], q[2], q[5], q[7], q[10], q[11]]);
            Adjoint ApplyRandomBlock1(q);
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