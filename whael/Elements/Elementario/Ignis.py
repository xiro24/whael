from whael.Elements.Elementario.BaseElement import BaseElement
class Ignis(BaseElement):
    def __init__(self):
        self.density = (1.2/4.8)
        self.charge = 8 #also known for the mass
        self.temperature = 400

        print("define wind effect here as well as AOE of entities")
