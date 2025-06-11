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



function __RandomFlag_f700addf() : Bool {
    let b0 = ResultAsBool(Zero);
    let b1 = ResultAsBool(Zero);
    let b2 = ResultAsBool(Zero);
    let b3 = ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_271b9a90() : Bool {
    let b0 = not false;
    let b1 = not true;
    let b2 = false;
    let b3 = not false;
    return (b0 and b1) or (b2 and not b3);
}



    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Adj {
        operation __ForLoopZeroBody_81688001(q : Qubit[]) : Unit is Adj {
            operation __ForLoopBody_7c71b9f9(q : Qubit[]) : Unit is Adj {
                operation __IfBody_87857bf0(q : Qubit[]) : Unit is Adj {
                            operation __GenBlock_3b2b0ca7(q : Qubit[]) : Unit is Adj {
                    
                        CX(q[9], q[11]);
                        SWAP(q[10], q[2]);
                        IncByLUsingIncByLE(RippleCarryCGIncByLE, IntAsBigInt(8), [q[0], q[1], q[2], q[4], q[8], q[11]]);
                        RippleCarryCGIncByLE([q[0], q[3]], [q[2], q[4], q[6], q[8], q[10], q[11]]);
                    }
                            __GenBlock_3b2b0ca7(q);
                }
                
                operation __ElseBody_87857bf0(q : Qubit[]) : Unit is Adj {
                }
                
                if __RandomFlag_f700addf() {
                    Adjoint __IfBody_87857bf0(q);
                } else {
                    Adjoint __ElseBody_87857bf0(q);
                }
            }
            for i in 1..3 {
                Adjoint __ForLoopBody_7c71b9f9(q);
            }
        }
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Ctl {
        operation __InlineApplyIfRelationLE_3106b255(q : Qubit[]) : Unit is Adj + Ctl {
                operation __GenBlock_53b62480(q : Qubit[]) : Unit is Adj + Ctl {
        
            R1(4.950605, q[2]);
            SX(q[5]);
            IncByIUsingIncByLE(RippleCarryTTKIncByLE, 2, [q[4], q[5]]);
            CX(q[3], q[8]);
            Exp([PauliX, PauliY, PauliX], 5.604072, [q[6], q[1], q[5]]);
            Exp([PauliY], 4.420781, [q[1]]);
            IncByL(IntAsBigInt(306), [q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8]]);
            CX(q[5], q[1]);
        }
                __GenBlock_53b62480(q);
        }
        let x = [q[5]];
        let y = [q[7]];
        let target = [q[0], q[1], q[2], q[3], q[4], q[6], q[8], q[9], q[10]];
        ApplyIfLessOrEqualLE(__InlineApplyIfRelationLE_3106b255, x, y, target);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Ctl {
        operation __InlineApplyIfRelationLE_c56a80a1(q : Qubit[]) : Unit is Adj + Ctl {
            operation __InlineIfElseDeadcode_ec4f9d96(q : Qubit[]) : Unit is Adj + Ctl {
                if __RandomFlag_271b9a90() {
                } else {
                }
            }
            
            __InlineIfElseDeadcode_ec4f9d96(q);
        }
        let x = [q[0], q[5], q[6]];
        let y = [q[1], q[2], q[4]];
        let target = [q[3], q[7], q[9]];
        ApplyIfGreaterLE(__InlineApplyIfRelationLE_c56a80a1, x, y, target);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            X(q[2]);
            Adjoint ApplyRandomBlock0(q);
            Controlled ApplyRandomBlock1([q[2]], [q[0], q[1], q[3], q[4], q[5], q[6], q[7], q[8], q[9], q[10], q[11]]);
            Controlled ApplyRandomBlock2([q[7], q[9]], [q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[8], q[10], q[11]]);
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