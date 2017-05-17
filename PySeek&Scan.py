from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog
import enchant
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
#print(pytesseract.image_to_string(Image.open('C:\\Users\\Marco Borchi\\Desktop\\242.jpg'),lang='ita'))
#print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='ita'))
im = Image.open("goblinENG.jpg") #NOTE: WITH 500X500 IMG NO PROBLEM TO READ THE TEXT
text=''
enchanceIndex=1
w,h=im.size
im.crop((0,0,w,h-250)).save("temp.jpg")
im2=Image.open("temp.jpg")#.convert('L')
#im2.show()
ReadedText=[]
enhancer = ImageEnhance.Contrast(im2)
im2 = im2.filter(ImageFilter.MinFilter(3))
while enchanceIndex<=20: #Testing
	
	im2 = enhancer.enhance(enchanceIndex)
	im2 = im2.convert('1')
	im2.show()
	text =(pytesseract.image_to_string(im2,lang='ita'))
	 #print (text)
	print(enchanceIndex)
	enchanceIndex+=1
	if text!='' :
		ReadedText.append(text)
d = enchant.request_dict("en_US")
	
#Cerca nel dizionario	
for text in ReadedText:
	print (text)
	
	for t in text.split(' '):
		print (d.suggest(t))
	

#Cerca con le api di magic
#nomes=text.split(' ')
nomes=ReadedText
for n in nomes:
	cards=Card.where(language="Italian").where(name=n).all()

	for c in cards:
		print(c.name,' ',c.cmc ,c.colors)	