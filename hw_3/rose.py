import numpy as np
import random

def eval_rose(theta):
    r = np.sin(2 * theta)
    return r * np.cos(theta), r * np.sin(theta)

def monte_sample_rect_area(x, y, alpha):
    w = 1
    h = 1/np.sqrt(2)
    theta = np.radians(alpha)
    cos_theta, sin_theta = np.cos(theta), np.sin(theta)
    
    num_inside = 0
    for _ in range(10000):
        loc_x, loc_y = random.uniform(-w/2, w/2), random.uniform(-h/2, h/2)
        new_x, new_y = x + (cos_theta * loc_x - sin_theta * loc_y), y + (sin_theta * loc_x + cos_theta * loc_y)
        
        if is_in_rose(new_x, new_y):
            num_inside += 1
    
    return (num_inside / 10000) * w * h
    

def is_in_rose(x,y):
    return (x**2 + y**2)**3 <= 4* x**2 * y**2

def rose():
    x, y, alpha = random.uniform(-1,1), random.uniform(-1,1), random.uniform(0,180)
    curr_best = monte_sample_rect_area(x, y, alpha)
    
    for i in range(20000):
        x_mod, y_mod, a_mod = x + random.uniform(-0.1,0.1), y + random.uniform(-0.1,0.1), (alpha + random.uniform(-0.1,0.1)) % 180 #symmetry exists, only need to do up to 180
        new_area = monte_sample_rect_area(x_mod, y_mod, a_mod)
        if new_area > curr_best:
            print(f"NEW BEST AREA: {new_area} at ITERATION: {i}")
            x, y, alpha = x_mod, y_mod, a_mod
            curr_best = new_area
        else:
            print("area:", new_area)
        
    print("Best values:")
    print(f"x: {x}\ny: {y}\nalpha: {alpha}\narea: {curr_best}")
    
if __name__ == "__main__":
    rose()