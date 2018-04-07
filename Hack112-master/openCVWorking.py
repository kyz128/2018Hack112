from collections import deque
import numpy as np
import cv2

redLower= (170,70,50)
redUpper= (180,255,255)
pts= deque(maxlen= 64)

cv2.namedWindow("webcam", cv2.WINDOW_AUTOSIZE)
camera= cv2.VideoCapture(0)

while True:
    (grabbed, frame)= camera.read()
    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask= cv2.inRange(hsv, redLower, redUpper)
    frame= cv2.bitwise_and(frame, frame, mask= mask)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None
 
    
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        M = cv2.moments(c)
        if M["m00"] != 0:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        else: 
            center= (0,0)
    

    pts.appendleft(center)
    # draw trail
    for i in range(1, len(pts)):
        if pts[i - 1] is None or pts[i] is None:
            continue
        cv2.line(frame, pts[i - 1], pts[i], (0, 255, 0), 5)
    
    
    cv2.imshow("webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
camera.release()
cv2.destroyAllWindows()