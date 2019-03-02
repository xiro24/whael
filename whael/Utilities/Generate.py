from whael.Elements.states import Gas, Liquid, Solid


class Generate:

    def solid(self,solid):
        element = Solid(solid)

    def liquid(self,liquid):
        element = Liquid(liquid)
    def gas(self,gas):
        element = Gas(gas)