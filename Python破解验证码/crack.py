#coding=gbk
#from PIL import Image

#im = Image.open('captcha.gif')
#im.convert('P')
#im2 = Image.new('P',im.size,255)

#for x in range(im.size[1]):
	#for y in range(im.size[0]):
		#pix = im.getpixel((y,x))
		#if pix == 220 or pix == 227:
			#im2.putpixel((y,x),0)
##im2.show()

##print(im.histogram)

##his = im.histogram()
##values = {}

##for i in range(256):
	##values[i] = his[i]

##for j,k in sorted(values.items(),key=lambda x:x[1],reverse=True)[:10]:
	##print(j,k)

#inletter = False
#foundletter = False

#start = 0
#end = 0
#letters = []

#for y in range(im2.size[0]):
	#for x in range(im2.size[1]):
		#pix = im2.getpixel((y,x))
		#if pix != 255:
			#inletter = True
	#if foundletter == False and inletter == True:
		#foundletter = True
		#start = y
	#if foundletter == True and inletter == False:
		#foundletter = False
		#end = y
		#letters.append((start,end))
	#inletter = False
#print(letters)

#����ȡ�ı�ͼƬ
from PIL import Image
im = Image.open('captcha.gif')
im.convert('P')
#print(im.histogram()) #��ӡ��ɫֱ��ͼ����ɫֱ��ͼ��ÿһλ���ֶ���������ͼƬ�к��ж�Ӧλ����ɫ�����ص�����

his = im.histogram()
values = {}
for i in range(256):
	values[i] = his[i]
for j,k in sorted(values.items(),key=lambda x:x[1],reverse=True)[:10]: #ֻȡǰ10����ɫ
	print(j,k)

im2 = Image.new('P',im.size,255)

for x in range(im.size[1]):
	for y in range(im.size[0]):
		pix = im.getpixel((y,x))
		if pix==220 or pix==227: #����220��227����������Ҫ�ĺ�ɫ�ͻ�ɫ
			im2.putpixel((y,x),0) #����ͨ����һѶϢ����һ�ֺڰ׶�ֵͼƬ
#im2.show()

#����ȡ�����ַ�ͼƬ����im2���������и�
inletter = False
foundletter = False
start = 0
end = 0
letters = []

for y in range(im2.size[0]):
	for x in range(im2.size[1]):
		pix = im2.getpixel((y,x))
		if pix != 255:
			inletter = True
	if foundletter == False and inletter == True:
		foundletter = True
		start = y
	if foundletter == True and inletter == False:
		foundletter = False
		end = y
		letters.append((start,end))
	inletter = False
print(letters) #�õ�ÿ���ַ���ʼ�ͽ����������

#��AI�������ռ�ͼ��ʶ��
import math

class VectorCompare():
	#����ʸ����С
	def magnitude(self,concordance):
		total = 0
		for word,count in concordance.iteritems():
			total += count ** 2
		return math.sqrt(total)
	#����ʸ��֮���cosֵ
	def relation(self,concordance1,concordance2):
		relevance = 0
		topvalue = 0
		for word,count in concordance1.items():
			if concordance2.has_key(word):
				topvalue += count * concordance2[word]
		return topvalue / (self.magnitude(concordance1)) * self.magnitude(concorddance2)

#��ͼƬת��Ϊʸ��
import os
import hashlib
import time

def buildvector(im):
	d1 = {}
	count = 0
	for i in im.getdata():
		d1[count] = i
		count += 1
	return d1

v = VectorCompare()

iconset = ['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#����ѵ����
imageset = []
for letter in iconset:
	for img in os.listdir('./iconset/%s/'%(letter)):
		temp = []
		if img != "Thumbs.db" and img != ".DS_Store":
			temp.append(buildvector(Image.open("./iconset/%s/%s"%(letter,img))))
		imageset.append({letter:temp})


count = 0
#����֤��ͼƬ�����и�
for letter in letters:
	m = hashlib.md5()
	im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))

	guess = []

	#���и�õ�����֤��СƬ����ÿ��ѵ��Ƭ�ν��бȽ�
	for image in imageset:
		for x,y in image.iteritems():
			if len(y) != 0:
				guess.append( ( v.relation(y[0],buildvector(im3)),x) )

	guess.sort(reverse=True)
	print("",guess[0])
	count += 1

