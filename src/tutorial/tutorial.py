
import Ragnarok as R

#We are telling Ragnarok that we want to create a window of size 640 by 480,
#and that it should bear the title "RAGNAROK TUTORIAL 1".
#Notice how we are making use of the Vector2 class to pass in the window size.

engine = R.Ragnarok(R.Vector2(640, 480), "RAGNAROK TUTORIAL 1")

world = engine.get_world()

#The world's clear_color property defines what color the backbuffer should be
#erased to after each draw operation.
world.clear_color = (0, 0, 0)

#A Sprite is essentially a container object for an image that allows us to manipulate 
#properties of it extremely easily. Let's start by creating the object.
sprite = R.Sprite()
sprite.update_order = 0
sprite.draw_order = 0
sprite.load_texture("../../lib/Ragnarok/Ragnarok.jpg")

#the last step to get this object onscreen is to
#add it to the world so it can be drawn and updated.
world.add_obj(sprite)


engine.run()

