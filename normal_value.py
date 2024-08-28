import pandas as pd
import numpy as np
data=pd.read_csv("E:\\反事实推理\\public_test_data.csv")
label=pd.read_csv("E:\\反事实推理\\label.csv")
data_columns=data.columns
for i in range(len(data_columns)):
    para=data_columns[i]
    print(para)
    aver_arr=[]
    for j in range(len(data)):
        if label[para].iloc[j]==0:
            aver_arr.append(data[para].iloc[j])
    print(np.std(aver_arr))
    print("*****************************")