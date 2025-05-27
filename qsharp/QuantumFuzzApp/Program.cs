using System;
using Microsoft.Quantum.Simulation.Simulators;

class Program
{
    static void Main(string[] args)
    {
        // ✅ 使用 QuantumSimulator（完全模拟）
        using var sim = new QuantumSimulator();

        // 调用 Q# 操作
        var result = QuantumFuzz.TestCircuit.Run(sim).Result;

        Console.WriteLine($"Result: {string.Join(", ", result)}");
    }
}
