import math

def addVectors(angle1, length1, angle2, length2):
    '''
    Adds two vectors of (direction, magnitude) and returns vector.
    '''
    x  = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y  = math.cos(angle1) * length1 + math.cos(angle2) * length2

    angle = 0.5 * math.pi - math.atan2(y, x)
    length  = math.hypot(x, y)

    return (angle, length)



def findParticle(particles, x, y):
    '''
    Checks if x and y coordinates are inside of a known particle.
    '''
    for p in particles:
        if math.hypot(p.x-x, p.y-y) <= p.radius:
            return p
    return None