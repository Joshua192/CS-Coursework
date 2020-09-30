import cv2
import PIL
import numpy as np
import pytesseract

crop_img = 1 ######
##################################################################################################
blur = cv2.GaussianBlur(crop_img, (3,3), 0)
thresh = cv2.threshold(blur, 0, 251, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

ret3,thresh1 = cv2.threshold(blur,100,255,cv2.THRESH_BINARY)
#cv2.imshow("Thresh 1", thresh1) 

# Morph open to remove noise and invert image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
invert = 255 - opening


# Perform text extraction
data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')
print(data)

#cv2.imshow('thresh', thresh)
# #cv2.imshow('opening', opening)
#cv2.imshow('Blurred', blur)
# #cv2.imshow('invert', invert)
#cv2.waitKey()
cv2.destroyAllWindows()
###################################################################################################