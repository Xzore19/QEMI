namespace Main {

    open Std.Arithmetic;
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Math;
    open Std.Measurement;
    open Std.StatePreparation;

    operation MySingleBlock_8eaa899f(q : Qubit) : Unit is Adj + Ctl {
        T(q);
        R1(4.352841, q);
    }
    operation MySingleBlock_e74bff36(q : Qubit) : Unit is Adj + Ctl {
        H(q);
        T(q);
        I(q);
    }

    operation ApplyRandomBlock0(q : Qubit[]) : Unit {
        // --- DEADCODE START ---
        operation __InlineApplyIfRelation_46d1b219(q : Qubit[]) : Unit is Adj + Ctl {
            operation __InlineApplyIfRelationL_8bf74d39(q : Qubit[]) : Unit is Adj + Ctl {
                operation __InlineApplyIfRelationL_e4ad5d86(q : Qubit[]) : Unit is Adj + Ctl {
                    operation __InlineApplyIfRelationLE_1aa5d649(q : Qubit[]) : Unit is Adj + Ctl {
                            Rx(1.478266, q[0]);
                            ApplyToEachCA(MySingleBlock_8eaa899f, q);
                            I(q[0]);
                            Z(q[0]);
                    }
                    let x = [q[3]];
                    let y = [q[2]];
                    let target = [q[1]];
                    ApplyIfGreaterLE(__InlineApplyIfRelationLE_1aa5d649, x, y, target);
                }
                let x = [q[2]];
                let target = [q[1], q[3], q[4], q[5], q[6], q[7]];
                ApplyIfGreaterL(__InlineApplyIfRelationL_e4ad5d86, 1L, x, target);
            }
            let x = [q[1]];
            let target = [q[2], q[3], q[4], q[5], q[6], q[7], q[8], q[9], q[10]];
            ApplyIfGreaterOrEqualL(__InlineApplyIfRelationL_8bf74d39, 0L, x, target);
        }
        use x = Qubit[2];
        X(x[1]);
        use y = Qubit[2];
        X(y[0]);
        let target = q;
        ApplyIfLessLE(__InlineApplyIfRelation_46d1b219, x, y, target);
        X(x[1]);
        X(y[0]);
        // --- DEADCODE END ---
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Ctl {
        operation __ForLoopBody_6cd6433a(q : Qubit[]) : Unit is Ctl {
            operation __InlineApplyIfRelationL_b66225b4(q : Qubit[]) : Unit is Adj + Ctl {
                operation __ForLoopBody_1ee286b4(q : Qubit[]) : Unit is Adj + Ctl {
                    operation __ForLoopBody_eac2c890(q : Qubit[]) : Unit is Adj + Ctl {
                        operation __InlineApplyIfRelationL_e312d200(q : Qubit[]) : Unit is Adj + Ctl {
                            operation __ForLoopBody_97e514cb(q : Qubit[]) : Unit is Adj + Ctl {
                                    Rzz(2.226582, q[0], q[1]);
                                    ApplyToEachCA(MySingleBlock_e74bff36, q);
                                    Rxx(1.56185, q[1], q[0]);
                                    Y(q[0]);
                            }
                            for i in 1..3 {
                                __ForLoopBody_97e514cb(q);
                            }
                        }
                        let x = [q[2]];
                        let target = [q[0], q[1]];
                        ApplyIfLessL(__InlineApplyIfRelationL_e312d200, 0L, x, target);
                    }
                    for i in 1..3 {
                        __ForLoopBody_eac2c890(q);
                    }
                }
                for i in 1..3 {
                    __ForLoopBody_1ee286b4(q);
                }
            }
            let x = [q[1]];
            let target = [q[0], q[2], q[3]];
            ApplyIfGreaterOrEqualL(__InlineApplyIfRelationL_b66225b4, 0L, x, target);
        }
        for i in 1..3 {
            __ForLoopBody_6cd6433a(q);
        }
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Adj {
        R1(5.672217, q[9]);
        H(q[2]);
        Y(q[6]);
        Z(q[5]);
        SWAP(q[1], q[3]);
        Rx(3.432108, q[1]);
        Rx(5.565255, q[11]);
        T(q[3]);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            ApplyRandomBlock0(q);
            Controlled ApplyRandomBlock1([q[5], q[9], q[10], q[11]], [q[0], q[1], q[2], q[3], q[4], q[6], q[7], q[8]]);
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