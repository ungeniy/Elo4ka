from mcpi.minecraft import Minecraft
import mcpi.block as block
mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
leaves = block.Block(18,1)
log = block.Block(17,1)

def setPixel(x1,z1,block):
	mc.setBlock(x1,y,z1,block)

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
buildTree()


