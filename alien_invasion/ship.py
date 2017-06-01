#coding=gbk

import pygame

class Ship():
	"""��ʼ���ɴ����������ʼλ��"""
	def __init__(self,ai_settings,screen):
		self.screen = screen #screenָ����Ҫ���ɴ����Ƶ�ʲô�ط�
		self.ai_settings = ai_settings
		
		#���طɴ�ͼ�񲢻�ȡ����Ӿ���
		self.image = pygame.image.load('images/ship.bmp') #����ͼ�񲢷���һ����ʾ�ɴ���surface���������surface�洢��self.image��
		self.rect = self.image.get_rect() #��get_rect()��ȡ��Ӧsurface������rect
		self.screen_rect = screen.get_rect() #����ʾ��Ļ�ľ��δ洢��self.screen_rect��
		
		#��ÿ���·ɴ�������Ļ�ײ�����
		self.rect.centerx = self.screen_rect.centerx #�ٽ�self.rect.centerx���ɴ����ĵ�x���꣩����Ϊ��ʾ��Ļ�ľ��ε�����centerx
		self.rect.bottom = self.screen_rect.bottom #����self.rect.bottom���ɴ��±�Ե��y���꣩����Ϊ��ʾ��Ļ�ľ��ε�����bottom
		self.center = float(self.rect.centerx) #�ڷɴ�������center�д洢С��ֵ
		#�ƶ���־
		self.moving_right = False
		self.moving_left = False
	
	def update(self):
		"""�����ƶ���־�����ɴ���λ��"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			#self.rect.centerx += 1
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			#self.rect.centerx -= 1
			self.center -= self.ai_settings.ship_speed_factor
		
		self.rect.centerx = self.center
	
	def blitme(self): 
		"""���ƶ�λ�����ɴ�"""
		self.screen.blit(self.image,self.rect)
