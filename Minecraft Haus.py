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


def Wand(xs,ys,zs,steps,ausrichtung,block):
    if ausrichtung == "g":
        for b in range(steps):
            for c in range(steps):
                mc.setBlock(xs+c,ys+b,zs,block)
    else:
        for h in range(steps):
            for k in range(steps):
                mc.setBlock(xs,ys+h,zs+k,block)

def fenster(xs,ys,zs,steps,ausrichtung,glass):
    if ausrichtung == "g":
        for b in range(steps):
            for c in range(steps):
                mc.setBlock(xs+c,ys+b,zs,glass)
    else:
        for h in range(steps):
            for k in range(steps):
                mc.setBlock(xs,ys+h,zs+k,glass)

def Tür(xs,ys,zs,steps,ausrichtung,block):
    if ausrichtung == "g":
        for b in range(steps):
            for c in range(steps):
                mc.setBlock(xs+c,ys+b,zs,block)
    else:
        for h in range(steps):
            for k in range(steps):
                mc.setBlock(xs,ys+h,zs+k,block)

def Bauehaus (a,b,c):
    Bodenplatte(a,b,c,8,wood)
    Wand(a,b,c,8,"g",wood)
    fenster(a+2,b+2,c,4,"g",glass)
    Wand(a,b,c+7,8,"g",wood)
    fenster(a+2,b+2,c+7,4,"g",glass)
    Wand(a,b,c,8,"r",wood)
    Tür(a,b+1,c+3,2,"r",air)
    Wand(a+7,b,c,8,"r",wood)
    Bodenplatte(a+1,b+7,c+1,6,glass)


#Befehle
Bauehaus(40,20,40)
