import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
im = cv2.imread('Images/B9n3s.png')
# Perhaps there is a better config
text = pytesseract.image_to_string(im, config='-l eng --oem 3 --psm 3')
# After printing, it seems to recognize the small image as an @ symbol, and tries to recognize the box around B as a
# line. It also didn't capitalize A, and didn't recognize the last line, however, it got the first to third
# lines mostly correct.
print(text)
