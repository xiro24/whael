from whael.Elements.Elementario.BaseElement import BaseElement
class Terra(BaseElement):
    def __init__(self):
        self.boilingPoint = 212
        self.meltingPoint = 10000
        self.density = 2.65
        self.charge = 260 # also known for the mass
        self.lightIntensity = []

    def setLightIntensity(self, x, y, z):
        self.lightIntensity.append(x)
        self.lightIntensity.append(y)
        self.lightIntensity.append(z)

    def getLightIntensity(self):
        return self.lightIntensity

