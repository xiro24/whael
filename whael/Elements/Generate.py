
import Constant
from Aqua import Aqua
from Caeli import Caeli
from Ignis import Ignis
from Lux import Lux
from Tenebris import Tenebris
from Terra import Terra
from Void import Void


class Generate:

    ##OFFENSIVE
    #you calculate the power through the level of the entity that's summond it,
    #the rest of the parameters are clacualted by the entity

    ##ENVIRONMENT
    #place dirt tiles if they have the same
    #then perhaps use some sort of concentration with certain elements

    def ConjureCaeli(self):
        caeli = Caeli()
        #print("define wind effect here as well as AOE of entities")
        return caeli

    def ConjureIgnis(self):
        ignis = Ignis()
        #print("define fire effect here as well as AOE of entities")
        return ignis

    def ConjureAqua(self):
        aqua = Aqua()
        #print("define water effect here as well as AOE of entities")
        return aqua

    def ConjureTerra(self):
        terra = Terra()
        #print("define Terra effect here as well as AOE of entities")
        return terra

    def ConjureLux(self):
        lux = Lux()
        #print("define light effect here as well as AOE of entities")
        return lux

    def ConjureTenebris(self):
        tenebris = Tenebris()
        #print("define light effect here as well as AOE of entities")
        return tenebris

    def ConjureVoid(self):
        void = Void()
        #print("define Void effect here as well as AOE of entities")
        return void