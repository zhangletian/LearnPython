#coding=gbk

import pygame

class Ship():
	"""��ʼ���ɴ����������ʼλ��"""
	def __init__(self,screen):
		self.screen = screen #screenָ����Ҫ���ɴ����Ƶ�ʲô�ط�
		
		#���طɴ�ͼ�񲢻�ȡ����Ӿ���
		self.image = pygame.image.load('images/ship.bmp') #����ͼ�񲢷���һ����ʾ�ɴ���surface���������surface�洢��self.image��
		self.rect = self.image.get_rect() #��get_rect()��ȡ��Ӧsurface������rect
		self.screen_rect = screen.get_rect() #����ʾ��Ļ�ľ��δ洢��self.screen_rect��
		
		#��ÿ���·ɴ�������Ļ�ײ�����
		self.rect.centerx = self.screen_rect.centerx #�ٽ�self.rect.centerx���ɴ����ĵ�x���꣩����Ϊ��ʾ��Ļ�ľ��ε�����centerx
		self.rect.bottom = self.screen_rect.bottom #����self.rect.bottom���ɴ��±�Ե��y���꣩����Ϊ��ʾ��Ļ�ľ��ε�����bottom
	
	def blitme(self): 
		"""���ƶ�λ�����ɴ�"""
		self.screen.blit(self.image,self.rect)
