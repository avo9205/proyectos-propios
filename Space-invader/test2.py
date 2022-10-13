import pygame,sys


class test(pygame.sprite.Sprite):
	def __init__(self,mario,screen,group):
		super().__init__()
		self.group = group
		self.mario = mario
		self.image = pygame.Surface([10,10])
		self.image.fill((55,1,255))

		self.rect = self.image.get_rect()
		self.rect.centerx = self.mario.mario_rect.centerx
		self.rect.bottom = self.mario.mario_rect.bottom

		self.y = float(self.rect.y)
	
	def update(self):
		self.y -= 1.5	
		self.rect.y = self.y
	def fire_bullets(self):
		self.group.draw(screen)
	

class Mario():
	def __init__(self,screen):
		self.screen = screen
		self.mario = pygame.image.load("pixel_mario.bmp")
		self.mario = pygame.transform.scale(self.mario,(100,100))
		self.mario_rect = self.mario.get_rect()
		self.screen_rect = self.screen.get_rect()
		self.mario_rect.centerx = self.screen_rect.centerx
		self.mario_rect.bottom = self.screen_rect.bottom




move_right= False
move_left = False
		

pygame.init()

screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption("window")

mario = Mario(screen)
group = pygame.sprite.Group()



while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if len(group) < 3:
					prueba = test(mario,screen,group)
					group.add(prueba)
					print(len(group))
			elif event.key == pygame.K_RIGHT:
				move_right = True	
			elif event.key == pygame.K_LEFT:
				move_left = True

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				move_right = False	
			elif event.key == pygame.K_LEFT:
				move_left = False		

	
	if move_right:
		mario.mario_rect.centerx += 1

	if move_left:
		mario.mario_rect.centerx -= 1				


	group.update()

	for gr in group.copy():
		if gr.rect.bottom <= 0:
			group.remove(gr)

	print(len(group))		

	screen.fill((255,255,255))
	
	
	


	for bullet in group.sprites():
		bullet.fire_bullets()

	screen.blit(mario.mario,mario.mario_rect)	

	pygame.display.flip()		