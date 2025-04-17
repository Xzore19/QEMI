def probability_checker(truth, fuzzing, shot, qnum):
    # 对于两个概率分布结果进行误差分析
    check_list = [f'{num:0{qnum}b}' for num in range(pow(2, qnum))]
    counter = 0
    for i in check_list:
        counter += abs(truth.get(i, 0) - fuzzing.get(i, 0))/2
    if counter/shot > 0.5:
        print("error:", counter/shot)
        return False
    else:
        return True