
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
        #self.j = 0

    def circadianRhythm(self,time,width,height):
        #have the time reset to zero once a year has passed - world properties are not affected - only incremented.
        #height=400
        #uptime for moon is 200 seconds (should be)
        #uptime for sun is 400 seconds
        if time%(height+(200)) < height:
            #self.j=0
            self.sun.drawSun(time, width, height, time%(height+(200)))
            #print("time %i",time%(height+(200)))
            #print("sun")
        else:
            #print("mooon %i", self.j)
            self.moon.drawMoon(time, width, height,time%(height+(200)))
            #self.j += 1
            #print("moon")
        #you'd need a much more robust mode for this...

