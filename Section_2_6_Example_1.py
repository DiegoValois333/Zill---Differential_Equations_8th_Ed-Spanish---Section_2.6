# Zill 8th Edition (Spanish) - Section. 2.6
# Example 1, pp 75.
# Euler's method for Problems with initial value contitions
# Problem:
# y' = 0.1*y**0.5 + 0.4*x**2.0
# y(2) = 4, y(2.5)

import numpy as np 
import matplotlib.pyplot as plt

dx = 0.1
x0 = 2.0
y0 = 4.0
xf = 2.5
N = int((xf-x0)/dx)

x = np.zeros(N+2)
y = np.zeros(N+2)

x[0] = x0
y[0] = y0
    

def f(x, y):
    return 0.1*y**0.5 + 0.4*x**2.0


def Euler(x0, y0, dx, N):
    print('\n--------SOLUTION--------')
    print('--------------------------')
    print('x0 \t y0 \t')
    print('--------------------------')
    
    for n in range(N+1):
        print('%.4f \t %.4f \t '% (x[n],y[n]))
        print('--------------------------')
        x[n+1] = x[n] + dx
        y[n+1] = y[n] + dx*f(x[n],y[n])    
    

# Call function
Euler(x0, y0, dx, N)

# Graphic
plt.plot(x,y,'ro')
plt.show()
