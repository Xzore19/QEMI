namespace Main_fuzzing {

    open Std.Arithmetic;
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Math;
    open Std.Measurement;
    open Std.StatePreparation;

    operation MySingleBlock_8f7cbeb4(q : Qubit) : Unit is Adj + Ctl {
        S(q);
        Rz(0.794571, q);
        Ry(4.626353, q);
    }
    operation MySingleBlock_6190629e(q : Qubit) : Unit is Adj + Ctl {
        X(q);
        Z(q);
        S(q);
        Ry(5.941228, q);
    }

    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Adj + Ctl {
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit {
        operation __InlineApplyIfRelationLE_8d652798(q : Qubit[]) : Unit is Adj + Ctl {
            operation __ForLoopBody_a3cb8bfe(q : Qubit[]) : Unit is Adj + Ctl {
                operation __InlineApplyIfRelationLE_0f4be706(q : Qubit[]) : Unit is Adj + Ctl {
                        Rz(1.336761, q[0]);
                        R1(4.761427, q[0]);
                        ApproximatelyPreparePureStateCP(
                    1e-6,
                    [
                        ComplexPolar(0.661092, 5.872935),
                        ComplexPolar(0.750304, 5.164368)
                    ],
                    q
                );
                        Rz(6.169969, q[0]);
                        Z(q[0]);
                }
                let x = [q[0], q[2], q[5]];
                let y = [q[1], q[4], q[7]];
                let target = [q[6]];
                ApplyIfGreaterLE(__InlineApplyIfRelationLE_0f4be706, x, y, target);
            }
            for i in 1..3 {
                __ForLoopBody_a3cb8bfe(q);
            }
        }
        let x = [q[7], q[11]];
        let y = [q[8], q[10]];
        let target = [q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[9]];
        ApplyIfGreaterLE(__InlineApplyIfRelationLE_8d652798, x, y, target);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit {
        S(q[9]);
        Ryy(4.42995, q[1], q[7]);
        I(q[4]);
        CCNOT(q[8], q[9], q[10]);
        Rxx(5.264461, q[1], q[7]);
        T(q[6]);
        Rx(1.267843, q[2]);
        I(q[5]);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            Controlled ApplyRandomBlock0([q[0], q[4], q[5], q[7], q[8], q[10], q[11]], [q[1], q[2], q[3], q[6], q[9]]);
            ApplyRandomBlock1(q);
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