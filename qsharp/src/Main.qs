namespace Main {
    open Std.Arithmetic;
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Math;
    open Std.Measurement;
    open Std.StatePreparation;

    operation MySingleBlock0(q : Qubit) : Unit is Adj + Ctl {
    I(q);
    H(q);
    Y(q);
    }
    operation MySingleBlock1(q : Qubit) : Unit is Adj + Ctl {
    X(q);
    Rx(6.114551, q);
    S(q);
    }
    operation MyAdjCtlBlock0(q : Qubit[]) : Unit is Adj + Ctl {
        Ryy(4.841687, q[3], q[5]);
        CCNOT(q[3], q[4], q[5]);
        Rxx(0.089671, q[0], q[4]);
        X(q[0]);
        S(q[5]);
        Rz(3.22752, q[0]);
        ApproximatelyPreparePureStateCP(
    1e-6,
    [
        ComplexPolar(0.159173, 4.272759),
        ComplexPolar(0.09913, 5.352492),
        ComplexPolar(0.158549, 6.222194),
        ComplexPolar(0.035375, 5.281114),
        ComplexPolar(0.04274, 1.751404),
        ComplexPolar(0.113408, 3.954915),
        ComplexPolar(0.104193, 1.761522),
        ComplexPolar(0.145381, 4.694055),
        ComplexPolar(0.074443, 1.973234),
        ComplexPolar(0.166315, 4.981673),
        ComplexPolar(0.045616, 4.713131),
        ComplexPolar(0.1011, 1.560373),
        ComplexPolar(0.023858, 2.144558),
        ComplexPolar(0.09673, 0.064182),
        ComplexPolar(0.121281, 1.717049),
        ComplexPolar(0.170826, 3.997882),
        ComplexPolar(0.066357, 5.254877),
        ComplexPolar(0.081382, 3.871778),
        ComplexPolar(0.045445, 5.612813),
        ComplexPolar(0.116639, 2.231728),
        ComplexPolar(0.107718, 2.086498),
        ComplexPolar(0.087294, 4.655849),
        ComplexPolar(0.05414, 4.071853),
        ComplexPolar(0.149404, 2.087622),
        ComplexPolar(0.126366, 5.799751),
        ComplexPolar(0.127073, 6.055801),
        ComplexPolar(0.145667, 5.338819),
        ComplexPolar(0.168956, 0.733472),
        ComplexPolar(0.087158, 1.943715),
        ComplexPolar(0.165838, 2.952141),
        ComplexPolar(0.169018, 1.803753),
        ComplexPolar(0.10364, 1.748792),
        ComplexPolar(0.126673, 5.793363),
        ComplexPolar(0.166471, 2.075408),
        ComplexPolar(0.161189, 4.53056),
        ComplexPolar(0.066468, 0.748024),
        ComplexPolar(0.157275, 1.34912),
        ComplexPolar(0.165234, 4.592535),
        ComplexPolar(0.125081, 5.140495),
        ComplexPolar(0.164035, 3.233385),
        ComplexPolar(0.10476, 2.728765),
        ComplexPolar(0.171357, 4.135854),
        ComplexPolar(0.115079, 0.59323),
        ComplexPolar(0.086996, 1.630592),
        ComplexPolar(0.105564, 0.76673),
        ComplexPolar(0.124751, 0.264748),
        ComplexPolar(0.109868, 4.617168),
        ComplexPolar(0.104861, 1.004623),
        ComplexPolar(0.162978, 1.817597),
        ComplexPolar(0.158645, 4.105059),
        ComplexPolar(0.122688, 4.020652),
        ComplexPolar(0.132284, 0.091978),
        ComplexPolar(0.115429, 0.101403),
        ComplexPolar(0.151087, 2.91101),
        ComplexPolar(0.164283, 5.894414),
        ComplexPolar(0.02829, 2.61604),
        ComplexPolar(0.140832, 3.99107),
        ComplexPolar(0.128667, 2.483946),
        ComplexPolar(0.140934, 0.114216),
        ComplexPolar(0.170824, 5.594024),
        ComplexPolar(0.110565, 5.556086),
        ComplexPolar(0.080242, 6.276015),
        ComplexPolar(0.131506, 2.382554),
        ComplexPolar(0.125311, 1.69614)
    ],
    q
);
        ApplyToEachCA(MySingleBlock1, q);
    }
    operation MySingleBlock2(q : Qubit) : Unit is Adj + Ctl {
    Rz(0.400113, q);
    T(q);
    }
    operation MySingleBlock3(q : Qubit) : Unit is Adj + Ctl {
    S(q);
    S(q);
    }
    operation MySingleBlock4(q : Qubit) : Unit is Adj + Ctl {
    Y(q);
    X(q);
    I(q);
    }
    operation MySingleBlock5(q : Qubit) : Unit is Adj + Ctl {
    T(q);
    Rz(6.2551, q);
    }
    operation MySingleBlock6(q : Qubit) : Unit is Adj + Ctl {
    Z(q);
    Rx(3.280034, q);
    Y(q);
    R1(3.569497, q);
    }

    operation ApplyRandomBlock0(q : Qubit[]) : Unit {
        ApplyToEach(H, q);
        SWAP(q[2], q[9]);
        ApplyQFT(q);
        Ry(5.501601, q[1]);
        Rxx(4.564167, q[8], q[10]);
        ApplyToEach(MySingleBlock0, q);
        let x = [q[2], q[4], q[8]];
let y = [q[7], q[9], q[11]];
let target = [q[0], q[1], q[3], q[5], q[6], q[10]];
ApplyIfEqualLE(MyAdjCtlBlock0, x, y, target);
        Rz(3.917102, q[8]);
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Adj {
        Ryy(1.701309, q[10], q[5]);
        ApplyToEachA(MySingleBlock2, q);
        Rz(1.969273, q[11]);
        ApplyToEachA(H, q);
        CNOT(q[3], q[6]);
        X(q[4]);
        ApplyQFT(q);
        Y(q[10]);
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit is Adj {
        Z(q[10]);
        ApplyToEachA(MySingleBlock3, q);
        R1(3.685908, q[6]);
        ApplyToEachA(MySingleBlock4, q);
        X(q[3]);
        let x = [q[2], q[4], q[8]];
let y = [q[7], q[9], q[11]];
let target = [q[0], q[1], q[3], q[5], q[6], q[10]];
ApplyIfEqualLE(MyAdjCtlBlock0, x, y, target);
        ApplyToEachA(MySingleBlock5, q);
        ApplyToEachA(MySingleBlock6, q);
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            ApplyRandomBlock0(q);
            Adjoint ApplyRandomBlock1(q);
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