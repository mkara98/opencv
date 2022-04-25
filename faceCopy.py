import cv2


#This program takes the snap of video
# and detect the face. Then copy all faces in target image


camera= cv2.VideoCapture(0)
while(1):
    _,frame = camera.read()
    cv2.imshow("Snap",frame)

    press = cv2.waitKey(1) % 256

    if(press)== 32:                   #press space tab
        name= input("Kayıt")              #name of snap with jpg format
        fileName = "{}.jpg".format(name)
        cv2.imwrite(fileName,frame)
        break
file= cv2.imread(fileName)
source = cv2.imread("Photos/yuz.jpg")
target= cv2.imread("Photos/kalabalik.jpg")
white = cv2.imread("beyaz.jpg")
face = cv2.CascadeClassifier('haarcascade-frontalface-default.xml')

snapGray = cv2.cvtColor(file,cv2.COLOR_BGR2GRAY)                     #All image returned Bgr to gray
sourceGray= cv2.cvtColor(source,cv2.COLOR_BGR2GRAY)                  # which is easier in image processing
targetGray= cv2.cvtColor(target,cv2.COLOR_BGR2GRAY)
fileFaces =  face.detectMultiScale(snapGray,1.1,4)                   #Detect face on the image with Haarcascade
sourceFaces = face.detectMultiScale(sourceGray,1.1,4)
targetFaces = face.detectMultiScale(targetGray,1.1,4)
white = cv2.resize(white, (480,640))                                  #Copying area of source's face
for(x,y,w,h) in fileFaces :
        #cv2.rectangle(source,(x,y),(x+w,y+h),(255,0,0))
        white[y:y+h,x:x+w] = file[y:y+h,x:x+w]
        white1= white[y:y+h,x:x+w]
for(x,y,w,h) in targetFaces:
    #cv2.rectangle(target,(x,y),(x+w,y+h),(255,0,0))
    white2=cv2.resize(white1,(h,w))
    target[y:y+h,x:x+w]=white2
target= cv2.resize(target,(880,440))
cv2.imshow("Source",source)
cv2.imshow("face",white1)
cv2.imshow("Target",target)
cv2.imwrite("Photos/Target.jpg", target)
cv2.waitKey(0)
cv2.destroyAllWindows()