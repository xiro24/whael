from pyglet.gl import *
import math
import random


# This class will generate random attribute status for each entity.
# Entities class should make an object of this that it references in it's own class.
# Entities class passes in it's entity type which will determine te base durability.
class EntityAttributes:
    def __init__(self, EntityType):
        # Depending on the age of the entity that will be returned in the EntityType.health - for example
        # (5/EntityType.health)*EntityType.health which would equal 5% of the Entities's health
        self.entityNumAttr = EntityType.numeralAttributeDict
        for i in self.entityNumAttr:
            self.entityNumAttr.update({i: self.GenerateAttributeValue(self.entityNumAttr.get(i))})
        # ------------------------------------------------------------------------------------------------#
        # condition attributes
        # these would be randomized for a more unique outcomes
        self.entityAttr = EntityType.AttributeDict
        #might need to debug
        for i in self.entityAttr:
            self.entityAttr.update({i: "normal"})

    def GenerateAttributeValue(self, AttributeValue):
        printThis = random.randint(0, AttributeValue)
        return printThis

    def DamageRecieved(self, DamageAmount):
        print("temp")

    def GrowthStatus(self, Age):
        # ensure you've accounted for bonuses here..
        # you would probably need a action checker to check what the activity is
        for i in self.entityNumAttr:
            if i == "Age":
                self.entityNumAttr.update({i: (Age + 1)})
                #else:
                    # ages them to deterioate
                #    self.entityNumAttr.update({i: ((Age + self.entityNumAttr.get(i)) / self.entityNumAttr.get(i)) - (
                #                self.entityNumAttr.get(i) / Age)})

#######################################################################

#    def __init__(self, EntityType):
        # Depending on the age of the entity that will be returned in the EntityType.health - for example
        # (5/EntityType.health)*EntityType.health which would equal 5% of the Entities's health
#        self.entityNumAttr=EntityType.numeralAttributeDict
#        for i in self.entityNumAttr:
#            self.entityNumAttr.update({i: self.GenerateAttributeValue(self.entityNumAttr.get(i))})
        # ------------------------------------------------------------------------------------------------#
        # condition attributes
        # these would be randomized for a more unique outcomes
#        self.entityAttr=EntityType.AttributeDict
#        for i in self.entityAttr:
#            self.entityNumAttr.update({i: "normal"})


#    def GenerateAttributeValue(self, AttributeValue):
#        printThis = random.randint(0, AttributeValue)
#        return printThis

#    def DamageRecieved(self, DamageAmount):
#        print("temp")

#    def GrowthStatus(self, Age):
        #ensure you've accounted for bonuses here..
        #you would probably need a action checker to check what the activity is
#        for i in self.entityNumAttr:
            #basically this will increase the percentage that's the entity will have as it grows
#            if self.entityNumAttr.get("Age") <= 40:
#                self.entityNumAttr.update({i: ((Age+self.entityNumAttr.get(i)) / self.entityNumAttr.get(i))})
#            else:
                #ages them to detorioate
#                self.entityNumAttr.update({i: ((Age+self.entityNumAttr.get(i)) / self.entityNumAttr.get(i)) - (self.entityNumAttr.get(i) / Age)})

    # this method requires access to the time class
#    def AgingStatus(self):
        #this method should call the time command from since birth t keep track of age.
#        print("temp")

# create getters/setters?
# create randomizers here in this class and set them
# this class will also be responsible for the status effects when the entity gets inflicted with damage
