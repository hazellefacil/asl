import cv2 

cap = cv2.VideoCapture(0)

_, frame = cap.read()
h, w, c = frame.shape

while cap.isOpened():
    _, frame = cap.read()

    cv2.imshow("you!",frame)

    #break when ESC is pressed 
    k = cv2.waitKey(1)
    if k%256 == 27:
        break

cap.release()
cv2.destroyAllWindows()
