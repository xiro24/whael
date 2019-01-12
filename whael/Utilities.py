from pyglet.gl import *

class Utilities:
    def load_image(self,img):
        return pyglet.image.load(img)

    def place_image(self,img,x,y):
        return pyglet.sprite.Sprite(img, x, y)

    def place_image(self,img,x,y,batch):
        return pyglet.sprite.Sprite(img, x, y,batch = batch)


    def color(self,sprite,x,y,z):
        sprite.color = (x,y,z)