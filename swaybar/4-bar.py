# this python code is intended to be used to model the 4-bar mechanism

import numpy as np
from scipy.integrate import odeint


def solution():
    L1 = float(input("请输入已知机构参数(杆1):"))
    L2 = float(input("请输入已知机构参数(杆2):"))
    L3 = float(input("请输入已知机构参数(杆3):"))
    Lx_detect=input("未知杆是不是机架??")
    if(Lx_detect=='yes'):
        print("机架为Lx")
        print("机架就是最短杆,必然是双曲柄机构")
    if(Lx_detect=='no'):
        min_bar = min([L1, L2, L3])
        max_bar = max([L1, L2, L3])
        sum_bar = L1 + L2 + L3
        Lx_bi = sum_bar - 2 * max_bar
        Lx_short_max = min(min_bar, Lx_bi)
        if(Lx_short_max>0):
            print("当Lx为最短杆子时:")
            print( str(Lx_short_max)+" <= Lx < "+str(min_bar)+"时,不满足Grashof条件,是双摇杆机构")
            print("0 < Lx < " + str(Lx_short_max) + " 时,满足Grashof条件,必然有曲柄机构")
            frames=input("确定你的机架是哪个杆子?L1,L2,L3")
            if frames=='L1':
                oppo=input("机架为L1,请确定您机架的对向杆,L2,L3,Lx")
                if oppo=='Lx':
                    print("机架为L1,对向杆为Lx")
                    print("机架在最短杆的对面,必然是双摇杆机构")
                else:
                    print("机架为L1,对向杆不为Lx")
                    print("机架在最短杆的侧面,必然是曲柄摇杆机构")
            elif frames=='L2':
                oppo = input("机架为L2,请确定您机架的对向杆,L1,L3,Lx")
                if oppo == 'Lx':
                    print("机架为L2,对向杆为Lx")
                    print("机架在最短杆的对面,必然是双摇杆机构")
                else:
                    print("机架为L2,对向杆不为Lx")
                    print("机架在最短杆的侧面,必然是曲柄摇杆机构")
            elif frames=='L3':
                oppo = input("机架为L3,请确定您机架的对向杆,L1,L2,Lx")
                if oppo == 'Lx':
                    print("机架为L3,对向杆为Lx")
                    print("机架在最短杆的对面,必然是双摇杆机构")
                else:
                    print("机架为L3,对向杆不为Lx")
                    print("机架在最短杆的侧面,必然是曲柄摇杆机构")
        if(Lx_short_max<=0):
            print("Lx为最短杆子时,必然满足Grashof条件,亦即必然有曲柄机构")
        print("当Lx介乎最短杆和最长杆子之间时:")
        
        
    
    
    
    
    
    # if(frames=='L1'):
    #     print("机架为L1")


# 调用函数
solution()