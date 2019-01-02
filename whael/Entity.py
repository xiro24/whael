from pyglet.gl import *
import math
from grid import Grid
import random


class Entity:
    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.colour = (0, 0, 255)
        self.thickness = 1
        self.size = size
        self.speed = 0.01
        self.angle = 0
        self.elasticity = 0.75

    def DrawCircle(self,numPoints):
        verts = []
        for i in range(numPoints):
            angle = math.radians(float(i) / numPoints * 360.0)
            x = self.size * math.cos(angle) + self.x
            y = self.size * math.sin(angle) + self.y
            verts += [x, y]
        self.circle = pyglet.graphics.vertex_list(numPoints, ('v2f', verts))
        self.draw()

    def draw(self):
        glColor3f(255, 255, 255)
        self.circle.draw(GL_LINE_LOOP)

    def Move(self):
        #gravity = (math.pi, 0.002)
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

        # particle.speed = random.random()
        # particle.angle = random.un

    def Display(self,width,height,ptarr):
        for i, mpt in enumerate(ptarr):
            mpt.Move()
            mpt.bounce(width,height)
            for mpt2 in ptarr[i+1:]:
                self.collide(mpt,mpt2)
            mpt.DrawCircle(20)

    def collide(self,p1,p2):
        dx = p1.x - p2.x
        dy = p1.y - p2.y

        distance = math.hypot(dx,dy)
        if distance < p1.size + p2.size:
            tangent = math.atan2(dy,dx)
            p1.angle = 2 * tangent - p1.angle
            p2.angle = 2 * tangent - p2.angle

            angle = 0.5 * math.pi + tangent
            p1.x += math.sin(angle)
            p1.y -= math.cos(angle)
            p2.x -= math.sin(angle)
            p2.y += math.cos(angle)

    def bounce(self,width,height):
        if self.x > width - self.size:
            self.x = 2 * (width - self.size) - self.x
            self.angle = - self.angle
        elif self.x < self.size:
            self.x = 2*self.size - self.x
            self.angle =- self.angle
        if self.y > height - self.size:
            self.y =2*(height-self.size) - self.y
            self.angle = math.pi - self.angle
        elif self.y < self.size:
            self.y = 2 * self.size - self.y
            self.angle = math.pi - self.angle