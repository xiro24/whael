from pyglet.gl import *
import math
from whael.world.grid import Grid
from whael.Elements.Elementario.Terra import Terra
from whael.Elements.Elementario.Aqua import Aqua
import random


#This class will generate random attribute status for each entity.
#Entity class should make an object of this that it references in it's own class.
#Entity class passes in it's entity type which will determine te base durability.
class EntityAttributes:
    def __init__(self,EntityType):
        # Depending on the age of the entity that will be returned in the EntityType.health - for example
        # (5/EntityType.health)*EntityType.health which would equal 5% of the Entity's health
        self.durability = EntityType.durability
        self.strength = EntityType.strength
        self.dexterity = EntityType.dexterity
        self.charisma = EntityType.charisma
        self.endurance = EntityType.endurance

        #------------------------------------------------------------------------------------------------#
        #condition attributes
        #these would be randomized for a more unique outcomes
        self.health = "online"
        self.condition = "none"
        self.mind = "normal"
        self.soul = "normal"

    #create getters/setters?
    #create randomizers here in this class and set them
    #this class will also be responsible for the status effects when the entity gets inflicted with damage