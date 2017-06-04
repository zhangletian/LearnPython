#coding=gbk
import sys
import pygame
from bullet import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
	"""��Ӧ����"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)

def fire_bullet(ai_settings,screen,ship,bullets):
	"""�����û�дﵽ�������ƣ��ͷ���һ���ӵ�"""
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)
		
def check_keyup_events(event,ship):
	"""��Ӧ�ɿ�"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN: #һ��KEYDOWN
			check_keydown_events(event,ai_settings,screen,ship,bullets)
						
		elif event.type == pygame.KEYUP: #һ��KEYUP
			check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship,bullets):
	"""������Ļ�ϵ�ͼ�񣬲��л�������Ļ"""
	screen.fill(ai_settings.bg_color) #��䱳��ɫ
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme() #�÷ɴ����Ƶ���Ļ��
	pygame.display.flip()

def update_bullets(bullets):
	"""�����ӵ���λ�ã���ɾ������ʧ���ӵ�"""
	bullets.update()
	#ɾ������ʧ���ӵ�
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
		#print(len(bullets))
