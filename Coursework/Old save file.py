import cv2 #Computer Vision package
import imutils #Image resizig library
import pytesseract #OCR library
import PIL 
pytesseract.pytesseract.tesseract_cmd =r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

# The imread function takes the location of the binary image and reads the image 
# Resize the Original Image
image = cv2.imread("license plates\license_plate(3).jpeg")

image = imutils.resize(image, width = 300)
### cv2.imshow("Original", image)
# cv2.waitKey(0)

# Converts the image into grayscale to reduce image complexity.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Grayscale", gray)
#cv2.waitKey(0)

# Use bilateral filter function to remove noise from the image
bilateral = cv2.bilateralFilter(gray, 11, 17, 17)
### cv2.imshow("Noise Removal", bilateral)
#cv2.waitKey(0)

# The Canny method is used to detect the 'edges' of an image
edgeFinder = cv2.Canny(gray, 190, 100)
#cv2.imshow("Canny Edge", edgeFinder)
#cv2.waitKey(0)

# Finding the contours of the image

cnts, new = cv2.findContours(edgeFinder.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# cnts -> contours, a curve joining all the continous points along an edge (boundary of the same colour intensity)
# RETR_LIST -> Collects all the contour data but doesn't create any parent-child relationships between points
# CHAIN_APPROX_SIMPLE -> Compresses the contour and  saves memory by removing redundant points.

newImage = image.copy()
cv2.drawContours(newImage, cnts, -1, (0, 255,0), 2) #Draws contours on the image
#cv2.imshow("Contoured Image", newImage)
#cv2.waitKey(0)

# In order to highlight the sections of the image containing the license plate, 
# the contours will need to be divided, grouped, and sorted.
cnts = sorted(cnts, key = cv2.contourArea, reverse=True)[:30]
numberPlateCount = None

# To get the contours associated with the plate, an edited copy of the original image needs to be made
newImage2 = image.copy()
cv2.drawContours(newImage2, cnts, -1, (0, 255,0), 2)
### cv2.imshow("Re-contoured Image ", newImage2)
#cv2.waitKey(0)


Edges = cv2.Canny(newImage2, 190, 100)
#cv2.imshow("Canny Edge 2.0", Edges)
#cv2.waitKey(0)


# running a for loop to find the best possible contour of the expected number plate
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

cv2.drawContours(image,[numberPlateCount], -1,(0, 255, 0), 3)
### cv2.imshow("Final Image", image)
### cv2.waitKey(0)

# print(crop_img)
# crop_img_loc = "1.png"
cv2.imshow("Cropped Image",crop_img)
# cv2.waitKey(0)

print(type(crop_img))
if crop_img.size ==0:
    print("Image size = 0")
else:
    print("Image size is > 0")


# cv2.imread(crop_img)
text = pytesseract.image_to_string(crop_img, lang="eng")
print("The license plate is: ", text)
cv2.waitKey(0)
