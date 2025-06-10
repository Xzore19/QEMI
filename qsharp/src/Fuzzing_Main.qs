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



function __RandomFlag_6d24ef69() : Bool {
    let b0 = not ResultAsBool(Zero);
    let b1 = ResultAsBool(One);
    let b2 = not ResultAsBool(One);
    let b3 = not ResultAsBool(Zero);
    return Xor(Xor(b0, b1), Xor(b2, b3));
}
function __RandomFlag_a173ef94() : Bool {
    let b0 = not true;
    let b1 = not false;
    let b2 = not true;
    let b3 = not false;
    return (b0 and b1) or (b2 and not b3);
}



    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Ctl {
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj {
        operation __InlineApplyIfRelationLE_d2b8c18d(q : Qubit[]) : Unit is Adj + Ctl {
                operation __GenBlock_4da8785f(q : Qubit[]) : Unit is Adj + Ctl {
        
            IncByLUsingIncByLE(RippleCarryTTKIncByLE, IntAsBigInt(7), [q[0], q[1], q[3]]);
            ReflectAboutInteger(1, [q[3], q[5], q[6]]);
            IncByLUsingIncByLE(RippleCarryTTKIncByLE, IntAsBigInt(0), [q[1], q[2], q[4]]);
            MAJ(q[1], q[6], q[4]);
            FourierTDIncByLE([q[3], q[4], q[6]], [q[0], q[1], q[5]]);
            IncByL(IntAsBigInt(5), [q[0], q[1], q[2], q[5]]);
            RippleCarryTTKIncByLE([q[1], q[2], q[6]], [q[3], q[4], q[5]]);
            IncByL(IntAsBigInt(113), [q[0], q[1], q[2], q[3], q[4], q[5], q[6]]);
        }
                __GenBlock_4da8785f(q);
        }
        let x = [q[7]];
        let y = [q[0]];
        let target = [q[2], q[3], q[4], q[5], q[9], q[10], q[11]];
        ApplyIfEqualLE(__InlineApplyIfRelationLE_d2b8c18d, x, y, target);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Ctl {
        operation __ForLoopBody_af994a33(q : Qubit[]) : Unit is Ctl {
                operation __GenBlock_e31cb310(q : Qubit[]) : Unit is Ctl {
        
            IncByL(IntAsBigInt(4), [q[1], q[2], q[6]]);
            IncByLEUsingAddLE(LookAheadDKRSAddLE, RippleCarryCGAddLE, [q[0], q[1], q[3]], [q[2], q[5], q[6]]);
            IncByI(0, [q[0], q[1], q[4], q[5], q[6]]);
            IncByLUsingIncByLE(RippleCarryTTKIncByLE, IntAsBigInt(1), [q[0], q[1], q[2], q[3], q[5]]);
            IncByLUsingIncByLE(RippleCarryTTKIncByLE, IntAsBigInt(19), [q[0], q[1], q[2], q[3], q[5]]);
            IncByLE([q[0]], [q[1], q[4]]);
            IncByLEUsingAddLE(LookAheadDKRSAddLE, RippleCarryCGAddLE, [q[3], q[5]], [q[2], q[6]]);
        }
                Controlled __GenBlock_e31cb310([q[3], q[4]], [q[0], q[1], q[2], q[5], q[6], q[7], q[8]]);
        }
        for i in 1..3 {
            __ForLoopBody_af994a33(q);
        }
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            Controlled ApplyRandomBlock0([q[3], q[5], q[11]], [q[0], q[1], q[2], q[4], q[6], q[7], q[8], q[9], q[10]]);
            Adjoint ApplyRandomBlock1(q);
            Controlled ApplyRandomBlock2([q[4], q[9], q[10]], [q[0], q[1], q[2], q[3], q[5], q[6], q[7], q[8], q[11]]);
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