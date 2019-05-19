#equivalent to a human
import random
from whael.Utilities.Clock import Time
from whael.Entity.BaseEntity import BaseEntity
from whael.Entity.EntityAttributes import EntityAttributes
#each Entity class should be it's own controller for that entity class
class Vir(BaseEntity):
    def __init__(self,x,y,size):
        #this super will call the the inherited init
        super().__init__(x,y,size)
        self.entityScale = 5
        self.food="berries"
        self.lifespan=27375
        self.numeralAttributeDict = {"durability": 0,
                                     "strength": 0,
                                     "dexterity": 0,
                                     "charisma": 0,
                                     "endurance": 0,
                                     "Age": 0}
        self.AttributeDict = {"condition": "", "mind": ""}

    #x and y are the starting coordinates
    def createEntity(self,amt,x,y):
        # add to list controller
        self.entityList = []
        #have a check if it's a baby being created...
        #and make the baby = the size. Else generate random as size
        for i in amt:
            size=random.randint(1, 10)
            #10 is an adult sized
            entity = Vir(x,y,size)
            self.Attribute=EntityAttributes(entity)
            self.entityList.append(entity)

    #changes the advances the age
    def witherRate(self):
        time = Time()
        if time.getTime()%time.day==0 and self.numeralAttributeDict.get("Age")!=self.lifespan:
            self.numeralAttributeDict.update({"Age": self.numeralAttributeDict.get("Age")+1})
            # updates the stats at a certain peak age
            self.Attribute.GrowthStatus(self.numeralAttributeDict.get("Age"))





