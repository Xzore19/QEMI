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



function __RandomFlag_04db24f7() : Bool {
    let b0 = false;
    let b1 = false;
    let b2 = false;
    let b3 = not true;
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_94d8d239() : Bool {
    let b0 = not ResultAsBool(Zero);
    let b1 = ResultAsBool(Zero);
    let b2 = ResultAsBool(One);
    let b3 = ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_6d4bc6f0() : Bool {
    let b0 = not ResultAsBool(Zero);
    let b1 = ResultAsBool(One);
    let b2 = ResultAsBool(One);
    let b3 = ResultAsBool(Zero);
    return Xor(Xor(b0, b1), Xor(b2, b3));
}
function __RandomFlag_2e8319c4() : Bool {
    let b0 = not ResultAsBool(Zero);
    let b1 = ResultAsBool(Zero);
    let b2 = not ResultAsBool(Zero);
    let b3 = ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}



    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Ctl {
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Ctl {
        operation __ForLoopBody_d7f48e3e(q : Qubit[]) : Unit is Ctl {
                operation __GenBlock_0316bb82(q : Qubit[]) : Unit is Ctl {
        
            X(q[1]);
            CX(q[2], q[0]);
            IncByLEUsingAddLE(LookAheadDKRSAddLE, RippleCarryCGAddLE, [q[1]], [q[0]]);
            RFrac(PauliZ, 2, 5, q[1]);
            CCNOT(q[1], q[2], q[0]);
            Exp([PauliY], 2.544397, [q[2]]);
            CZ(q[2], q[1]);
        }
                Controlled __GenBlock_0316bb82([q[1], q[3]], [q[0], q[2], q[4]]);
        }
        for i in 1..3 {
            Controlled __ForLoopBody_d7f48e3e([q[1]], [q[0], q[2], q[3], q[4], q[5]]);
        }
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Ctl {
        operation __ControlledBody_6c5ef92b(q : Qubit[]) : Unit is Adj + Ctl {
            operation __InlineIfElseDeadcode_7f115821(q : Qubit[]) : Unit is Adj + Ctl {
                if __RandomFlag_2e8319c4() {
                        operation __ForLoopZeroBody_9ffbbe91(q : Qubit[]) : Unit is Adj + Ctl {
                                operation __GenBlock_646d02e8(q : Qubit[]) : Unit is Adj + Ctl {
                        
                            CX(q[3], q[2]);
                            IncByI(21, [q[0], q[1], q[2], q[3], q[4]]);
                            S(q[1]);
                            SWAP(q[1], q[4]);
                            SWAP(q[1], q[3]);
                        }
                                __GenBlock_646d02e8(q);
                        }
                } else {
                }
            }
            
            __InlineIfElseDeadcode_7f115821(q);
        }
        ApplyControlledOnInt(1, __ControlledBody_6c5ef92b, [q[1], q[5]], [q[0], q[2], q[3], q[4], q[6]]);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[8] {
            X(q[0]);
            X(q[3]);
            X(q[4]);
            Controlled ApplyRandomBlock0([q[4]], [q[0], q[1], q[2], q[3], q[5], q[6], q[7]]);
            Controlled ApplyRandomBlock1([q[0], q[3]], [q[1], q[2], q[4], q[5], q[6], q[7]]);
            Controlled ApplyRandomBlock2([q[4]], [q[0], q[1], q[2], q[3], q[5], q[6], q[7]]);
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