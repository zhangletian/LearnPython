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
	#注意这一句：from settings import Settings 并赋给ai_settings
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption('Alien Invation')

	ship = Ship(ai_settings,screen)
	bullets = Group()
	
	#开始游戏的循环
	while True:
		gf.check_events(ai_settings,screen,ship,bullets)#检查玩家的输入
		ship.update()#更新飞船的位置
		gf.update_bullets(bullets)#更新所有未消失的子弹的位置
		gf.update_screen(ai_settings,screen,ship,bullets)#使用更新后的位置来绘制新屏幕

run_game()
