import numpy as np
from scipy.integrate import odeint

g = 9.8
dt = 0.08

# The following function gives the ordinary differential
# equation that our plant follows. Do not meddle with this.
def f(x,t ,theta):
    return (x[1], (-5 * g / 7) * np.radians(theta))


# Write your function here.

def solve(target, x, theta):
    t=np.linspace(0,dt,2)
    y=odeint(f,x, t, args=(theta,))
    dx = y[1][1] * dt
    return dx, y[1]

def pid(x, target, integral, prev_error, theta_init):
    error = target-x
    print("err", error)

    integral += error * dt
    i_term = -0* integral

    derivative = (error -prev_error) / dt
    d_term = -15* derivative

    theta = -error * 2 + d_term + i_term
    dtheta = theta - theta_init
 
    
    if abs(theta) > 15:
            if theta > 0:
                theta=15
            else:
                theta = -15 
    # else:
    #     if dtheta >= 1:
    #      theta = theta_init + 1
    #     if dtheta <= -1:
    #         theta = theta_init - 1           

    return theta, integral, error
