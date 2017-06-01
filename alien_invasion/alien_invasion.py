#coding=gbk
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf #①直接导入整个模块，所以不用from；②引入别名
from pygame.sprite import Group

def run_game():
	
	"""初始化游戏并创建一个屏幕对象"""
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption('Alien Invation')

	ship = Ship(ai_settings,screen)
	bullets = Group()
	
	#开始游戏的循环
	while True:
		
		##监视键盘和鼠标事件
		#for event in pygame.event.get():
			#if event.type == pygame.QUIT:
				#sys.exit()
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		bullets.update()
		gf.update_screen(ai_settings,screen,ship,bullets)
		
		##每次循环时都将重绘屏幕
		##screen.fill(bg_color)
		#screen.fill(ai_settings.bg_color)
		#ship.blitme()
		
		##让最近绘制的屏幕可见
		#pygame.display.flip()

run_game()
