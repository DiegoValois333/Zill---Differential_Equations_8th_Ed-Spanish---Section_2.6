# Zill 8th Ed (Spanish) - Section. 2.6
# Problem 4, pp 77.
# Euler's Method for Initial Value Problem
# y' = 2*x*y,
# y(1) = 1, y(1.5)

import numpy as np 
import matplotlib.pyplot as plt

dx = 0.05
x0 = 1.0
y0 = 1.0
xf = 1.5
N = int((xf-x0)/dx)

x = np.zeros(N+2)
y = np.zeros(N+2)
s = np.zeros(N+2)
error = np.zeros(N+2)
error_relativo = np.zeros(N+2)

x[0] = x0
y[0] = y0
s[0] = y0

def f(x, y):
    return 2*x*y

def sol(x):
    return np.exp(x**2.0 - 1.0)

def Euler(x0, y0, dx, N):
    print('\n--------------------------SOLUTION-----------------------------\n')
    print('---------------------------------------------------------------')
    print(' x0 \t y0  \t Valor Real  Error Absoluto %Error Relativo')
    print('---------------------------------------------------------------')
    
    for n in range(N+1):
        print('%.4f \t %.4f \t %.4f \t %.4f \t %.4f \t'% (x[n],y[n],s[n], error[n], error_relativo[n]))
        print('---------------------------------------------------------------')
        x[n+1] = x[n] + dx
        y[n+1] = y[n] + dx*f(x[n],y[n])
        s[n+1] = sol(x[n+1])
        error[n+1] = s[n+1] - y[n+1]
        error_relativo[n+1] =100* error[n+1]/s[n+1]
        
# Call Function
Euler(x0, y0, dx, N)

# Graphic
plt.plot(x,y,'ro', x, s)
plt.show()
