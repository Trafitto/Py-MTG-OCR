from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
#print(pytesseract.image_to_string(Image.open('C:\\Users\\Marco Borchi\\Desktop\\242.jpg'),lang='ita'))
#print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='ita'))
im = Image.open("goblin.jpg")
text=''
enchanceIndex=1
#im = im.filter(ImageFilter.MedianFilter())
#enhancer = ImageEnhance.Contrast(im)
#im = enhancer.enhance(2)
#im = im.convert('1')
#im.save('temp2.jpg')
#im2=Image.open('temp2.jpg')
w,h=im.size
im.crop((0,0,w,h-350)).save("temp.jpg")
im2=Image.open("temp.jpg")#.convert('L')
#im2.show()
enhancer = ImageEnhance.Contrast(im2)
im2 = im2.filter(ImageFilter.MinFilter(3))
while True: #Testing
	
	im2 = enhancer.enhance(enchanceIndex)
	im2 = im2.convert('1')
	im2.show()
	text =(pytesseract.image_to_string(im2,lang='ita'))
	print (text)
	print(enchanceIndex)
	enchanceIndex+=1
	
if text=='':
	text='none'
nomes=text.split(' ')
for n in nomes:
	cards=Card.where(language="Italian").where(name=n).all()

	for c in cards:
		print(c.name,' ',c.cmc ,c.colors)	