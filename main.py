import cv2 
import pytesseract

img = cv2.imread('img.jpg')
# Adding custom options
custom_config = r'--oem 3 --psm 6'

text = pytesseract.image_to_string(img, lang='eng', config=custom_config)
# write the text to a file
with open('text.txt', 'w') as f:
    f.write(text)
print(text)