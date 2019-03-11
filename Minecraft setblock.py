from mcpi.minecraft import Minecraft
from mcpi import block

mc=Minecraft.create()

def bodenplatte():
    mc.setBlock(10,31,15,1)
    mc.setBlock(11,31,15,1)
    mc.setBlock(12,31,15,1)
    mc.setBlock(13,31,15,1)
    mc.setBlock(14,31,15,1)
    mc.setBlock(15,31,15,1)
bodenplatte()
