import numpy as np
# from sympy import symbols, diff, sin, lambdify
import random

def evaluate(v: float) -> float:
    return np.e**(-v**3) - (v**4) - np.sin(v)
    #7 flops, 3 powers = 3 flops, 1 sin = 1 flop, 2 subtractions = 2 flops, 1 negative multiplcation = 1 flop


#ORIGINALLY USED FOR GETTING DERIVATIVE OF A FUNCTION THAT'S NOT HARD CODED
# def deriv():
#     x = symbols('x')
#     f = np.e**(-x**3) - (x**4) - sin(x)
#     f_deriv = diff(f, x)
#     # print("Derivative", f_deriv)
#     # print(type(lambdify(x,f_deriv)))
#     return lambdify(x,f_deriv) #turns sympy expressions into lambda functions (anonymous funct)

#USING THIS FOR HARD-CODED DERIVATIVE FOR SPEED
def deriv_eval(v: float) -> float:
    return -3*(v**2)*np.e**(-v**3) - 4*(v**3) - np.cos(v)
    #11 flops, -3*(v**2) 2 flops, e^(-v^3) 3 flops, multiply 1 flop, -4*v^3: 2 flops cos(v): 1 flop 2 subtractions: 2 flops

def bisection(a: float, b: float) -> float:
    a, b = float(a), float(b)
    sign_a = evaluate(a)
    cnt, flops = 0, 7 #evaluating the function takes 7 flops
    while abs(b-a) > 0.0001: #need to be accurate within 0.00005, 0.0001 is enough if we use intervals as midpoint would guarantee root is only < 0.00005 away
        # print(f" a:{a}, b:{b}")
        c = (a+b)/2
        flops += 2
        sign_c = evaluate(c)
        flops += 7
        # print(f"c: {c}, c_value: {sign_c}")
        if sign_a * sign_c < 0: #root in left side, set b to be middle (no need sign_b)
            b = c
        else: #root in right side, set a to be middle and set value from previous so no recalculation
            a, sign_a = c, sign_c
        flops += 1
        cnt += 1
    # print(f"Ending a:{a} b:{b}, returning: {a+b/2}")
    return (a+b)/2, cnt, flops  #the final boundary is set, get middle of that
  
def newton(x: int) -> float:
    # f_deriv = deriv() #grabs the derivative 
    curr = x
    cnt, flops = 0, 0
    while True:
        new_x = curr - evaluate(curr)/deriv_eval(curr)
        flops += 18
        cnt += 1
        if abs(new_x - curr) < 0.00005: #Exit the loop the moment we're only changing by 0.00005 for x values
            flops += 1
            return new_x, cnt, flops
        flops += 1
        curr = new_x

def secant(x1: int, x2: int) -> float:
    cnt, flops = 0, 0
    while True:
        eval_x1, eval_x2 = evaluate(x1), evaluate(x2)
        flops += 14
        new_x = x2 - eval_x2/((eval_x2 - eval_x1)/(x2 - x1))
        flops += 5
        cnt += 1
        if abs(new_x - x2) < 0.00005: #Exit the loop the moment we're only changing by 0.00005 for x values
            flops += 1
            return new_x, cnt, flops
        flops += 1
        x1, x2 = x2, new_x

def monte_carlo(a: int, b: int) -> float:
    cnt, flops = 0, 0
    while True:
        point = random.uniform(a,b) #get a uniformly random number between [a,b], Prof Deng said to just use a randomizer for this
        eval_pt = evaluate(point)
        flops += 7
        cnt += 1
        if abs(eval_pt) < 0.00005: 
            flops += 1
            return point, cnt, flops
        flops += 1

if __name__ == "__main__":
    res = bisection(-1,1)
    print("Bisection method:")
    print(f"root estimation: {res[0]}")
    print(f"number of iter: {res[1]}")
    print(f"number of flops: {res[2]}")

    
    res = newton(0)
    print("Newton method:")
    print(f"root estimation: {res[0]}")
    print(f"number of iter: {res[1]}")
    print(f"number of flops: {res[2]}")

    res = secant(-1,1)
    print("Secant method:")
    print(f"root estimation: {res[0]}")
    print(f"number of iter: {res[1]}")
    print(f"number of flops: {res[2]}")

    res = monte_carlo(0.5,0.75)
    print("Monte Carlo Method:")
    print(f"root estimation: {res[0]}")
    print(f"number of iter: {res[1]}")
    print(f"number of flops: {res[2]}")

    