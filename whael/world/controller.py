
import whael.Utilities.Constant as CONST
from whael.Particles.Sun import Sun
from whael.Particles.Moon import Moon
class controller:

    #initialize sun and moon
    def initializer(self):
        #would require polymorphism to streamline code
        self.sun = Sun()
        self.moon = Moon()
        self.sun.initial()
        self.sun.sep()
        self.moon.initial()
        self.moon.sep()
        print("hm")

    def circadianRhythm(self,time,width,height):
        #have the time reset to zero once a year has passed - world properties are not affected - only incremented.

        if time%(height+(200)) < height:
            self.sun.drawSun(time, width, height)
        else:
            self.moon.drawMoon(time, width, height)
        #you'd need a much more robust mode for this...

