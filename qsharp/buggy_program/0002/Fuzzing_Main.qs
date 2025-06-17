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

    operation MySingleBlock_30aecd08(q : Qubit) : Unit is Adj + Ctl {
        Rx(2.437572, q);
        Y(q);
        S(q);
    }
    operation MySingleBlock_3abc4eeb(q : Qubit) : Unit is Adj + Ctl {
        R1(2.603796, q);
        Z(q);
        I(q);
    }

function __RandomFlag_beb4b53a() : Bool {
    let b0 = not true;
    let b1 = not false;
    let b2 = true;
    let b3 = not true;
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_b1c5e849() : Bool {
    let b0 = true;
    let b1 = true;
    let b2 = not false;
    let b3 = not true;
    return Xor(Xor(b0, b1), Xor(b2, b3));
}



    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Adj + Ctl {
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj {
        operation __IfBody_022e8a62(q : Qubit[]) : Unit is Adj {
                    operation __GenBlock_71824932(q : Qubit[]) : Unit is Adj {
            
                SX(q[7]);
                CY(q[7], q[4]);
                SWAP(q[4], q[6]);
                X(q[5]);
                ApplyToEachA(MySingleBlock_30aecd08, q);
                R1(1.995845, q[3]);
                Relabel([q[2], q[3], q[7]], [q[7], q[3], q[2]]);
            }
                    __GenBlock_71824932(q);
        }
        
        operation __ElseBody_022e8a62(q : Qubit[]) : Unit is Adj {
                operation __InlineApplyIfRelationL_d1f316c4(q : Qubit[]) : Unit is Adj + Ctl {
                    operation __InlineApplyIfRelationL_5be0287d(q : Qubit[]) : Unit is Adj + Ctl {
                            operation __GenBlock_bb715480(q : Qubit[]) : Unit is Adj + Ctl {
                    
                        I(q[0]);
                        Ry(1.184371, q[0]);
                        SX(q[0]);
                    }
                            __GenBlock_bb715480(q);
                    }
                    let x = [q[1]];
                    let target = [q[5]];
                    ApplyIfLessL(__InlineApplyIfRelationL_5be0287d, 1L, x, target);
                    operation __GenBlock_460c6d95(q : Qubit[]) : Unit is Adj + Ctl {
                
                    SWAP(q[0], q[1]);
                }
                    Controlled Adjoint __GenBlock_460c6d95([q[2], q[3], q[4]], [q[0], q[1], q[5]]);
                }
                let x = [q[0]];
                let target = [q[1], q[2], q[3], q[4], q[5], q[6]];
                ApplyIfEqualL(__InlineApplyIfRelationL_d1f316c4, 1L, x, target);
                operation __GenBlock_38377994(q : Qubit[]) : Unit is Adj {
            
                S(q[1]);
                X(q[6]);
            }
                __GenBlock_38377994(q);
        }
        
        if __RandomFlag_b1c5e849() {
            Adjoint __IfBody_022e8a62(q);
        } else {
            Adjoint __ElseBody_022e8a62(q);
        }
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Adj {
        operation __ControlledBody_977ae7cc(q : Qubit[]) : Unit is Adj + Ctl {
                operation __GenBlock_39354e13(q : Qubit[]) : Unit is Adj + Ctl {
        
            ApplyToEachCA(MySingleBlock_3abc4eeb, q);
            H(q[2]);
            CZ(q[0], q[2]);
            Rz(4.044672, q[2]);
            RippleCarryTTKIncByLE([q[4]], [q[0]]);
            S(q[1]);
            Y(q[1]);
        }
                Controlled Adjoint __GenBlock_39354e13([q[0], q[1]], [q[2], q[3], q[4], q[5], q[6]]);
        }
        ApplyControlledOnInt(0, __ControlledBody_977ae7cc, [q[5]], [q[0], q[1], q[2], q[3], q[4], q[6], q[7]]);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[8] {
            X(q[2]);
            X(q[3]);
            Controlled Adjoint ApplyRandomBlock0([q[2], q[3]], [q[0], q[1], q[4], q[5], q[6], q[7]]);
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
            ResetAll(q);
            return [r0, r1, r2, r3, r4, r5, r6, r7];
        }
    }
}