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



function __RandomFlag_2a2e6c08() : Bool {
    let b0 = ResultAsBool(One);
    let b1 = not ResultAsBool(Zero);
    let b2 = not ResultAsBool(Zero);
    let b3 = ResultAsBool(Zero);
    return Xor(Xor(b0, b1), Xor(b2, b3));
}
function __RandomFlag_c8bab292() : Bool {
    let b0 = false;
    let b1 = not true;
    let b2 = not true;
    let b3 = true;
    return Xor(Xor(b0, b1), Xor(b2, b3));
}



    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Ctl {
        operation __ForLoopZeroBody_21518fa4(q : Qubit[]) : Unit is Ctl {
                operation __GenBlock_03d80786(q : Qubit[]) : Unit is Ctl {
        
            IncByLUsingIncByLE(RippleCarryTTKIncByLE, IntAsBigInt(2), [q[0], q[1], q[2], q[3], q[6]]);
            SX(q[5]);
            let bits = [true];
        ApplyPauliFromBitString(PauliY, true, bits, [q[0]]);
        ApplyPauliFromBitString(PauliX, false, bits, [q[0]]);
            IncByLE([q[3]], [q[0], q[4]]);
            S(q[6]);
            R1Frac(6, 1, q[4]);
            ApplyCNOTChain([q[2], q[1], q[4], q[6]]);
            IncByLE([q[2], q[4], q[5]], [q[1], q[3], q[6]]);
        }
                Controlled __GenBlock_03d80786([q[4]], [q[0], q[1], q[2], q[3], q[5], q[6], q[7]]);
        }
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Ctl {
        operation __ControlledBody_b2548fc5(q : Qubit[]) : Unit is Adj + Ctl {
            operation __ForLoopZeroBody_caac779b(q : Qubit[]) : Unit is Adj + Ctl {
                operation __IfBody_dde0cc4f(q : Qubit[]) : Unit is Adj + Ctl {
                        operation __IfBody_bb092770(q : Qubit[]) : Unit is Adj + Ctl {
                                operation __InlineApplyIfRelationL_8c3b7e30(q : Qubit[]) : Unit is Adj + Ctl {
                                    operation __InlineApplyIfRelationLE_c499ce8d(q : Qubit[]) : Unit is Adj + Ctl {
                                        operation __InlineApplyIfRelationL_5e2d01e1(q : Qubit[]) : Unit is Adj + Ctl {
                                                operation __GenBlock_90bb5fee(q : Qubit[]) : Unit is Adj + Ctl {
                                        
                                            
                                        }
                                                Controlled Adjoint __GenBlock_90bb5fee([q[3]], [q[0], q[1], q[2]]);
                                        }
                                        let x = [q[3]];
                                        let target = [q[0], q[1], q[2], q[4]];
                                        ApplyIfEqualL(__InlineApplyIfRelationL_5e2d01e1, 1L, x, target);
                                    }
                                    let x = [q[5]];
                                    let y = [q[2]];
                                    let target = [q[0], q[1], q[3], q[4], q[6]];
                                    ApplyIfLessOrEqualLE(__InlineApplyIfRelationLE_c499ce8d, x, y, target);
                                }
                                let x = [q[0], q[4]];
                                let target = [q[1], q[2], q[3], q[5], q[6], q[7], q[8]];
                                ApplyIfGreaterL(__InlineApplyIfRelationL_8c3b7e30, 1L, x, target);
                        }
                        
                        operation __ElseBody_bb092770(q : Qubit[]) : Unit is Adj + Ctl {
                                    operation __GenBlock_f73e5d15(q : Qubit[]) : Unit is Adj + Ctl {
                            
                                MAJ(q[4], q[0], q[1]);
                                T(q[3]);
                                Z(q[1]);
                            }
                                    Controlled Adjoint __GenBlock_f73e5d15([q[1], q[2], q[6], q[7]], [q[0], q[3], q[4], q[5], q[8]]);
                        }
                        
                        if __RandomFlag_2a2e6c08() {
                            __IfBody_bb092770(q);
                        } else {
                            __ElseBody_bb092770(q);
                        }
                }
                
                operation __ElseBody_dde0cc4f(q : Qubit[]) : Unit is Adj + Ctl {
                            operation __GenBlock_4b6c90ba(q : Qubit[]) : Unit is Adj + Ctl {
                    
                        CZ(q[1], q[5]);
                        ApplyQFT(q);
                        ApplyP(PauliZ, q[1]);
                        CNOT(q[1], q[0]);
                        CX(q[4], q[5]);
                    }
                            Controlled Adjoint __GenBlock_4b6c90ba([q[1], q[3], q[4]], [q[0], q[2], q[5], q[6], q[7], q[8]]);
                }
                
                if __RandomFlag_c8bab292() {
                    __IfBody_dde0cc4f(q);
                } else {
                    __ElseBody_dde0cc4f(q);
                }
            }
        }
        ApplyControlledOnBitString([false], __ControlledBody_b2548fc5, [q[2]], [q[0], q[1], q[3], q[4], q[5], q[6], q[7], q[8], q[9]]);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Adj {
        operation __InlineApplyIfRelationL_74b827cc(q : Qubit[]) : Unit is Adj + Ctl {
                operation __GenBlock_613571a4(q : Qubit[]) : Unit is Adj + Ctl {
        
            IncByIUsingIncByLE(RippleCarryTTKIncByLE, 0, [q[1]]);
            T(q[1]);
            ApplyCNOTChain([q[0]]);
            ApplyP(PauliZ, q[0]);
            CX(q[0], q[1]);
            IncByL(IntAsBigInt(2), [q[0], q[1]]);
            CZ(q[0], q[1]);
            S(q[1]);
        }
                __GenBlock_613571a4(q);
        }
        let x = [q[11]];
        let target = [q[3], q[10]];
        ApplyIfEqualL(__InlineApplyIfRelationL_74b827cc, 0L, x, target);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            Controlled ApplyRandomBlock0([q[3], q[7], q[10]], [q[0], q[1], q[2], q[4], q[5], q[6], q[8], q[9], q[11]]);
            Controlled ApplyRandomBlock1([q[6], q[11]], [q[0], q[1], q[2], q[3], q[4], q[5], q[7], q[8], q[9], q[10]]);
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