import numpy as np
from sympy import symbols, diff, sin, lambdify
import time

def eval_sign(v: np.float64) -> int: 
    return np.sign(np.float64(np.e)**(-v**3) - (v**4) - np.sin(v))

def evaluate(v: np.float64) -> np.float64:
    return np.e**(-v**3) - (v**4) - np.sin(v)

def deriv():
    x = symbols('x')
    f = np.e**(-x**3) - (x**4) - sin(x)
    f_deriv = diff(f, x)
    # print("Derivative", f_deriv)
    # print(type(lambdify(x,f_deriv)))
    return lambdify(x,f_deriv) #turns sympy expressions into lambda functions (anonymous funct)

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
    f_deriv = deriv() #grabs the derivative 
    curr = x
    while True:
        new_x = curr - evaluate(curr)/f_deriv(curr)
        if abs(new_x - curr) <= 0.00005:
            return new_x
        curr = new_x
    return None

def secant(x1: int, x2: int) -> np.float64:
    while True:
        eval_x1, eval_x2 = evaluate(x1), evaluate(x2)
        new_x = x2 - eval_x2/((eval_x2 - eval_x1)/(x2 - x1))
        if abs(new_x - x2) <= 0.00005:
            return new_x
        x1, x2 = x2, new_x
    return None
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
    