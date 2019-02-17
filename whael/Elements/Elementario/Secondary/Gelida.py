from BaseElement import BaseElement


class Gelida(BaseElement):
    def __init__(self,force,range,radius):
        self.boilingPoint = 100
        self.density = 0.92 *radius
        self.hardness = 1.5
        self.charge = 18 *radius #also known for the mass
        self.temperature = 0
        self.amount = radius
        self.force = force
        self.range = range
        print("define wind effect here as well as AOE of entities")