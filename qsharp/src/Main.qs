namespace Main {

    open Std.Arithmetic;
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Math;
    open Std.Measurement;
    open Std.StatePreparation;

    operation MySingleBlock_4da4c4b0(q : Qubit) : Unit is Adj + Ctl {
        T(q);
        H(q);
    }
    operation MySingleBlock_a1960e33(q : Qubit) : Unit is Adj + Ctl {
        R1(1.438987, q);
        Ry(0.451851, q);
    }

    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Adj {
        // --- DEADCODE START ---
        operation __InlineApplyIfRelation_19393df6(q : Qubit[]) : Unit is Adj + Ctl {
            operation __InlineApplyIfRelationL_577831f3(q : Qubit[]) : Unit is Adj + Ctl {
                operation __InlineApplyIfRelationLE_ada3cd20(q : Qubit[]) : Unit is Adj + Ctl {
                    operation __InlineApplyIfRelationL_f850eb51(q : Qubit[]) : Unit is Adj + Ctl {
                            X(q[0]);
                            Rz(5.646367, q[0]);
                            I(q[0]);
                            ApproximatelyPreparePureStateCP(
                        1e-6,
                        [
                            ComplexPolar(0.797956, 4.115717),
                            ComplexPolar(0.602716, 6.05288)
                        ],
                        q
                    );
                            Ry(6.020409, q[0]);
                            I(q[0]);
                    }
                    let x = [q[0]];
                    let target = [q[1]];
                    ApplyIfEqualL(__InlineApplyIfRelationL_f850eb51, 1L, x, target);
                }
                let x = [q[0], q[3], q[5]];
                let y = [q[1], q[4], q[6]];
                let target = [q[2], q[7]];
                ApplyIfGreaterLE(__InlineApplyIfRelationLE_ada3cd20, x, y, target);
            }
            let x = [q[1], q[6], q[8]];
            let target = [q[0], q[2], q[3], q[4], q[5], q[7], q[9], q[10]];
            ApplyIfGreaterL(__InlineApplyIfRelationL_577831f3, 6L, x, target);
        }
        use x = Qubit[2];
        X(x[0]);
        use y = Qubit[2];
        X(y[1]);
        let target = q;
        ApplyIfGreaterLE(__InlineApplyIfRelation_19393df6, x, y, target);
        X(x[0]);
        X(y[1]);
        // --- DEADCODE END ---
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj + Ctl {
        operation __InlineApplyIfRelationLE_cce7f546(q : Qubit[]) : Unit is Adj + Ctl {
            operation __InlineApplyIfRelationLE_ed1a0846(q : Qubit[]) : Unit is Adj + Ctl {
                    X(q[1]);
                    ApplyToEachCA(MySingleBlock_4da4c4b0, q);
                    H(q[0]);
                    SWAP(q[1], q[0]);
                    Rzz(5.040434, q[1], q[0]);
                    Z(q[0]);
                    SWAP(q[1], q[0]);
                    Rzz(0.645123, q[1], q[0]);
            }
            let x = [q[1]];
            let y = [q[2]];
            let target = [q[3], q[4]];
            ApplyIfGreaterOrEqualLE(__InlineApplyIfRelationLE_ed1a0846, x, y, target);
        }
        let x = [q[0]];
        let y = [q[1]];
        let target = [q[3], q[4], q[5], q[6], q[7]];
        ApplyIfEqualLE(__InlineApplyIfRelationLE_cce7f546, x, y, target);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Adj + Ctl {
        Rx(3.123363, q[6]);
        Rx(4.41275, q[6]);
        R1(1.249646, q[2]);
        ApplyToEachCA(MySingleBlock_a1960e33, q);
        T(q[8]);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            Adjoint ApplyRandomBlock0(q);
            Controlled ApplyRandomBlock1([q[1], q[2], q[5], q[11]], [q[0], q[3], q[4], q[6], q[7], q[8], q[9], q[10]]);
            Controlled ApplyRandomBlock2([q[2], q[11]], [q[0], q[1], q[3], q[4], q[5], q[6], q[7], q[8], q[9], q[10]]);
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