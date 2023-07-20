1)Initialised variables in the main.py file
integral = 0
prev_error = 0
X=400
x_arr = [0,0] 
and in the Control.py
dt = 0.08

2)added these functions in Control.py
def solve(target, x, theta):
    t=np.linspace(0,dt,2)
    y=odeint(f,x, t, args=(theta,))
    dx = y[1][1] * dt
    return dx, y[1]             //returns the state of the system and dx

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
    else:
        if dtheta >= 1:
         theta = theta_init + 1
        if dtheta <= -1:
            theta = theta_init - 1           

    return theta, integral, error    //returns theta, integral and error

    3)target =- (X-400)/np.cos(theta)
    added target in main.py from X in the game loop taken from mouse click.

    4)theta, integral, prev_error = c.pid(x,target, integral, prev_error, theta)
    dx, x_arr= c.solve(target,x_arr, theta)
    x=x_arr[0]
    used pid fuction from Control.py and solve.py and updated the value of x from the solve function

    5)Ran main.py to open the game window and printed errors and velocity