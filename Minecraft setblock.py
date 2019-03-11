from mcpi.minecraft import Minecraft
from mcpi import block

mc=Minecraft.create()

def bodenplatte():
   for i in range(8):
       mc.setBlock(10+i,15,10,1)
       
bodenplatte()
