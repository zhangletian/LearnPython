from PIL import Image

im = Image.open('captcha.gif')
im.convert('P')
im2 = Image.new('P',im.size,255)

for x in range(im.size[1]):
	for y in range(im.size[0]):
		pix = im.getpixel((y,x))
		if pix == 220 or pix == 227:
			im2.putpixel((y,x),0)
#im2.show()

#print(im.histogram)

#his = im.histogram()
#values = {}

#for i in range(256):
	#values[i] = his[i]

#for j,k in sorted(values.items(),key=lambda x:x[1],reverse=True)[:10]:
	#print(j,k)

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
print(letters)
