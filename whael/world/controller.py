
import whael.Utilities.Constant as CONST

class controller:

    def circadianRhythm(self,time,width,height):
        #have the time reset to zero once a year has passed - world properties are not affected - only incremented.
        if (time % (height + 200)) != 0:
            tempus = (time % (height + 200))
        else:
            tempus = 0

        if time%(height+(200)) < height:
            print('place holder')
        else:
            print('place holder')