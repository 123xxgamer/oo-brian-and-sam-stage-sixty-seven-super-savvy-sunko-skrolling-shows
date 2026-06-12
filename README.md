Web VPython 3.2

#Our project simulates the transition of an axially symmetrical object -- with a user-defined initial velocity relative
#to the floor, and no initial angular speed -- from skidding to rolling.

#Before running the simulation, the user can change the following parameters of the scene:
# - Shape: Hollow/Solid Cylinder, Hollow/Solid Sphere              (0.4; 0.5; 0.67; 1.0)
# - Mass of the Object                                             (0.1  -- 10.0)
# - Coefficient of kinetic friction                                (0.05 -- 0.80)
# - Radius of the Object                                           (0.1  -- 5.00)
# - Initial Velocity of the Object                                 (0.5  -- 15.0)
#Additionally, the user can also zoom in and out of the simulation using the zoom slider, though this can be changed
#while the simulation is running as well.

#**If variables are changed, the simulation needs to be reset to update parameters, even on the first run.

#At the beginning of the simulation, the object is released parallel to the floor with an initial velocity through a 
#non-physical start, and it loses translational kinetic energy as it gets converted to rotational kinetic energy. Two 
#marked points: one, red, on the outer edge of the object and one, green, at the COM of the object, leave trails as 
#they roll. The camera also folows the center of mass of the object as it moves.

#Because there is a non-physical start (the simulation is spawned with the object already having a translation velocity
#and no rotational velocity), and because the ground is always horizontal, there will not be any static friction at any
#point, which is why there is no slider for static friction.

#Once the object begins to roll, the edge marker changes its own color and its trail color to blue, while the COM marker
#changes its color to purple. The simulation pauses 1 second after rolling begins, though the user can choose to continue 
#the simulation.

#At any time during the simulation, the user can pause/unpause/reset (also resetting the parameters of) the simulation,
#or clear the trail of the marker. After the marker trail is cleared, the marker will continue its trail as the object 
#moves, so the trail clear button only removes pervious trails.

#Graphs include Translational/Rotational/Total Energy vs. Time, Linear Momentum vs. Time, Angular Momentum vs. Time,
#COM Velocity/Marker Horizontal Veocity/Marker Speed, Relative to COM vs. Time.
