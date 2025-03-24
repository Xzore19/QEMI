from qutefuzz.qiskit_gen import QiskitGenerator

if __name__ == "__main__":
	a = QiskitGenerator(5,1)
	a.check_code()
	a.run()