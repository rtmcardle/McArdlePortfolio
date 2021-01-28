import pygame, random, math, sys
import config, util
from Particle import Particle
from QuadTree import QuadTree
import numpy as np


def main():
    particles = [Particle(radius=10,density=10) for _ in range(config.number_of_particles)]  

    ## Game Loop
    while True:                                                                                         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ## While mouse button pressed, select clicked particle
                (mouseX, mouseY) = pygame.mouse.get_pos()
                config.selected_particle = util.findParticle(particles, mouseX, mouseY)
            elif event.type == pygame.MOUSEBUTTONUP:
                ## De-select particle on mouse up
                config.selected_particle = None
            elif event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()   
                ## Switches gravity on/off
                if key[pygame.K_SPACE] != 0:
                    config.gravity_switch = not config.gravity_switch
                    if config.gravity_switch:
                        config.gravity = (config.gravity_angle, config.gravity_switch*config.gravity_force/config.FPS)
                    else:
                        config.gravity = (0,0)
                else:
                    ## Changes direction of gravity with arrow key press
                    ## If gravity_switch == False, applies a force
                    if key[pygame.K_UP] != 0:
                        #config.gravity = (math.pi, -9.8/config.FPS)
                        config.gravity_angle = 0
                    elif key[pygame.K_DOWN] != 0:
                        config.gravity_angle = math.pi
                    elif key[pygame.K_RIGHT] != 0:
                        config.gravity_angle = math.pi/2
                    elif key[pygame.K_LEFT] != 0:
                        config.gravity_angle = 3*math.pi/2
                    ## If gravity is not on, increment the force in the direction
                    if not config.gravity_switch:
                        config.gravity = util.addVectors(config.gravity[0], config.gravity[1], config.gravity_angle, config.gravity_delta)
                        if config.gravity[1] >= config.gravity_force/config.FPS: config.gravity = util.maxVector(config.gravity,config.gravity_force/config.FPS)
                        print(config.gravity)
                    ## If gravity is on, set the direction of gravity
                    else:
                        config.gravity = (config.gravity_angle, config.gravity_switch*config.gravity_force/config.FPS)

            

        if config.selected_particle:                                                           
            ## If particle selected, drag with mouse
            mouseX, mouseY = pygame.mouse.get_pos()
            dx = mouseX - config.selected_particle.x
            dy = mouseY - config.selected_particle.y
            config.selected_particle.angle = 0.5*math.pi + math.atan2(dy, dx)
            config.selected_particle.speed = math.hypot(dx, dy) * 0.5

        ## Draws the background
        config.DISPLAYSURF.fill(config.BGCOLOR)

        ## Creates and the QuadTree for fast collision checks
        tree = QuadTree(0, pygame.Rect(0,0,config.DISPLAYWIDTH,config.DISPLAYHEIGHT), particles=particles)
        tree.update(config.DISPLAYSURF)

        ## Updates and draws particles
        for particle in particles: 
            particle.update()
        
        ## Update display
        config.FPSCLOCK.tick(config.FPS)
        pygame.display.update()


if __name__=='__main__':
    main()