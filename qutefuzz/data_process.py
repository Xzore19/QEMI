def file_filter(filename):
    text = ""
    with open(filename, "r") as file:
        for line in file:
            text += line

    # remove the same result
    txt_list = text.split("\ncircuit")
    new_list = [i for i in txt_list if "same" not in i]

    # choice crash
    crash_list = [i for i in new_list if "Traceback" in i]
    print("\n\ncircuit".join(crash_list))
    with open("qiskit_result/crash_result.txt", "w") as file:
        file.write("\n\ncircuit".join(crash_list))

    ks_list = [i for i in new_list if "Traceback" not in i]
    ks_list = [i for i in ks_list if ("KS value: 0.0" in i) or ("np.float64(0.0" in i)]

    with open("qiskit_result/wrong_result.txt", "w") as file:
        file.write("\ncircuit".join(ks_list))

    index = []
    for i in ks_list:
        a,b = i.split(".py")
        index.append(a)
    with open("qiskit_result/need_check.txt", "w") as file:
        for j in index:
            file.write(j+"\n")
    print("\ncircuit".join(ks_list))

def crash_filter(filename):
    text = ""
    with open(filename, "r") as file:
        for line in file:
            text += line

    txt_list = text.split("\ncircuit")
    new_list = [i for i in txt_list if "CXCancellation" not in i]
    new_list = [i for i in new_list if "NormalizeRXAngle" not in i]
    print("\ncircuit".join(new_list))


if __name__ == "__main__":
    # filename = "qiskit_result/quantum_circuits/_results.txt"
    # file_filter(filename)

    filename = "qiskit_result/crash_result.txt"
    crash_filter(filename)
