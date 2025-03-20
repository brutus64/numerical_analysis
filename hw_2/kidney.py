from sympy import *
import numpy as np
'''
USING CARTESIAN IS HARD
turning kidney into polar:
(x^2+y^2)^2 = x^3+y^3
(r^2cos^2 + r^2sin^2)^2 = r^3cos^3 + r^3sin^3
(r^2(cos^2+sin^2))^2 = r^3(cos^3+sin^3)      #cos^2+sin^2 = 1
(r^2)^2 = r^3(cos^3+sin^3)
r^4 = r^3(cos^3+sin^3)
r = cos^3+sin^3
integrate from -pi to 3pi/4 with r^2 dtheta * 0.5
this is because it only intersects with y=-x so it never goes past 45 degrees or pi/4

Turning disc into polar:
disc (area is same as if its in origin, it's easier to turn it into centered at origin)
x^2+y^2 = 0.125
r^2cos^2 + r^2sin^2 = 0.125
r^2 = 0.125
r = sqrt(0.125)
'''

def eval_kidney(v):
    r = np.cos(v)**3 + np.sin(v)**3
    return 0.5 * r**2 #integral is basically 0.5 * r^2

def eval_disc(v):
    return 0.5 * 0.125 #0.5 * r^2, r^2 = 0.125

def rect_points(start, end, num_pts):
    pts = np.linspace(start, end, num_pts+1) #idea is to have a bunch of x1,x2...x_n+1 then take midpoint of every 2
    ret = []
    i, j = 0, 1
    while j < len(pts): #stop when 2nd pointer hits end of list
        ret.append((pts[i] + pts[j])/2) #midpoint of 2 points
        i, j = i+1, j+1
    return ret, (end-start)/num_pts

def trape_points(start, end, num_pts):
    return np.linspace(start,end, num_pts+1), (end-start)/num_pts

def rect(n): #midpoint method
    #evaluate kidney at proper equation and limits of integration (adjust interval # as needed)
    arr1, step_size1 = rect_points(-np.pi/4,3*np.pi/4, n)
    arr2, step_size2 = rect_points(0,2*np.pi, n)
    # print(arr, x)
    total = 0
    total2 = 0
    for pt in arr1: #get the evaluation and multiply by step size
        total += step_size1 * eval_kidney(pt)
    for pt in arr2:
        total2 += step_size2 *eval_disc(pt)
    print("Rectangle method:")
    print(f"Kidney area: {total}, Disc area: {total2}")
    print(f"Total area: {total-total2}")
    #evaluate disc at proper equation and limits of integration (adjust interval # as needed)
    

def trapezoidal(n):
    arr1, step_size1 = trape_points(-np.pi/4,3*np.pi/4, n)
    arr2, step_size2 = trape_points(0,2*np.pi, n)
    i, j = 0, 1
    total = 0
    total2 = 0
    while j < len(arr1): #get the evaluation and multiply by step size
        total += step_size1 * (eval_kidney(arr1[i]) + eval_kidney(arr1[j]))/2
        total2 += step_size2 * (eval_disc(arr2[i]) + eval_disc(arr2[j]))/2
        i,j = i+1, j+1
    print("Trapezoid method:")
    print(f"Kidney area: {total}, Disc area: {total2}")
    print(f"Total area: {total-total2}")

if __name__ == '__main__':
    print("Both strategies use 100 points")
    rect(100)
    trapezoidal(100)
    