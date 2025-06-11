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



function __RandomFlag_e79f3195() : Bool {
    let b0 = false;
    let b1 = not false;
    let b2 = true;
    let b3 = not true;
    return (b0 and b1) or (b2 and not b3);
}



    operation ApplyRandomBlock0(q : Qubit[]) : Unit {
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj + Ctl {
        operation __IfBody_a2847efe(q : Qubit[]) : Unit is Adj + Ctl {
                    operation __GenBlock_89235536(q : Qubit[]) : Unit is Adj + Ctl {
            
                H(q[3]);
                Y(q[0]);
                RFrac(PauliX, 4, 2, q[4]);
                T(q[7]);
                X(q[4]);
                H(q[1]);
                SwapReverseRegister([q[0], q[2]]);
            }
                    Controlled Adjoint __GenBlock_89235536([q[6]], [q[0], q[1], q[2], q[3], q[4], q[5], q[7], q[8], q[9], q[10]]);
        }
        
        operation __ElseBody_a2847efe(q : Qubit[]) : Unit is Adj + Ctl {
                    operation __GenBlock_72918a6f(q : Qubit[]) : Unit is Adj + Ctl {
            
                I(q[6]);
                IncByLE([q[2]], [q[1], q[4]]);
                H(q[0]);
                CZ(q[7], q[6]);
                CY(q[6], q[0]);
                CY(q[4], q[7]);
                MAJ(q[2], q[7], q[0]);
            }
                    Controlled Adjoint __GenBlock_72918a6f([q[1], q[8], q[9]], [q[0], q[2], q[3], q[4], q[5], q[6], q[7], q[10]]);
        }
        
        if __RandomFlag_e79f3195() {
            __IfBody_a2847efe(q);
        } else {
            __ElseBody_a2847efe(q);
        }
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Adj {
        operation __ControlledBody_b486305a(q : Qubit[]) : Unit is Adj + Ctl {
                operation __GenBlock_cf201fd9(q : Qubit[]) : Unit is Adj + Ctl {
        
            CCNOT(q[4], q[7], q[6]);
            Ry(2.072976, q[4]);
            Ry(5.082413, q[2]);
            Ry(4.007366, q[5]);
            IncByL(IntAsBigInt(6), [q[2], q[3], q[6], q[8], q[9], q[10]]);
            CNOT(q[3], q[1]);
            Ryy(5.847539, q[0], q[6]);
            Rzz(0.736585, q[4], q[5]);
        }
                __GenBlock_cf201fd9(q);
        }
        ApplyControlledOnInt(1, __ControlledBody_b486305a, [q[4]], [q[0], q[1], q[2], q[3], q[5], q[6], q[7], q[8], q[9], q[10], q[11]]);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            X(q[6]);
            ApplyRandomBlock0(q);
            Controlled Adjoint ApplyRandomBlock1([q[6]], [q[0], q[1], q[2], q[3], q[4], q[5], q[7], q[8], q[9], q[10], q[11]]);
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