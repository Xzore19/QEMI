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



function __RandomFlag_e937bc50() : Bool {
    let b0 = false;
    let b1 = false;
    let b2 = true;
    let b3 = not true;
    return Xor(Xor(b0, b1), Xor(b2, b3));
}
function __RandomFlag_2c43f869() : Bool {
    let b0 = true;
    let b1 = false;
    let b2 = not true;
    let b3 = false;
    return Xor(Xor(b0, b1), Xor(b2, b3));
}
function __RandomFlag_966a48ac() : Bool {
    let b0 = ResultAsBool(Zero);
    let b1 = not ResultAsBool(Zero);
    let b2 = ResultAsBool(Zero);
    let b3 = not ResultAsBool(One);
    return Xor(Xor(b0, b1), Xor(b2, b3));
}
function __RandomFlag_a2f3270f() : Bool {
    let b0 = not true;
    let b1 = true;
    let b2 = true;
    let b3 = true;
    return Xor(Xor(b0, b1), Xor(b2, b3));
}
function __RandomFlag_6b349875() : Bool {
    let b0 = ResultAsBool(Zero);
    let b1 = not ResultAsBool(Zero);
    let b2 = ResultAsBool(Zero);
    let b3 = not ResultAsBool(Zero);
    return Xor(Xor(b0, b1), Xor(b2, b3));
}
function __RandomFlag_acf9d076() : Bool {
    let b0 = not false;
    let b1 = true;
    let b2 = not true;
    let b3 = false;
    return Xor(Xor(b0, b1), Xor(b2, b3));
}



    operation ApplyRandomBlock0(q : Qubit[]) : Unit {
        operation __WhileBody_d7374574(q : Qubit[]) : Unit {
            operation __ForLoopBody_52d74d93(q : Qubit[]) : Unit {
                operation __RepeatBody_02d6cdb9(q : Qubit[]) : Unit {
                        operation __GenBlock_3d6de5a7(q : Qubit[]) : Unit {
                
                    Reset(q[4]);
                    Rz(4.667021, q[1]);
                    ResetAll([q[5], q[3], q[4], q[1]]);
                    T(q[1]);
                    T(q[3]);
                }
                        __GenBlock_3d6de5a7(q);
                }
                repeat {
                    __RepeatBody_02d6cdb9(q);
                } until (__RandomFlag_e937bc50()) fixup {
                }
            }
            for i in 1..3 {
                __ForLoopBody_52d74d93(q);
            }
            operation __GenBlock_ab3166fc(q : Qubit[]) : Unit {
        
            T(q[5]);
            IncByLE([q[3], q[4]], [q[0], q[2]]);
        }
            __GenBlock_ab3166fc(q);
        }
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Ctl {
        operation __InlineApplyIfRelationL_a1fcafd2(q : Qubit[]) : Unit is Adj + Ctl {
                operation __GenBlock_86ba8d74(q : Qubit[]) : Unit is Adj + Ctl {
        
            S(q[0]);
            H(q[0]);
            S(q[0]);
            R1Frac(10, 4, q[0]);
            R1(1.094269, q[0]);
            R1(1.617876, q[0]);
            S(q[0]);
        }
                __GenBlock_86ba8d74(q);
        }
        let x = [q[1]];
        let target = [q[4]];
        ApplyIfGreaterOrEqualL(__InlineApplyIfRelationL_a1fcafd2, 1L, x, target);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Adj + Ctl {
        operation __ForLoopBody_be80b2d5(q : Qubit[]) : Unit is Adj + Ctl {
            operation __IfBody_282820b8(q : Qubit[]) : Unit is Adj + Ctl {
                    operation __ForLoopBody_d13f1df7(q : Qubit[]) : Unit is Adj + Ctl {
                            operation __GenBlock_dafe4fd3(q : Qubit[]) : Unit is Adj + Ctl {
                    
                        SX(q[0]);
                        Y(q[2]);
                        CNOT(q[2], q[1]);
                    }
                            __GenBlock_dafe4fd3(q);
                    }
                    for i in 1..3 {
                        __ForLoopBody_d13f1df7(q);
                    }
                    operation __GenBlock_582a78ed(q : Qubit[]) : Unit is Adj + Ctl {
                
                    Rzz(1.589732, q[1], q[2]);
                }
                    __GenBlock_582a78ed(q);
            }
            
            operation __ElseBody_282820b8(q : Qubit[]) : Unit is Adj + Ctl {
                    operation __ForLoopZeroBody_145c5186(q : Qubit[]) : Unit is Adj + Ctl {
                            operation __GenBlock_616af3e1(q : Qubit[]) : Unit is Adj + Ctl {
                    
                        S(q[0]);
                        Ry(4.395554, q[0]);
                        Y(q[0]);
                        R1Frac(1, 4, q[0]);
                    }
                            Controlled Adjoint __GenBlock_616af3e1([q[1]], [q[0]]);
                    }
            }
            
            if __RandomFlag_acf9d076() {
                __IfBody_282820b8(q);
            } else {
                __ElseBody_282820b8(q);
            }
            operation __GenBlock_1f84b493(q : Qubit[]) : Unit is Adj + Ctl {
        
            Exp([PauliX, PauliX, PauliX], 4.005898, [q[1], q[2], q[0]]);
            SWAP(q[1], q[2]);
        }
            __GenBlock_1f84b493(q);
        }
        for i in 1..3 {
            Controlled Adjoint __ForLoopBody_be80b2d5([q[1]], [q[0], q[2], q[3]]);
        }
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[6] {
            X(q[5]);
            ApplyRandomBlock0(q);
            Controlled ApplyRandomBlock1([q[5]], [q[0], q[1], q[2], q[3], q[4]]);
            Controlled Adjoint ApplyRandomBlock2([q[2], q[4]], [q[0], q[1], q[3], q[5]]);
            let r0 = M(q[0]);
            let r1 = M(q[1]);
            let r2 = M(q[2]);
            let r3 = M(q[3]);
            let r4 = M(q[4]);
            let r5 = M(q[5]);
            ResetAll(q);
            return [r0, r1, r2, r3, r4, r5];
        }
    }
}