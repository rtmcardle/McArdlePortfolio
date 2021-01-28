# Particle Simulation

A [Pygame][1] simulation of Newtonian particle collisions in three dimensions. A number of particles (default 500) are created which default to random radii, density, and momentum. The particle class itself is defined within [Particle.py](Particle.py). The simulation uses a [QuadTree](QuadTree.py) in order to handle collision-detection in a reasonable amount of time. Various physical parameters, such as the force of gravity and the mass of the air for drag effects can be manipulated within [config.py](config.py).

## Controls

The simulation initializes without any grvity effects in place. Gravity can be turned on and off by pressing the space bar. While off, the user can increase forces in any direction by pressing the arrow keys. When turned on, the gravity will default to the direction last pressed by the user, or down in the case that no arrow keys have been pressed. The user is able to click and drag a particle from the simulation in order to propell it in a certain direction.

## Known Issues

- When dragging a particle, collisions do not function as well as desired as the velocity of the selected particle is effectively zero. 
- The total momentum of the particles fluctuates, and in the case that radii and density are randomized at initalization, the momentum has a tendency to consistently rise. As such, the particles are set to initalize with a constant radius and density in order to minimize these effects until collisions can be improved upon. 


[1]: https://www.pygame.org/news
