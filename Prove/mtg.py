from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog
import csv
import json
#Card.where(language="Italian")



cards = Card.where(language="Italian").where(set='ktk').where(subtypes='warrior,human').all()
for c in cards:
	print(c.name,' ',c.cmc ,c.colors)	
	

cardss=Card.where(language="Italian").where(name='fulmine').all()

for c in cardss:
	print(c.name,' ',c.cmc ,c.colors)	