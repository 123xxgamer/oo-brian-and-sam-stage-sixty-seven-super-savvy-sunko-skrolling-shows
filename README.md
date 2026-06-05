# oo-brian-and-sam-stage-sixty-seven-super-savvy-sunko-skrolling-shows
oo! brian and sam stage sixty-seven super savvy sunko skrolling shows

#Our project simulates the transition of an axially symmetrical object -- with a user-defined initial velocity relative
#to the floor, and no initial angular speed -- from skidding to rolling.

#Before running the simulation, the user can change the following parameters of the scene:
# - Shape, or Custom Moment of Inertia (As a coefficient to MR^2)  (???  -- 1.00)
# - Mass of the Object                                             (0.1  -- 10.0)
# - Coefficient of kinetic friction                                (0.05 -- 0.80)
# - Radius of the Object                                           (0.1  -- 5.00)
# - Initial Velocity of the Object                                 (0.5  -- 20.0)
#Additionally, the user can also zoom in and out of the simulation using the zoom slider, though this can be changed
#while the simulation is running as well.

#At the beginning of the simulation, the object is shot parallel to the floor with an initial velocity, and it loses 
#translational kinetic energy as it gets converted to rotational kinetic energy. A marked point on the outer edge of
#the object leaves a trail as it rolls. The camera also folows the center of mass of the object as it moves.

#Once the object begins to roll, the marker changes its own color and its trail color to blue. The simulaton pauses
#1 second after rolling begins, though the user can choose to continue the simulation.

#At any time during the simulation, the user can pause, reset (also resetting the parameters), or clear the trail of
#the marker. After the marker trail is cleared, the marker will continue its trail as the object moves, so the trail
#clear button only removes pervious trails.

#Graphs include Translational/Rotational/Total Energy vs. Time, Linear Momentum vs. Time, Angular Momentum vs. Time.
