import cv2
import pytesseract
from pdf2image import convert_from_path

pages = convert_from_path('output.pdf', 500)
for page in pages:
	page.save('out.png', 'PNG')

def ocr_core(img):
	text = pytesseract.image_to_string(img)
	return text

img = cv2.imread('out.png')

print(ocr_core(img))
