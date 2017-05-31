#coding=gbk

import pygame

class Ship():
	"""初始化飞船并设置其初始位置"""
	def __init__(self,screen):
		self.screen = screen #screen指定了要将飞船绘制到什么地方
		
		#加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('images/ship.bmp') #加载图像并返回一个表示飞船的surface，并将这个surface存储到self.image中
		self.rect = self.image.get_rect() #用get_rect()获取相应surface的属性rect
		self.screen_rect = screen.get_rect() #将表示屏幕的矩形存储到self.screen_rect中
		
		#将每艘新飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx #再将self.rect.centerx（飞船中心的x坐标）设置为表示屏幕的矩形的属性centerx
		self.rect.bottom = self.screen_rect.bottom #并将self.rect.bottom（飞船下边缘的y坐标）设置为表示屏幕的矩形的属性bottom
	
	def blitme(self): 
		"""在制定位置描绘飞船"""
		self.screen.blit(self.image,self.rect)
