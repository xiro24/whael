from pyglet.gl import *
from whael.Entities.Entity import Entity
import math
import random


class CreateEntity:

    def Particle(self, width, height,amt):
        pt =[]
        for n in range(amt):
            self.size = random.randint(2,10)
            x = random.randint(self.size,width - self.size)
            y = random.randint(self.size, height - self.size)
            x= 400
            y= 200
            part = Entity(x, y,self.size)
            part.speed = random.random()
            part.angle = random.uniform(0,math.pi*2)
            pt.append(part)
        return pt