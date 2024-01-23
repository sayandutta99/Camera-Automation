import cv2
cam = cv2.VideoCapture(10)
while cam.isOpened():
    ret, frame=cam.read()
    if cv2.waitKey(100) == ord('q'):
        break
    cv2.imshow('Sayan Cam', frame)