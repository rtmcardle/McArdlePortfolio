import pygame

class QuadTree(object):
    def __init__(self, level, rect, particles=[], color = (0,0,0), display_tree=False):
        '''Quadtree box at with a current level, rect, list of particles, and color(if displayed)
        level: set to zero for "trunk" of quadtree
        rect: should be entire display for "trunk" of quadtree
        particles: list of all particles for collision testing'''
        self.maxlevel = 20                              #max number of subdivisions
        self.level = level                              #current level of subdivision
        self.maxparticles = 10                          #max number of particles without subdivision
        self.rect = rect                                #pygame rect object
        self.particles = particles                      #list of particles
        self.color = color                              #color of box if displayed
        self.branches = []                              #empty list that is filled with four branches if subdivided
        self.display_tree = display_tree

    def get_rect(self):
        '''Returns quadtree rect object'''
        return self.rect

    def subdivide(self):
        '''Subdivides quadtree into four branches'''
        for rect in self.rect_quad_split(self.rect):
            branch = QuadTree(self.level+1, rect, [], (self.color[0],self.color[1],self.color[2]+30),display_tree=self.display_tree)
            self.branches.append(branch)

    def rect_quad_split(self, rect):
        '''Splits rect object into four smaller rect objects'''
        w=rect.width/2.0
        h=rect.height/2.0
        rl=[]
        rl.append(pygame.Rect(rect.left, rect.top, w, h))
        rl.append(pygame.Rect(rect.left+w, rect.top, w, h))
        rl.append(pygame.Rect(rect.left, rect.top+h, w, h))
        rl.append(pygame.Rect(rect.left+w, rect.top+h, w, h))
        return rl

    def add_particle(self, particle):
        '''Adds a particle to the list of particles inside quadtree box'''
        self.particles.append(particle)

    def subdivide_particles(self):
        '''Subdivides list of particles in current box to four branch boxes'''
        for particle in self.particles:
            for branch in self.branches:
                if branch.get_rect().colliderect(particle.get_rect()):
                    branch.add_particle(particle)

    def render(self, display):
        '''Displays quadtree box on the display surface given'''
        pygame.draw.rect(display, self.color, self.rect)

    def test_collisions(self):
        '''Tests for collisions between all particles in the particle list'''
        for i, particle in enumerate(self.particles):
            for particle2 in self.particles[i+1:]:
                particle.collide(particle2)

    def update(self, display):
        '''Updates the quadtree and begins recursive process of subdividing or collision testing'''
        if len(self.particles) > self.maxparticles and self.level <= self.maxlevel:
            self.subdivide()
            self.subdivide_particles()
            for branch in self.branches:
                branch.update(display)
        else:
            self.test_collisions()
            if self.display_tree:
                self.render(display)


