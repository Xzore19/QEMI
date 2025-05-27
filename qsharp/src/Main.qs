namespace Main {
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Math;
    open Std.Measurement;
    open Std.StatePreparation;

    operation MySingleBlock0(q : Qubit) : Unit is Adj + Ctl {
    Z(q);
    T(q);
    I(q);
    }
    operation MySingleBlock1(q : Qubit) : Unit is Adj + Ctl {
    Y(q);
    Y(q);
    Z(q);
    I(q);
    }
    operation MySingleBlock2(q : Qubit) : Unit is Adj + Ctl {
    Ry(0.586497, q);
    I(q);
    }
    operation MySingleBlock3(q : Qubit) : Unit is Adj + Ctl {
    X(q);
    R1(3.476504, q);
    }

    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Adj {
        Y(q[0]);
        Ryy(2.770383, q[0], q[1]);
        Ry(3.889915, q[3]);
        Rzz(5.944369, q[2], q[3]);
        Rx(3.939716, q[0]);
        I(q[3]);
        H(q[3]);
        ApplyToEachCA(MySingleBlock0, q);
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj {
        X(q[1]);
        S(q[0]);
        Rxx(4.350752, q[0], q[3]);
        Y(q[3]);
        T(q[0]);
        Ryy(1.12719, q[1], q[3]);
        Rx(5.880906, q[0]);
        ApproximatelyPreparePureStateCP(
    1e-6,
    [
        ComplexPolar(0.148813, 0.523397),
        ComplexPolar(0.272479, 4.400932),
        ComplexPolar(0.342781, 1.728115),
        ComplexPolar(0.287482, 5.580267),
        ComplexPolar(0.271242, 1.771571),
        ComplexPolar(0.330903, 0.219778),
        ComplexPolar(0.335758, 1.871764),
        ComplexPolar(0.053853, 1.343644),
        ComplexPolar(0.324897, 5.894832),
        ComplexPolar(0.175086, 1.960393),
        ComplexPolar(0.30799, 2.496362),
        ComplexPolar(0.136276, 1.166373),
        ComplexPolar(0.10416, 3.744659),
        ComplexPolar(0.326967, 5.216538),
        ComplexPolar(0.135962, 1.147662),
        ComplexPolar(0.1374, 4.866712)
    ],
    q
);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Adj {
        H(q[3]);
        R1(3.331522, q[0]);
        ApplyToEachCA(MySingleBlock1, q);
        ApproximatelyPreparePureStateCP(
    1e-6,
    [
        ComplexPolar(0.148813, 0.523397),
        ComplexPolar(0.272479, 4.400932),
        ComplexPolar(0.342781, 1.728115),
        ComplexPolar(0.287482, 5.580267),
        ComplexPolar(0.271242, 1.771571),
        ComplexPolar(0.330903, 0.219778),
        ComplexPolar(0.335758, 1.871764),
        ComplexPolar(0.053853, 1.343644),
        ComplexPolar(0.324897, 5.894832),
        ComplexPolar(0.175086, 1.960393),
        ComplexPolar(0.30799, 2.496362),
        ComplexPolar(0.136276, 1.166373),
        ComplexPolar(0.10416, 3.744659),
        ComplexPolar(0.326967, 5.216538),
        ComplexPolar(0.135962, 1.147662),
        ComplexPolar(0.1374, 4.866712)
    ],
    q
);
        ApplyToEachCA(MySingleBlock2, q);
        CNOT(q[0], q[2]);
        CNOT(q[1], q[2]);
        ApplyToEachCA(MySingleBlock3, q);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[4] {
            ApplyRandomBlock0(q);
            Adjoint ApplyRandomBlock1(q);
            Adjoint ApplyRandomBlock2(q);
            let r0 = M(q[0]);
            let r1 = M(q[1]);
            let r2 = M(q[2]);
            let r3 = M(q[3]);
            ResetAll(q);
            return [r0, r1, r2, r3];
        }
    }
}