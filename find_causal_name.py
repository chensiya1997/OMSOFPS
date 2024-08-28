import pandas as pd
from sklearn.linear_model import LinearRegression

def find_causal_name(data,predict_info,input_para,predict_data,size):
    causal_name=[]
    # model=[]
    # length_info=[]
    for i in range(len(predict_info)):
        length = len(predict_data)
        if predict_info['para'].iloc[i] == input_para + '_t_0':
            new_data = pd.DataFrame(predict_data[input_para][size:length]).reset_index(drop=True)
            length_info = predict_info['info'].iloc[i].split(":")
            for j in range(len(length_info)):
                name = length_info[j].split("_")[0]  # 参数名
                if name not in causal_name:
                    causal_name.append(name)
                ssize = int(length_info[j].split("_")[2])  # 长度
                new_data[length_info[j]] = pd.DataFrame(data[name][size - ssize:length - ssize]).reset_index(drop=True)
            model = LinearRegression()
            model.fit(new_data.iloc[0:len(new_data) - 1, 1:len(new_data)], new_data.iloc[0:len(new_data) - 1, 0])
    return causal_name,model,length_info,length