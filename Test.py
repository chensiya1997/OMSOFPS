import pandas as pd
import numpy as np
data=pd.read_csv("E:\\反事实推理\\predict_info.csv")
for i in range(len(data)):
    print(data['para'].iloc[i])
    array=data['info'].iloc[i].split(":")
    count_array=[]
    for j in range(len(array)):
        count_array.append(array[j][0])
    print(len(set(count_array)))



# inter_var = np.random.randint(0, 2, (5,6))
# inter_time = np.random.randint(0, 4, (5,6))
# output1 = pd.DataFrame(inter_var)
# output2 = pd.DataFrame(inter_time)
# print(output1)
# print(output2)
# output1.to_csv("E:\\反事实推理\\data_ganyv.csv",index=False)
# output2.to_csv("E:\反事实推理\\data_time.csv",index=False)
# print(inter_var)

# ganyv = pd.read_csv("C:\\Users\\longx\\Desktop\\data_ganyv.csv")
# inter_time = pd.read_csv("C:\\Users\\longx\\Desktop\\data_time.csv")
# print(inter_time.iloc[1][:])