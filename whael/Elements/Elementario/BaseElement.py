from pyglet.gl import *

class BaseElement:
    #contains what all elements require to become an element
    def __init__(self):
        self.density = "?"
        self.meltingPoint = "?"
        self.boilingPoint = "?"
        self.hardness = "?"
        self.charge = "?" #also known for the mass
        self.speed = "?"
        self.mass = "?"
        self.lifespan = "?" #to be modified by summoner
        self.temperature = "?"
        self.lightIntensity =[]

    def setLightIntensity(self,x,y,z):
        self.lightIntensity.append(x)
        self.lightIntensity.append(y)
        self.lightIntensity.append(z)

    def getLightIntensity(self):
        return self.lightIntensity

    #not sure if this fits here
    def Fire(self,dmg_obj):
        return dmg_obj