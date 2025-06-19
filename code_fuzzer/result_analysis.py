from scipy.stats import ks_2samp
from scipy.spatial.distance import jensenshannon
import numpy as np

def remove_cr(dis, qnum):
    cleaned_counts = {}
    for k, v in dis.items():
        bits = k.replace(" ", "")[-qnum:]  # 提取最后5位
        cleaned_counts[bits] = cleaned_counts.get(bits, 0) + v
    # print(cleaned_counts)
    return cleaned_counts

# def probability_checker(truth, fuzzing, shot, qnum):
#     truth = remove_cr(truth, qnum)
#     fuzzing = remove_cr(fuzzing, qnum)
#     # 对于两个概率分布结果进行误差分析
#     check_list = [f'{num:0{qnum}b}' for num in range(pow(2, qnum))]
#     truth_list = [truth.get(i, 0) for i in check_list]
#     fuzzing_list = [fuzzing.get(i, 0) for i in check_list]

#     stat, pvalue = ks_2samp(truth_list, fuzzing_list)

#     if stat > 0.2 and pvalue < 0.2:
#         print("stat:", stat)
#         print("pvalue", pvalue)
#         print(truth)
#         print("=========================================")
#         print(fuzzing)
#         return False
#     else:
#         return True

def probability_checker(truth, fuzzing, shot, qnum):
    truth = remove_cr(truth, qnum)
    fuzzing = remove_cr(fuzzing, qnum)
    check_list = [f'{num:0{qnum}b}' for num in range(pow(2, qnum))]
    truth_list = [truth.get(i, 0) for i in check_list]
    fuzzing_list = [fuzzing.get(i, 0) for i in check_list]

    # 归一化为概率分布
    p = np.asarray(truth_list)
    q = np.asarray(fuzzing_list)

    p = p / p.sum()
    q = q / q.sum()

    metric = np.sqrt(0.5 * np.sum((np.sqrt(p) - np.sqrt(q)) ** 2))

    if metric > 0.1:
        # print("Hellinger Distance:", metric)
        # print(truth)
        # print("=========================================")
        # print(fuzzing)
        return False
    else:
        return True