import cv2
import numpy as np

kamera= cv2.VideoCapture(0)
img_counter=0
while(1):
    ret, frame=kamera.read()

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    kenarlar=cv2.Canny(frame,100,150)




    cv2.imshow('orjinal',frame)
    cv2.imshow('kenarlar', kenarlar)

    k = cv2.waitKey(1)

    if k % 256 == 27:
        # ESC pressed

        break
    elif k % 256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

kamera.release()
cv2.destroyAllWindows()