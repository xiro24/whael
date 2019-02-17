import Generate
import math
import random

#Gas(ele.GenerateCaeli(x,y,z)).smoke()
class Gas(Generate):
    def __init__(self,element):
        #temp
        element.density %= 60
        element.hardness /= 2
        return element

    def smoke(self,element):
        element.hardness = 0.10
        #cahnge properties to amke element into smoke
        #make more caeli as well?