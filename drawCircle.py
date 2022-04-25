import cv2
import numpy as np

down = []
up = []
# mouse callback function
def draw_circle(event,x,y,flags,param):

    if event == cv2.EVENT_LBUTTONDOWN:
        down.append(x)
        down.append(y)
        #cv2.line(img, (x, y), (x + 50, y + 50),(0, 0, 255),5)
        # draw rectangle
        #cv2.rectangle(img, (x, y), (x + 50, y + 50),(0, 255, 0),5)
        # draw circle
        cv2.circle(img, (x, y), 25, (0, 0, 0),3)
        cv2.circle(img, (x+30, y+25), 25, (0, 255, 0),3)
        cv2.circle(img, (x-30, y+25), 25, (0, 255, 255), 3)
        cv2.circle(img, (x+60, y), 25, (0, 0, 255), 3)
        cv2.circle(img, (x-60, y), 25, (255, 0, 0), 3)

    elif event == cv2.EVENT_LBUTTONUP:
        up.append(x)
        up.append(y)
    #draw line



img = cv2.imread('Photos/beyaz.jpg')
img= cv2.resize(img,(480,480))
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k= cv2.waitKey(1)
    if(k%256==27):
        break
    elif(k%256==32):
        name = input("Name?")
        cv2.imwrite("{}.jpg".format(name),img)
    elif(k%256)== 82:
        img=cv2.imread('beyaz.jpg')
        img= cv2.resize(img,(480,480))


print(down)
print(up)