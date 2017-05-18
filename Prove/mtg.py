from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog
import csv
import json
#Card.where(language="Italian")



#cards = Card.where(language="Italian").where(set='ktk').where(subtypes='warrior,human').all()
#for c in cards:
	#print(c.name,' ',c.cmc ,c.colors)	
print ('Ricerca in corso...')	

cardss=Card.all()
textFile=open('magicTest.txt',wb)
print('Scrittura su file')
for c in cardss:
	#print(c.name)
	textFile.writelines(c.name)
textFile.close()
print ('Fine')