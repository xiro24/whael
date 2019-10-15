from whael.Utilities.Clock import Time
from whael.Entity.Entities.Vir import Vir

class acclimatize:
    def processTime(self,timeObj,list_biodegradables):
        timeObj.print_time()


    def test(self,entitylist,vegelist):
        #print(entitylist)

        #this should be enhanced for floor item
        for entity in entitylist:
            for vegetation in vegelist:
                #check if entity is on a food souce location and ivke the eat command
                if isinstance(entity, Vir):
                    print(entity)


    # just focus on the AI movement later
    def Display(self, width, height, entitylist, map):

        print("test")

        #for i, mpt in enumerate(entitylist):
        #    mpt.Move(map)
        #    # mpt.bounce(map)
        #    for mpt2 in entitylist[i + 1:]:
        #        self.collide(mpt, mpt2)
        #    mpt.DrawCircle(20)