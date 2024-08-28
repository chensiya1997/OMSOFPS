from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
import pandas as pd
data_real=pd.read_csv("E:\\transfer_entropy_predict\LSTM\\Alstm_label.csv")
data_rdbn=pd.read_csv("E:\\transfer_entropy_predict\\data\\short_predict.csv")
columns=data_real.columns
for i in range(len(columns)):
    print(columns[i])
    print("LSTM")
    print("MSE")
    print(mean_squared_error(data_real[columns[i]],data_rdbn[columns[i]]))
    print("MAE")
    print(mean_absolute_error(data_real[columns[i]],data_rdbn[columns[i]]))
    print("***********************************")