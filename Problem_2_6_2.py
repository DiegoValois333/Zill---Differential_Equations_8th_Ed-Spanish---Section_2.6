# Zill 8th Ed (Spanish) - Section. 2.6
# Problem 2, pp 77.
# Euler's Method for Initial Value Problem
# y' = x + y**2.0,
# y(0) = 0, y(0.2)

import numpy as np 
import matplotlib.pyplot as plt

dx = 0.1
x0 = 0.0
y0 = 0.0
xf = 0.2
N = int((xf-x0)/dx)

x = np.zeros(N+2)
y = np.zeros(N+2)


x[0] = x0
y[0] = y0


def f(x, y):
    return x + y**2.0

def Euler(x0, y0, dx, N):
    print('\n-----------SOLUTION-----------\n')
    print('-----------------------------------')
    print(' x0 \t y0  \t')
    print('-----------------------------------')
    
    for n in range(N+1):
        print('%.4f \t %.4f \t '% (x[n],y[n]))
        print('------------------------------------')
        x[n+1] = x[n] + dx
        y[n+1] = y[n] + dx*f(x[n],y[n])
        
        
# Call Function
Euler(x0, y0, dx, N)

# Graph
plt.plot(x,y,'ro')
plt.show()
