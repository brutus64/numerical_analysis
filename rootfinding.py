import numpy as np
# from sympy import symbols, diff, sin, lambdify
import time
import random

def eval_sign(v: np.float64) -> int: 
    return np.sign(np.float64(np.e)**(-v**3) - (v**4) - np.sin(v))

def evaluate(v: np.float64) -> np.float64:
    return np.e**(-v**3) - (v**4) - np.sin(v)


#ORIGINALLY USED FOR GETTING DERIVATIVE OF A FUNCTION THAT'S NOT HARD CODED
# def deriv():
#     x = symbols('x')
#     f = np.e**(-x**3) - (x**4) - sin(x)
#     f_deriv = diff(f, x)
#     # print("Derivative", f_deriv)
#     # print(type(lambdify(x,f_deriv)))
#     return lambdify(x,f_deriv) #turns sympy expressions into lambda functions (anonymous funct)

#USING THIS FOR HARD-CODED DERIVATIVE FOR SPEED
def deriv_eval(v: np.float64) -> np.float64:
    return -3*(v**2)*np.e**(-v**3) - 4*(v**3) - np.cos(v)

def bisection(a: int,b: int) -> np.float64:
    a, b = np.float64(a), np.float64(b)
    sign_a = eval_sign(a)
    cnt = 0
    while abs(b-a) > 0.0001: #need to be accurate within 0.00005, 0.0001 is enough if we use intervals as midpoint would guarantee root is only < 0.00005 away
        c = (a+b)/2
        sign_c = eval_sign(np.float64(c))
        if sign_a * sign_c < 0: #root in a side, set b to be middle (no need sign_b)
            b = c
        else: #root in b side, set a to be middle and set sign_a so no recalculation
            a, sign_a = c, sign_c
        cnt += 1
    return (a+b)/2, cnt  #the final boundary is set, get middle of that
  
def newton(x: int) -> np.float64:
    # f_deriv = deriv() #grabs the derivative 
    curr = x
    cnt = 0
    while True:
        new_x = curr - evaluate(curr)/deriv_eval(curr)
        cnt += 1
        if abs(new_x - curr) < 0.00005: #Exit the loop the moment we're only changing by 0.00005 for x values
            return new_x, cnt
        curr = new_x

def secant(x1: int, x2: int) -> np.float64:
    cnt = 0
    while True:
        eval_x1, eval_x2 = evaluate(x1), evaluate(x2)
        new_x = x2 - eval_x2/((eval_x2 - eval_x1)/(x2 - x1))
        cnt += 1
        if abs(new_x - x2) < 0.00005: #Exit the loop the moment we're only changing by 0.00005 for x values
            return new_x, cnt
        x1, x2 = x2, new_x

def monte_carlo(a: int, b: int) -> np.float64:
    cnt = 0
    while True:
        point = random.random()*(b-a) + a
        eval_pt = evaluate(point) #Prof Deng mentioned that we are to use this
        cnt += 1
        if abs(eval_pt) < 0.00005: 
            return point, cnt

if __name__ == "__main__":
    res = bisection(-1,1)
    print("Bisection method:")
    print(f"root estimation: {res[0]}")
    print(f"number of iter: {res[1]}")
    
    res = newton(0)
    print("Newton method:")
    print(f"root estimation: {res[0]}")
    print(f"number of iter: {res[1]}")
    
    res = secant(-1,1)
    print("Secant method:")
    print(f"root estimation: {res[0]}")
    print(f"number of iter: {res[1]}")
    
    res = monte_carlo(0.5,0.75)
    print("Monte Carlo Method:")
    print(f"root estimation: {res[0]}")
    print(f"number of iter: {res[1]}")
    