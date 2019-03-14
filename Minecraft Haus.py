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

def Glassdach(xs,ys,zs, stepsG,block):
    for j in range(stepsG):
        for i in range(stepsG):  
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

def fenster(xs,ys,zs,stepsF,ausrichtung,glass):
    if ausrichtung == "g":
        for b in range(stepsF):
            for c in range(stepsF):
                mc.setBlock(xs+c,ys+b,zs,glass)
    else:
        for h in range(stepsF):
            for k in range(stepsF):
                mc.setBlock(xs,ys+h,zs+k,glass)

def Tür(xs,ys,zs,stepsT,ausrichtung,block):
    if ausrichtung == "g":
        for b in range(stepsT):
            for c in range(stepsT):
                mc.setBlock(xs+c,ys+b,zs,block)
    else:
        for h in range(stepsT):
            for k in range(stepsT):
                mc.setBlock(xs,ys+h,zs+k,block)

def Bauehaus (a,b,c,steps,stepsG,stepsF,stepsT):
    Bodenplatte(a,b,c,steps,wood)
    Wand(a,b,c,steps,"g",wood)
    fenster(a+2,b+2,c,stepsF,"g",glass)
    Wand(a,b,c+7,steps,"g",wood)
    fenster(a+2,b+2,c+7,stepsF,"g",glass)
    Wand(a,b,c,steps,"r",wood)
    Tür(a,b+1,c+3,stepsT,"r",air)
    Wand(a+7,b,c,steps,"r",wood)
    Glassdach(a+1,b+7,c+1,stepsG,glass)


#Befehle
Bauehaus(40,10,40,8,6,4,2)
