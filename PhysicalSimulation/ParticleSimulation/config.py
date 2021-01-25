import math
import pygame
import random

## Pygame configuration
pygame.init()
BGCOLOR = (255,255,255)                                                 # Background color for simulation
DISPLAYWIDTH, DISPLAYHEIGHT = 1280, 720                                 # Resolution of simulation
DISPLAYSURF = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT))    # Creates display surface
FPSCLOCK = pygame.time.Clock()                                          # FPS clock to control game speed
FPS = 120                                                               # Sets to 120FPS
pygame.display.set_caption("Newtonian Particle Simulation")             # Window title

selected_particle = None


## Physical simulation configuration
mass_of_air = 0.1                                                       # Determines amount of drag on the particles
elasticity = 0.75                                                       # Determines loss of speed in bounces and collisions
gravity_switch = True													# Allows switching gravity on and off
gravity_angle = math.pi													# Initialize gravity downwards
gravity_force = 9.8														# Initialize gravity force
gravity = (gravity_angle, gravity_switch*gravity_force/FPS)             # Vector quantity of gravity with (direction, magnitude)
number_of_particles = 500                                               # Number of particles in simulation
min_density = 1
max_density = 20
min_radius = 5
max_radius = 10
