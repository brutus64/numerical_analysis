import numpy as np
import time

def eval_sign(v: np.float16) -> int: 
    return np.sign(np.float16(np.e)**(-v**3) - (v**4) - np.sin(v))

def evaluate(v: np.float64) -> np.float64:
    return np.e**(-v**3) - (v**4) - np.sin(v)

def bisection(a:np.float32,b:np.float32) -> np.float64:
    sign_a = eval_sign(a)
    #sign_b = eval_sign(b)
    while b-a > 0.00005: #need to be accurate within 0.00005
        c = (a+b)/2
        print(f"value a:{a}, b:{b}, c:{c}")
        print(f"eval a:{evaluate(a)}, b:{evaluate(b)}, c:{evaluate(c)}")
        sign_c = eval_sign(np.float16(c))
        if sign_a * sign_c < 0: #root in a side, set b to be middle (no need sign_b)
            b = c
            # sign_b = sign_c
        else: #root in b side, set a to be middle and set sign_a so no recalculation
            a, sign_a = c, sign_c
    return (np.float64(a)+np.float64(b))/2 #the final booundary is set, get middle of that

def newton():
    pass

def secant():
    pass

def monte():
    pass

if __name__ == "__main__":
    start = time.time()
    res = bisection(-1,1)
    end = time.time()
    print(f"root estimation: {res}")
    print(f"time: {end-start} seconds")