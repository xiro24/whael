from whael.Elements.Elementario.BaseElement import BaseElement

class Aqua(BaseElement):
    def __init__(self):
        self.boilingPoint = 100
        self.density = 999
        self.hardness = 180
        self.charge = 18#also known for the mass
        #print("define wind effect here as well as AOE of entities")
        self.lightIntensity = []

    def setLightIntensity(self, x, y, z):
        self.lightIntensity.append(x)
        self.lightIntensity.append(y)
        self.lightIntensity.append(z)

    def getLightIntensity(self):
        return self.lightIntensity
