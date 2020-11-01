import pygame

pygame.init()
resolution = 640
win = pygame.display.set_mode((resolution, resolution))
pygame.display.set_caption("There is no game")
my=resolution-12-50


class bricks(object):
	"""docstring for bricks"""
	def init():
		bricks.brick(mx,my,100,50)
		pass
	cl = False
	def brick(bx,by,bwith,bheight):
		br = pygame.draw.rect(win, (0,0,200), (bx,by,bwith,bheight))
		if br.collidepoint(pygame.mouse.get_pos()): bricks.cl = True
		else: bricks.cl = False
		return br
		pass
	pass
class circles(object):
	"""docstring for circles"""
	x = resolution/2
	y = resolution/2
	x_angle = 0.6
	y_angle = 0.8
	direction=0
	radius = 10
	def circle0(pos_x,pos_y):
		cr = pygame.draw.circle(win, (200,0,0), (pos_x, pos_y), circles.radius)
		return cr
		pass
	def circle_move():
		circles.circle0(circles.x,circles.y)
		if circles.direction == 0:
			circles.x += circles.x_angle
			circles.y += circles.y_angle
			pass
		elif circles.direction == 1:
			circles.x -= circles.x_angle
			circles.y += circles.y_angle
			pass
		elif circles.direction == 2:
			circles.x -= circles.x_angle
			circles.y -= circles.y_angle
			pass
		elif circles.direction == 3:
			circles.x += circles.x_angle
			circles.y -= circles.y_angle
			pass
		if (circles.x>resolution-circles.radius and circles.direction == 0) or (circles.y<0+circles.radius and circles.direction == 2):
			circles.direction = 1
			pass
		elif (circles.y>resolution-circles.radius and circles.direction == 1) or (circles.x>resolution-circles.radius and circles.direction == 3): 
			circles.direction = 2
			pass
		elif (circles.x<0+circles.radius and circles.direction == 2) or (circles.y>resolution-circles.radius and circles.direction == 0): 
			circles.direction = 3
			pass
		elif (circles.x<0+circles.radius and circles.direction == 1) or (circles.y<0+circles.radius and circles.direction == 3):
			circles.direction = 0
			pass
		pass
	pass

	pass
class controls(object):
	mx=12
	"""docstring for controls"""
	def mouse():
		mouse_x , mouse_y = pygame.mouse.get_pos()
		if pygame.mouse.get_pressed()[0] and bricks.cl:
			bricks.brick(mouse_x-50, my,100,50)
			controls.mx = mouse_x-50
			##my = mouse_y
			pass
		else:
			bricks.brick(controls.mx, my,100,50)
			pass
		pass
	pass


run=True
while run:
	pygame.time.delay(1)
	for event in pygame.event.get():
		if event.type == pygame.QUIT: run = False
		pass
	win.fill((0,0,0))
	controls.mouse()
	circles.circle_move()
	keys = pygame.key.get_pressed()
	pygame.display.update()	
pygame.quit()
quit(0)