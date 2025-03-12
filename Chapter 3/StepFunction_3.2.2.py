import numpy as np

def step_function(x):
    '''
    if x > 0:
        return 1
    else:
        return 0
    '''
    y = x > 0 #array([True, True, False])를 [1,1,0]으로 변환해줌
    return y.astype(np.int)
