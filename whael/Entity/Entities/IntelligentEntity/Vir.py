#equivalent to a human
import math
import random
from whael.Utilities.Clock import Time
from whael.Entity.BaseEntity import BaseEntity
from whael.Elements.Elementario.Terra import Terra
from whael.Entity.EntityAttributes import EntityAttributes

#each Entity class should be it's own controller for that entity class
class Vir(BaseEntity):
    def __init__(self,x,y,size,list_biodegradables):
        #this super will call the the inherited init
        super().__init__(x,y,size)
        self.entityScale = size
        self.food = "berries"
        #self.lifespan=27375
        self.lifespan = 100
        self.numeralAttributeDict = {"durability": 0,
                                     "strength": 0,
                                     "dexterity": 0,
                                     "charisma": 0,
                                     "endurance": 0,
                                     "Age": 0}
        self.AttributeDict = {"condition": "", "mind": ""}

        self.tempfix = list_biodegradables
        self.Attribute = EntityAttributes(self)

    ############################Entity Based time needs to be moved to acclimatize#############################
    #x and y are the starting coordinates
    def createEntity(self,amt,width,height, map, dimensions):
        # add to list controller
        self.entityList = []
        #have a check if it's a baby being created...
        #and make the baby = the size. Else generate random as size
        for i in range(amt):
            size=random.randint(1, self.entityScale)
            #10 is an adult sized
            while True:
                x = random.randint(0, dimensions[0]-1)
                y = random.randint(0, dimensions[1]-1)
                #you should try implementing an array to decide who's on top
                if isinstance(map[1][x][y], Terra):
                    break
            entity = Vir(x*dimensions[2],y*dimensions[2],size,self.tempfix)
            entity.speed = random.random()
            entity.angle = random.uniform(0, math.pi * 2)
            self.entityList.append(entity)
        return self.entityList

    #changes the advances the age
    def witherRate(self):
        if self.numeralAttributeDict.get("Age")!= self.lifespan:
            self.numeralAttributeDict.update({"Age": self.numeralAttributeDict.get("Age")+1})
            # updates the stats at a certain peak age
            self.Attribute.GrowthStatus(self.numeralAttributeDict.get("Age"))

    #########################################################################################################

    def perform_base_needs(self):
        #wither function
        self.witherRate()
        #feed_function
        #sleep_function
        #breed_function
        self.breed()


    def breed(self):
        maturity = int(0.3*self.lifespan)
        if self.numeralAttributeDict.get("Age") >= maturity:
            print("breeding?")
            # 1. check if there is 1:1 for each food

            #think



