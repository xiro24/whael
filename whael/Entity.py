import pygame
import math
import random

class randParticle:
    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.colour = (0, 0, 255)
        self.thickness = 1
        self.size = size
        self.speed = 0.01
        self.angle = 0
        self.elasticity = 0.75

    def Particle(self, screen, width, height):
        noPt = 20
        pt =[]
        for n in range(noPt):
            size = random.randint(10,20)
            x = random.randint(size,width - size)
            y = random.randint(size, height - size)
            part = randParticle(x, y,size)
            part.speed = random.random()
            part.angle = random.uniform(0,math.pi*2)
            pt.append(part)
        self.pt = pt

    def Move(self):
        #gravity = (math.pi, 0.002)
        drag = 0.999
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        self.speed*=drag
        (self.angle, self.speed) = self.addVectors(self.angle, self.speed,math.pi,0.002)

        # particle.speed = random.random()
        # particle.angle = random.un


    def Display(self,screen,width,height):
        for mpt in self.pt:
            mpt.Move()
            mpt.bounce(width,height)
            mpt.draw(screen)



    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)

    def bounce(self,width,height):
        if self.x > width - self.size:
            self.x = 2 * (width - self.size) - self.x
            self.speed*= self.elasticity
            self.angle = - self.angle
        elif self.x < self.size:
            self.speed *= self.elasticity
            self.x = 2*self.size - self.x
            self.angle =- self.angle

        if self.y > height - self.size:
            self.speed *= self.elasticity
            self.y =2*(height-self.size) - self.y
            self.angle = math.pi - self.angle
        elif self.y < self.size:
            self.speed *= self.elasticity
            self.y = 2 * self.size - self.y
            self.angle = math.pi - self.angle

    def addVectors(self,angle1,length1,angle2,length2):
        x = math.sin(angle1)*length1+math.sin(angle2)*length2
        y = math.cos(angle1)*length1+math.cos(angle2)*length2

        length = math.hypot(x,y)
        angle = 0.5 * math.pi - math.atan2(y,x)
        return (angle,length)

    def findParticle(self,x , y):
        for p in self.pt:
            if math.hypot(p.x-x, p.y-y) <= p.size:
                return p
        return None

    def followMouse(self,spt,dx,dy):
        spt.angle = math.atan2(dy, dx) + 0.5 * math.pi
        spt.speed = math.hypot(dx, dy) * 0.1