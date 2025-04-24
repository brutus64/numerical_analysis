import numpy as np
import matplotlib.pyplot as plt
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
    x, y, xf = x0, y0, 0
    h = -0.0001 #our step size backwards
    stored_x, stored_y = [x0], [y0]
    stored_slopes = []
    while x >= xf:
        slope = dydx(x,y, k)
        stored_slopes.append(slope)
        print(f"(x,y):({x:.4f},{y:.4f}), slope:{slope:.4f} -> new: (x,y): ({x+h:.4f},{y+h*slope:.4f})")
        x += h
        stored_x.append(x)
        y += h * slope
        stored_y.append(y)
    print(f"Final (x,y): ({x:.4f},{y})")
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

    # First plot: trajectory
    ax1.plot(stored_x, stored_y, 'o-', color="blue", linewidth=1)
    ax1.set_title("Trajectory of Object")
    ax1.set_xlabel("x position")
    ax1.set_ylabel("y position")
    ax1.grid(True)

    # Second plot: slope vs x
    ax2.plot(stored_x[:-1], stored_slopes, color="red", linewidth=1)
    ax2.set_title("Slope (dy/dx) vs. x")
    ax2.set_xlabel("x position")
    ax2.set_ylabel("Slope (dy/dx)")
    ax2.grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    euler_method()