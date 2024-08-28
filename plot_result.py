import matplotlib.pyplot as plt
import pandas as pd
import datetime
plt.rc('font',family='Times New Roman')
plt.rcParams.update({'font.size':10})
plt.figure(figsize=(12, 10))
plt.tight_layout()
plt.subplots_adjust(left=0.1,bottom=None,right=None,top=None,wspace=None,hspace=None)
time=pd.read_csv("E:\\反事实推理\\time.csv")
data=pd.read_csv("E:\\transfer_entropy_predict\\public_test_data.csv")[70000:]
label=pd.read_csv("E:\\transfer_entropy_predict\\data\\label.csv")[70000:]
print(len(data))
ax1=plt.subplot(4,3,1)
ax1.set_ylabel("A")
ax1.plot(time['time'].values,data['A'].values,label='A')
ax1.plot(time['time'].values,label['A'].values,label='fault')
####################################
ax2=plt.subplot(4,3,2)
ax2.set_ylabel("E")
ax2.plot(time['time'].values,data['E'].values,label='E')
ax2.plot(time['time'].values,label['E'].values,label='fault')

####################
ax3=plt.subplot(4,3,3)
ax3.set_ylabel("H")
ax3.plot(time['time'].values,data['H'].values,label='H')
ax3.plot(time['time'].values,label['H'].values,label='fault')

###############
ax4=plt.subplot(4,3,4)
ax4.set_ylabel("I")
ax4.plot(time['time'].values,data['I'].values,label='I')
ax4.plot(time['time'].values,label['I'].values,label='fault')

##########
ax5=plt.subplot(4,3,5)
ax5.set_ylabel("J")
ax5.plot(time['time'].values,data['J'].values,label='J')
ax5.plot(time['time'].values,label['J'].values,label='fault')

###########
ax6=plt.subplot(4,3,6)
ax6.set_ylabel("K")
ax6.plot(time['time'].values,data['K'].values,label='K')
ax6.plot(time['time'].values,label['K'].values,label='fault')

ax7=plt.subplot(4,3,7)
ax7.set_ylabel("M")
ax7.plot(time['time'].values,data['M'].values,label='M')
ax7.plot(time['time'].values,label['M'].values,label='fault')

ax8=plt.subplot(4,3,8)
ax8.set_ylabel("N")
ax8.plot(time['time'].values,data['N'].values,label='N')
ax8.plot(time['time'].values,label['N'].values,label='fault')

ax9=plt.subplot(4,3,9)
ax9.set_ylabel("O")
ax9.plot(time['time'].values,data['O'].values,label='O')
ax9.plot(time['time'].values,label['O'].values,label='fault')

ax10=plt.subplot(4,3,10)
ax10.set_ylabel("P")
ax10.plot(time['time'].values,data['P'].values,label='P')
ax10.plot(time['time'].values,label['P'].values,label='fault')

ax11=plt.subplot(4,3,11)
ax11.set_ylabel("R")
ax11.plot(time['time'].values,data['R'].values,label='R')
ax11.plot(time['time'].values,label['R'].values,label='fault')

ax12=plt.subplot(4,3,12)
ax12.set_ylabel("T")
ax12.plot(time['time'].values,data['T'].values,label='value')
ax12.plot(time['time'].values,label['T'].values,label='fault')


plt.legend(bbox_to_anchor=(0.7, 1), loc='lower left')
plt.savefig("E:\\反事实推理\\反事实论文\\数据展示.png", dpi=1000, bbox_inches = 'tight')
plt.show()