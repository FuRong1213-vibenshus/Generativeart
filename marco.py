import math

import matplotlib.pyplot as plt

def dy(x,y):

    y_marked = 2 - math.exp(-4*x) - 2*y

    return y_marked
 
def euler_metod(x0, y0 ,n , h):

    x = [""]*n

    y = [""]*n

    x[0] = x0

    y[0] = y0
 
    for j in range (0, n-1):

        y[j + 1] = y[j] + h * dy(x[j], y[j])

        x[j + 1] = x[j] + h

    return x, y
 
def test():

    print(euler_metod(0, 1, 100, 0.1))

    print(euler_metod(0, 1, 100, 0.01))

    plt.subplot(2, 1, 1)

    x1, y1 = euler_metod(0, 1, 100, 0.1)

    plt.plot(x1,y1)

    plt.subplot(2,1,2)

    x2, y2 = euler_metod(0, 1, 100, 0.01)

    plt.plot(x2,y2)

    plt.show()
 
test()