from mcpi.minecraft import Minecraft
from mcpi import block

mc=Minecraft.create()

#Variabeln
stone=1
wood=5
glass=20
air=0
x,y,z=mc.player.getPos()
#Funktionen
def Bodenplatte(xs,ys,zs, steps,block):
    for j in range(steps):
        for i in range(steps):  
            mc.setBlock(xs+i,ys,zs+j,block)


def Wände(xs,ys,zs,steps,ausrichtung,block):
    if ausrichtung == x:
        for b in range(steps):
            for c in range(steps):
                mc.setBlock(xs+c,ys+b,zs,block)
    else:
        for h in range(steps):
            for k in range(steps):
                mc.setBlock(xs,ys+h,zs+k,block)

def fenster(xs,ys,zs,steps,ausrichtung,glass):
    if ausrichtung == x:
        for b in range(steps):
            for c in range(steps):
                mc.setBlock(xs+c,ys+b,zs,glass)
    else:
        for h in range(steps):
            for k in range(steps):
                mc.setBlock(xs,ys+h,zs+k,glass)

def Tür(xs,ys,zs,steps,ausrichtung,block):
    if ausrichtung == x:
        for b in range(steps):
            for c in range(steps):
                mc.setBlock(xs+c,ys+b,zs,block)
    else:
        for h in range(steps):
            for k in range(steps):
                mc.setBlock(xs,ys+h,zs+k,block)

#Befehle
Bodenplatte(10,20,30,8,wood)
Wände(10,20,30,8,x,wood)
fenster(12,22,30,4,x,glass)
Wände(10,20,37,8,x,wood)
fenster(12,22,37,4,x,glass)
Wände(10,20,30,8,z,wood)
Tür(10,21,33,2,z,air)
Wände(17,20,30,8,z,wood)
Bodenplatte(11,27,31,6,glass)
