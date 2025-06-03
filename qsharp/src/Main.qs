namespace Main {

    open Std.Arithmetic;
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Math;
    open Std.Measurement;
    open Std.StatePreparation;



    operation ApplyRandomBlock0(q : Qubit[]) : Unit {
        // --- DEADCODE START ---
        operation __InlineApplyIfRelation_8d577906(q : Qubit[]) : Unit is Adj + Ctl {
            operation __InlineApplyIfRelationLE_65aa6998(q : Qubit[]) : Unit is Adj + Ctl {
                    R1(2.05499, q[0]);
                    T(q[0]);
                    ApproximatelyPreparePureStateCP(
                1e-6,
                [
                    ComplexPolar(0.480425, 4.50951),
                    ComplexPolar(0.877036, 0.325618)
                ],
                q
            );
                    ApproximatelyPreparePureStateCP(
                1e-6,
                [
                    ComplexPolar(0.465312, 1.642487),
                    ComplexPolar(0.885147, 0.839787)
                ],
                q
            );
                    S(q[0]);
            }
            let x = [q[7]];
            let y = [q[9]];
            let target = [q[2]];
            ApplyIfEqualLE(__InlineApplyIfRelationLE_65aa6998, x, y, target);
        }
        use x = Qubit[2];
        X(x[0]);
        use y = Qubit[2];
        X(y[1]);
        let target = q;
        ApplyIfGreaterLE(__InlineApplyIfRelation_8d577906, x, y, target);
        X(x[0]);
        X(y[1]);
        // --- DEADCODE END ---
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj {
        operation __InlineApplyIfRelationLE_e1c4f4a5(q : Qubit[]) : Unit is Adj + Ctl {
            operation __InlineApplyIfRelationLE_402b0e78(q : Qubit[]) : Unit is Adj + Ctl {
                    Rx(5.623362, q[0]);
                    R1(4.159186, q[0]);
                    H(q[0]);
                    ApproximatelyPreparePureStateCP(
                1e-6,
                [
                    ComplexPolar(0.682788, 4.902728),
                    ComplexPolar(0.730616, 6.099237)
                ],
                q
            );
                    Ry(0.49739, q[0]);
                    X(q[0]);
            }
            let x = [q[2]];
            let y = [q[3]];
            let target = [q[0]];
            ApplyIfLessOrEqualLE(__InlineApplyIfRelationLE_402b0e78, x, y, target);
        }
        let x = [q[0], q[1]];
        let y = [q[2], q[7]];
        let target = [q[3], q[5], q[8], q[10]];
        ApplyIfLessLE(__InlineApplyIfRelationLE_e1c4f4a5, x, y, target);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Adj + Ctl {
        operation __InlineApplyIfRelationLE_7b19bbe3(q : Qubit[]) : Unit is Adj + Ctl {
                S(q[0]);
                Rz(0.409885, q[0]);
                Rx(2.336522, q[0]);
                R1(4.86142, q[0]);
                ApproximatelyPreparePureStateCP(
            1e-6,
            [
                ComplexPolar(0.831173, 3.994748),
                ComplexPolar(0.556013, 0.279095)
            ],
            q
        );
                S(q[0]);
        }
        let x = [q[1], q[2], q[6]];
        let y = [q[0], q[4], q[5]];
        let target = [q[3]];
        ApplyIfEqualLE(__InlineApplyIfRelationLE_7b19bbe3, x, y, target);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            ApplyRandomBlock0(q);
            Adjoint ApplyRandomBlock1(q);
            Controlled Adjoint ApplyRandomBlock2([q[0], q[4], q[7], q[8], q[10]], [q[1], q[2], q[3], q[5], q[6], q[9], q[11]]);
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