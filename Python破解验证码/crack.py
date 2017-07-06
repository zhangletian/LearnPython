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

#①提取文本图片
from PIL import Image
im = Image.open('captcha.gif')
im.convert('P')
#print(im.histogram()) #打印颜色直方图，颜色直方图的每一位数字都代表了在图片中含有对应位的颜色的像素的数量

his = im.histogram()
values = {}
for i in range(256):
	values[i] = his[i]
for j,k in sorted(values.items(),key=lambda x:x[1],reverse=True)[:10]: #只取前10的颜色
	print(j,k)

im2 = Image.new('P',im.size,255)

for x in range(im.size[1]):
	for y in range(im.size[0]):
		pix = im.getpixel((y,x))
		if pix==220 or pix==227: #其中220和227才是我们需要的红色和灰色
			im2.putpixel((y,x),0) #可以通过这一讯息构造一种黑白二值图片
#im2.show()

#②提取单个字符图片，对im2进行纵向切割
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
print(letters) #得到每个字符开始和结束的列序号

#③AI与向量空间图像识别
import math

class VectorCompare():
	#计算矢量大小
	def magnitude(self,concordance):
		total = 0
		for word,count in concordance.iteritems():
			total += count ** 2
		return math.sqrt(total)
	#计算矢量之间的cos值
	def relation(self,concordance1,concordance2):
		relevance = 0
		topvalue = 0
		for word,count in concordance1.items():
			if concordance2.has_key(word):
				topvalue += count * concordance2[word]
		return topvalue / (self.magnitude(concordance1)) * self.magnitude(concorddance2)

#将图片转换为矢量
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

#加载训练集
imageset = []
for letter in iconset:
	for img in os.listdir('./iconset/%s/'%(letter)):
		temp = []
		if img != "Thumbs.db" and img != ".DS_Store":
			temp.append(buildvector(Image.open("./iconset/%s/%s"%(letter,img))))
		imageset.append({letter:temp})


count = 0
#对验证码图片进行切割
for letter in letters:
	m = hashlib.md5()
	im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))

	guess = []

	#将切割得到的验证码小片段与每个训练片段进行比较
	for image in imageset:
		for x,y in image.iteritems():
			if len(y) != 0:
				guess.append( ( v.relation(y[0],buildvector(im3)),x) )

	guess.sort(reverse=True)
	print("",guess[0])
	count += 1

