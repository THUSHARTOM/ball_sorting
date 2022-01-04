import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Frame',frame)
        cv2.waitKey(1)
    else:
        break

cap.release()
cv2.destroyAllWindows
