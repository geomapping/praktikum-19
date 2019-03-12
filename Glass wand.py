from mcpi.minecraft import Minecraft
from mcpi import block

mc=Minecraft.create()
wood=5
stone=1
glass=20
x,y,z=mc.player.getPos()

def Wände(xs,ys,zs,steps,ausrichtung,glass):
    if ausrichtung == x:
        for b in range(steps):
            for c in range(steps):
                mc.setBlock(xs+c,ys+b,zs,glass)
    else:
        for h in range(steps):
            for k in range(steps):
                mc.setBlock(xs,ys+h,zs+k,glass)


Wände(25,46,10,8,z,glass)
