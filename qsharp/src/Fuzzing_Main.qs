namespace Main_fuzzing {

    open Std.Arithmetic;
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Math;
    open Std.Measurement;
    open Std.StatePreparation;

    operation MySingleBlock_01f90dbb(q : Qubit) : Unit is Adj + Ctl {
        X(q);
        S(q);
        S(q);
    }
    operation MySingleBlock_321180cf(q : Qubit) : Unit is Adj + Ctl {
        Y(q);
        Rx(0.051947, q);
    }
    operation MySingleBlock_c194768b(q : Qubit) : Unit is Adj + Ctl {
        H(q);
        Rz(3.890488, q);
    }

function __RandomFlag_96e3676a() : Bool {
    let b0 = not ResultAsBool(Zero);
    let b1 = ResultAsBool(Zero);
    let b2 = ResultAsBool(One);
    let b3 = ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_3776dd70() : Bool {
    let b0 = ResultAsBool(One);
    let b1 = not ResultAsBool(One);
    let b2 = ResultAsBool(Zero);
    let b3 = ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_e39b060b() : Bool {
    let b0 = not ResultAsBool(Zero);
    let b1 = ResultAsBool(Zero);
    let b2 = ResultAsBool(One);
    let b3 = not ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_7b6794c7() : Bool {
    let b0 = not ResultAsBool(One);
    let b1 = ResultAsBool(One);
    let b2 = ResultAsBool(One);
    let b3 = ResultAsBool(One);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_40454ace() : Bool {
    let b0 = ResultAsBool(Zero);
    let b1 = not ResultAsBool(Zero);
    let b2 = not ResultAsBool(One);
    let b3 = not ResultAsBool(One);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_3b7c637c() : Bool {
    let b0 = not ResultAsBool(One);
    let b1 = ResultAsBool(Zero);
    let b2 = not ResultAsBool(Zero);
    let b3 = not ResultAsBool(One);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_f141203b() : Bool {
    let b0 = not ResultAsBool(Zero);
    let b1 = not ResultAsBool(One);
    let b2 = ResultAsBool(Zero);
    let b3 = ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_c566bed2() : Bool {
    let b0 = ResultAsBool(One);
    let b1 = ResultAsBool(One);
    let b2 = ResultAsBool(One);
    let b3 = not ResultAsBool(One);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_ee9a0b09() : Bool {
    let b0 = ResultAsBool(One);
    let b1 = not ResultAsBool(Zero);
    let b2 = not ResultAsBool(One);
    let b3 = not ResultAsBool(One);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_8cef805b() : Bool {
    let b0 = not ResultAsBool(Zero);
    let b1 = ResultAsBool(One);
    let b2 = ResultAsBool(One);
    let b3 = not ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_9dcf28e6() : Bool {
    let b0 = ResultAsBool(Zero);
    let b1 = not ResultAsBool(One);
    let b2 = ResultAsBool(One);
    let b3 = ResultAsBool(One);
    return (b0 and b1) or (b2 and not b3);
}

    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Ctl {
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj {
        operation __ForLoopBody_0f6ce633(q : Qubit[]) : Unit is Adj {
            operation __InlineApplyIfRelationL_421be355(q : Qubit[]) : Unit is Adj + Ctl {
                operation __IfBody_986acdc9(q : Qubit[]) : Unit is Adj + Ctl {
                        operation __ForLoopBody_3e73fb06(q : Qubit[]) : Unit is Adj + Ctl {
                            operation __InlineApplyIfRelationLE_882e7364(q : Qubit[]) : Unit is Adj + Ctl {
                                operation __ForLoopBody_b1a1ad5d(q : Qubit[]) : Unit is Adj + Ctl {
                                    operation __ForLoopBody_4c671aa1(q : Qubit[]) : Unit is Adj + Ctl {
                                            Ry(0.798265, q[0]);
                                            ApplyQFT(q);
                                    }
                                    for i in 1..3 {
                                        __ForLoopBody_4c671aa1(q);
                                    }
                                }
                                for i in 1..3 {
                                    __ForLoopBody_b1a1ad5d(q);
                                }
                            }
                            let x = [q[3], q[5], q[6]];
                            let y = [q[0], q[1], q[2]];
                            let target = [q[8]];
                            ApplyIfEqualLE(__InlineApplyIfRelationLE_882e7364, x, y, target);
                        }
                        for i in 1..3 {
                            Controlled Adjoint __ForLoopBody_3e73fb06([q[5]], [q[0], q[1], q[2], q[3], q[4], q[6], q[7], q[8], q[9], q[10]]);
                        }
                }
                
                operation __ElseBody_986acdc9(q : Qubit[]) : Unit is Adj + Ctl {
                        operation __InlineApplyIfRelationLE_1eb0f842(q : Qubit[]) : Unit is Adj + Ctl {
                            operation __IfBody_457768ad(q : Qubit[]) : Unit is Adj + Ctl {
                                    operation __ForLoopBody_412996cc(q : Qubit[]) : Unit is Adj + Ctl {
                                        operation __IfBody_b00a4503(q : Qubit[]) : Unit is Adj + Ctl {
                                                operation __InlineApplyIfRelationLE_4904e6ea(q : Qubit[]) : Unit is Adj + Ctl {
                                                        I(q[0]);
                                                        R1(0.557334, q[0]);
                                                }
                                                let x = [q[2]];
                                                let y = [q[1]];
                                                let target = [q[0]];
                                                ApplyIfLessLE(__InlineApplyIfRelationLE_4904e6ea, x, y, target);
                                        }
                                        
                                        operation __ElseBody_b00a4503(q : Qubit[]) : Unit is Adj + Ctl {
                                                operation __ForLoopBody_6686ab42(q : Qubit[]) : Unit is Adj + Ctl {
                                                    operation __ForLoopBody_39a156f5(q : Qubit[]) : Unit is Adj + Ctl {
                                                            ApproximatelyPreparePureStateCP(
                                                        1e-6,
                                                        [
                                                            ComplexPolar(0.430166, 5.034773),
                                                            ComplexPolar(0.600054, 4.019244),
                                                            ComplexPolar(0.441891, 5.281012),
                                                            ComplexPolar(0.509533, 4.582645)
                                                        ],
                                                        q
                                                    );
                                                    }
                                                    for i in 1..3 {
                                                        Controlled Adjoint __ForLoopBody_39a156f5([q[2]], [q[0], q[1]]);
                                                    }
                                                }
                                                for i in 1..3 {
                                                    __ForLoopBody_6686ab42(q);
                                                }
                                        }
                                        
                                        if __RandomFlag_40454ace() {
                                            __IfBody_b00a4503(q);
                                        } else {
                                            __ElseBody_b00a4503(q);
                                        }
                                    }
                                    for i in 1..3 {
                                        Controlled Adjoint __ForLoopBody_412996cc([q[0], q[1]], [q[2], q[3], q[4]]);
                                    }
                            }
                            
                            operation __ElseBody_457768ad(q : Qubit[]) : Unit is Adj + Ctl {
                                    operation __InlineApplyIfRelationLE_128a6602(q : Qubit[]) : Unit is Adj + Ctl {
                                        operation __IfBody_79be1d18(q : Qubit[]) : Unit is Adj + Ctl {
                                                    Rz(0.700679, q[0]);
                                                    Y(q[0]);
                                                    X(q[0]);
                                                    I(q[0]);
                                        }
                                        
                                        operation __ElseBody_79be1d18(q : Qubit[]) : Unit is Adj + Ctl {
                                                    H(q[0]);
                                                    T(q[0]);
                                                    ApplyToEachCA(MySingleBlock_321180cf, q);
                                                    Y(q[0]);
                                        }
                                        
                                        if __RandomFlag_3b7c637c() {
                                            __IfBody_79be1d18(q);
                                        } else {
                                            __ElseBody_79be1d18(q);
                                        }
                                    }
                                    let x = [q[3], q[4]];
                                    let y = [q[0], q[2]];
                                    let target = [q[1]];
                                    ApplyIfGreaterLE(__InlineApplyIfRelationLE_128a6602, x, y, target);
                            }
                            
                            if __RandomFlag_f141203b() {
                                __IfBody_457768ad(q);
                            } else {
                                __ElseBody_457768ad(q);
                            }
                        }
                        let x = [q[2], q[8], q[9]];
                        let y = [q[1], q[5], q[6]];
                        let target = [q[0], q[3], q[4], q[7], q[10]];
                        ApplyIfLessLE(__InlineApplyIfRelationLE_1eb0f842, x, y, target);
                }
                
                if __RandomFlag_c566bed2() {
                    __IfBody_986acdc9(q);
                } else {
                    __ElseBody_986acdc9(q);
                }
            }
            let x = [q[7]];
            let target = [q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[8], q[9], q[10], q[11]];
            ApplyIfLessOrEqualL(__InlineApplyIfRelationL_421be355, 0L, x, target);
        }
        for i in 1..3 {
            Adjoint __ForLoopBody_0f6ce633(q);
        }
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Adj {
        operation __IfBody_2e2e6cd0(q : Qubit[]) : Unit is Adj {
                operation __InlineApplyIfRelationL_3503510f(q : Qubit[]) : Unit is Adj + Ctl {
                    operation __IfBody_865f640b(q : Qubit[]) : Unit is Adj + Ctl {
                            operation __InlineApplyIfRelationLE_5f210fa7(q : Qubit[]) : Unit is Adj + Ctl {
                                    SWAP(q[0], q[1]);
                                    I(q[1]);
                                    ApplyToEachCA(MySingleBlock_c194768b, q);
                                    Rz(5.28368, q[0]);
                                    R1(1.926029, q[0]);
                                    Y(q[0]);
                            }
                            let x = [q[0], q[5]];
                            let y = [q[3], q[4]];
                            let target = [q[1], q[2]];
                            ApplyIfGreaterOrEqualLE(__InlineApplyIfRelationLE_5f210fa7, x, y, target);
                    }
                    
                    operation __ElseBody_865f640b(q : Qubit[]) : Unit is Adj + Ctl {
                            operation __InlineApplyIfRelationLE_8edbf19d(q : Qubit[]) : Unit is Adj + Ctl {
                                    Ry(5.285136, q[0]);
                                    I(q[0]);
                                    Y(q[0]);
                                    R1(0.117792, q[0]);
                            }
                            let x = [q[4]];
                            let y = [q[5]];
                            let target = [q[1]];
                            ApplyIfGreaterLE(__InlineApplyIfRelationLE_8edbf19d, x, y, target);
                    }
                    
                    if __RandomFlag_ee9a0b09() {
                        __IfBody_865f640b(q);
                    } else {
                        __ElseBody_865f640b(q);
                    }
                }
                let x = [q[1], q[6], q[9]];
                let target = [q[0], q[2], q[4], q[5], q[10], q[11]];
                ApplyIfGreaterOrEqualL(__InlineApplyIfRelationL_3503510f, 4L, x, target);
        }
        
        operation __ElseBody_2e2e6cd0(q : Qubit[]) : Unit is Adj {
                operation __InlineApplyIfRelationL_78490a3a(q : Qubit[]) : Unit is Adj + Ctl {
                    operation __IfBody_56aba51f(q : Qubit[]) : Unit is Adj + Ctl {
                            operation __InlineApplyIfRelationL_cad4b89b(q : Qubit[]) : Unit is Adj + Ctl {
                                    CNOT(q[0], q[1]);
                                    Z(q[1]);
                                    Rzz(3.637961, q[1], q[0]);
                                    ApproximatelyPreparePureStateCP(
                                1e-6,
                                [
                                    ComplexPolar(0.542423, 1.392054),
                                    ComplexPolar(0.651858, 1.316364),
                                    ComplexPolar(0.311365, 1.804012),
                                    ComplexPolar(0.428847, 0.107752)
                                ],
                                q
                            );
                                    Rx(3.172053, q[0]);
                                    CNOT(q[1], q[0]);
                            }
                            let x = [q[0], q[2], q[5]];
                            let target = [q[3], q[4]];
                            ApplyIfGreaterL(__InlineApplyIfRelationL_cad4b89b, 4L, x, target);
                    }
                    
                    operation __ElseBody_56aba51f(q : Qubit[]) : Unit is Adj + Ctl {
                            operation __InlineApplyIfRelationLE_976c3682(q : Qubit[]) : Unit is Adj + Ctl {
                                operation __InlineApplyIfRelationL_85bb176d(q : Qubit[]) : Unit is Adj + Ctl {
                                        Z(q[0]);
                                        Rz(2.207439, q[0]);
                                        Z(q[0]);
                                        R1(1.218666, q[0]);
                                }
                                let x = [q[0]];
                                let target = [q[1]];
                                ApplyIfLessL(__InlineApplyIfRelationL_85bb176d, 1L, x, target);
                            }
                            let x = [q[2], q[5]];
                            let y = [q[1], q[4]];
                            let target = [q[0], q[3]];
                            ApplyIfEqualLE(__InlineApplyIfRelationLE_976c3682, x, y, target);
                    }
                    
                    if __RandomFlag_8cef805b() {
                        __IfBody_56aba51f(q);
                    } else {
                        __ElseBody_56aba51f(q);
                    }
                }
                let x = [q[1], q[10]];
                let target = [q[0], q[3], q[6], q[7], q[9], q[11]];
                ApplyIfLessL(__InlineApplyIfRelationL_78490a3a, 3L, x, target);
        }
        
        if __RandomFlag_9dcf28e6() {
            Adjoint __IfBody_2e2e6cd0(q);
        } else {
            Adjoint __ElseBody_2e2e6cd0(q);
        }
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            Controlled ApplyRandomBlock0([q[2], q[3], q[5], q[6], q[7], q[10]], [q[0], q[1], q[4], q[8], q[9], q[11]]);
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