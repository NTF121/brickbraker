import pygame

pygame.init()
resolution = 640
win = pygame.display.set_mode((resolution, resolution))
pygame.display.set_caption("Brickbraker")
my=resolution-12-20
runn=True

class bricks(object):
	"""docstring for bricks"""
	br = None
	bwith = 100
	def brick(bx,by,bwith,bheight):
		if controls.mx < 0:
			controls.mx = 0
		if controls.mx+bricks.bwith > resolution:
			controls.mx = resolution-bricks.bwith
		bricks.br = pygame.draw.rect(win, (0,0,200), (bx,by,bwith,bheight))
		return bricks.br
	brs = []
	brs_rm = set()
	def brickss():
		iter_cur = 0
		for y in range(1,7):
			for x in range(1,19):
				if not iter_cur in bricks.brs_rm:
					bricks.brs.append(pygame.draw.rect(win, (187, 191, 61), (x*32,y*30,30,20)))
				else:
					bricks.brs.append(pygame.draw.rect(win, (187, 191, 61), (0,0,0,0)))
				iter_cur+=1
		for b in range(len(bricks.brs)):
			if bricks.brs[b].colliderect(circles.cr):
				bricks.brs_rm.add(b)
				circles.circle_collide_brs()
		return bricks.brs


class circles(object):
	"""docstring for circles"""
	x = resolution/2
	y = resolution/2
	x_angle = 0.2
	y_angle = 0.3
	direction=1
	radius = 10
	cr = None
	def circle0(pos_x,pos_y):
		circles.cr = pygame.draw.circle(win, (200,0,0), (pos_x, pos_y), circles.radius)
		return circles.cr
	def circle_move():
		circles.circle0(circles.x,circles.y)
		if circles.direction == 0:
			circles.x += circles.x_angle
			circles.y += circles.y_angle
		elif circles.direction == 1:
			circles.x -= circles.x_angle
			circles.y += circles.y_angle
		elif circles.direction == 2:
			circles.x -= circles.x_angle
			circles.y -= circles.y_angle
		elif circles.direction == 3:
			circles.x += circles.x_angle
			circles.y -= circles.y_angle
		circles.circle_collide_br(0.1,0.1)
		circles.circle_collide_wall()
	def circle_collide_wall():
		if circles.x>resolution-circles.radius:
			circles.x = resolution-circles.radius
		elif circles.y>resolution-circles.radius:
			circles.y = resolution-circles.radius
		elif circles.x<circles.radius:
			circles.x = circles.radius
		elif circles.y<circles.radius:
			circles.y = circles.radius
		if (circles.x>resolution-circles.radius-1 and circles.direction == 0) or (circles.y<circles.radius+1 and circles.direction == 2):
			circles.direction = 1
		elif (circles.y>resolution-circles.radius-1 and circles.direction == 1) or (circles.x>resolution-circles.radius-1 and circles.direction == 3): 
			circles.direction = 2
		elif (circles.x<circles.radius+1 and circles.direction == 2) or (circles.y>resolution-circles.radius-1 and circles.direction == 0): 
			circles.direction = 3
		elif (circles.x<circles.radius+1 and circles.direction == 1) or (circles.y<circles.radius+1 and circles.direction == 3):
			circles.direction = 0
	def circle_collide_br(x_angle_change,y_angle_change):
		if circles.x_angle > 0.5 or circles.y_angle > 0.5 or circles.y_angle < 0.1:
			circles.x_angle = 0.3
			circles.y_angle = 0.2
	
		if bricks.br.colliderect(circles.cr) and circles.x<=controls.mx and circles.y<my-circles.radius:
			circles.direction = 2
			circles.x_angle -= x_angle_change
			circles.y_angle += y_angle_change
			circles.x = controls.mx
	
		if bricks.br.colliderect(circles.cr) and circles.x>=controls.mx+bricks.bwith and circles.y<my-circles.radius:
			circles.direction = 3
			circles.x_angle -= x_angle_change
			circles.y_angle += y_angle_change
			circles.x = controls.mx+bricks.bwith
	
		if bricks.br.colliderect(circles.cr) and circles.x<((controls.mx+bricks.bwith/2)+controls.mx)/2 and not circles.y<my-circles.radius:
			circles.direction = 2
			circles.x_angle += x_angle_change
			circles.y_angle -= y_angle_change
	
		elif bricks.br.colliderect(circles.cr) and circles.x>((controls.mx+bricks.bwith/2)+controls.mx)/2 and circles.x<controls.mx+bricks.bwith/2 and not circles.y<my-circles.radius:
			circles.direction = 2
			circles.x_angle -= x_angle_change
			circles.y_angle += y_angle_change
	
		elif bricks.br.colliderect(circles.cr) and circles.x<((controls.mx+bricks.bwith/2)+bricks.bwith)/2 and not circles.y<my-circles.radius:
			circles.direction = 3
			circles.x_angle -= x_angle_change
			circles.y_angle += y_angle_change
	
		elif bricks.br.colliderect(circles.cr) and circles.x>((controls.mx+bricks.bwith/2)+bricks.bwith)/2 and not circles.y<my-circles.radius:
			circles.direction = 3
			circles.x_angle += x_angle_change
			circles.y_angle -= y_angle_change
	def circle_collide_brs():
		if circles.direction == 0 or circles.direction == 2:
			circles.direction = 1
		elif circles.direction == 1 or circles.direction == 3: 
			circles.direction = 2
		elif circles.direction == 2 or circles.direction == 0: 
			circles.direction = 3
		elif circles.direction == 1 or circles.direction == 3:
			circles.direction = 0


class controls(object):
	mx=12
	"""docstring for controls"""
	def mouse():
		mouse_x , mouse_y = pygame.mouse.get_pos()
		if pygame.mouse.get_pressed()[0] and bricks.br.collidepoint(pygame.mouse.get_pos()):
			bricks.brick(mouse_x-bricks.bwith/2, my,bricks.bwith,20)
			controls.mx = mouse_x-bricks.bwith/2
			##my = mouse_y
	
		else:
			bricks.brick(controls.mx, my,bricks.bwith,20)
	def keyboard():
		keys=pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
		    controls.mx -= 0.5
		if keys[pygame.K_RIGHT]:
		    controls.mx += 0.5


while runn:
	pygame.time.delay(1)
	for event in pygame.event.get():
		if event.type == pygame.QUIT: runn = False
	win.fill((0,0,0))
	controls.mouse()
	controls.keyboard()
	circles.circle_move()
	if circles.y>resolution-circles.radius-1:
		runn = False
	bricks.brickss()
	if len(bricks.brs) == len(bricks.brs_rm): 
		runn = False
	bricks.brs.clear()
	pygame.display.update()
pygame.quit()