from vpython import *

m = 1.0 # mass (kg)
R = 1.0 # radius (m)
v_init = 5.0 # initial velocity (m/s)
mu_k = 0.05 # coefficient of kinetic friction
I_factor = 0.5 # moment of inertia factor for a solid disk
I = I_factor * m * R**2 # moment of inertia (kg*m^2)

g = 9.81 # acceleration due to gravity (m/s^2)

v = v_init
omega = 0.0 # initial angular velocity (rad/s)

running = True
t = 0.0
dt = 0.01

scene = canvas(title="Skidding to Rolling Transition", width=800, height=400, center=vector(5,1,0), background=color.white)
scene.camera.pos = vector(5, 1, 15)

ground=box(pos=vector(10,0,0), size=vector(30,0.1,10), color=color.gray(0.5))
object = cylinder(pos=vector(0, R, 0), axis=vector(0, 0, 0.5), radius=R, texture=textures.wood)

while True:
    rate(100)
    
    if running:
        if v > -omega * R:
            # Skidding phase
            F_friction = -mu_k * m * g
            tau_friction = F_friction * R
        else:
            # Rolling phase
            F_friction = 0
            tau_friction = 0
        a = F_friction * / m
        alpha = tau_friction / I
        v += a * dt
        omega += alpha * dt
        d_theta = omega * dt
        object.rotate(angle=d_theta, axis=vector(0, 0, 1), origin=object.pos)
        object.pos.x += v * dt
        t += dt