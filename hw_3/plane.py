import numpy as np

def dydx(x, y, k):
    try:
        #the dy/dx to find slope
        return (y/x) - k * np.sqrt(1 + (y/x)**2)
    except:
        return 0


def euler_method():
    a, w, v0 = 100, 44, 88
    k = w/v0
    
    x0, y0 = a, 0
    #idea is we start at (a,0) use to find next point, we have some step size that goes backwards
    x, y, xf, yf = x0, y0, 0, 0
    h = -0.1 #our step size backwards
    
    while x >= xf:
        slope = dydx(x,y, k)
        print(f"(x,y):({x:.4f},{y:.4f}), slope:{slope:.4f} -> new: (x,y): ({x-h:.4f},{y-h*slope:.4f})")
        x += h
        y += h * slope
    print(f"Final (x,y): ({x},{y})")
    
    
if __name__ == "__main__":
    euler_method()