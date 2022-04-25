import cv2
img= cv2.imread('Photos/saat.jpg')

img[80,80]=[255,255,255]

bolge=img[30:120,100:200]
img[0:90,0:100]=bolge
print(img.shape)
cv2.rectangle(img,(100,30),(200,120),(0,255,225))
cv2.rectangle(img,(0,0),(300,168),(255,0,0))
cv2.rectangle(img,(0,0),(100,90),(0,0,255))
cv2.imshow('saat',img)
cv2.imshow('saat2',bolge)
cv2.waitKey(0)
cv2.destroyAllWindows()