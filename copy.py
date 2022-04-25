import cv2
import numpy as np

messi = cv2.imread('Photos/messi.jpg')
#cv2.imshow('messi',messi)
top = cv2.imread('Photos/top.jpg')
cv2.imshow('top',top)
dimension= (53,55)
top= cv2.resize(top,dimension)
cv2.imshow('top2',top)
image=messi[305:390,272:325]
print(top.shape)
print(image.shape)
#cv2.imshow('image',image)
messi[305:390,172:225] = image
messi[305:390,272:325] = top
cv2.imshow('messi',messi)
cv2.waitKey(0)
cv2.destroyAllWindows()