from Entity.Entities.IntelligentEntity.Vir import Vir

class acclimatize:
    def processTime(self,timeObj,list_biodegradables):
        timeObj.print_time()


    def Floor_Item(self, entitylist, WorldMaps):
        #this should be enhanced for floor item
        #use WorldMaps[2] and use it's indexes
        updated_entities = []

        for entity in entitylist:
            #check if entity is on a food souce location and ivke the eat command
            #if isinstance(entity, Vir):
            #    print("wa")
            #check lifespan
            if entity.lifespan > 0:
                entity.witherRate()
                updated_entities.append(entity)

        print("len of entities",len(updated_entities))
        return updated_entities

    # just focus on the AI movement later
    def Display(self, width, height, entitylist, map):

        print("test")

        #for i, mpt in enumerate(entitylist):
        #    mpt.Move(map)
        #    # mpt.bounce(map)
        #    for mpt2 in entitylist[i + 1:]:
        #        self.collide(mpt, mpt2)
        #    mpt.DrawCircle(20)