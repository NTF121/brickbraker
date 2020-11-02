import pygame

pygame.init()
resolution = 640
win = pygame.display.set_mode((resolution, resolution))
pygame.display.set_caption("Brickbraker")
my=resolution-12-50


class bricks(object):
	"""docstring for bricks"""
	br = None
	bwith = 100
	def brick(bx,by,bwith,bheight):
		bricks.br = pygame.draw.rect(win, (0,0,200), (bx,by,bwith,bheight))
		return bricks.br
		pass
	pass
class circles(object):
	"""docstring for circles"""
	x = resolution/2
	y = resolution/2
	x_angle = 0.2
	y_angle = 0.3
	direction=0
	radius = 10
	cr = None
	def circle0(pos_x,pos_y):
		circles.cr = pygame.draw.circle(win, (200,0,0), (pos_x, pos_y), circles.radius)
		return circles.cr
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
		circles.circle_collide_br(0.1,0.1)
		circles.circle_collide_wall()
		pass
	def circle_collide_wall():
		if circles.x>resolution-circles.radius:
			circles.x = resolution-circles.radius
			pass
		elif circles.y>resolution-circles.radius:
			circles.y = resolution-circles.radius
			pass
		elif circles.x<circles.radius:
			circles.x = circles.radius
			pass
		elif circles.y<circles.radius:
			circles.y = circles.radius
			pass
		if (circles.x>resolution-circles.radius-1 and circles.direction == 0) or (circles.y<circles.radius+1 and circles.direction == 2):
			circles.direction = 1
			pass
		elif (circles.y>resolution-circles.radius-1 and circles.direction == 1) or (circles.x>resolution-circles.radius-1 and circles.direction == 3): 
			circles.direction = 2
			pass
		elif (circles.x<circles.radius+1 and circles.direction == 2) or (circles.y>resolution-circles.radius-1 and circles.direction == 0): 
			circles.direction = 3
			pass
		elif (circles.x<circles.radius+1 and circles.direction == 1) or (circles.y<circles.radius+1 and circles.direction == 3):
			circles.direction = 0
			pass
		pass
	def circle_collide_br(x_angle_change,y_angle_change):
		if circles.x_angle > 1 or circles.y_angle > 1 or circles.y_angle < 0.1:
			circles.x_angle = 0.5
			circles.y_angle = 0.5
			pass
		if bricks.br.colliderect(circles.cr) and circles.x<=controls.mx and circles.y<my-circles.radius:
			circles.direction = 2
			circles.x_angle -= x_angle_change
			circles.y_angle += y_angle_change
			circles.x = controls.mx
			pass
		if bricks.br.colliderect(circles.cr) and circles.x>=controls.mx+bricks.bwith and circles.y<my-circles.radius:
			circles.direction = 3
			circles.x_angle -= x_angle_change
			circles.y_angle += y_angle_change
			circles.x = controls.mx+bricks.bwith
			pass
		if bricks.br.colliderect(circles.cr) and circles.x<((controls.mx+bricks.bwith/2)+controls.mx)/2 and not circles.y<my-circles.radius:
			circles.direction = 2
			circles.x_angle += x_angle_change
			circles.y_angle -= y_angle_change
			pass
		elif bricks.br.colliderect(circles.cr) and circles.x>((controls.mx+bricks.bwith/2)+controls.mx)/2 and circles.x<controls.mx+bricks.bwith/2 and not circles.y<my-circles.radius:
			circles.direction = 2
			circles.x_angle -= x_angle_change
			circles.y_angle += y_angle_change
			pass
		elif bricks.br.colliderect(circles.cr) and circles.x<((controls.mx+bricks.bwith/2)+bricks.bwith)/2 and not circles.y<my-circles.radius:
			circles.direction = 3
			circles.x_angle -= x_angle_change
			circles.y_angle += y_angle_change
			pass
		elif bricks.br.colliderect(circles.cr) and circles.x>((controls.mx+bricks.bwith/2)+bricks.bwith)/2 and not circles.y<my-circles.radius:
			circles.direction = 3
			circles.x_angle += x_angle_change
			circles.y_angle -= y_angle_change
			pass
		pass
	pass

	pass
class controls(object):
	mx=12
	"""docstring for controls"""
	def mouse():
		mouse_x , mouse_y = pygame.mouse.get_pos()
		if pygame.mouse.get_pressed()[0] and bricks.br.collidepoint(pygame.mouse.get_pos()):
			bricks.brick(mouse_x-bricks.bwith/2, my,bricks.bwith,50)
			controls.mx = mouse_x-bricks.bwith/2
			##my = mouse_y
			pass
		else:
			bricks.brick(controls.mx, my,bricks.bwith,50)
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