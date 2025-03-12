import numpy as np
import matplotlib.pylab as plt

def Sigmoid(x):
    '''
    return 1 / (1 + np.exp(-x))
    '''
    x = np.array([-5.0, 5.0, 0.1])
    y = sigmoid(x)
    plt.plot(x,y)
    plt.ylim(-0.1, 1.1)
    plt.show()