import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# data=pd.read_csv("E:\\反事实推理\\public_test_data.csv")
# predict_info=pd.read_csv("E:\\反事实推理\\predict_info.csv")
# train_len=len(data)
# predict_data=data.iloc[0:train_len,:]
# size=3
# length = len(predict_data)
# coef=[]
# intercept=[]
# for i in range(len(predict_info)):
#     pre_para = predict_info['para'].iloc[i].split("_")[0]
#     new_data = pd.DataFrame(predict_data[pre_para][size:length]).reset_index(drop=True)
#     length_info = predict_info['info'].iloc[i].split(":")
#     for j in range(len(length_info)):
#         name = length_info[j].split("_")[0]  # 参数名
#         ssize = int(length_info[j].split("_")[2])  # 长度
#         new_data[length_info[j]] = pd.DataFrame(data[name][size - ssize:length - ssize]).reset_index(drop=True)
#     model = LinearRegression()
#     model.fit(new_data.iloc[0:70000, 1:len(new_data)], new_data.iloc[0:70000,0])
#     coef.append(model.coef_)
#     intercept.append(model.intercept_)
#
# predict_info['coef']=coef
# predict_info['intercept']=intercept
# print(coef)
# print(intercept)
# print(predict_info)
# predict_info.to_csv("E:\\反事实推理\\test_predict_info.csv")
#
# data=pd.read_csv("E:\\反事实推理\\test_predict_info.csv")
# for i in range(len(data)):
#     x=np.array(data['coef'].iloc[i].split(','))
#     y=x.astype(np.float)
#     print(y)

# response='A'
# para_merge=response+'_t_0'
# coef=np.array(data[data['para'] == para_merge]['coef'].iloc[0].split(',')).astype(np.float)
# intercept=data[data['para'] == para_merge]['intercept'].iloc[0]
# print(coef)
# print(intercept)

#每个参数的取值范围
data=pd.read_csv("E:\\反事实推理\\public_test_data.csv")
columns=data.columns
for i in range(len(columns)):
    plt.title(columns[i])
    plt.plot(data[columns[i]])
    plt.show()