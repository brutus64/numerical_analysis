import numpy as np
import time

def eval_sign(v: np.float64) -> int: 
    return np.sign(np.float64(np.e)**(-v**3) - (v**4) - np.sin(v))

def evaluate(v: np.float64) -> np.float64:
    return np.e**(-v**3) - (v**4) - np.sin(v)

def bisection(a: int,b: int) -> np.float64:
    a, b = np.float64(a), np.float64(b)
    sign_a = eval_sign(a)
    #sign_b = eval_sign(b)
    while b-a > 0.0001: #need to be accurate within 0.00005, 0.0001 is enough if we use intervals as midpoint would guarantee root is only < 0.00005 away
        c = (a+b)/2
        # print(f"value a:{a}, b:{b}, c:{c}")
        # print(f"eval a:{evaluate(a)}, b:{evaluate(b)}, c:{evaluate(c)}")
        sign_c = eval_sign(np.float64(c))
        if sign_a * sign_c < 0: #root in a side, set b to be middle (no need sign_b)
            b = c
            # sign_b = sign_c
        else: #root in b side, set a to be middle and set sign_a so no recalculation
            a, sign_a = c, sign_c
    return (a+b)/2 #the final boundary is set, get middle of that

def newton(x: int) -> np.float64:
    pass

def secant(a: int, b: int) -> np.float64:
    pass

def monte_carlo(a: int, b: int) -> np.float64:
    pass

if __name__ == "__main__":
    start = time.time()
    res = bisection(-1,1)
    end = time.time()
    print("Bisection method:")
    print(f"root estimation: {res}")
    print(f"time: {end-start} seconds")
    
    start = time.time()
    res = newton(0)
    end = time.time()
    print("Newton method:")
    print(f"root estimation: {res}")
    print(f"time: {end-start} seconds")
    
    start = time.time()
    res = secant(-1,1)
    end = time.time()
    print("Secant method:")
    print(f"root estimation: {res}")
    print(f"time: {end-start} seconds")
    
    start = time.time()
    res = monte_carlo(0.5,0.75)
    end = time.time()
    print("Monte Carlo Method:")
    print(f"root estimation: {res}")
    print(f"time: {end-start} seconds")
    