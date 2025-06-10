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



function __RandomFlag_f9ae1b61() : Bool {
    let b0 = not true;
    let b1 = not false;
    let b2 = not true;
    let b3 = not true;
    return Xor(Xor(b0, b1), Xor(b2, b3));
}



    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Adj + Ctl {
        operation __ForLoopZeroBody_eaa3218a(q : Qubit[]) : Unit is Adj + Ctl {
            operation __ForLoopBody_e74671d8(q : Qubit[]) : Unit is Adj + Ctl {
                    FourierTDIncByLE([q[1], q[7]], [q[0], q[5]]);
                    SwapReverseRegister([q[1], q[6], q[7]]);
                    MAJ(q[2], q[6], q[3]);
                    ReflectAboutInteger(1, [q[3]]);
                    ReflectAboutInteger(62, [q[0], q[1], q[3], q[4], q[5], q[6], q[7]]);
                    SwapReverseRegister([q[0], q[1], q[2], q[3], q[5], q[6]]);
            }
            for i in 1..3 {
                __ForLoopBody_e74671d8(q);
            }
        }
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Ctl {
        operation __InlineApplyIfRelationLE_fd5a3831(q : Qubit[]) : Unit is Adj + Ctl {
            operation __InlineApplyIfRelationLE_25b55b8f(q : Qubit[]) : Unit is Adj + Ctl {
                    ReflectAboutInteger(0, [q[0]]);
                    ReflectAboutInteger(1, [q[0]]);
                    ReflectAboutInteger(0, [q[0]]);
                    ReflectAboutInteger(0, [q[0]]);
                    ReflectAboutInteger(1, [q[0]]);
                    ReflectAboutInteger(1, [q[0]]);
                    ReflectAboutInteger(0, [q[0]]);
            }
            let x = [q[3], q[4]];
            let y = [q[0], q[2]];
            let target = [q[5]];
            ApplyIfLessOrEqualLE(__InlineApplyIfRelationLE_25b55b8f, x, y, target);
        }
        let x = [q[8]];
        let y = [q[6]];
        let target = [q[1], q[2], q[3], q[5], q[7], q[9], q[10]];
        ApplyIfLessOrEqualLE(__InlineApplyIfRelationLE_fd5a3831, x, y, target);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Adj + Ctl {
        operation __IfBody_cfeb1677(q : Qubit[]) : Unit is Adj + Ctl {
                operation __InlineApplyIfRelationL_95569c43(q : Qubit[]) : Unit is Adj + Ctl {
                    operation __ForLoopBody_fbfc266a(q : Qubit[]) : Unit is Adj + Ctl {
                            ReflectAboutInteger(1, [q[0]]);
                            MAJ(q[0], q[1], q[2]);
                            ReflectAboutInteger(0, [q[1], q[2]]);
                            SwapReverseRegister([q[1], q[2]]);
                    }
                    for i in 1..3 {
                        Controlled Adjoint __ForLoopBody_fbfc266a([q[0]], [q[1], q[2], q[3]]);
                    }
                }
                let x = [q[1], q[4]];
                let target = [q[0], q[3], q[6], q[7]];
                ApplyIfLessL(__InlineApplyIfRelationL_95569c43, 1L, x, target);
        }
        
        operation __ElseBody_cfeb1677(q : Qubit[]) : Unit is Adj + Ctl {
                operation __ForLoopBody_d2c0be17(q : Qubit[]) : Unit is Adj + Ctl {
                    operation __ForLoopBody_380dcc1d(q : Qubit[]) : Unit is Adj + Ctl {
                            MAJ(q[2], q[0], q[1]);
                            FourierTDIncByLE([q[2]], [q[1]]);
                            MAJ(q[0], q[1], q[2]);
                    }
                    for i in 1..3 {
                        Controlled Adjoint __ForLoopBody_380dcc1d([q[0], q[2], q[3]], [q[1], q[4], q[5]]);
                    }
                }
                for i in 1..3 {
                    Controlled Adjoint __ForLoopBody_d2c0be17([q[4], q[5]], [q[0], q[1], q[2], q[3], q[6], q[7]]);
                }
        }
        
        if __RandomFlag_f9ae1b61() {
            __IfBody_cfeb1677(q);
        } else {
            __ElseBody_cfeb1677(q);
        }
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            Controlled Adjoint ApplyRandomBlock0([q[2], q[3], q[8], q[11]], [q[0], q[1], q[4], q[5], q[6], q[7], q[9], q[10]]);
            Controlled ApplyRandomBlock1([q[11]], [q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9], q[10]]);
            Controlled Adjoint ApplyRandomBlock2([q[5], q[7], q[8], q[9]], [q[0], q[1], q[2], q[3], q[4], q[6], q[10], q[11]]);
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