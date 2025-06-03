namespace Main {

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
        operation __DeadBlock_48548c53(q : Qubit[]) : Unit is Ctl {
                operation __ForLoopBody_d83f165d(q : Qubit[]) : Unit is Ctl {
                    operation __ForLoopBody_9d373ce5(q : Qubit[]) : Unit is Ctl {
                        operation __ForLoopBody_f86f2403(q : Qubit[]) : Unit is Ctl {
                            operation __InlineApplyIfRelationLE_7a861c58(q : Qubit[]) : Unit is Adj + Ctl {
                                    ApproximatelyPreparePureStateCP(
                                1e-6,
                                [
                                    ComplexPolar(0.399485, 0.756448),
                                    ComplexPolar(0.91674, 0.076801)
                                ],
                                q
                            );
                                    Y(q[0]);
                            }
                            let x = [q[1]];
                            let y = [q[0]];
                            let target = [q[2]];
                            ApplyIfGreaterLE(__InlineApplyIfRelationLE_7a861c58, x, y, target);
                        }
                        for i in 1..3 {
                            __ForLoopBody_f86f2403(q);
                        }
                    }
                    for i in 1..3 {
                        Controlled __ForLoopBody_9d373ce5([q[2], q[3]], [q[0], q[1], q[4]]);
                    }
                }
                for i in 1..3 {
                    Controlled __ForLoopBody_d83f165d([q[0]], [q[1], q[2], q[3], q[4], q[5]]);
                }
        }
        
        operation __InlineIfElseDeadcode_b8a8f530(q : Qubit[]) : Unit is Ctl {
            use ctrl = Qubit();
            within { } apply {
                // --- DEADCODE START ---
                Controlled __DeadBlock_48548c53([ctrl], q);
                // --- DEADCODE END ---
            }
                operation __InlineApplyIfRelationL_757c4543(q : Qubit[]) : Unit is Adj + Ctl {
                    operation __ForLoopBody_dad0d2a8(q : Qubit[]) : Unit is Adj + Ctl {
                            T(q[0]);
                            SWAP(q[1], q[0]);
                            ApproximatelyPreparePureStateCP(
                        1e-6,
                        [
                            ComplexPolar(0.594818, 0.836726),
                            ComplexPolar(0.458242, 6.187618),
                            ComplexPolar(0.100751, 3.944103),
                            ComplexPolar(0.652729, 4.562707)
                        ],
                        q
                    );
                            ApplyQFT(q);
                            CNOT(q[1], q[0]);
                            Rx(1.429625, q[1]);
                    }
                    for i in 1..3 {
                        Controlled Adjoint __ForLoopBody_dad0d2a8([q[1]], [q[0], q[2]]);
                    }
                }
                let x = [q[2], q[3]];
                let target = [q[0], q[1], q[5]];
                ApplyIfGreaterOrEqualL(__InlineApplyIfRelationL_757c4543, 1L, x, target);
        }
        
        __InlineIfElseDeadcode_b8a8f530(q);
        // --- DEADCODE IF-ELSE END ---
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj + Ctl {
        operation __InlineApplyIfRelationL_3c72a25c(q : Qubit[]) : Unit is Adj + Ctl {
            operation __InlineApplyIfRelationL_cb660cb4(q : Qubit[]) : Unit is Adj + Ctl {
                    H(q[0]);
                    H(q[0]);
                    H(q[0]);
                    Z(q[0]);
                    Y(q[0]);
                    Rz(3.111409, q[0]);
            }
            let x = [q[1]];
            let target = [q[0]];
            ApplyIfGreaterL(__InlineApplyIfRelationL_cb660cb4, 0L, x, target);
        }
        let x = [q[0], q[7], q[9]];
        let target = [q[1], q[5]];
        ApplyIfLessL(__InlineApplyIfRelationL_3c72a25c, 4L, x, target);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Adj {
        operation __ForLoopBody_a92d4e12(q : Qubit[]) : Unit is Adj {
            operation __InlineApplyIfRelationL_0035debc(q : Qubit[]) : Unit is Adj + Ctl {
                operation __ForLoopBody_3a792f34(q : Qubit[]) : Unit is Adj + Ctl {
                        Rxx(0.090051, q[0], q[1]);
                        ApproximatelyPreparePureStateCP(
                    1e-6,
                    [
                        ComplexPolar(0.336014, 5.353538),
                        ComplexPolar(0.694496, 5.903975),
                        ComplexPolar(0.462906, 4.040268),
                        ComplexPolar(0.43645, 1.132266)
                    ],
                    q
                );
                        T(q[0]);
                        ApplyQFT(q);
                        Ry(4.851594, q[1]);
                        T(q[0]);
                }
                for i in 1..3 {
                    __ForLoopBody_3a792f34(q);
                }
            }
            let x = [q[3], q[6], q[11]];
            let target = [q[0], q[2]];
            ApplyIfEqualL(__InlineApplyIfRelationL_0035debc, 2L, x, target);
        }
        for i in 1..3 {
            Adjoint __ForLoopBody_a92d4e12(q);
        }
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            Controlled ApplyRandomBlock0([q[0], q[5], q[6], q[8], q[10], q[11]], [q[1], q[2], q[3], q[4], q[7], q[9]]);
            Controlled Adjoint ApplyRandomBlock1([q[0], q[9]], [q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[10], q[11]]);
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