#coding=gbk
import sys
import pygame

def check_events(ship):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = True
			elif event.key == pygame.K_LEFT:
				ship.moving_left = True
						
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = False
			elif event.key == pygame.K_LEFT:
				ship.moving_left = False

def update_screen(ai_settings,screen,ship):
	"""更新屏幕上的图像，并切换到新屏幕"""
	screen.fill(ai_settings.bg_color) #填充背景色
	ship.blitme() #让飞船绘制到屏幕上
	pygame.display.flip()
