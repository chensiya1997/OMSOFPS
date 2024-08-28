import time
import types
import pandas as pd
import math
import numpy as np
from datetime import datetime
file="E:\\lx\\data\\Sensor1_to_Target.txt"
sensors1=pd.DataFrame(columns=['start_time','end_time','duration','start_time2','end_time2','duration2','start_time3','end_time3','duration3'])
# with open(file,"r") as f:
#     lines=f.readlines()
#     for i in range(len(lines)-2):
#         if len(lines[i].split())>0:
#             print(lines[i].split())
#             if lines[i].split()[0]=='No':
#                 start_time='3 Mar 2023 04:00:00.000'
#                 end_time='3 Mar 2023 04:00:00.000'
#                 duration='3 Mar 2023 04:00:00.000'
#                 data_s={
#                     'start_time':start_time,
#                     'end_time':end_time,
#                     'duration':duration
#                 }
#                 sensors1=sensors1.append(pd.DataFrame(data_s,index=[len(sensors1)]))
#
#             if lines[i].split()[0]=='1':
#                 if len(lines[i+1].split())==0:
#                     start_time = lines[i].split()[1] + ' ' + lines[i].split()[2] + ' ' + lines[i].split()[3] + ' ' + \
#                                  lines[i].split()[4]
#                     end_time = lines[i].split()[5] + ' ' + lines[i].split()[6] + ' ' + lines[i].split()[7] + ' ' + \
#                                lines[i].split()[8]
#                     duration = lines[i].split()[9]
#                     data_s = {
#                         'start_time': start_time,
#                         'end_time': end_time,
#                         'duration': duration
#                     }
#                     sensors1 = sensors1.append(pd.DataFrame(data_s, index=[len(sensors1)]))
#                 else:
#                     #如果需要3,4的话加判断
#                     start_time = lines[i].split()[1] + ' ' + lines[i].split()[2] + ' ' + lines[i].split()[3] + ' ' + \
#                                  lines[i].split()[4]
#                     end_time = lines[i].split()[5] + ' ' + lines[i].split()[6] + ' ' + lines[i].split()[7] + ' ' + \
#                                lines[i].split()[8]
#                     duration = lines[i].split()[9]
#                     start_time2 = lines[i + 1].split()[1] + ' ' + lines[i + 1].split()[2] + ' ' + \
#                                   lines[i + 1].split()[
#                                       3] + ' ' + lines[i + 1].split()[4]
#                     end_time2 = lines[i + 1].split()[5] + ' ' + lines[i + 1].split()[6] + ' ' + \
#                                 lines[i + 1].split()[
#                                     7] + ' ' + lines[i + 1].split()[8]
#                     duration2 = lines[i + 1].split()[9]
#
#                     data_s = {
#                         'start_time': start_time,
#                         'end_time': end_time,
#                         'duration': duration,
#                         'start_time2': start_time2,
#                         'end_time2': end_time2,
#                         'duration2': duration2
#                     }
#                     sensors1 = sensors1.append(pd.DataFrame(data_s, index=[len(sensors1)]))
#
#
#
#
#
#
#
#
# sensors1.to_csv("E:\\lx\\data\\sensors1.csv")


#***************分割线***************************
data=pd.read_csv("E:\\lx\\data\\sensors1.csv")
for i in range(len(data)):
    if isinstance(data['start_time2'].iloc[i],float):
        print("****************")
        start_time = datetime.strptime(data['start_time'].iloc[i], "%Y/%m/%d %H:%M")
        end_time = datetime.strptime(data['end_time'].iloc[i], "%Y/%m/%d %H:%M")
        std_time = datetime.strptime('2023/3/3 4:00', "%Y/%m/%d %H:%M")
        #  diff=end_time-std_time
        data_s = {
            'start_time': (start_time - std_time).total_seconds(),
            'end_time': (end_time - std_time).total_seconds(),
            'duration': data['duration'].iloc[i]
        }
        sensors1 = sensors1.append(pd.DataFrame(data_s, index=[len(sensors1)]))
    else:
        start_time = datetime.strptime(data['start_time'].iloc[i], "%Y/%m/%d %H:%M")
        end_time = datetime.strptime(data['end_time'].iloc[i], "%Y/%m/%d %H:%M")
        std_time = datetime.strptime('2023/3/3 4:00', "%Y/%m/%d %H:%M")
        start_time2 = datetime.strptime(data['start_time2'].iloc[i], "%Y/%m/%d %H:%M")
        end_time2 = datetime.strptime(data['end_time2'].iloc[i], "%Y/%m/%d %H:%M")
        std_time2 = datetime.strptime('2023/3/3 4:00', "%Y/%m/%d %H:%M")
        #  diff=end_time-std_time
        data_s = {
            'start_time': (start_time - std_time).total_seconds(),
            'end_time': (end_time - std_time).total_seconds(),
            'duration': data['duration'].iloc[i],
            'start_time2': (start_time2 - std_time2).total_seconds(),
            'end_time2': (end_time2 - std_time2).total_seconds(),
            'duration2': data['duration2'].iloc[i]
        }
        sensors1 = sensors1.append(pd.DataFrame(data_s, index=[len(sensors1)]))

  #  print(diff.seconds)
sensors1.to_csv("E:\\lx\\data\\processed_sensors1.csv")