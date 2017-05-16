from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
#print(pytesseract.image_to_string(Image.open('C:\\Users\\Marco Borchi\\Desktop\\242.jpg'),lang='ita'))
#print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='ita'))
im = Image.open("Montagna.jpg")

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
im2 = enhancer.enhance(5)
im2 = im2.convert('1')
im2.show()
text =(pytesseract.image_to_string(im2,lang='ita'))
print (text)
