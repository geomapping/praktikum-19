from mcpi.minecraft import Minecraft
from mcpi import block

mc=Minecraft.create()

def Bodenplatte(xs,ys,zs, steps):
    for j in range(steps):
        for i in range(steps):  
            mc.setBlock(xs+i,ys,zs+j,1)

Bodenplatte(10,30,10,8,)
