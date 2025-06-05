namespace Main_fuzzing {

    open Std.Arithmetic;
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Math;
    open Std.Measurement;
    open Std.StatePreparation;



function __RandomFlag_22333fb3() : Bool {
    let b0 = not ResultAsBool(One);
    let b1 = ResultAsBool(Zero);
    let b2 = ResultAsBool(One);
    let b3 = ResultAsBool(One);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_b80e6636() : Bool {
    let b0 = not false;
    let b1 = not true;
    let b2 = not true;
    let b3 = not true;
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_94bb3228() : Bool {
    let b0 = not ResultAsBool(Zero);
    let b1 = ResultAsBool(Zero);
    let b2 = ResultAsBool(One);
    let b3 = not ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_352c1bb7() : Bool {
    let b0 = ResultAsBool(One);
    let b1 = ResultAsBool(Zero);
    let b2 = not ResultAsBool(Zero);
    let b3 = not ResultAsBool(Zero);
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_ca13b3ad() : Bool {
    let b0 = not true;
    let b1 = not false;
    let b2 = true;
    let b3 = not false;
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_f87573f8() : Bool {
    let b0 = not false;
    let b1 = not true;
    let b2 = false;
    let b3 = not true;
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_8fbad987() : Bool {
    let b0 = not true;
    let b1 = not true;
    let b2 = not false;
    let b3 = true;
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_16f3152b() : Bool {
    let b0 = not false;
    let b1 = false;
    let b2 = true;
    let b3 = true;
    return (b0 and b1) or (b2 and not b3);
}
function __RandomFlag_9ad67635() : Bool {
    let b0 = not ResultAsBool(One);
    let b1 = ResultAsBool(Zero);
    let b2 = ResultAsBool(One);
    let b3 = not ResultAsBool(One);
    return (b0 and b1) or (b2 and not b3);
}

    operation ApplyRandomBlock0(q : Qubit[]) : Unit {
        operation __RepeatBody_53c5caf9(q : Qubit[]) : Unit {
            operation __WhileBody_fea67271(q : Qubit[]) : Unit {
                operation __WhileBody_35da3f78(q : Qubit[]) : Unit {
                        R1(4.705544, q[2]);
                        Rzz(4.12544, q[3], q[11]);
                }
                use flag = Qubit();
                mutable result = Zero;
                X(flag);
                set result = M(flag);
                while (result == One) {
                    __WhileBody_35da3f78(q);
                    X(flag);
                    set result = M(flag);
                }
            }
            use flag = Qubit();
            mutable result = Zero;
            X(flag);
            set result = M(flag);
            while (result == One) {
                __WhileBody_fea67271(q);
                X(flag);
                set result = M(flag);
            }
        }
        repeat {
            __RepeatBody_53c5caf9(q);
        } until (__RandomFlag_9ad67635()) fixup {
        }
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit {
        operation __WhileBody_e1756cd3(q : Qubit[]) : Unit {
            operation __WhileBody_726ec51c(q : Qubit[]) : Unit {
                    H(q[2]);
                    Ry(0.10754, q[10]);
            }
            use flag = Qubit();
            mutable result = Zero;
            X(flag);
            set result = M(flag);
            while (result == One) {
                __WhileBody_726ec51c(q);
                X(flag);
                set result = M(flag);
            }
        }
        use flag = Qubit();
        mutable result = Zero;
        X(flag);
        set result = M(flag);
        while (result == One) {
            __WhileBody_e1756cd3(q);
            X(flag);
            set result = M(flag);
        }
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit {
        operation __WhileBody_71b91ce2(q : Qubit[]) : Unit {
            operation __WhileBody_0ae9562e(q : Qubit[]) : Unit {
                    Ry(4.425204, q[3]);
                    X(q[3]);
            }
            use flag = Qubit();
            mutable result = Zero;
            X(flag);
            set result = M(flag);
            while (result == One) {
                __WhileBody_0ae9562e(q);
                X(flag);
                set result = M(flag);
            }
        }
        use flag = Qubit();
        mutable result = Zero;
        X(flag);
        set result = M(flag);
        while (result == One) {
            __WhileBody_71b91ce2(q);
            X(flag);
            set result = M(flag);
        }
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            ApplyRandomBlock0(q);
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