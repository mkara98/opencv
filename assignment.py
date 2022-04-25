import cv2
import numpy as np

orijinal_image=cv2.imread('assignment.jpg')
#cv2.imshow('ass',image)
siyah = cv2.imread("beyaz.jpg")
image1Array= []
image2Array= []
image3Array= []
def array(image,x,y,arrayName,color):
    for i in range(x):
        for j in range(int(y / 3)):
            arrayName.append(image.item(j, i, color))
def itemSet(image,x,y,color,array):
    for i in range(x):
        for j in range(int(y / 3)):
            image.itemset((j,i,color),array[(i*j) + j])


yAxis,xAxis,channel = orijinal_image.shape

image1= orijinal_image[0:int(yAxis/3),0:xAxis]
image2= orijinal_image[int(yAxis/3):2*int(yAxis/3),0:xAxis]
image3= orijinal_image[2*int(yAxis/3):yAxis-1,0:xAxis]
siyah1 = cv2.resize(siyah,(401,341))
print(image1.shape)
print(siyah.shape)
array(image1,xAxis,yAxis,image1Array,0)
array(image2,xAxis,yAxis,image2Array,1)
array(image3,xAxis,yAxis,image3Array,2)
#print(image1.item(340,400,0))
print(image1Array[3080],image2Array[3080],image3Array[3080])

itemSet(siyah1,xAxis,yAxis,0,image1Array)
itemSet(siyah1,xAxis,yAxis,1,image2Array)
itemSet(siyah1,xAxis,yAxis,2,image3Array)




cv2.imshow('image',image1)
cv2.imshow('image1',image2)
cv2.imshow('image2',image3)
cv2.imshow('siyah',siyah1)


cv2.waitKey(0)
cv2.destroyAllWindows()