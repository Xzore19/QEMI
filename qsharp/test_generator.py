from qsharp_generator import QSharpGenerator

if __name__ == "__main__":
    g = QSharpGenerator(qubit_num=12, num_blocks=3, depth_per_block=8)
    g.save_to_file("src/Main.qs")
