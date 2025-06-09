namespace Main_fuzzing {

    open Std.Arithmetic;
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Math;
    open Std.Measurement;
    open Std.StatePreparation;

    operation MySingleBlock_25bf2541(q : Qubit) : Unit is Adj + Ctl {
        X(q);
        Rz(1.818241, q);
        Y(q);
    }
    operation MySingleBlock_029e438a(q : Qubit) : Unit is Adj + Ctl {
        Ry(4.870005, q);
        Y(q);
        S(q);
        Y(q);
    }
    operation MySingleBlock_0734385b(q : Qubit) : Unit is Adj + Ctl {
        Rx(5.205727, q);
        H(q);
    }

function __RandomFlag_22227e85() : Bool {
    let b0 = ResultAsBool(Zero);
    let b1 = ResultAsBool(Zero);
    let b2 = not ResultAsBool(One);
    let b3 = ResultAsBool(One);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_f029a957() : Bool {
    let b0 = not ResultAsBool(One);
    let b1 = not ResultAsBool(One);
    let b2 = ResultAsBool(One);
    let b3 = not ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_3f281223() : Bool {
    let b0 = not true;
    let b1 = not true;
    let b2 = false;
    let b3 = true;
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_f967afb6() : Bool {
    let b0 = ResultAsBool(One);
    let b1 = not ResultAsBool(One);
    let b2 = ResultAsBool(Zero);
    let b3 = ResultAsBool(One);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_68d4bc49() : Bool {
    let b0 = not false;
    let b1 = not true;
    let b2 = false;
    let b3 = true;
    return (b0 and b1) or (b2 and not b3);
}



    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Adj + Ctl {
        operation __InlineIfElseDeadcode_d9dafd0c(q : Qubit[]) : Unit is Adj + Ctl {
            if __RandomFlag_3f281223() {
            } else {
                    operation __ForLoopBody_f14358e7(q : Qubit[]) : Unit is Adj + Ctl {
                        operation __IfBody_2495c397(q : Qubit[]) : Unit is Adj + Ctl {
                                    RFrac(PauliY, 1, 5, q[1]);
                                    R1Frac(15, 1, q[2]);
                                    ApplyCNOTChain([q[4], q[1], q[2], q[3]]);
                                    ApplyPauli([PauliY, PauliX, PauliZ], [q[1], q[4], q[0]]);
                                    RFrac(PauliX, 12, 8, q[0]);
                                    ApplyPauli([PauliX, PauliZ], [q[3], q[4]]);
                        }
                        
                        operation __ElseBody_2495c397(q : Qubit[]) : Unit is Adj + Ctl {
                                    R1Frac(13, 3, q[3]);
                                    ApplyToEachCA(MySingleBlock_029e438a, q);
                                    RFrac(PauliY, 9, 8, q[3]);
                                    RFrac(PauliX, 1, 10, q[0]);
                                    ApproximatelyPreparePureStateCP(
                                1e-6,
                                [
                                    ComplexPolar(0.197051, 1.880475),
                                    ComplexPolar(0.22318, 5.426801),
                                    ComplexPolar(0.220837, 3.359331),
                                    ComplexPolar(0.190593, 4.181918),
                                    ComplexPolar(0.196519, 1.540651),
                                    ComplexPolar(0.234449, 5.796881),
                                    ComplexPolar(0.165026, 2.028512),
                                    ComplexPolar(0.102053, 4.988367),
                                    ComplexPolar(0.225701, 2.380713),
                                    ComplexPolar(0.169905, 2.276647),
                                    ComplexPolar(0.204999, 3.463956),
                                    ComplexPolar(0.08103, 2.023086),
                                    ComplexPolar(0.128017, 0.153964),
                                    ComplexPolar(0.193737, 1.342047),
                                    ComplexPolar(0.158161, 3.24429),
                                    ComplexPolar(0.11462, 1.282022),
                                    ComplexPolar(0.108661, 3.896908),
                                    ComplexPolar(0.180151, 0.561932),
                                    ComplexPolar(0.240441, 2.408466),
                                    ComplexPolar(0.109483, 5.19186),
                                    ComplexPolar(0.072397, 2.806814),
                                    ComplexPolar(0.185033, 0.629247),
                                    ComplexPolar(0.098712, 1.380266),
                                    ComplexPolar(0.127961, 6.117414),
                                    ComplexPolar(0.232532, 1.854148),
                                    ComplexPolar(0.188939, 2.204289),
                                    ComplexPolar(0.203645, 4.985106),
                                    ComplexPolar(0.209682, 2.206569),
                                    ComplexPolar(0.099402, 0.351846),
                                    ComplexPolar(0.180011, 2.006225),
                                    ComplexPolar(0.232289, 4.375164),
                                    ComplexPolar(0.153143, 2.90136)
                                ],
                                q
                            );
                                    R1Frac(10, 7, q[4]);
                        }
                        
                        if __RandomFlag_f029a957() {
                            __IfBody_2495c397(q);
                        } else {
                            __ElseBody_2495c397(q);
                        }
                    }
                    for i in 1..3 {
                        Controlled Adjoint __ForLoopBody_f14358e7([q[0], q[4], q[6]], [q[1], q[2], q[3], q[5], q[7]]);
                    }
            }
        }
        
        __InlineIfElseDeadcode_d9dafd0c(q);
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj + Ctl {
        operation __ForLoopBody_3805e32e(q : Qubit[]) : Unit is Adj + Ctl {
            operation __ForLoopBody_e4fd1cde(q : Qubit[]) : Unit is Adj + Ctl {
                operation __IfBody_6d903ff0(q : Qubit[]) : Unit is Adj + Ctl {
                        operation __IfBody_7d1c6e1e(q : Qubit[]) : Unit is Adj + Ctl {
                                operation __ForLoopBody_69383686(q : Qubit[]) : Unit is Adj + Ctl {
                                        ApplyToEachCA(MySingleBlock_0734385b, q);
                                        ApplyCNOTChain([q[2], q[4], q[3], q[1], q[0]]);
                                        ApplyPauli([PauliZ, PauliY], [q[0], q[2]]);
                                }
                                for i in 1..3 {
                                    __ForLoopBody_69383686(q);
                                }
                        }
                        
                        operation __ElseBody_7d1c6e1e(q : Qubit[]) : Unit is Adj + Ctl {
                                    ApplyPauli([PauliX, PauliZ], [q[2], q[1]]);
                                    RFrac(PauliX, 14, 1, q[0]);
                                    ApplyCNOTChain([q[3], q[0]]);
                                    ApplyCNOTChain([q[2], q[3], q[4]]);
                        }
                        
                        if __RandomFlag_f967afb6() {
                            __IfBody_7d1c6e1e(q);
                        } else {
                            __ElseBody_7d1c6e1e(q);
                        }
                }
                
                operation __ElseBody_6d903ff0(q : Qubit[]) : Unit is Adj + Ctl {
                        operation __ForLoopBody_ee0dd59c(q : Qubit[]) : Unit is Adj + Ctl {
                            operation __InlineApplyIfRelationLE_a34b3a54(q : Qubit[]) : Unit is Adj + Ctl {
                                    R1Frac(14, 1, q[1]);
                                    ApproximatelyPreparePureStateCP(
                                1e-6,
                                [
                                    ComplexPolar(0.546344, 2.85392),
                                    ComplexPolar(0.587483, 3.324085),
                                    ComplexPolar(0.565859, 4.883461),
                                    ComplexPolar(0.190198, 6.034568)
                                ],
                                q
                            );
                                    ApplyCNOTChain([q[1], q[0]]);
                                    RFrac(PauliY, 10, 10, q[0]);
                            }
                            let x = [q[2]];
                            let y = [q[0]];
                            let target = [q[1], q[3]];
                            ApplyIfLessLE(__InlineApplyIfRelationLE_a34b3a54, x, y, target);
                        }
                        for i in 1..3 {
                            Controlled Adjoint __ForLoopBody_ee0dd59c([q[4]], [q[0], q[1], q[2], q[3]]);
                        }
                }
                
                if __RandomFlag_68d4bc49() {
                    __IfBody_6d903ff0(q);
                } else {
                    __ElseBody_6d903ff0(q);
                }
            }
            for i in 1..3 {
                Controlled Adjoint __ForLoopBody_e4fd1cde([q[4], q[5], q[6]], [q[0], q[1], q[2], q[3], q[7]]);
            }
        }
        for i in 1..3 {
            Controlled Adjoint __ForLoopBody_3805e32e([q[0], q[2]], [q[1], q[3], q[4], q[5], q[6], q[7], q[8], q[9]]);
        }
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Adj + Ctl {
        operation __ForLoopBody_1c195058(q : Qubit[]) : Unit is Adj + Ctl {
                R1Frac(13, 4, q[4]);
                ApplyPauli([PauliX, PauliX], [q[1], q[2]]);
                RFrac(PauliZ, 11, 3, q[0]);
                RFrac(PauliY, 11, 1, q[2]);
                RFrac(PauliX, 4, 1, q[1]);
                ApplyCNOTChain([q[5], q[4], q[0]]);
                RFrac(PauliY, 8, 2, q[2]);
        }
        for i in 1..3 {
            Controlled Adjoint __ForLoopBody_1c195058([q[0], q[7]], [q[1], q[2], q[3], q[4], q[5], q[6], q[8]]);
        }
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            Controlled Adjoint ApplyRandomBlock0([q[0], q[3], q[8], q[9]], [q[1], q[2], q[4], q[5], q[6], q[7], q[10], q[11]]);
            Controlled Adjoint ApplyRandomBlock1([q[2], q[5]], [q[0], q[1], q[3], q[4], q[6], q[7], q[8], q[9], q[10], q[11]]);
            Controlled Adjoint ApplyRandomBlock2([q[0], q[2], q[9]], [q[1], q[3], q[4], q[5], q[6], q[7], q[8], q[10], q[11]]);
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