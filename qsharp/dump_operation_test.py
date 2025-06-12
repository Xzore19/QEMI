import qsharp
from qsharp.utils import dump_operation

qsharp.init(project_root=".")

# 调用并接收返回值
results = qsharp.eval("Main.TestCircuit()")

# 打印结果（比如前 5 条测量结果）
for i, shot in enumerate(results[:5]):
    bits = ''.join('1' if r == 1 else '0' for r in shot)
    print(f"Shot {i}: {bits}")