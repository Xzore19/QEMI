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



function __RandomFlag_2cf92b28() : Bool {
    let b0 = not ResultAsBool(Zero);
    let b1 = not ResultAsBool(Zero);
    let b2 = not ResultAsBool(Zero);
    let b3 = ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}



    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Ctl {
        // --- DEADCODE START ---
        let target = [q[0], q[1], q[3], q[4]]; 
        operation __InlineApplyIfRelation_295e0d81(q : Qubit[]) : Unit is Adj + Ctl {
                operation __GenBlock_24047536(q : Qubit[]) : Unit is Adj + Ctl {
        
            H(q[2]);
            H(q[3]);
            Ryy(2.305261, q[1], q[3]);
            MAJ(q[3], q[0], q[2]);
            ApplyPauli([PauliY], [q[2]]);
            CCNOT(q[1], q[2], q[0]);
            Rzz(3.769804, q[1], q[0]);
            T(q[1]);
        }
                __GenBlock_24047536(q);
        }
        use x = Qubit[2];
        X(x[1]);
        use y = Qubit[2];
        X(y[0]);
        Controlled Adjoint ApplyIfLessOrEqualLE([q[2]], (__InlineApplyIfRelation_295e0d81, x, y, target));
        X(x[1]);
        X(y[0]);
        // --- DEADCODE END ---
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit {
        operation __InlineApplyIfRelationL_14cbdfe7(q : Qubit[]) : Unit is Adj + Ctl {
                operation __GenBlock_4ec31524(q : Qubit[]) : Unit is Adj + Ctl {
        
            ApplyP(PauliY, q[0]);
            R1Frac(7, 6, q[0]);
            IncByI(0, [q[0]]);
            ApplyCNOTChain([q[0]]);
            S(q[0]);
            S(q[0]);
            Y(q[0]);
        }
                Controlled Adjoint __GenBlock_4ec31524([q[0]], [q[1]]);
        }
        let x = [q[3], q[4], q[5]];
        let target = [q[0], q[2]];
        ApplyIfGreaterOrEqualL(__InlineApplyIfRelationL_14cbdfe7, 6L, x, target);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Ctl {
        operation __IfBody_c4f8d04f(q : Qubit[]) : Unit is Ctl {
                operation __ForLoopBody_5d9373a1(q : Qubit[]) : Unit is Ctl {
                    operation __ForLoopBody_46019af2(q : Qubit[]) : Unit is Ctl {
                            operation __GenBlock_e88587e4(q : Qubit[]) : Unit is Ctl {
                    
                        H(q[2]);
                        Exp([PauliY, PauliY, PauliZ], 5.919024, [q[1], q[2], q[0]]);
                        X(q[2]);
                    }
                            Controlled __GenBlock_e88587e4([q[3]], [q[0], q[1], q[2]]);
                    }
                    for i in 1..3 {
                        __ForLoopBody_46019af2(q);
                    }
                    operation __GenBlock_2242daf7(q : Qubit[]) : Unit is Ctl {
                
                    let n = 1;
                ApplyPauliFromInt(PauliZ, true, n, [q[0]]);
                ApplyPauliFromInt(PauliX, false, n, [q[0]]);
                }
                    __GenBlock_2242daf7(q);
                }
                for i in 1..3 {
                    Controlled __ForLoopBody_5d9373a1([q[4]], [q[0], q[1], q[2], q[3]]);
                }
                operation __GenBlock_a9bd8fde(q : Qubit[]) : Unit is Ctl {
            
                IncByLEUsingAddLE(LookAheadDKRSAddLE, RippleCarryCGAddLE, [q[1]], [q[2]]);
                IncByLEUsingAddLE(LookAheadDKRSAddLE, RippleCarryCGAddLE, [q[2]], [q[0]]);
            }
                Controlled __GenBlock_a9bd8fde([q[1], q[3]], [q[0], q[2], q[4]]);
        }
        
        operation __ElseBody_c4f8d04f(q : Qubit[]) : Unit is Ctl {
                    operation __GenBlock_5246a5a7(q : Qubit[]) : Unit is Ctl {
            
                let bits = [true];
            ApplyPauliFromBitString(PauliZ, true, bits, [q[0]]);
            ApplyPauliFromBitString(PauliY, false, bits, [q[0]]);
                FourierTDIncByLE([q[1]], [q[2]]);
                Exp([PauliX], 3.826865, [q[0]]);
                CY(q[0], q[2]);
                ApplyCNOTChain([q[3], q[1]]);
                ApplyPauli([PauliX, PauliY, PauliY], [q[2], q[1], q[3]]);
                T(q[2]);
            }
                    Controlled __GenBlock_5246a5a7([q[2]], [q[0], q[1], q[3], q[4]]);
        }
        
        if __RandomFlag_2cf92b28() {
            __IfBody_c4f8d04f(q);
        } else {
            __ElseBody_c4f8d04f(q);
        }
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[6] {
            X(q[5]);
            Controlled ApplyRandomBlock0([q[5]], [q[0], q[1], q[2], q[3], q[4]]);
            ApplyRandomBlock1(q);
            Controlled ApplyRandomBlock2([q[1]], [q[0], q[2], q[3], q[4], q[5]]);
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