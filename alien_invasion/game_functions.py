#coding=gbk
import sys
import pygame
from bullet import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
	"""响应按键"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)

def fire_bullet(ai_settings,screen,ship,bullets):
	"""如果还没有达到数量限制，就发射一颗子弹"""
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)
		
def check_keyup_events(event,ship):
	"""响应松开"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN: #一个KEYDOWN
			check_keydown_events(event,ai_settings,screen,ship,bullets)
						
		elif event.type == pygame.KEYUP: #一个KEYUP
			check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship,bullets):
	"""更新屏幕上的图像，并切换到新屏幕"""
	screen.fill(ai_settings.bg_color) #填充背景色
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme() #让飞船绘制到屏幕上
	pygame.display.flip()

def update_bullets(bullets):
	"""更新子弹的位置，并删除已消失的子弹"""
	bullets.update()
	#删除已消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
		#print(len(bullets))
