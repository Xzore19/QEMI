class DeadCodeFuzzer():
    def __init__(self):
        pass

    def classical_dead(self):
        # append dead code for classical condition
        code_line = "\n"
        code_line += "a = 1 \n"
        code_line += "if a == 2:\n"
        code_line += "\tqc.h(0) \n"
        return code_line

    def quantum_dead(self):
        pass