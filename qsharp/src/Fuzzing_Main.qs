namespace Main_fuzzing {

    open Std.Arithmetic;
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Math;
    open Std.Measurement;
    open Std.StatePreparation;



    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Ctl {
        // --- DEADCODE IF-ELSE START ---
        operation __DeadBlock_99eb414c(q : Qubit[]) : Unit is Ctl {
                operation __InlineApplyIfRelationLE_30544d2e(q : Qubit[]) : Unit is Adj + Ctl {
                    operation __ForLoopBody_9db910ae(q : Qubit[]) : Unit is Adj + Ctl {
                        operation __ForLoopBody_4bebd3a5(q : Qubit[]) : Unit is Adj + Ctl {
                                S(q[0]);
                                R1(4.204171, q[0]);
                                Z(q[0]);
                                T(q[0]);
                        }
                        for i in 1..3 {
                            __ForLoopBody_4bebd3a5(q);
                        }
                    }
                    for i in 1..3 {
                        Controlled Adjoint __ForLoopBody_9db910ae([q[0]], [q[1]]);
                    }
                }
                let x = [q[4], q[5]];
                let y = [q[0], q[3]];
                let target = [q[1], q[6]];
                ApplyIfLessLE(__InlineApplyIfRelationLE_30544d2e, x, y, target);
        }
        
        operation __InlineIfElseDeadcode_78ade821(q : Qubit[]) : Unit is Ctl {
            use ctrl = Qubit();
            within { } apply {
            }
                operation __ForLoopBody_fa9f3b45(q : Qubit[]) : Unit is Ctl {
                    operation __ForLoopBody_3b90c5a7(q : Qubit[]) : Unit is Ctl {
                        operation __InlineApplyIfRelationL_33a0cc80(q : Qubit[]) : Unit is Adj + Ctl {
                            operation __InlineApplyIfRelationLE_a9d114a5(q : Qubit[]) : Unit is Adj + Ctl {
                                operation __ForLoopBody_0c5e6c9a(q : Qubit[]) : Unit is Adj + Ctl {
                                        Ry(2.995238, q[0]);
                                        Z(q[0]);
                                }
                                for i in 1..3 {
                                    __ForLoopBody_0c5e6c9a(q);
                                }
                            }
                            let x = [q[2], q[3]];
                            let y = [q[0], q[4]];
                            let target = [q[1]];
                            ApplyIfLessOrEqualLE(__InlineApplyIfRelationLE_a9d114a5, x, y, target);
                        }
                        let x = [q[5]];
                        let target = [q[0], q[1], q[2], q[3], q[4]];
                        ApplyIfEqualL(__InlineApplyIfRelationL_33a0cc80, 0L, x, target);
                    }
                    for i in 1..3 {
                        __ForLoopBody_3b90c5a7(q);
                    }
                }
                for i in 1..3 {
                    __ForLoopBody_fa9f3b45(q);
                }
        }
        
        __InlineIfElseDeadcode_78ade821(q);
        // --- DEADCODE IF-ELSE END ---
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj + Ctl {
        operation __InlineApplyIfRelationLE_1ef9424c(q : Qubit[]) : Unit is Adj + Ctl {
            operation __ForLoopBody_96adf6e8(q : Qubit[]) : Unit is Adj + Ctl {
                    T(q[0]);
                    Z(q[0]);
                    Z(q[0]);
            }
            for i in 1..3 {
                __ForLoopBody_96adf6e8(q);
            }
        }
        let x = [q[0], q[1], q[5]];
        let y = [q[3], q[4], q[6]];
        let target = [q[2]];
        ApplyIfGreaterLE(__InlineApplyIfRelationLE_1ef9424c, x, y, target);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Adj + Ctl {
        Ry(3.868303, q[6]);
        H(q[2]);
        Ry(6.24682, q[2]);
        ApplyQFT(q);
        ApplyQFT(q);
        ApplyQFT(q);
        R1(4.883235, q[2]);
        Z(q[5]);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            Controlled ApplyRandomBlock0([q[0], q[4], q[6], q[9], q[11]], [q[1], q[2], q[3], q[5], q[7], q[8], q[10]]);
            Controlled Adjoint ApplyRandomBlock1([q[0], q[3], q[4], q[5], q[9]], [q[1], q[2], q[6], q[7], q[8], q[10], q[11]]);
            Controlled Adjoint ApplyRandomBlock2([q[3], q[5], q[8], q[10]], [q[0], q[1], q[2], q[4], q[6], q[7], q[9], q[11]]);
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