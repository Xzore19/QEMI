import qsharp

qsharp.init(project_root=".")

print(qsharp.eval("Main.Main()"))