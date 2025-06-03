namespace Main {

    open Std.Arithmetic;
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Math;
    open Std.Measurement;
    open Std.StatePreparation;



    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Adj {
        // --- DEADCODE START ---
        operation __InlineApplyIfRelation_e2e22bda(q : Qubit[]) : Unit is Adj + Ctl {
            operation __ForLoopBody_ded9c2d6(q : Qubit[]) : Unit is Adj + Ctl {
                operation __InlineApplyIfRelationLE_8d95f851(q : Qubit[]) : Unit is Adj + Ctl {
                    operation __InlineApplyIfRelationLE_3f1a5865(q : Qubit[]) : Unit is Adj + Ctl {
                        operation __IfBody_926b1cd2(q : Qubit[]) : Unit is Adj + Ctl {
                                    S(q[0]);
                                    T(q[0]);
                                    X(q[0]);
                                    R1(6.197479, q[0]);
                        }
                        
                        operation __ElseBody_926b1cd2(q : Qubit[]) : Unit is Adj + Ctl {
                                operation __ForLoopBody_9deac4ce(q : Qubit[]) : Unit is Adj + Ctl {
                                        Rz(2.311096, q[0]);
                                        I(q[0]);
                                }
                                for i in 1..3 {
                                    __ForLoopBody_9deac4ce(q);
                                }
                        }
                        
                        mutable flag = true;
                        if flag {
                            __IfBody_926b1cd2(q);
                        } else {
                            __ElseBody_926b1cd2(q);
                        }
                    }
                    let x = [q[0], q[1]];
                    let y = [q[2], q[4]];
                    let target = [q[3]];
                    ApplyIfGreaterOrEqualLE(__InlineApplyIfRelationLE_3f1a5865, x, y, target);
                }
                let x = [q[4]];
                let y = [q[2]];
                let target = [q[3], q[5], q[6], q[9], q[11]];
                ApplyIfGreaterLE(__InlineApplyIfRelationLE_8d95f851, x, y, target);
            }
            for i in 1..3 {
                __ForLoopBody_ded9c2d6(q);
            }
        }
        use x = Qubit[2];
        X(x[1]);
        use y = Qubit[2];
        X(y[0]);
        let target = q;
        ApplyIfLessLE(__InlineApplyIfRelation_e2e22bda, x, y, target);
        X(x[1]);
        X(y[0]);
        // --- DEADCODE END ---
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj {
        R1(5.83606, q[8]);
        Rz(3.681371, q[3]);
        CCNOT(q[5], q[4], q[6]);
        ApplyQFT(q);
        ApplyToEachA(H, q);
        CCNOT(q[8], q[5], q[9]);
        Rx(1.982762, q[1]);
        Z(q[3]);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Ctl {
        operation __InlineApplyIfRelationL_269c8b74(q : Qubit[]) : Unit is Adj + Ctl {
            operation __ForLoopBody_6b41b03d(q : Qubit[]) : Unit is Adj + Ctl {
                operation __ForLoopBody_8e3cadf8(q : Qubit[]) : Unit is Adj + Ctl {
                        Z(q[0]);
                        X(q[0]);
                        Rz(1.498056, q[0]);
                        S(q[0]);
                }
                for i in 1..3 {
                    __ForLoopBody_8e3cadf8(q);
                }
            }
            for i in 1..3 {
                Controlled Adjoint __ForLoopBody_6b41b03d([q[0]], [q[1]]);
            }
        }
        let x = [q[1]];
        let target = [q[4], q[6]];
        ApplyIfGreaterOrEqualL(__InlineApplyIfRelationL_269c8b74, 1L, x, target);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            Adjoint ApplyRandomBlock0(q);
            Adjoint ApplyRandomBlock1(q);
            Controlled ApplyRandomBlock2([q[0], q[1], q[9]], [q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[10], q[11]]);
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