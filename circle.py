import cv2

camera= cv2.VideoCapture(0)

while(1):
    _,frame = camera.read()
    for i in range(0,frame.shape[1],10):

        cv2.circle(frame, (i, i), (10), (255-i % 255, i %255, i+125 %255),3)
        cv2.imshow('ss', frame)

    print(frame.shape)

    k=cv2.waitKey(1)

    if k% 256 == 27:
        break

camera.release()
cv2.destroyAllWindows()
