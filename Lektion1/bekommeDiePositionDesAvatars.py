from mcpi.minecraft import Minecraft
mc = Minecraft.create()

positionDesSpielers = mc.player.getPos()
x = positionDesSpielers.x
y = positionDesSpielers.y
z = positionDesSpielers.z
mc.postToChat(" x: " + str(x) + " y: "  +str(y) + " z: "+ str(z))


