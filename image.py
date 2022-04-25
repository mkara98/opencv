import cv2

camera = cv2.VideoCapture(0)
while(1):
    _,frame= camera.read()
    cv2.imshow("Camera",frame)

    k= cv2.waitKey(1)
    if k %256 == 32:
        cv2.imwrite("camera.jpg",frame)
        break
camera.release()
image= cv2.imread("camera.jpg")

cv2.imshow("SS",image)
Gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
Gaussian = cv2.GaussianBlur(image,(7,7),100)
Canny = cv2.Canny(image,150,100)
Cool = cv2.applyColorMap(image,cv2.COLORMAP_COOL)
Hot = cv2.applyColorMap(image,cv2.COLORMAP_HOT)
AUTUMN = cv2.applyColorMap(image,cv2.COLORMAP_AUTUMN)
Ocean = cv2.applyColorMap(image,cv2.COLORMAP_OCEAN)
Hsv = cv2.applyColorMap(image,cv2.COLORMAP_HSV)
Jet = cv2.applyColorMap(image,cv2.COLORMAP_JET)
Parula = cv2.applyColorMap(image,cv2.COLORMAP_PARULA)
Rainbow = cv2.applyColorMap(image,cv2.COLORMAP_RAINBOW)
Pink = cv2.applyColorMap(image,cv2.COLORMAP_PINK)


print(image.shape)
print(Gray.shape)
cv2.imshow("Blur SS",Gaussian)
cv2.imshow("Canny",Canny)
cv2.imshow("Cool",Cool)
cv2.imshow("Hot",Hot)
cv2.imshow("AUTUMN",AUTUMN)
cv2.imshow("Ocean",Ocean)
cv2.imshow("Hsv",Hsv)
cv2.imshow("Jet",Jet)
cv2.imshow("Parula",Parula)
cv2.imshow("Rainbow",Rainbow)
cv2.imshow("Pink",Pink)


cv2.waitKey(0)

cv2.destroyAllWindows()