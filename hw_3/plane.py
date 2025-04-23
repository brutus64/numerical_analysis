import numpy as np

def euler_eval(x, y, k):
    try:
        return (y/x) - k * np.sqrt(1 + (y/x)**2)
    except:
        return 0

def euler_method(x, y):
    pass

def plane():
    a, w, v0 = 100, 44, 88
    k = w/v0
    
    x0, y0 = a, 0
    x, y = euler_method(x0,y0)
    
if __name__ == "__main__":
    plane()