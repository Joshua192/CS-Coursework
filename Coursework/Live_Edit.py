import cv2 #Computer Vision package
import imutils #Image resizig library
import pytesseract #OCR library
import PIL 
pytesseract.pytesseract.tesseract_cmd =r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
image = cv2.imread("license plates\license_plate(2).jpeg")  #Original Image
image = imutils.resize(image, width = 300)  #Resized Image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  #Grayscale Image
bilateral = cv2.bilateralFilter(gray, 11, 17, 17) #Noise Removed
# cv2.imshow(" ", bilateral)


edgeFinder = cv2.Canny(gray, 190, 100)
cnts, new = cv2.findContours(edgeFinder.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

newImage = image.copy()
cv2.drawContours(newImage, cnts, -1, (0, 255,0), 2) #Draws contours on the image

newImage2 = image.copy()
cv2.drawContours(newImage2, cnts, -1, (0, 255,0), 2) #Re Countoured Image
cnts = sorted(cnts, key = cv2.contourArea, reverse=True)[:30]
Edges = cv2.Canny(newImage2, 190, 100)  #Canny Edge Image


#For loop to find the best possible contour of the expected number plate
numberPlateCount = None
count = 0
name = 1
for i in cnts:
    arcLength = cv2.arcLength(i, True)
    approx = cv2.approxPolyDP(i, 0.02*arcLength, True)
# PolyDP is a function used to approximate the curve of a polygon
    if len(approx) == 4:
        numberPlateCount = approx
        x, y, w, h = cv2.boundingRect(i)
        crop_img = bilateral[y:y+h, x:x+w]
        
        cv2.imwrite(str(name)+ '.jpeg', crop_img)
        name +=1
        break
cv2.imshow("Cropped image",crop_img)
#cv2.waitKey(0)
##################################################################################################
blur = cv2.GaussianBlur(crop_img, (3,3), 0)

ret3,thresh = cv2.threshold(blur,180, 225,cv2.THRESH_BINARY)
cv2.imshow("Threshold", thresh) 

# Morph open to remove noise and invert image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
invert = 255 - opening


# Perform text extraction
data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')
print(data.upper())

#cv2.imshow('thresh', thresh)
# #cv2.imshow('opening', opening)
#cv2.imshow('Blurred', blur)
# #cv2.imshow('invert', invert)
cv2.waitKey()
cv2.destroyAllWindows()
###################################################################################################
