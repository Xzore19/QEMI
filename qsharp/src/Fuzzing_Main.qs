namespace Main_fuzzing {

    open Std.Arithmetic;
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Math;
    open Std.Measurement;
    open Std.StatePreparation;

    operation MySingleBlock_42a9a690(q : Qubit) : Unit is Adj + Ctl {
        X(q);
        Y(q);
        Y(q);
    }
    operation MySingleBlock_72c6f806(q : Qubit) : Unit is Adj + Ctl {
        T(q);
        T(q);
        T(q);
        X(q);
    }
    operation MySingleBlock_381c0f3b(q : Qubit) : Unit is Adj + Ctl {
        Z(q);
        Z(q);
    }
    operation MySingleBlock_9b09c46e(q : Qubit) : Unit is Adj + Ctl {
        Ry(4.964165, q);
        Rz(1.96999, q);
    }

function __RandomFlag_817cbce4() : Bool {
    let b0 = not ResultAsBool(One);
    let b1 = not ResultAsBool(Zero);
    let b2 = ResultAsBool(One);
    let b3 = ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_2e149266() : Bool {
    let b0 = not ResultAsBool(One);
    let b1 = not ResultAsBool(One);
    let b2 = not ResultAsBool(Zero);
    let b3 = not ResultAsBool(One);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_a8ed4bf8() : Bool {
    let b0 = not false;
    let b1 = false;
    let b2 = not true;
    let b3 = false;
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_20343df6() : Bool {
    let b0 = not ResultAsBool(One);
    let b1 = ResultAsBool(One);
    let b2 = ResultAsBool(One);
    let b3 = not ResultAsBool(One);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_79aa625f() : Bool {
    let b0 = not ResultAsBool(Zero);
    let b1 = ResultAsBool(One);
    let b2 = not ResultAsBool(Zero);
    let b3 = ResultAsBool(One);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_8edaa6e4() : Bool {
    let b0 = ResultAsBool(One);
    let b1 = ResultAsBool(Zero);
    let b2 = ResultAsBool(One);
    let b3 = not ResultAsBool(One);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_5ad9cc7f() : Bool {
    let b0 = not ResultAsBool(Zero);
    let b1 = ResultAsBool(One);
    let b2 = not ResultAsBool(One);
    let b3 = ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_ff5ee531() : Bool {
    let b0 = not true;
    let b1 = not false;
    let b2 = not true;
    let b3 = false;
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_56ccb245() : Bool {
    let b0 = ResultAsBool(One);
    let b1 = ResultAsBool(One);
    let b2 = not ResultAsBool(Zero);
    let b3 = ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}

    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Adj {
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit {
        // --- RANDOM FLAG BASED IF ---
        CNOT(q[9], q[10]);
        T(q[10]);
        ApplyQFT(q);
        let r0 = Measure([PauliZ], [q[4]]);
        let r1 = Measure([PauliZ], [q[9]]);
        let r2 = Measure([PauliZ], [q[10]]);
        if r0 == One or r1 == One or r2 == One {
                operation __InlineApplyIfRelationL_ccd3c334(q : Qubit[]) : Unit is Adj + Ctl {
                        Rz(1.568667, q[0]);
                        Z(q[0]);
                        S(q[0]);
                }
                let x = [q[0], q[7]];
                let target = [q[4]];
                ApplyIfLessL(__InlineApplyIfRelationL_ccd3c334, 0L, x, target);
        } else {
                operation __ForLoopBody_bd0d55fd(q : Qubit[]) : Unit {
                    operation __InlineApplyIfRelationLE_844e4243(q : Qubit[]) : Unit is Adj + Ctl {
                            ApplyToEachCA(MySingleBlock_72c6f806, q);
                            Y(q[0]);
                            ApplyQFT(q);
                    }
                    let x = [q[4], q[8]];
                    let y = [q[2], q[11]];
                    let target = [q[1]];
                    ApplyIfEqualLE(__InlineApplyIfRelationLE_844e4243, x, y, target);
                }
                for i in 1..3 {
                    __ForLoopBody_bd0d55fd(q);
                }
        }
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Adj {
        operation __ForLoopBody_591fdea7(q : Qubit[]) : Unit is Adj {
            operation __IfBody_11859518(q : Qubit[]) : Unit is Adj {
                    operation __InlineApplyIfRelationL_c08d99d7(q : Qubit[]) : Unit is Adj + Ctl {
                        operation __ForLoopBody_d34086a7(q : Qubit[]) : Unit is Adj + Ctl {
                            operation __InlineApplyIfRelationLE_1f84497c(q : Qubit[]) : Unit is Adj + Ctl {
                                operation __IfBody_8c1acecf(q : Qubit[]) : Unit is Adj + Ctl {
                                        operation __InlineApplyIfRelationL_99f8c7fa(q : Qubit[]) : Unit is Adj + Ctl {
                                                T(q[0]);
                                                Y(q[1]);
                                                ApplyToEachCA(MySingleBlock_381c0f3b, q);
                                                ApproximatelyPreparePureStateCP(
                                            1e-6,
                                            [
                                                ComplexPolar(0.473804, 2.252674),
                                                ComplexPolar(0.662759, 2.326009),
                                                ComplexPolar(0.503369, 4.061112),
                                                ComplexPolar(0.28789, 4.135466)
                                            ],
                                            q
                                        );
                                        }
                                        let x = [q[2]];
                                        let target = [q[0], q[1]];
                                        ApplyIfEqualL(__InlineApplyIfRelationL_99f8c7fa, 0L, x, target);
                                }
                                
                                operation __ElseBody_8c1acecf(q : Qubit[]) : Unit is Adj + Ctl {
                                        operation __InlineApplyIfRelationL_b2e8d23d(q : Qubit[]) : Unit is Adj + Ctl {
                                            operation __IfBody_25db30e9(q : Qubit[]) : Unit is Adj + Ctl {
                                                        Rz(0.245591, q[0]);
                                                        X(q[0]);
                                                        ApplyToEachCA(MySingleBlock_9b09c46e, q);
                                            }
                                            
                                            operation __ElseBody_25db30e9(q : Qubit[]) : Unit is Adj + Ctl {
                                                    operation __IfBody_f64d6138(q : Qubit[]) : Unit is Adj + Ctl {
                                                            operation __ForLoopBody_2e788609(q : Qubit[]) : Unit is Adj + Ctl {
                                                                    Rx(2.479333, q[0]);
                                                            }
                                                            for i in 1..3 {
                                                                __ForLoopBody_2e788609(q);
                                                            }
                                                    }
                                                    
                                                    operation __ElseBody_f64d6138(q : Qubit[]) : Unit is Adj + Ctl {
                                                                X(q[0]);
                                                    }
                                                    
                                                    if __RandomFlag_79aa625f() {
                                                        __IfBody_f64d6138(q);
                                                    } else {
                                                        __ElseBody_f64d6138(q);
                                                    }
                                            }
                                            
                                            if __RandomFlag_8edaa6e4() {
                                                __IfBody_25db30e9(q);
                                            } else {
                                                __ElseBody_25db30e9(q);
                                            }
                                        }
                                        let x = [q[0], q[1]];
                                        let target = [q[2]];
                                        ApplyIfGreaterOrEqualL(__InlineApplyIfRelationL_b2e8d23d, 3L, x, target);
                                }
                                
                                if __RandomFlag_5ad9cc7f() {
                                    __IfBody_8c1acecf(q);
                                } else {
                                    __ElseBody_8c1acecf(q);
                                }
                            }
                            let x = [q[6], q[7]];
                            let y = [q[1], q[2]];
                            let target = [q[0], q[3], q[4]];
                            ApplyIfEqualLE(__InlineApplyIfRelationLE_1f84497c, x, y, target);
                        }
                        for i in 1..3 {
                            __ForLoopBody_d34086a7(q);
                        }
                    }
                    let x = [q[1], q[9]];
                    let target = [q[2], q[4], q[5], q[6], q[7], q[8], q[10], q[11]];
                    ApplyIfEqualL(__InlineApplyIfRelationL_c08d99d7, 1L, x, target);
            }
            
            operation __ElseBody_11859518(q : Qubit[]) : Unit is Adj {
                    operation __ForLoopBody_ea7442db(q : Qubit[]) : Unit is Adj {
                        operation __ForLoopBody_fc9e68fe(q : Qubit[]) : Unit is Adj {
                            operation __InlineApplyIfRelationL_e25a5567(q : Qubit[]) : Unit is Adj + Ctl {
                                operation __ForLoopBody_73215723(q : Qubit[]) : Unit is Adj + Ctl {
                                    operation __InlineApplyIfRelationL_6d379165(q : Qubit[]) : Unit is Adj + Ctl {
                                        operation __IfBody_066065f0(q : Qubit[]) : Unit is Adj + Ctl {
                                                    Rx(0.60515, q[0]);
                                                    R1(0.528077, q[0]);
                                        }
                                        
                                        operation __ElseBody_066065f0(q : Qubit[]) : Unit is Adj + Ctl {
                                                    S(q[0]);
                                                    Rz(4.468466, q[0]);
                                        }
                                        
                                        if __RandomFlag_ff5ee531() {
                                            __IfBody_066065f0(q);
                                        } else {
                                            __ElseBody_066065f0(q);
                                        }
                                    }
                                    let x = [q[0]];
                                    let target = [q[1]];
                                    ApplyIfLessOrEqualL(__InlineApplyIfRelationL_6d379165, 0L, x, target);
                                }
                                for i in 1..3 {
                                    Controlled Adjoint __ForLoopBody_73215723([q[0], q[1]], [q[2], q[3]]);
                                }
                            }
                            let x = [q[1], q[6]];
                            let target = [q[5], q[8], q[10], q[11]];
                            ApplyIfGreaterL(__InlineApplyIfRelationL_e25a5567, 2L, x, target);
                        }
                        for i in 1..3 {
                            Adjoint __ForLoopBody_fc9e68fe(q);
                        }
                    }
                    for i in 1..3 {
                        Adjoint __ForLoopBody_ea7442db(q);
                    }
            }
            
            if __RandomFlag_56ccb245() {
                Adjoint __IfBody_11859518(q);
            } else {
                Adjoint __ElseBody_11859518(q);
            }
        }
        for i in 1..3 {
            Adjoint __ForLoopBody_591fdea7(q);
        }
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            Adjoint ApplyRandomBlock0(q);
            ApplyRandomBlock1(q);
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