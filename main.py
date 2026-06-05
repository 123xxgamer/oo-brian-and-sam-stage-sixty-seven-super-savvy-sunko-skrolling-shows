from vpython import *

m_new = 1.0 # initial mass (kg)
m = m_new # mass (kg)
R_new = 1.0 # initial radius (m)
R = R_new # radius (m)
v_init = 5.0 # initial velocity (m/s)
mu_k_new = 0.05 # initial coefficient of kinetic friction
mu_k = mu_k_new # coefficient of kinetic friction
new_I_factor = 0.5 # initial moment of inertia factor for a solid disk
I_factor = 0.5 # moment of inertia factor for a solid disk
I = I_factor * m * R**2 # moment of inertia (kg*m^2)

t_roll = 9999

g = 9.81 # acceleration due to gravity (m/s^2)

v = v_init
omega = 0.0 # initial angular velocity (rad/s)
theta = 0.0 

trans_ke = 0.5 * m * v**2
rot_ke = 0.5 * I * omega**2

running = False
t = 0.0
dt = 0.01

scene = canvas(title="Skidding to Rolling Transition", width=800, height=400, center=vector(5,1,0), background=color.white, align='left')
scene.camera.pos = vector(0, 1, 8)
scene.userspin = False
scene.userzoom = False
scene.userpan = False

length = 105
segment_size = 3 # Matches the texture's aspect ratio
total_segments = int(length / segment_size)

# Create multiple non-stretched boxes next to each other
for i in range(total_segments):
    box(pos=vector(i * segment_size - 15 + (segment_size/2), -segment_size/2, 0),
        size=vector(segment_size, segment_size, segment_size),
        texture=textures.rug)
    
roll_obj = cylinder(pos=vector(0, R, 0), axis=vector(0, 0, 0.5), radius=R, texture=textures.wood)
marker = sphere(pos=roll_obj.pos + vector(0, -R, 0.5), radius=0.1, color=color.red, make_trail = True)

marker_offset = marker.pos - roll_obj.pos

#UI callback funcs
def toggle_play(b):
    global running
    running = not running
    if running:
        marker.make_trail = True
        b.text = "Pause"
    else:
        b.text = "Play"

def reset_sim(b):
    global v, omega, running, t, R, m, mu_k, roll_obj, total_energy, translational_ke, rotational_ke, lin_momentum, ang_momentum, I, R_new, m_new, mu_k_new, v_init, I_factor, scene, marker, marker_offset, new_I_factor, t_roll, trans_ke, rot_ke, theta
    running = False
    button_play.text = "Play"
    alert_label.visible = False
    t = 0.0
    t_roll = 9999
    v = v_init
    R=R_new
    m = m_new
    mu_k = mu_k_new
    omega = 0.0
    theta = 0.0
    marker.make_trail = False
    I_factor = new_I_factor
    scene.camera.pos = vector(0, 1, 8)
    total_energy.data = []
    translational_ke.data = []
    rotational_ke.data = []
    lin_momentum.data = []
    ang_momentum.data = []
    
    roll_obj.visible = False
    if menu_shape.selected == 'Solid Cylinder':
        roll_obj = cylinder(pos=vector(0, R, -0.5), axis=vector(0, 0, 0.5), radius=R, texture=textures.wood)
    elif menu_shape.selected == 'Hollow Cylinder':
        roll_obj = ring(pos=vector(0, R, -0.5), axis=vector(0, 0, 0.5), radius=R, thickness=R*0.2, texture=textures.wood)
    elif menu_shape.selected == 'Solid Sphere':
        roll_obj = sphere(pos=vector(0, R, -0.5), radius=R, texture=textures.earth)
    elif menu_shape.selected == 'Hollow Sphere':
        roll_obj = sphere(pos=vector(0, R, -0.5), radius=R, texture=textures.stucco, shininess=0.1)
    else:
        roll_obj = cylinder(pos=vector(0, R, -0.5), axis=vector(0, 0, 0.5), radius=R, texture=textures.wood)
    roll_obj.visible = True
    roll_obj.radius = R
    roll_obj.pos = vector(0, R, 0)
    marker.pos = roll_obj.pos + vector(0, -R, 0.5)
    #marker.make_trail = True
    marker.color = color.red
    marker.trail_color = color.red
    marker_offset = marker.pos - roll_obj.pos
    roll_obj.axis = vector(0, 0, 0.5)
    button_play.text = "Play"
    I = I_factor * m * R**2
    trans_ke = 0.5 * m * v**2
    rot_ke = 0.5 * I * omega**2
    

def set_mass(s):
    global m_new
    m_new = s.value
    text_mass.text = f"Mass: {m_new:1.1f} kg"

def set_fric(s):
    global mu_k_new
    mu_k_new = s.value
    text_fric.text = f"Kinetic Friction: {mu_k_new:1.2f}"

def set_shape(m_item):
    global I_factor, I, new_I_factor
    val = m_item.selected
    if val == 'Solid Cylinder':
        new_I_factor = 0.5
    elif val == 'Hollow Cylinder':
        new_I_factor = 1.0
    elif val == 'Solid Sphere':
        new_I_factor = 0.4
    elif val == 'Hollow Sphere':
        new_I_factor = 0.67
def set_radius(s):
    global R_new
    R_new = s.value
    text_radius.text = f"Radius: {R_new:1.1f} m"

def set_init_vel(s):
    global v_init, v
    v_init = s.value
    text_init_vel.text = f"Initial Velocity: {v_init:1.1f} m/s"

def delete_trail(b):
    marker.make_trail = False
    marker.clear_trail()


#UI elements
scene.append_to_caption("\nControls:\n")
button_play = button(text="Play", bind=toggle_play)
button_reset = button(text="Reset with new parameters", bind=reset_sim)
button_delete_trail = button(text="Delete Trail(s)", bind=delete_trail)
scene.append_to_caption("\n\n")


menu_shape = menu(choices=['Solid Cylinder', 'Hollow Cylinder', 'Solid Sphere', 'Hollow Sphere'], bind=set_shape)
scene.append_to_caption("\n\n")

slider_mass = slider(min=0.1, max=10.0, value=m_new, bind=set_mass, length=200)
text_mass = wtext(text=f"Mass: {m_new:1.1f} kg")
scene.append_to_caption("\n\n")

slider_fric = slider(min=0.01, max=0.8, value=mu_k_new, bind=set_fric, length=200)
text_fric = wtext(text=f"Kinetic Friction: {mu_k_new:1.2f}")
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


alert_label = label(pos=vector(0, 5, 0), text="Simulation paused 1s after rolling began.", visible=False, box=True)

while True:
    rate(100)
    
    if running:
        if v > -omega * R:
            # Skidding phase
            F_friction = -mu_k * m * g
            tau_friction = F_friction * R
        else:
            # Rolling phase
            if t_roll == 9999:
                t_roll = t
            F_friction = 0
            tau_friction = 0
        if t >= t_roll and t < t_roll + dt:
            marker.color=color.blue
            marker.trail_color=color.blue
        if t >= t_roll + 1 and t < t_roll + 1 + dt:
            running=False
            button_play.text="Play"
            alert_label.pos = vector(roll_obj.pos.x, 5, 0)
            alert_label.visible=True
        else:
            alert_label.visible=False
        a = F_friction / m
        alpha = tau_friction / I
        v += a * dt
        omega += alpha * dt
        d_theta = omega * dt
        theta += d_theta
        roll_obj.rotate(angle=d_theta, axis=vector(0, 0, 1), origin=roll_obj.pos)
        roll_obj.pos.x += v * dt
        marker.pos = roll_obj.pos + marker_offset.rotate(angle=theta, axis=roll_obj.axis)

        trans_ke = 0.5 * m * v**2
        rot_ke = 0.5 * I * omega**2

        total_energy.plot(t, trans_ke + rot_ke)
        translational_ke.plot(t, trans_ke)
        rotational_ke.plot(t, rot_ke)

        lin_momentum.plot(t, m * v)
        ang_momentum.plot(t, -I * omega)
        scene.camera.pos = vector(roll_obj.pos.x, 1, 8)
        t += dt