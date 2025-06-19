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



function __RandomFlag_8407735b() : Bool {
    let b0 = not ResultAsBool(Zero);
    let b1 = ResultAsBool(One);
    let b2 = not ResultAsBool(Zero);
    let b3 = not ResultAsBool(One);
    return (b0 and b1) or (b2 and not b3);
}



    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Adj + Ctl {
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj + Ctl {
        operation __ControlledBody_e43bd8a0(q : Qubit[]) : Unit is Adj + Ctl {
            operation __InlineApplyIfRelationL_9365999c(q : Qubit[]) : Unit is Adj + Ctl {
                operation __InlineApplyIfRelationLE_d36655d1(q : Qubit[]) : Unit is Adj + Ctl {
                    operation __ForLoopBody_53b6da28(q : Qubit[]) : Unit is Adj + Ctl {
                        operation __ForLoopZeroBody_6e214d4d(q : Qubit[]) : Unit is Adj + Ctl {
                                operation __GenBlock_0f13b5dc(q : Qubit[]) : Unit is Adj + Ctl {
                        
                            Rx(3.203308, q[0]);
                            IncByL(IntAsBigInt(0), [q[0]]);
                            R1(5.531504, q[0]);
                        }
                                __GenBlock_0f13b5dc(q);
                        }
                    }
                    for i in 1..3 {
                        Controlled Adjoint __ForLoopBody_53b6da28([q[2]], [q[0], q[1]]);
                    }
                }
                let x = [q[1]];
                let y = [q[3]];
                let target = [q[0], q[2], q[4]];
                ApplyIfLessOrEqualLE(__InlineApplyIfRelationLE_d36655d1, x, y, target);
            }
            let x = [q[4]];
            let target = [q[0], q[1], q[2], q[3], q[7]];
            ApplyIfLessOrEqualL(__InlineApplyIfRelationL_9365999c, 1L, x, target);
        }
        ApplyControlledOnBitString([true, false], __ControlledBody_e43bd8a0, [q[4], q[7]], [q[0], q[1], q[2], q[3], q[5], q[6], q[8], q[9]]);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit {
        operation __ForLoopBody_0e5a9017(q : Qubit[]) : Unit {
                operation __GenBlock_7918bbfe(q : Qubit[]) : Unit {
        
            MAJ(q[0], q[3], q[2]);
            SX(q[2]);
            ResetAll([q[2], q[10], q[4], q[0], q[11], q[3], q[1], q[9], q[8]]);
            SWAP(q[0], q[4]);
            SX(q[3]);
            ReflectAboutInteger(1, [q[11]]);
            ResetAll([q[0], q[1], q[2], q[5], q[11]]);
        PreparePureStateD(
            [
                0.226344,
                0.073033,
                0.094796,
                0.158057,
                0.030186,
                0.065853,
                0.015837,
                0.012286,
                0.208705,
                0.152761,
                0.019662,
                0.248581,
                0.290438,
                0.269376,
                0.072565,
                0.140338,
                0.129738,
                0.258909,
                0.173105,
                0.093581,
                0.051909,
                0.235488,
                0.195470,
                0.085517,
                0.110290,
                0.210573,
                0.230066,
                0.308343,
                0.269169,
                0.141415,
                0.248678,
                0.088346
            ],
            [q[0], q[1], q[2], q[5], q[11]]
        );
        }
                __GenBlock_7918bbfe(q);
        }
        for i in 1..3 {
            __ForLoopBody_0e5a9017(q);
        }
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            X(q[1]);
            X(q[7]);
            X(q[8]);
            Controlled Adjoint ApplyRandomBlock0([q[8]], [q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[9], q[10], q[11]]);
            Controlled Adjoint ApplyRandomBlock1([q[1], q[7]], [q[0], q[2], q[3], q[4], q[5], q[6], q[8], q[9], q[10], q[11]]);
            ApplyRandomBlock2(q);
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