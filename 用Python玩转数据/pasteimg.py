from PIL import Image

im1 = Image.open('1.jpg')
print(im1.size,im1.format,im1.mode)
Image.open('1.jpg').save('2.png')
im2 = Image.open('2.png')
size = (640,360)
im2.thumbnail(size)
out = im2.rotate(45)
im1.paste(out,(50,50))
