'''
    5 * x1 - 25 = 0
    5 * x0 * x0 - x1 * x2 = 0
    x2 * x0 -27 = 0

scipy.optimize fsolve(func, x)
#   所使用的scipy中的库optimize以及方法fsolve
#   func 是自己构造的函数
'''

from scipy.optimize import fsolve
from math import *

def func(x):
    x0, x1 = x.tolist()
    return [
            sqrt((x0-3)**2+ (x1)**2 )- sqrt(x0**2 + x1**2) + 0.006006724149965059,
            sqrt(x0**2  + (x1-3)**2)  -sqrt(x0**2 + x1**2) + 0.8630323110262648
           ]

r = fsolve(func,[1,1])
print(r)


'''

x0 = 1.505208
x1 = 2.125000

-0.006006724149965059
-0.8630323110262648
-0.8720294217854525

'''
