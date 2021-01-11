import pygame, math, random
import config
import util



class Particle():
    def __init__(self, x = None, y = None, radius = None, density = None):
        '''A particle at coordinates (x,y) represented by a circle with mass'''
        self.radius = random.randint(config.min_radius, config.max_radius) if radius==None else radius
        self.density = random.randint(config.min_density, config.max_density) if density==None else density
        self.x = random.randint(self.radius, config.DISPLAYWIDTH-self.radius) if x==None else x
        self.y = random.randint(self.radius, config.DISPLAYHEIGHT-self.radius) if y==None else y
        self.mass = self.density * math.pi * self.radius**2
        self.color = (100+155*(1-self.density/config.max_density), 0, 0)
        self.thickness = 0
        self.speed = random.random()#magnitude of velocity vector
        self.angle = random.uniform(0, math.pi*2)#direction of velocity vector
        
        self.drag = (self.mass/(self.mass + config.mass_of_air)) ** self.radius
        self.set_rect()#sets particle rect for collision testing with quadtree boxes

    def get_rect(self):
        '''Returns particle rect object'''
        return self.rect

    def set_rect(self):
        '''Sets particle rect object at current coordinates with side length 2*radius'''
        self.rect = pygame.Rect(int(self.x-self.radius), int(self.y-self.radius), int(self.radius*2), int(self.radius*2))

    def display(self):
        '''Draws particle onto DISPLAYSURF'''
        pygame.draw.circle(config.DISPLAYSURF, self.color, (int(self.x), int(self.y)), self.radius, self.thickness)

    def move(self):
        '''Adds gravity and particle movement vectors and then moves particle'''
        (self.angle, self.speed) = util.addVectors(self.angle, self.speed, config.gravity[0],config.gravity[1])
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        self.speed *= self.drag

    def bounce(self):
        '''Tests for wall collisions and changes particle velocity accordingly'''
        if self.x > config.DISPLAYWIDTH - self.radius:
            self.x = 2*(config.DISPLAYWIDTH - self.radius) - self.x
            self.angle = - self.angle
            self.speed *= config.elasticity

        elif self.x < self.radius:
            self.x = 2*self.radius - self.x
            self.angle = - self.angle
            self.speed *= config.elasticity

        if self.y > config.DISPLAYHEIGHT - self.radius:
            self.y = 2*(config.DISPLAYHEIGHT - self.radius) - self.y
            self.angle = math.pi - self.angle
            self.speed *= config.elasticity

        elif self.y < self.radius:
            self.y = 2*self.radius - self.y
            self.angle = math.pi - self.angle
            self.speed *= config.elasticity

    def collide(self, p2):
        '''Tests if two particles collide and changes their speed and direction'''
        dx = self.x - p2.x
        dy = self.y - p2.y

        dist = math.hypot(dx, dy)
        if dist < self.radius + p2.radius:
            angle = math.atan2(dy, dx) + 0.5 * math.pi
            total_mass = self.mass + p2.mass
            (self.angle, self.speed) = util.addVectors(self.angle, self.speed*(self.mass-p2.mass)/total_mass, angle, 2*p2.speed*p2.mass/total_mass)
            (p2.angle, p2.speed) = util.addVectors(p2.angle, p2.speed*(p2.mass-self.mass)/total_mass, angle+math.pi, 2*self.speed*self.mass/total_mass)
            self.speed *= config.elasticity
            p2.speed *= config.elasticity

            overlap = 0.5*(self.radius + p2.radius - dist+1)
            self.x += math.sin(angle)*overlap
            self.y -= math.cos(angle)*overlap
            p2.x -= math.sin(angle)*overlap
            p2.y += math.cos(angle)*overlap

    def update(self):
        self.move()
        self.bounce()
        self.set_rect()
        self.display()