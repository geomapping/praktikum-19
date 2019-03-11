from mcpi.minecraft import Minecraft
from mcpi import block

mc=Minecraft.create()
stone=1
air=0
x,y,z=mc.player.getPos()

def Wände(xs,ys,zs,steps,ausrichtung,block):
    if ausrichtung == x:
        for b in range(steps):
            for c in range(steps):
                mc.setBlock(xs+c,ys+b,zs,block)
    else:
        for h in range(steps):
            for k in range(steps):
                mc.setBlock(xs,ys+h,zs+k,block)

Wände(20,46,23,2,z,air)
