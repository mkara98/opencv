import cv2

messi = cv2.imread('Photos/messi.jpg')

#blue delete
#messi[ :,:,0]=0
#Green delete
#messi[ :,:,1]=0
#red delete
# messi[ :,:,2]=0
#blue filter
#messi[:,:,0] =255
#green filter
#messi[:,:,1] =255
#red filter
messi[:,:,2] =255
cv2.imshow('filter',messi)
cv2.waitKey(0)
cv2.destroyAllWindows()