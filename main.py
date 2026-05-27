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

running = False
t = 0.0
dt = 0.01

scene = canvas(title="Skidding to Rolling Transition", width=800, height=400, center=vector(5,1,0), background=color.white)
scene.camera.pos = vector(5, 1, 15)

ground=box(pos=vector(10,0,0), size=vector(30,0.1,10), color=color.gray(0.5))
object = cylinder(pos=vector(0, R, 0), axis=vector(0, 0, 0.5), radius=R, texture=textures.wood)

#UI callback funcs
def toggle_play(b):
    global running
    running = not running
    # update button text

def reset_sim(b):
    global v, omega, running, t
    running = False
    t = 0.0
    # update button text, reset positions and velocities

def set_mass(s):
    global m
    m = s.value
    #update text

def set_fric(s):
    global mu_k
    mu_k = s.value
    #update text

def set_shape(m_item):
    global I_factor, I
    val = m_item.selected
    # set I_factor based on shape and update I


#UI elements
scene.append_to_caption("\nControls:\n")
button_play = button(text="Play", bind=toggle_play)
button_reset = button(text="Reset", bind=reset_sim)
scene.append_to_caption("\n\n")

menu_shape = menu(choices=['Solid Cylinder', 'Hollow Cylinder', 'Solid Sphere', 'Hollow Sphere'], bind=set_shape)
scene.append_to_caption("\n\n")

slider_mass = slider(min=0.1, max=10.0, value=m, bind=set_mass, length=200)
text_mass = wtext(text=f"Mass: {m:1.1f} kg")
scene.append_to_caption("\n\n")

slider_fric = slider(min=0.01, max=0.8, value=mu_k, bind=set_fric, length=200)
text_fric = wtext(text=f"Kinetic Friction: {mu_k:1.2f}")
scene.append_to_caption("\n\n")





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
        a = F_friction / m
        alpha = tau_friction / I
        v += a * dt
        omega += alpha * dt
        d_theta = omega * dt
        object.rotate(angle=d_theta, axis=vector(0, 0, 1), origin=object.pos)
        object.pos.x += v * dt
        t += dt