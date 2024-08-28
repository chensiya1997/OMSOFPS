import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from find_causal_name import find_causal_name
from input_output import input_and_output
data=pd.read_csv("/mnt/反事实推理/public_test_data.csv")
predict_info=pd.read_csv("/mnt/反事实推理/predict_info.csv")
train_len=len(data)   #训练集
predict_data=data.iloc[0:train_len,:]
size=4
input_para='A'
length_info=[]


def fit(inter_var,inter_time,inter_values):
    causal_name, model, length_info, length = find_causal_name(data, predict_info, input_para, predict_data, size)

    current_time = 71853  # 给定当前时刻
    # 原因参数个数
    T = 2  # 回溯的最长时间
    inter_var = np.random.randint(0, 2, len(causal_name))  # 表示哪些变量需要干预
    inter_time = np.random.randint(0, 1, len(causal_name))  # 表示变量的干预时刻
    inter_values = np.zeros(len(causal_name))  # 具体的取值

    for j in range(len(inter_var)):
        if inter_var[j] == 1:
            inter_time[j] = np.random.randint(1, T)
            inter_values[j] = np.random.random()  # 设置的具体值需要查找
    # print("原因变量：")
    # print(causal_name)
    # print("干预哪些原因变量：")
    # print(inter_var)
    # print("干预的时刻：")
    # print(inter_time)
    # print("干预设置的值：")
    # print(inter_values)
    result = input_and_output(input_para, causal_name, inter_var, inter_time, inter_values, current_time, length, model,
                              length_info)
    return causal_name,inter_var,inter_time,inter_time
