import argparse
from gr_generator import generate_grover_subcircuit
from grover_replay import replay_grover_case
from math import floor, pi, sqrt

parser = argparse.ArgumentParser(description="Grover 测试生成器 & 重放工具")
parser.add_argument("--mode", choices=["generate", "replay"], required=True)
parser.add_argument("--json", help="重放模式下指定 JSON 路径")
parser.add_argument("--qubits", type=int, default=4, help="Grover Qubit 数")
args = parser.parse_args()

if args.mode == "generate":
    from datetime import datetime
    ts = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    path = f"test_runs/{ts}_grover_{args.qubits}q.json"
    print(f"🧪 正在生成并保存到 {path}")
    generate_grover_subcircuit(num_qubits=args.qubits, save_info_to=path)

elif args.mode == "replay":
    if not args.json:
        print("❗ 请提供 --json 路径以复现")
    else:
        replay_grover_case(args.json)
