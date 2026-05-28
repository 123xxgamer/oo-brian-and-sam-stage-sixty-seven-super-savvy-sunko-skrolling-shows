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

trans_ke = 0.5 * m * v**2
rot_ke = 0.5 * I * omega**2

running = False
t = 0.0
dt = 0.01

scene = canvas(title="Skidding to Rolling Transition", width=800, height=400, center=vector(5,1,0), background=color.white)
scene.camera.pos = vector(5, 1, 15)
scene.userspin = False
scene.userzoom = False
scene.userpan = False

ground=box(pos=vector(10,0,0), size=vector(30,0.1,10), color=color.gray(0.5))
object = cylinder(pos=vector(0, R, 0), axis=vector(0, 0, 0.5), radius=R, texture=textures.wood)

#UI callback funcs
def toggle_play(b):
    global running
    running = not running
    if running:
        b.text = "Pause"
    else:
        b.text = "Play"

def reset_sim(b):
    global v, omega, running, t
    running = False
    v = v_init
    omega = 0.0
    object.pos = vector(0, R, 0)
    object.axis = vector(0, 0, 0.5)
    b.text = "Play"
    I = I_factor * m * R**2
    trans_ke = 0.5 * m * v**2
    rot_ke = 0.5 * I * omega**2
    t = 0.0
    

def set_mass(s):
    global m
    m = s.value
    s.text = f"Mass: {m:1.1f} kg"

def set_fric(s):
    global mu_k
    mu_k = s.value
    s.text = f"Kinetic Friction: {mu_k:1.2f}"

def set_shape(m_item):
    global I_factor, I
    val = m_item.selected
    if val == 'Solid Cylinder':
        I_factor = 0.5
    elif val == 'Hollow Cylinder':
        I_factor = 1.0
    elif val == 'Solid Sphere':
        I_factor = 0.4
    elif val == 'Hollow Sphere':
        I_factor = 0.67

def set_radius(s):
    global R, I
    R = s.value
    I = I_factor * m * R**2
    s.text = f"Radius: {R:1.1f} m"

def set_init_vel(s):
    global v_init, v
    v_init = s.value
    s.text = f"Initial Velocity: {v_init:1.1f} m/s"


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

slider_radius = slider(min=0.1, max=5.0, value=R, bind=set_radius, length=200)
text_radius = wtext(text=f"Radius: {R:1.1f} m")
scene.append_to_caption("\n\n")

slider_init_vel = slider(min=0.5, max=20.0, value=v_init, bind=set_init_vel, length=200)
text_init_vel = wtext(text=f"Initial Velocity: {v_init:1.1f} m/s")
scene.append_to_caption("\n\n")

g_energy = graph(title="Energy vs Time", align="left", xtitle="Time (s)", ytitle="Energy (J)", width=800, height=250)
total_energy = gcurve(graph=g_energy, color=color.blue, label="Total Energy")
translational_ke = gcurve(graph=g_energy, color=color.red, label="Translational Kinetic Energy")
rotational_ke = gcurve(graph=g_energy, color=color.green, label="Rotational Kinetic Energy")

g_lin_momentum = graph(title="Momentum vs Time", align="left", xtitle="Time (s)", ytitle="Momentum (kg*m/s)", width=800, height=250)
lin_momentum = gcurve(graph=g_lin_momentum, color=color.orange, label="Linear Momentum")

g_ang_momentum = graph(title="Angular Momentum vs Time", align="left", xtitle="Time (s)", ytitle="Angular Momentum (kg*m^2/s)", width=800, height=250)
ang_momentum = gcurve(graph=g_ang_momentum, color=color.purple, label="Angular Momentum")


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

        trans_ke = 0.5 * m * v**2
        rot_ke = 0.5 * I * omega**2

        total_energy.plot(t, trans_ke + rot_ke)
        translational_ke.plot(t, trans_ke)
        rotational_ke.plot(t, rot_ke)

        lin_momentum.plot(t, m * v)
        ang_momentum.plot(t, -I * omega)

        t += dt