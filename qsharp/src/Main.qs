namespace Main {

    open Std.Arithmetic;
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Math;
    open Std.Measurement;
    open Std.StatePreparation;

    operation MySingleBlock_2ef56aa0(q : Qubit) : Unit is Adj + Ctl {
        Ry(5.948145, q);
        I(q);
        Z(q);
    }
    operation MySingleBlock_242468a7(q : Qubit) : Unit is Adj + Ctl {
        Rz(5.678347, q);
        R1(5.061008, q);
    }

    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Adj {
        // --- DEADCODE START ---
        operation __InlineApplyIfRelation_d87a8e2f(q : Qubit[]) : Unit is Adj + Ctl {
            operation __InlineApplyIfRelationL_480cbf2f(q : Qubit[]) : Unit is Adj + Ctl {
                    ApplyToEachCA(MySingleBlock_2ef56aa0, q);
                    Rz(4.218952, q[0]);
                    Y(q[0]);
                    S(q[0]);
                    T(q[0]);
                    Z(q[0]);
            }
            let x = [q[1], q[2], q[3]];
            let target = [q[0]];
            ApplyIfLessOrEqualL(__InlineApplyIfRelationL_480cbf2f, 4L, x, target);
        }
        use x = Qubit[2];
        X(x[0]);
        X(x[1]);
        let target = q;
        ApplyIfGreaterL(__InlineApplyIfRelation_d87a8e2f, 0L, x, target);
        X(x[0]);
        X(x[1]);
        // --- DEADCODE END ---
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj + Ctl {
        operation __InlineApplyIfRelationL_54ef1d6f(q : Qubit[]) : Unit is Adj + Ctl {
            operation __InlineApplyIfRelationL_8b845350(q : Qubit[]) : Unit is Adj + Ctl {
                operation __ForLoopBody_59786ed8(q : Qubit[]) : Unit is Adj + Ctl {
                        Z(q[0]);
                        I(q[0]);
                        S(q[0]);
                        Rz(0.834369, q[0]);
                        R1(3.768172, q[0]);
                        ApplyQFT(q);
                }
                for i in 1..3 {
                    __ForLoopBody_59786ed8(q);
                }
            }
            let x = [q[0]];
            let target = [q[2]];
            ApplyIfGreaterL(__InlineApplyIfRelationL_8b845350, 0L, x, target);
        }
        let x = [q[4], q[7], q[8]];
        let target = [q[0], q[2], q[3]];
        ApplyIfLessOrEqualL(__InlineApplyIfRelationL_54ef1d6f, 2L, x, target);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Ctl {
        operation __InlineApplyIfRelationL_458099ef(q : Qubit[]) : Unit is Adj + Ctl {
            operation __InlineApplyIfRelationL_b7ce1b0c(q : Qubit[]) : Unit is Adj + Ctl {
                operation __InlineApplyIfRelationL_48663759(q : Qubit[]) : Unit is Adj + Ctl {
                        R1(1.542014, q[0]);
                        I(q[0]);
                        T(q[0]);
                        ApplyToEachCA(MySingleBlock_242468a7, q);
                        I(q[0]);
                }
                let x = [q[0]];
                let target = [q[1]];
                ApplyIfLessL(__InlineApplyIfRelationL_48663759, 1L, x, target);
            }
            let x = [q[1]];
            let target = [q[0], q[2]];
            ApplyIfGreaterL(__InlineApplyIfRelationL_b7ce1b0c, 1L, x, target);
        }
        let x = [q[1], q[3], q[4]];
        let target = [q[0], q[2], q[5]];
        ApplyIfGreaterOrEqualL(__InlineApplyIfRelationL_458099ef, 6L, x, target);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            Adjoint ApplyRandomBlock0(q);
            Controlled Adjoint ApplyRandomBlock1([q[0], q[8], q[10]], [q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[9], q[11]]);
            Controlled ApplyRandomBlock2([q[0], q[2], q[3], q[4], q[6], q[10]], [q[1], q[5], q[7], q[8], q[9], q[11]]);
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