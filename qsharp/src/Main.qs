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



function __RandomFlag_a7225d3c() : Bool {
    let b0 = not false;
    let b1 = true;
    let b2 = not false;
    let b3 = true;
    return Xor(Xor(b0, b1), Xor(b2, b3));
}



    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Adj {
        // --- DEADCODE START ---
        let target = [q[0], q[2], q[3], q[4], q[5]]; 
        operation __InlineApplyIfRelation_457e7d22(q : Qubit[]) : Unit is Adj + Ctl {
            operation __ForLoopBody_0f9fd905(q : Qubit[]) : Unit is Adj + Ctl {
                operation __ForLoopBody_c6129b19(q : Qubit[]) : Unit is Adj + Ctl {
                        operation __GenBlock_77bff183(q : Qubit[]) : Unit is Adj + Ctl {
                
                    Y(q[0]);
                    R1(5.287182, q[0]);
                    RFrac(PauliZ, 13, 10, q[0]);
                    RFrac(PauliX, 2, 2, q[0]);
                }
                        Controlled Adjoint __GenBlock_77bff183([q[0]], [q[1]]);
                }
                for i in 1..3 {
                    Controlled Adjoint __ForLoopBody_c6129b19([q[0], q[3]], [q[1], q[2]]);
                }
                operation __GenBlock_6ddfe6cb(q : Qubit[]) : Unit is Adj + Ctl {
            
                CX(q[2], q[0]);
                CZ(q[3], q[0]);
            }
                __GenBlock_6ddfe6cb(q);
            }
            for i in 1..3 {
                Controlled Adjoint __ForLoopBody_0f9fd905([q[3]], [q[0], q[1], q[2], q[4]]);
            }
            operation __GenBlock_19565382(q : Qubit[]) : Unit is Adj + Ctl {
        
            let n = 6;
        ApplyPauliFromInt(PauliY, true, n, [q[0], q[1], q[2], q[3]]);
        ApplyPauliFromInt(PauliX, false, n, [q[0], q[1], q[2], q[3]]);
            ApplyCNOTChain([q[0], q[1], q[4], q[3], q[2]]);
        }
            __GenBlock_19565382(q);
        }
        use x = Qubit[2];
        X(x[0]);
        X(x[1]);
        Controlled Adjoint ApplyIfGreaterOrEqualL([q[1]], (__InlineApplyIfRelation_457e7d22, 0L, x, target));
        X(x[0]);
        X(x[1]);
        // --- DEADCODE END ---
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj {
        operation __InlineApplyIfRelationLE_7c1abfeb(q : Qubit[]) : Unit is Adj + Ctl {
            operation __DeadBlock_639aa1e7(q : Qubit[]) : Unit is Adj + Ctl {
                        operation __GenBlock_5f73789c(q : Qubit[]) : Unit is Adj + Ctl {
                
                    S(q[0]);
                    T(q[0]);
                    Rx(0.052069, q[0]);
                    R1(4.912861, q[0]);
                    R1(5.616016, q[0]);
                    IncByI(1, [q[0]]);
                }
                        __GenBlock_5f73789c(q);
            }
            
            operation __InlineIfElseDeadcode_458b8fa0(q : Qubit[]) : Unit is Adj + Ctl {
                use ctrl = Qubit();
                within { } apply {
                    // --- DEADCODE START ---
                    Controlled __DeadBlock_639aa1e7([ctrl], q);
                    // --- DEADCODE END ---
                }
                    operation __ForLoopBody_5edbc4af(q : Qubit[]) : Unit is Adj + Ctl {
                            operation __GenBlock_e14efc82(q : Qubit[]) : Unit is Adj + Ctl {
                    
                        Exp([PauliX], 1.08835, [q[0]]);
                        RFrac(PauliX, 2, 5, q[0]);
                        R1(2.685419, q[0]);
                        Z(q[0]);
                    }
                            __GenBlock_e14efc82(q);
                    }
                    for i in 1..3 {
                        __ForLoopBody_5edbc4af(q);
                    }
                    operation __GenBlock_7d0c3b07(q : Qubit[]) : Unit is Adj + Ctl {
                
                    ReflectAboutInteger(0, [q[0]]);
                    let n = 1;
                ApplyPauliFromInt(PauliZ, true, n, [q[0]]);
                ApplyPauliFromInt(PauliX, false, n, [q[0]]);
                }
                    __GenBlock_7d0c3b07(q);
            }
            
            __InlineIfElseDeadcode_458b8fa0(q);
        }
        let x = [q[2], q[3]];
        let y = [q[0], q[1]];
        let target = [q[5]];
        ApplyIfLessLE(__InlineApplyIfRelationLE_7c1abfeb, x, y, target);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Adj {
        operation __IfBody_d4cb248b(q : Qubit[]) : Unit is Adj {
                operation __InlineApplyIfRelationLE_0ab95d90(q : Qubit[]) : Unit is Adj + Ctl {
                        operation __GenBlock_48cded12(q : Qubit[]) : Unit is Adj + Ctl {
                
                    ApplyPauli([PauliZ], [q[0]]);
                    ApplyP(PauliX, q[0]);
                    S(q[0]);
                    ReflectAboutInteger(1, [q[0]]);
                    ApplyCNOTChain([q[0]]);
                }
                        __GenBlock_48cded12(q);
                }
                let x = [q[0], q[5]];
                let y = [q[2], q[4]];
                let target = [q[1]];
                ApplyIfLessOrEqualLE(__InlineApplyIfRelationLE_0ab95d90, x, y, target);
                operation __GenBlock_d4afcfc0(q : Qubit[]) : Unit is Adj {
            
                IncByI(12, [q[0], q[1], q[3], q[5]]);
                ApplyP(PauliZ, q[3]);
            }
                __GenBlock_d4afcfc0(q);
        }
        
        operation __ElseBody_d4cb248b(q : Qubit[]) : Unit is Adj {
                    operation __GenBlock_8f57bfca(q : Qubit[]) : Unit is Adj {
            
                IncByL(IntAsBigInt(5), [q[0], q[2], q[5]]);
                Rzz(3.380513, q[5], q[1]);
                IncByI(14, [q[0], q[1], q[2], q[5]]);
                Ry(4.602815, q[0]);
                H(q[0]);
                let bits = [false, false, false, false, true, false];
            ApplyPauliFromBitString(PauliZ, true, bits, [q[0], q[1], q[2], q[3], q[4], q[5]]);
            ApplyPauliFromBitString(PauliY, false, bits, [q[0], q[1], q[2], q[3], q[4], q[5]]);
                ApplyP(PauliZ, q[1]);
            }
                    __GenBlock_8f57bfca(q);
        }
        
        if __RandomFlag_a7225d3c() {
            Adjoint __IfBody_d4cb248b(q);
        } else {
            Adjoint __ElseBody_d4cb248b(q);
        }
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[6] {
            Adjoint ApplyRandomBlock0(q);
            Adjoint ApplyRandomBlock1(q);
            Adjoint ApplyRandomBlock2(q);
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