import cv2

counter=0
def open(FileName,counter1=counter):
    image = cv2.imread(FileName)
    name = "File_{}".format(counter1)
    cv2.imshow(name,image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



open('Photos/messi.jpg')
counter+=1
open("Photos/gri.jpg")
counter+=1
open("Photos/opencv.jpg")
counter+=1
open("Photos/siyah.jpg")
