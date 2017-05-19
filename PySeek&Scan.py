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

#print (enchant.dict_exists("en_US"))		 #Dict chek
#print(enchant.list_languages())

#print(pytesseract.image_to_string(Image.open('C:\\Users\\Marco Borchi\\Desktop\\242.jpg'),lang='ita'))
#print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='ita'))
im = Image.open("Pianura2.jpg") #NOTE: WITH 500X500 IMG NO PROBLEM TO READ THE TEXT
text=''
enchanceIndex=1 #per fare una prova ho visto che da 12 in poi legge bene
w,h=im.size
im.crop((0,0,w,h-250)).save("temp.jpg")
im2=Image.open("temp.jpg")#.convert('L')
#im2.show()
ReadedText=[]
enhancer = ImageEnhance.Contrast(im2)
im2 = im2.filter(ImageFilter.MinFilter(3))
d = enchant.DictWithPWL("en_US","MagicCardName.txt")
while enchanceIndex<=15: #Testing
	
	im2 = enhancer.enhance(enchanceIndex)
	im2 = im2.convert('1')
	#im2.show()
	text =(pytesseract.image_to_string(im2,lang='ita'))
	 #print (text)
	print('\nValore contrasto= ',enchanceIndex)
	enchanceIndex+=1
	if text!='' :
		#ReadedText.append(text)
		print ('\n---------Name of Cards---------\n')
		print ('Testo rilevato ',text)
		print ('Testi suggeriti ',d.suggest(text))
		suggerimenti=d.suggest(text)
		if (len(suggerimenti)>0):
			print('Ricerca...')
			for s in suggerimenti:
				if s==text:
					cardToSearch=s
				else:
					cardToSearch=suggerimenti[0] #quella con maggior probabilità di essere esatta
			
			print ('Cerca -> ',cardToSearch)
			cards=Card.where(name=cardToSearch).all()
			if (len(cards)>0):
				for c in cards:
					print(c.name,' ',c.cmc ,c.colors)
				break
			else:
				cardsITA=Card.where(language="Italian").where(name=cardToSearch).all()
				if (len(cardsITA)>0):
					for c in cardsITA:
						print(c.name,' ',' costo= ',c.cmc ,' colore= ', c.colors)
					break
#Cerca nel dizionario	
#for text in ReadedText:
	
	
	#print ('\n---------Splittati---------\n')
	#for t in text.split(' '):
		#print (t)
		#print (d.suggest(t))
	

#Cerca con le api di magic
#nomes=text.split(' ')
#nomes=ReadedText
#for n in nomes:
	#cards=Card.where(language="Italian").where(name=n).all()

	#for c in cards:
		#print(c.name,' ',c.cmc ,c.colors)	