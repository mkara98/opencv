import cv2

blue = [255,0,0]
green = [0,255,0]
red = [0,0,255]

image = cv2.imread('Photos/opencv.jpg')

Blueconstant = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_CONSTANT,value=blue)
Greenconstant = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_CONSTANT,value=green)
Redconstant = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_CONSTANT,value=red)
REPLICATE = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_REPLICATE)
#TRANSPARENT = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_TRANSPARENT)
REFLECT = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_REFLECT)
WRAP = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_WRAP)
cv2.imshow('constant',Greenconstant)

cv2.waitKey(0)
cv2.destroyAllWindows()