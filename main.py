from vpython import *

m = 1.0 # mass (kg)
R = 1.0 # radius (m)
v_init = 5.0 # initial velocity (m/s)
mu_k = 0.2 # coefficient of kinetic friction
I_factor = 0.5 # moment of inertia factor for a solid disk

running = False
t = 0.0
dt = 0.01
