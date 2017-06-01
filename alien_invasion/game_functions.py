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
	"""������Ļ�ϵ�ͼ�񣬲��л�������Ļ"""
	screen.fill(ai_settings.bg_color) #��䱳��ɫ
	ship.blitme() #�÷ɴ����Ƶ���Ļ��
	pygame.display.flip()
