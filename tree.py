from mcpi.minecraft import Minecraft
import mcpi.block as block
from threading import Thread
import math
import time
mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
leaves = block.Block(18,1)
log = block.Block(17,1)

def setPixel(x1,z1,block):
	mc.setBlock(x1,y,z1,block)
def Sphere():
    planetId = block.GLOWSTONE_BLOCK.id
    x = pos.x
    y = pos.y + 17
    z = pos.z + 10

    mc.setBlock(x,y,z,15)

    radius = 15
    angle = 0
    speed = math.pi/ 10
     
    dx = math.cos(angle) * radius
    dz = math.sin(angle) * radius
    Px = round(x + dx)
    Py = y
    Pz = round(z + dz)
    mc.setBlock(Px,Py,Pz,planetId)

    while True:
        period = 0.1
        angle += speed * period
        mc.setBlocks(Px + 2,Py + 2,Pz,Px,Py,Pz + 2,0)
        dx = math.cos(angle) * radius
        dz = math.sin(angle) * radius
        Px = round(x + dx)
        Py = y
        Pz = round(z + dz)
        mc.setBlocks(Px + 1,Py + 1,Pz,Px,Py,Pz + 1,planetId)
        time.sleep(period)

def buildCubes():
	while True:
		x = pos.x + 4
		y = pos.y + 4
		z = pos.z + 1
		mc.setBlock(x,y,z,41)
		x -= 1
		y += 3
		z += 1
		mc.setBlock(x,y,z,20)
		x += 2
		y += 3
		z += 2
		mc.setBlock(x,y,z,57)
		x += 2
		z += 2
		mc.setBlock(x,y,z,79)
		x += 2
		y -= 3
		z += 1
		mc.setBlock(x,y,z,41)
		z += 6
		mc.setBlock(x,y,z,20)
		x -= 2
		y += 3
		z += 1
		mc.setBlock(x,y,z,57)
		x -= 2
		z += 2
		mc.setBlock(x,y,z,79)
		x-= 2
		y -=3
		z += 2
		mc.setBlock(x,y,z,41)
		x -= 6
		mc.setBlock(x,y,z,20)
		x -= 2
		y += 3
		z -= 2
		mc.setBlock(x,y,z,57)
		x -= 2
		z -= 2
		mc.setBlock(x,y,z,79)
		x -= 2
		y -= 3
		z -= 1
		mc.setBlock(x,y,z,41)
		z -= 6
		mc.setBlock(x,y,z,20)
		x += 2
		y += 3
		z -= 1
		mc.setBlock(x,y,z,57)
		x += 2
		z -= 2
		mc.setBlock(x,y,z,79)
		x += 2
		y -= 3
		z -= 2
		mc.setBlock(x,y,z,41)
		y += 15
		x += 1
		z += 5
		mc.setBlock(x,y,z,20)
		x -= 1
		y += 3
		z += 2
		mc.setBlock(x,y,z,57)
		z += 2
		mc.setBlock(x,y,z,79)
		x += 6
		mc.setBlock(x,y,z,41)
		z -= 2
		mc.setBlock(x,y,z,20)



def buildStar():
	x = pos.x - 6 
	y = pos.y + 28
	z = pos.z + 8
	while True:
		mc.setBlocks(x,y,z,x+11,y+10,z+4,95)
		mc.setBlocks(x+3,y,z,x+9,y,z+4,0)
		mc.setBlocks(x+4,y+1,z,x+8,y+1,z+4,0)
		mc.setBlocks(x+5,y+2,z+4,x+7,y+2,z,0)
		mc.setBlocks(x,y,z+4,x,y+6,z,0)
		mc.setBlocks(x+2,y+3,z+4,x+2,y+4,z,0)
		mc.setBlocks(x+1,y+2,z+4,x+1,y+5,z,0)
		mc.setBlocks(x,y+8,z+4,x+4,y+11,z,0)
		mc.setBlocks(x+2,y+7,z+4,x+3,y+7,z,0)
		mc.setBlocks(x+7,y+8,z+4,x+11,y+10,z,0)
		mc.setBlocks(x+8,y+7,z+4,x+9,y+7,z,0)
		mc.setBlocks(x+12,y,z+4,x+12,y+6,z,0)
		mc.setBlocks(x+11,y+2,z+4,x+11,y+6,z,0)
		mc.setBlocks(x+10,y+3,z+4,x+11,y+5,z,0)
		mc.setBlocks(x+9,y+4,z+4,x+9,y+4,z,0)
		time.sleep(5)
		mc.setBlocks(x,y,z,x+11,y+10,z + 4,89)
		mc.setBlocks(x+3,y,z,x+9,y,z + 4,0)
		mc.setBlocks(x+4,y+1,z,x+8,y+1,z + 4,0)
		mc.setBlocks(x+5,y+2,z + 4,x+7,y+2,z,0)
		mc.setBlocks(x,y,z + 4,x,y+6,z,0)
		mc.setBlocks(x+2,y+3,z + 4,x+2,y+4,z,0)
		mc.setBlocks(x+1,y+2,z + 4,x+1,y+5,z,0)
		mc.setBlocks(x,y+8,z + 4,x+4,y+11,z,0)
		mc.setBlocks(x+2,y+7,z + 4,x+3,y+7,z,0)
		mc.setBlocks(x+7,y+8,z + 4,x+11,y+10,z,0)
		mc.setBlocks(x+8,y+7,z + 4,x+9,y+7,z,0)
		mc.setBlocks(x+12,y,z + 4,x+12,y+6,z,0)
		mc.setBlocks(x+11,y+2,z + 4,x+11,y+6,z,0)
		mc.setBlocks(x+10,y+3,z + 4,x+11,y+5,z,0)
		mc.setBlocks(x+9,y+4,z + 4,x+9,y+4,z,0)
		time.sleep(5)
		mc.setBlocks(x,y,z,x+11,y+10,z + 4,152)
		mc.setBlocks(x+3,y,z,x+9,y,z + 4,0)
		mc.setBlocks(x+4,y+1,z,x+8,y+1,z + 4,0)
		mc.setBlocks(x+5,y+2,z + 4,x+7,y+2,z,0)
		mc.setBlocks(x,y,z + 4,x,y+6,z,0)
		mc.setBlocks(x+2,y+3,z + 4,x+2,y+4,z,0)
		mc.setBlocks(x+1,y+2,z + 4,x+1,y+5,z,0)
		mc.setBlocks(x,y+8,z + 4,x+4,y+11,z,0)
		mc.setBlocks(x+2,y+7,z + 4,x+3,y+7,z,0)
		mc.setBlocks(x+7,y+8,z + 4,x+11,y+10,z,0)
		mc.setBlocks(x+8,y+7,z + 4,x+9,y+7,z,0)
		mc.setBlocks(x+12,y,z + 4,x+12,y+6,z,0)
		mc.setBlocks(x+11,y+2,z + 4,x+11,y+6,z,0)
		mc.setBlocks(x+10,y+3,z + 4,x+11,y+5,z,0)
		mc.setBlocks(x+9,y+4,z + 4,x+9,y+4,z,0)
		time.sleep(5)
		mc.setBlocks(x,y,z,x+11,y+10,z + 4,133)
		mc.setBlocks(x+3,y,z,x+9,y,z + 4,0)
		mc.setBlocks(x+4,y+1,z,x+8,y+1,z + 4,0)
		mc.setBlocks(x+5,y+2,z + 4,x+7,y+2,z,0)
		mc.setBlocks(x,y,z + 4,x,y+6,z,0)
		mc.setBlocks(x+2,y+3,z + 4,x+2,y+4,z,0)
		mc.setBlocks(x+1,y+2,z + 4,x+1,y+5,z,0)
		mc.setBlocks(x,y+8,z + 4,x+4,y+11,z,0)
		mc.setBlocks(x+2,y+7,z + 4,x+3,y+7,z,0)
		mc.setBlocks(x+7,y+8,z + 4,x+11,y+10,z,0)
		mc.setBlocks(x+8,y+7,z + 4,x+9,y+7,z,0)
		mc.setBlocks(x+12,y,z + 4,x+12,y+6,z,0)
		mc.setBlocks(x+11,y+2,z + 4,x+11,y+6,z,0)
		mc.setBlocks(x+10,y+3,z + 4,x+11,y+5,z,0)
		mc.setBlocks(x+9,y+4,z + 4,x+9,y+4,z,0)
		time.sleep(5)
def draw_circle(x, y, r,block):
    disp_x = x
    disp_y = z + 10
    x = 0
    y = r
    delta = (1-2*r)
    error = 0
    while y >= 0:
        setPixel(disp_x + x, disp_y + y,block)
        setPixel(disp_x + x, disp_y - y,block)
        setPixel(disp_x - x, disp_y + y,block)
        setPixel(disp_x - x, disp_y - y,block)
        
        error = 2 * (delta + y) - 1
        if ((delta < 0) and (error <=0)):
            x+=1
            delta = delta + (2*x+1)
            continue
        error = 2 * (delta - x) - 1
        if ((delta > 0) and (error > 0)):
            y -= 1
            delta = delta + (1 - 2 * y)
            continue
        x += 1
        delta = delta + (2 * (x - y))
        y -= 1
def buildTree():
	global x
	global y
	global log
	global leaves
	while True:
		x = pos.x
		y = pos.y
		yMin = y
		r = 10
		draw_circle(x,y,r,leaves)
		y += 1
		draw_circle(x,y,r,leaves)
		while(r != 0):
			for i in range(1,4):
				draw_circle(x,y,r,leaves)
				y += 1
			r -= 1
		y -= 4
		yMin -= 8
		while y != yMin:
			draw_circle(x,y,1,log)
			y -= 1

#Threads
tree = Thread(target=buildTree)
star = Thread(target=buildStar)
cubes = Thread(target=buildCubes)
sphere = Thread(target=Sphere)

tree.start()
star.start()
cubes.start()
sphere.start()
