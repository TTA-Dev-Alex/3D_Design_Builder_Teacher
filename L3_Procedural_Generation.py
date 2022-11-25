from random import *
counter = 0
while counter < 100:
     x = randint(-100, 100)
     y = randint(-100, 100)
     bpy.ops.object.duplicate(linked=False)
     thing = bpy.context.active_object
     thing.location[0] = thing.location[0] + x
     thing.location[1] = thing.location[1] + y
     counter = counter + 1
