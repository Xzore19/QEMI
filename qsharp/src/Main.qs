namespace Main {

    open Std.Arithmetic;
    open Std.Canon;
    open Std.Convert;
    open Std.Diagnostics;
    open Std.Intrinsic;
    open Std.Logical;
    open Std.Math;
    open Std.Measurement;
    open Std.StatePreparation;

    operation MySingleBlock_9bc97d9b(q : Qubit) : Unit is Adj + Ctl {
        Y(q);
        Rz(2.124106, q);
    }
    operation MySingleBlock_8e6b91bc(q : Qubit) : Unit is Adj + Ctl {
        I(q);
        Ry(2.214992, q);
        Rz(4.278491, q);
    }

function __RandomFlag_a9d20074() : Bool {
    let b0 = true;
    let b1 = not false;
    let b2 = false;
    let b3 = not true;
    return (b0 and b1) or (b2 and not b3);
}



    operation ApplyRandomBlock0(q : Qubit[]) : Unit is Adj {
        operation __InlineIfElseDeadcode_2e4df533(q : Qubit[]) : Unit is Adj {
            if __RandomFlag_a9d20074() {
                    operation __ForLoopZeroBody_f1587f01(q : Qubit[]) : Unit is Adj {
                            operation __GenBlock_4d8aab8f(q : Qubit[]) : Unit is Adj {
                    
                        RippleCarryCGIncByLE([q[1]], [q[2], q[4], q[5], q[9]]);
                        I(q[0]);
                        R1(5.088855, q[3]);
                        ApplyToEachA(MySingleBlock_9bc97d9b, q);
                        S(q[6]);
                        Exp([PauliY, PauliX], 6.166208, [q[5], q[0]]);
                        CCNOT(q[3], q[10], q[2]);
                    }
                            __GenBlock_4d8aab8f(q);
                    }
                    // --- DEADCODE START ---
                    for i in 1..0 {
                        Adjoint __ForLoopZeroBody_f1587f01(q);
                    }
                    // --- DEADCODE END ---
            } else {
                // --- DEADCODE START ---
                        operation __GenBlock_fade4582(q : Qubit[]) : Unit is Adj {
                
                    R1(3.788345, q[3]);
                    Z(q[3]);
                    ApplyPauli([PauliY, PauliY, PauliX], [q[10], q[11], q[9]]);
                    Rzz(5.367358, q[10], q[2]);
                    SWAP(q[10], q[5]);
                    Relabel([q[3], q[4], q[8], q[9]], [q[9], q[8], q[4], q[3]]);
                    S(q[5]);
                    CCNOT(q[4], q[1], q[10]);
                }
                        __GenBlock_fade4582(q);
                // --- DEADCODE END ---
            }
        }
        
        __InlineIfElseDeadcode_2e4df533(q);
    }
    operation ApplyRandomBlock1(q : Qubit[]) : Unit is Ctl {
        operation __ForLoopBody_1501a9bd(q : Qubit[]) : Unit is Ctl {
            operation __ControlledBody_7f35d7ac(q : Qubit[]) : Unit is Adj + Ctl {
                operation __ForLoopZeroBody_8a9c8412(q : Qubit[]) : Unit is Adj + Ctl {
                    operation __ControlledBody_b94b02a1(q : Qubit[]) : Unit is Adj + Ctl {
                            operation __GenBlock_80936c8e(q : Qubit[]) : Unit is Adj + Ctl {
                    
                        Ry(0.16665, q[3]);
                        CY(q[2], q[3]);
                    }
                            Controlled Adjoint __GenBlock_80936c8e([q[2]], [q[0], q[1], q[3], q[4]]);
                    }
                    ApplyControlledOnBitString([true], __ControlledBody_b94b02a1, [q[4]], [q[0], q[1], q[2], q[3], q[5]]);
                    operation __GenBlock_a6a1fdae(q : Qubit[]) : Unit is Adj + Ctl {
                
                    Ryy(2.957319, q[4], q[3]);
                }
                    __GenBlock_a6a1fdae(q);
                }
                // --- DEADCODE START ---
                for i in 1..0 {
                    __ForLoopZeroBody_8a9c8412(q);
                }
                // --- DEADCODE END ---
            }
            ApplyControlledOnInt(3, __ControlledBody_7f35d7ac, [q[1], q[6]], [q[0], q[2], q[3], q[4], q[5], q[7]]);
            operation __GenBlock_6877243b(q : Qubit[]) : Unit is Ctl {
        
            ApplyP(PauliZ, q[2]);
            Rx(3.704701, q[1]);
        }
            __GenBlock_6877243b(q);
        }
        for i in 1..3 {
            Controlled __ForLoopBody_1501a9bd([q[4], q[8]], [q[0], q[1], q[2], q[3], q[5], q[6], q[7], q[9]]);
        }
    }
    operation ApplyRandomBlock2(q : Qubit[]) : Unit {
        operation __RepeatBody_076aa9f0(q : Qubit[]) : Unit {
            operation __WhileBody_1aaa64cc(q : Qubit[]) : Unit {
                    operation __GenBlock_5e807d86(q : Qubit[]) : Unit {
            
                ResetAll([q[8], q[0], q[9], q[6], q[4], q[11]]);
            }
                    __GenBlock_5e807d86(q);
            }
            use flag = Qubit();
            mutable result = Zero;
            X(flag);
            set result = M(flag);
            while (result == One) {
                __WhileBody_1aaa64cc(q);
                X(flag);
                set result = M(flag);
            }
            operation __GenBlock_07264802(q : Qubit[]) : Unit {
        
            ApplyToEach(MySingleBlock_8e6b91bc, q);
        }
            __GenBlock_07264802(q);
        }
        operation __FixupBody_7f73b521(q : Qubit[]) : Unit {
            operation __ForLoopZeroBody_8850b370(q : Qubit[]) : Unit {
                    operation __GenBlock_aba93d90(q : Qubit[]) : Unit {
            
                T(q[4]);
                CZ(q[10], q[11]);
                ResetAll([q[7], q[8], q[10]]);
            AddLE([q[0], q[3], q[5], q[11]], [q[1], q[2], q[4], q[9]], [q[6], q[7], q[8], q[10]]);
                Rzz(3.742874, q[9], q[6]);
            }
                    __GenBlock_aba93d90(q);
            }
            // --- DEADCODE START ---
            for i in 1..0 {
                __ForLoopZeroBody_8850b370(q);
            }
            // --- DEADCODE END ---
        }
        use flag = Qubit();
        mutable result = One;
        repeat {
            X(flag);
            __RepeatBody_076aa9f0(q);
            set result = M(flag);
        } until (result == Zero) fixup {
            __FixupBody_7f73b521(q);
        }
    }

    operation TestCircuit() : Result[] {
        use q = Qubit[12] {
            X(q[0]);
            X(q[6]);
            Adjoint ApplyRandomBlock0(q);
            Controlled ApplyRandomBlock1([q[0], q[6]], [q[1], q[2], q[3], q[4], q[5], q[7], q[8], q[9], q[10], q[11]]);
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