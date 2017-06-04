#coding=gbk
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf #��ֱ�ӵ�������ģ�飬���Բ���from�����������
from pygame.sprite import Group

def run_game():
	
	"""��ʼ����Ϸ������һ����Ļ����"""
	pygame.init()
	#ע����һ�䣺from settings import Settings ������ai_settings
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption('Alien Invation')

	ship = Ship(ai_settings,screen)
	bullets = Group()
	
	#��ʼ��Ϸ��ѭ��
	while True:
		gf.check_events(ai_settings,screen,ship,bullets)#�����ҵ�����
		ship.update()#���·ɴ���λ��
		gf.update_bullets(bullets)#��������δ��ʧ���ӵ���λ��
		gf.update_screen(ai_settings,screen,ship,bullets)#ʹ�ø��º��λ������������Ļ

run_game()
