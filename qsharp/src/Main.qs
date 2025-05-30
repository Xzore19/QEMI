namespace Main {

    open Std.Arithmetic;
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Math;
    open Std.Measurement;
    open Std.StatePreparation;

    operation MySingleBlock_e37d3e68(q : Qubit) : Unit is Adj + Ctl {
        X(q);
        Y(q);
        Rx(4.385957, q);
    }

    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Adj + Ctl {
        // --- DEADCODE START ---
        operation __InlineApplyIfRelation_13df1646(q : Qubit[]) : Unit is Adj + Ctl {
            operation __InlineApplyIfRelationLE_5ab2898a(q : Qubit[]) : Unit is Adj + Ctl {
                operation __ForLoopBody_bb720a4b(q : Qubit[]) : Unit is Adj + Ctl {
                    operation __ForLoopBody_b51500ff(q : Qubit[]) : Unit is Adj + Ctl {
                            Ry(0.005387, q[0]);
                            Rx(4.963956, q[1]);
                            Y(q[0]);
                            Ry(0.18331, q[1]);
                            ApplyToEachCA(MySingleBlock_e37d3e68, q);
                    }
                    for i in 1..3 {
                        __ForLoopBody_b51500ff(q);
                    }
                }
                for i in 1..3 {
                    Controlled Adjoint __ForLoopBody_bb720a4b([q[2]], [q[0], q[1]]);
                }
            }
            let x = [q[7], q[8], q[10]];
            let y = [q[1], q[3], q[6]];
            let target = [q[2], q[5], q[9]];
            ApplyIfGreaterOrEqualLE(__InlineApplyIfRelationLE_5ab2898a, x, y, target);
        }
        use x = Qubit[2];
        let target = q;
        ApplyIfLessL(__InlineApplyIfRelation_13df1646, 0L, x, target);
        // --- DEADCODE END ---
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Ctl {
        operation __ForLoopBody_645d258d(q : Qubit[]) : Unit is Ctl {
            operation __InlineApplyIfRelationL_4df4df7c(q : Qubit[]) : Unit is Adj + Ctl {
                operation __InlineApplyIfRelationLE_014c4632(q : Qubit[]) : Unit is Adj + Ctl {
                        ApproximatelyPreparePureStateCP(
                    1e-6,
                    [
                        ComplexPolar(0.748773, 1.955711),
                        ComplexPolar(0.662826, 0.960154)
                    ],
                    q
                );
                        Z(q[0]);
                        R1(3.470325, q[0]);
                        R1(6.181013, q[0]);
                }
                let x = [q[3]];
                let y = [q[2]];
                let target = [q[0]];
                ApplyIfLessOrEqualLE(__InlineApplyIfRelationLE_014c4632, x, y, target);
            }
            let x = [q[1], q[4], q[8]];
            let target = [q[0], q[5], q[6], q[7]];
            ApplyIfEqualL(__InlineApplyIfRelationL_4df4df7c, 2L, x, target);
        }
        for i in 1..3 {
            Controlled __ForLoopBody_645d258d([q[3]], [q[0], q[1], q[2], q[4], q[5], q[6], q[7], q[8], q[9]]);
        }
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Adj {
        operation __InlineApplyIfRelationL_1a4aa230(q : Qubit[]) : Unit is Adj + Ctl {
            operation __InlineApplyIfRelationLE_2b1a3dee(q : Qubit[]) : Unit is Adj + Ctl {
                operation __ForLoopBody_1059fda0(q : Qubit[]) : Unit is Adj + Ctl {
                        ApproximatelyPreparePureStateCP(
                    1e-6,
                    [
                        ComplexPolar(0.555739, 5.117901),
                        ComplexPolar(0.831357, 4.591651)
                    ],
                    q
                );
                        T(q[0]);
                        I(q[0]);
                        S(q[0]);
                        X(q[0]);
                        T(q[0]);
                }
                for i in 1..3 {
                    __ForLoopBody_1059fda0(q);
                }
            }
            let x = [q[2], q[5]];
            let y = [q[1], q[4]];
            let target = [q[7]];
            ApplyIfEqualLE(__InlineApplyIfRelationLE_2b1a3dee, x, y, target);
        }
        let x = [q[1], q[6], q[10]];
        let target = [q[2], q[3], q[4], q[5], q[7], q[8], q[9], q[11]];
        ApplyIfGreaterL(__InlineApplyIfRelationL_1a4aa230, 5L, x, target);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            Controlled Adjoint ApplyRandomBlock0([q[9]], [q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[10], q[11]]);
            Controlled ApplyRandomBlock1([q[4], q[11]], [q[0], q[1], q[2], q[3], q[5], q[6], q[7], q[8], q[9], q[10]]);
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