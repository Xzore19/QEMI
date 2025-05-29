namespace Main_fuzzing {

    open Std.Arithmetic;
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Math;
    open Std.Measurement;
    open Std.StatePreparation;

    operation MySingleBlock_78cf336b(q : Qubit) : Unit is Adj + Ctl {
        Z(q);
        X(q);
    }

    operation ApplyRandomBlock0(q : Qubit[]) : Unit {
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj {
        operation __InlineApplyIfEqualAction_b3b945bd(q : Qubit[]) : Unit is Adj + Ctl {
            operation __InlineApplyIfEqualAction_e84bfeb4(q : Qubit[]) : Unit is Adj + Ctl {
                    Z(q[0]);
                    Z(q[0]);
                    ApproximatelyPreparePureStateCP(
                1e-6,
                [
                    ComplexPolar(0.671934, 2.493431),
                    ComplexPolar(0.389354, 5.018479),
                    ComplexPolar(0.391598, 4.658062),
                    ComplexPolar(0.493517, 2.631798)
                ],
                q
            );
                    ApplyQFT(q);
                    H(q[0]);
                    ApproximatelyPreparePureStateCP(
                1e-6,
                [
                    ComplexPolar(0.129195, 4.174653),
                    ComplexPolar(0.635635, 2.107569),
                    ComplexPolar(0.654756, 4.770825),
                    ComplexPolar(0.388034, 3.524348)
                ],
                q
            );
                    SWAP(q[0], q[1]);
            }
            let x = [q[2]];
            let y = [q[3]];
            let target = [q[0], q[1]];
            ApplyIfEqualLE(__InlineApplyIfEqualAction_e84bfeb4, x, y, target);
        }
        let x = [q[4]];
        let y = [q[11]];
        let target = [q[2], q[5], q[8], q[10]];
        ApplyIfEqualLE(__InlineApplyIfEqualAction_b3b945bd, x, y, target);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit {
        operation __InlineApplyIfEqualAction_e0b1ea47(q : Qubit[]) : Unit is Adj + Ctl {
            operation __InlineApplyIfEqualAction_acc6d485(q : Qubit[]) : Unit is Adj + Ctl {
                    X(q[0]);
                    I(q[0]);
                    X(q[0]);
                    I(q[0]);
                    Rz(1.117047, q[0]);
                    Rz(5.67864, q[0]);
                    Rz(2.498388, q[0]);
            }
            let x = [q[1], q[4]];
            let y = [q[0], q[2]];
            let target = [q[3]];
            ApplyIfEqualLE(__InlineApplyIfEqualAction_acc6d485, x, y, target);
        }
        let x = [q[0], q[7], q[8]];
        let y = [q[2], q[6], q[10]];
        let target = [q[1], q[3], q[5], q[9], q[11]];
        ApplyIfEqualLE(__InlineApplyIfEqualAction_e0b1ea47, x, y, target);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            ApplyRandomBlock0(q);
            Adjoint ApplyRandomBlock1(q);
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