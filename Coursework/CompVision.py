import cv2 #Computer Vision package
import imutils #Image resizig library
import pytesseract #OCR library

pytesseract.pytesseract.tesseract_cmd =r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

#The imread function takes the location of the binary immage and reads the image 
#Resize the Original Image
image = cv2.imread("license plates\license_plate(3).jpeg")
image = imutils.resize(image, width = 400, height= 300)
cv2.imshow("Original", image)
cv2.waitKey(0)

#Converts the image into grayscale to reduce image complexity.
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Grayscale", grayscale)
# cv2.waitKey(0)

#Use bilateral filter function to remove noise from the image
place_holder = cv2.bilateralFilter(grayscale, 11, 17, 17)
# cv2.imshow("Noise Removal", place_holder)
# cv2.waitKey(0)

#The Canny method is used to detect the 'edges' of an image
edgeFinder = cv2.Canny(grayscale, 100, 200)
# cv2.imshow("Canny Edge", edgeFinder)
# cv2.waitKey(0)

#Finding the contours of the image
cnts, new = cv2.findContours(edgeFinder.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#cnts -> contours, a curve joining all the continous points along an edge (boundary of the same colour intensity)
#RETR_LIST -> Collects all the contour data but doesn't create any parent-child relationships between points
#CHAIN_APPROX_SIMPLE -> Compresses the contour and  saves memory by removing redundant points.

newImage = image.copy()
cv2.drawContours(newImage, cnts, -1, (0, 255,0), 2)# Draws contours on the image
cv2.imshow("Contoured Image", newImage)
cv2.waitKey(0)

#In order to highlight the sections of the image containing the license plate, 
#the contours will need to be divided, grouped, and sorted on the basis of **what the area contains**
#Then the sections with the maximum 
cnts = sorted(cnts, key = cv2.contourArea, reverse=True)[:30]
numberPlateCount = None

#To get the contours associated with the plate, an edited copy of the original image needs to be made
newImage2 = image.copy()
cv2.drawContours(newImage2, cnts, -1, (0, 255,0), 2)
cv2.imshow("Re-contoured Image ", newImage2)
cv2.waitKey(0)

#running a for loop to find the best possible contour of the expected number plate
conut = 0
name = 1
for i in cnts:
    arcLength = cv2.arcLength(i, True)
    approx = cv2.approxPolyDP(i, 0.02*arcLength, True) #PolDP is a function used to calculate the curve of a 
    if len(approx) == 4:

