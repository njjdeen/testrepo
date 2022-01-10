'''

couple of exercises to get familiar with working with images

'''

from PIL import Image

mac = Image.open('example.jpg')

#mac.show()

mac.resize(3000,500)

pencils = Image.open('pencils.jpg')
print(pencils.size)


x=0
y=0

w = 1950/3
h = 1300/10

cropped_pencils = pencils.crop((x,y,w,h))

cropped_pencils.show()

