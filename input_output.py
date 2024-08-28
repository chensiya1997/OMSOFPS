import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
data=pd.read_csv("/mnt/反事实推理/public_test_data.csv")
predict_info=pd.read_csv("/mnt/反事实推理/test_predict_info.csv")
train_len=len(data)   #训练集
predict_data=data.iloc[0:train_len,:]
size=4




def input_and_output(input_para,causal_name,inter_var,inter_time,inter_values,current_time,length,model,length_info):
    for j in range(len(inter_time)):
        if inter_time[j] > 0:
            data[causal_name[j]].iloc[current_time - inter_time[j]] = inter_values[
                j]  # 在inter_time[j]时刻进行干预，将值设置为inter_values[j]
            for k in range(1, inter_time[j]):
                str_name = causal_name[j] + '_t_1'  # 会对其他变量产生影响的原因变量，即解释变量
                for m in range(len(predict_info)):  # 判断有哪些列的名称需要修改
                    length_info_ss = predict_info['info'].iloc[m].split(":")
                    if str_name in length_info_ss:
                        response = predict_info['para'].iloc[m][0]
                        new_data_ss = pd.DataFrame(predict_data[response][size:length]).reset_index(drop=True)
                        for n in range(len(length_info_ss)):
                            name_ss = length_info_ss[n].split("_")[0]  # 参数名
                            sssize = int(length_info_ss[n].split("_")[2])  # 长度
                            new_data_ss[length_info_ss[n]] = pd.DataFrame(
                                data[name_ss][size - sssize:length - sssize]).reset_index(drop=True)
                        para_merge = response + '_t_0'
                        coef = np.array(predict_info[predict_info['para'] == para_merge]['coef'].iloc[0].split(',')).astype(np.float)
                        intercept = predict_info[predict_info['para'] == para_merge]['intercept'].iloc[0]
                        inter_s_value=np.dot(new_data_ss.iloc[current_time - size - k,1:len(new_data_ss)].values,coef.T)+intercept
#***************************************
                        # models = LinearRegression()  #
                        # models.fit(new_data_ss.iloc[0:70000, 1:len(new_data_ss)],
                        #            new_data_ss.iloc[0:70000, 0])  # 参数学习
                        # inter_s_value = models.predict(
                        #     new_data_ss.iloc[(current_time - size - k):(current_time - size - k + 1),
                        #     1:len(new_data_ss)])
                        data[response].iloc[current_time - k] = inter_s_value

    new_new_data = pd.DataFrame(predict_data[input_para][size:length]).reset_index(drop=True)
    for j in range(len(length_info)):
        name = length_info[j].split("_")[0]  # 参数名
        ssize = int(length_info[j].split("_")[2])  # 长度
        new_new_data[length_info[j]] = pd.DataFrame(data[name][size - ssize:length - ssize]).reset_index(drop=True)
    result_new = model.predict(new_new_data.iloc[current_time - size:current_time - size + 1, 1:len(new_new_data)])
    return result_new[0]


