namespace Main {
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Math;
    open Std.Measurement;
    open Std.StatePreparation;

    operation Block_1bd215(q : Qubit[]) : Unit is Adj + Ctl {
        S(q[1]);
        Rz(6.136523, q[0]);
        Ry(2.874984, q[0]);
        Ry(5.889982, q[2]);
    }
    operation Block_e3efe6(q : Qubit[]) : Unit is Adj {
        T(q[2]);
        H(q[1]);
        Ry(0.275098, q[0]);
        ApproximatelyPreparePureStateCP(
    1e-6,
    [
        ComplexPolar(0.221304, 0.515688),
        ComplexPolar(0.197224, 5.338292),
        ComplexPolar(0.294185, 4.034087),
        ComplexPolar(0.291143, 4.112717),
        ComplexPolar(0.222621, 4.402896),
        ComplexPolar(0.257744, 2.799776),
        ComplexPolar(0.291935, 5.713679),
        ComplexPolar(0.233169, 2.355129),
        ComplexPolar(0.269595, 2.341501),
        ComplexPolar(0.261994, 5.398591),
        ComplexPolar(0.294521, 4.803372),
        ComplexPolar(0.286555, 0.026167),
        ComplexPolar(0.021241, 3.024416),
        ComplexPolar(0.281862, 0.084347),
        ComplexPolar(0.258941, 5.997816),
        ComplexPolar(0.167648, 5.9051)
    ],
    q
);
        T(q[3]);
    }
    operation Block_96eba4(q : Qubit[]) : Unit {
        T(q[3]);
        ApplyQFT(q);
        Z(q[3]);
        Ry(0.389413, q[0]);
        I(q[3]);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[4] {
            Controlled Block_1bd215([q[2]], [q[0], q[1], q[3]]);
            Adjoint Block_e3efe6(q);
            Block_96eba4(q);
            let r0 = M(q[0]);
            let r1 = M(q[1]);
            let r2 = M(q[2]);
            let r3 = M(q[3]);
            ResetAll(q);
            return [r0, r1, r2, r3];
        }
    }
}