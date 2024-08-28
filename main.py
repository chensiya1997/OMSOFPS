#还需要写循环，判断时刻是否异常，计算正确率，需要计算方差，利用3-sigma法则判断是否异常
import math
import random
import datetime
import time
import numpy as np
import matplotlib.pyplot as plt
import pylab as mpl
import math
from demo import fit
import pandas as pd
from find_causal_name import find_causal_name
from input_output import input_and_output
mpl.rcParams['font.sans-serif'] = ['SimHei']
data=pd.read_csv("/mnt/反事实推理/public_test_data.csv")
predict_info=pd.read_csv("/mnt/反事实推理/test_predict_info.csv") #因果图 亲子关系函数
normal_value=pd.read_csv("/mnt/反事实推理/normal_value.csv")
info=pd.read_csv("/mnt/反事实推理/predict_info.csv")
train_len=len(data)   #训练集
predict_data=data.iloc[0:train_len,:]
label=pd.read_csv("/mnt/反事实推理/label.csv")
size=4 #马尔科夫阶数
result_accuracy=pd.DataFrame(columns=['para','accuracy'])
#input_para='D'  #['A','C']  （这个参数也需要循环）


# ganyv = pd.read_csv("E:\\反事实推理\\data_ganyv.csv")
# inter_time = pd.read_csv("E:\\反事实推理\\data_time.csv")
#print(len(ganyv.columns))

# x = [0, 1, 1, 0, 0, 0, 0, 0, 1]  # 表示哪些变量需要干预
# y = [0, 2, 3, 0, 0, 0, 0, 0, 2]  # 表示变量的干预时刻
class PSO:
    def __init__(self, dimension, time, size, low, up, v_low, v_high,current_time,input_para):
        # 初始化
        self.dimension = dimension  # 变量个数
        self.time = time  # 迭代的代数
        self.size = size  # 种群大小
        self.current_time=current_time
        self.input_para=input_para
        self.bound = []  # 变量的约束范围
        self.bound.append(low)
        self.bound.append(up)
        self.v_low = v_low
        self.v_high = v_high
        self.x = np.zeros((self.size, self.dimension))  # 所有粒子的位置
        self.v = np.zeros((self.size, self.dimension))  # 所有粒子的速度
        self.p_best = np.zeros((self.size, self.dimension))  # 每个粒子最优的位置
        self.g_best = np.zeros((1, self.dimension))[0]  # 全局最优的位置

        # 初始化第0代初始全局最优解
        temp = -1000000
        for i in range(self.size):
            for j in range(self.dimension):
                self.x[i][j] = random.uniform(self.bound[0][j], self.bound[1][j])
                self.v[i][j] = random.uniform(self.v_low, self.v_high)
            self.p_best[i] = self.x[i]  # 储存最优的个体
            fit = self.fitness(x,y,self.p_best[i])
            # 做出修改
            if fit > temp:
                self.g_best = self.p_best[i]
                temp = fit

    def fitness(self,x,y,z):
        """
        个体适应值计算
        """
        causal_name, model, length_info, length = find_causal_name(data, predict_info, input_para, predict_data, size)
        do_level=np.random.randint(1,3,len(x))
        do_normal = np.random.randint(1, 3, len(x))
        z=x*z
        target2=0
        target3=0
        target4=0
        for m in range(len(x)):
            target2=target2+x[m]*do_level[m]
            target3=target3+x[m]*y[m]
            target4 = target4 + x[m] * do_normal[m]

#        z = np.multiply(x.values,z)
        # z = np.zeros(len(causal_name))  # 具体的取值
        # for j in range(len(x)):
        #     if x[j] == 1:
        #         y[j] = np.random.randint(1, T)
        #         z[j] = np.random.random()  # 设置的具体值需要查找
        result = input_and_output(input_para, causal_name, x, y, z, current_time, length,
                                  model,
                                  length_info)

        return -math.fabs(result-input_normal_value)-0.1*target2-0.1*target3-0.1*target4  #目标函数，目标函数需要改变，改成自动查询

    def update(self, size):
        c1 = 2.0  # 学习因子
        c2 = 2.0
        # 自适应权重更新粒子群优化
        w_max = 0.8  # 自身权重因子
        w_min = 0.2
        for i in range(size):
            # 更新速度(核心公式)
            w = (w_max-w_min)/(i+1)
            self.v[i] = w * self.v[i] + c1 * random.uniform(0, 1) * (
                    self.p_best[i] - self.x[i]) + c2 * random.uniform(0, 1) * (self.g_best - self.x[i])
            # 速度限制
            for j in range(self.dimension):
                if self.v[i][j] < self.v_low:
                    self.v[i][j] = self.v_low
                if self.v[i][j] > self.v_high:
                    self.v[i][j] = self.v_high

            # 更新位置
            self.x[i] = self.x[i] + self.v[i]
            # 位置限制
            for j in range(self.dimension):
                if self.x[i][j] < self.bound[0][j]:
                    self.x[i][j] = self.bound[0][j]
                if self.x[i][j] > self.bound[1][j]:
                    self.x[i][j] = self.bound[1][j]
            # 找到最优的粒子，看最大还是最小，之后代入
            # 更新p_best和g_best
            if self.fitness(x,y,self.x[i]) > self.fitness(x,y,self.p_best[i]):
                self.p_best[i] = self.x[i]
            if self.fitness(x,y,self.x[i]) > self.fitness(x,y,self.g_best):
                self.g_best = self.x[i]

    def pso(self):
        best = []
        self.final_best = np.zeros(len(ganyv.columns))   #这里需要改
        for gen in range(self.time):
            self.update(self.size)
            if self.fitness(x,y,self.g_best) > self.fitness(x,y,self.final_best):
                self.final_best = self.g_best.copy()
            # print('当前最佳位置：{}'.format(self.final_best))
            temp = self.fitness(x,y,self.final_best)
            # print('当前的最佳适应度：{}'.format(temp))
            best.append(temp)
        return self.final_best,best[len(best)-1]


if __name__ == '__main__':
    start_time=datetime.datetime.now()
    #从此处开始循环，要是异常的话开始反事实推理
    data_columns=data.columns
    for m in range(10,len(data_columns)):
        input_para=data_columns[m]
        print(input_para)
        count=0
        total_count=0
        for k in range(70000, 71853):
            current_time = k
            if label[input_para].iloc[k] == 1:
                total_count=total_count+1
                print("当前时刻")
                print(current_time)
                input_normal_value = normal_value[normal_value['para'] == input_para]['value'].iloc[0]
                input_normal_std = normal_value[normal_value['para'] == input_para]['std'].iloc[0]
                length_info = []
                # current_time = 71853   #需要循环的部分
                T = 4 # 回溯的最长时间
                input_para_t = input_para + "_t_0"
                causal_length = info[info['para'] == input_para_t]['number'].iloc[0]

                inter_var = np.random.randint(0, 2, (5, causal_length))
                inter_time = np.random.randint(0, 4, (5, causal_length)) #intervention time
                ganyv = pd.DataFrame(inter_var)
                inter_time = pd.DataFrame(inter_time)
                ganyv.to_csv("/mnt/反事实推理/data_ganyv.csv", index=False)
                inter_time.to_csv("/mnt/反事实推理/data_time.csv", index=False)
                col = 0
                row = 0
                final_inter_value = []
                final_best = -10000
                for i in range(len(ganyv)):
                    for j in range(len(inter_time)):
                        print(i)
                        print(j)
                        causal_name, model, length_info, length = find_causal_name(data, predict_info, input_para,
                                                                                   predict_data, size)
                        time = 3  # 100
                        size = 5  # 50  种群大小
                        dimension = len(causal_name)
                        v_low = -1
                        v_high = 1
                        low = np.zeros(len(causal_name))  
                        up = 5 * np.ones(len(causal_name))
                        for k in range(len(causal_name)):
                            para_merge = causal_name[k] + '_t_0'
                            low[k] = predict_info[predict_info['para'] == para_merge]['min'].iloc[0]
                            up[k] = predict_info[predict_info['para'] == para_merge]['max'].iloc[0]

                        x = ganyv.iloc[i][:]
                        y = inter_time.iloc[j][:]
                        # print(x)
                        pso = PSO(dimension, time, size, low, up, v_low, v_high, current_time, input_para)
                        inter_value, best_value = pso.pso()
                        if best_value > final_best:
                            final_best = best_value
                            col = i
                            row = j
                            final_inter_value = inter_value

                        print("当前最优解：")
                        print(inter_value)
                        print("当前最优值：")
                        print(best_value)
                print("最佳干预变量：")
                print(col)
                print("最佳干预时刻：")
                print(row)
                print("最佳干预值：")

                print(final_inter_value)
                print("干预后的目标函数：")
                print(final_best)
                if math.fabs(final_best) < 3*input_normal_std:  # 根据3-sigma法则判断是否异常
                    count = count + 1
        print("****************")
        print(input_para)
        if total_count==0:
            print("该时间段无故障")
        else:
            date_s={
                'para':input_para,
                'accuracy':count/total_count
            }
            print("准确率")
            print(date_s)
            print(count / total_count)
            result_accuracy=result_accuracy.append(pd.DataFrame(date_s,index=[len(result_accuracy)]))
            result_accuracy.to_csv("/mnt/反事实推理/result.csv")

        print("****************")



    end_time=datetime.datetime.now()
    print((end_time-start_time))

            # 每步的ij数据记录下来，之后再整体中找到最小/最大的