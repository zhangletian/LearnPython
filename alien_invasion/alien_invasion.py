#coding=gbk
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf #��ֱ�ӵ�������ģ�飬���Բ���from�����������

def run_game():
	
	"""��ʼ����Ϸ������һ����Ļ����"""
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption('Alien Invation')

	ship = Ship(ai_settings,screen)
	
	#��ʼ��Ϸ��ѭ��
	while True:
		
		##���Ӽ��̺�����¼�
		#for event in pygame.event.get():
			#if event.type == pygame.QUIT:
				#sys.exit()
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings,screen,ship)
		
		##ÿ��ѭ��ʱ�����ػ���Ļ
		##screen.fill(bg_color)
		#screen.fill(ai_settings.bg_color)
		#ship.blitme()
		
		##��������Ƶ���Ļ�ɼ�
		#pygame.display.flip()

run_game()
