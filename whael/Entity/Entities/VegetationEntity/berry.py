import random

from Entity.BaseVegetationEntity import BaseVegetationEntity
from Entity.EntityAttributes import EntityAttributes
from whael.Elements.Elementario.Terra import Terra
from Utilities.Clock import Time

class berry(BaseVegetationEntity):
    def __init__(self, x, y, size,list_biodegradables):
        # this super will call the the inherited init
        super().__init__(x, y, size)
        self.entityScale = 5
        self.food = "berries"
        self.lifespan = 6
        self.numeralAttributeDict = {"durability": 0,
                                    "nutrition": 0,
                                    "Age": 0}
        self.AttributeDict = {"condition": ""}

        self.tempfix = list_biodegradables
        self.Attribute = ""

    ############################Entity Based time needs to be moved to acclimatize#############################
        #there is a bit of code duplication, refactoring should be considered
        # x and y are the starting coordinates
    def createEntity(self, amt, width, height, map, dimensions):
       # add to list controller
        self.entityList = []
        # have a check if it's a baby being created...
        # and make the baby = the size. Else generate random as size

        for i in range(amt):
            size = random.randint(1, self.entityScale)
            # 3 is an adult sized
            #place holder you would need to restrict it by suing the MAP grid. so then the food only spawns
            #on the land
            while True:
                x = random.randint(0, dimensions[0]-1)
                y = random.randint(0, dimensions[1]-1)
                if isinstance(map[1][x][y],Terra):
                    break
            entity = berry(x*dimensions[2], y*dimensions[2], size,self.tempfix)

            self.entityList.append(entity)
        return self.entityList

    # changes the advances the age
    def witherRate(self):
        self.Attribute = EntityAttributes(self)
        time = Time()
        if time.getTime() % time.day == 0 and self.numeralAttributeDict.get("Age") != self.lifespan:
            self.numeralAttributeDict.update({"Age": self.numeralAttributeDict.get("Age") + 1})
            self.lifespan -= 1
            # updates the stats at a certain peak age
            self.Attribute.GrowthStatus(self.numeralAttributeDict.get("Age"))
    ############################Entity Based time needs to be moved to acclimatize#############################




