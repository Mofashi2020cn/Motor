'''


r21,r31,r41 = 2.949576  2.899993  4.156833

0.000833  0.050000       #real value

-0.21555216 -0.16274831   #measure value

x0 = 0.000833
x1 = 0.050000

sqrt((x0-3)*(x0-3)+ (x1)*(x1) )- sqrt(x0*x0 + x1*x1)
sqrt(x0*x0  + (x1-3)*(x1-3))  -sqrt(x0*x0 + x1*x1)


x0 = -0.21555216
x1 = -0.16274831

x0 = 0.000833
x1 = 0.050000
'''


from scipy.optimize import fsolve
from math import *

x0 = 1.505208
x1 = 2.125000

r21 = sqrt((x0-3)**2+ (x1)**2 )- sqrt(x0**2 + x1**2)
r31 = sqrt(x0**2  + (x1-3)**2)  -sqrt(x0**2 + x1**2)
r41 = sqrt((x0-3)**2  + (x1-3)**2)  -sqrt(x0**2 + x1**2)

print(r21)
print(r31)
print(r41)

'''
r0 = sqrt((x0-3)*(x0-3)+ (x1)*(x1) )- sqrt(x0*x0 + x1*x1)
r1 = sqrt(x0*x0  + (x1-3)*(x1-3))  -sqrt(x0*x0 + x1*x1)

'''
