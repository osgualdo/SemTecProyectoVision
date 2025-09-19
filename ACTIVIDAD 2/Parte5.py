import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    edges = cv2.Canny(frame, 100, 200)
    cv2.imshow('Canny Edge Detection', edges)
    if cv2.waitKey(1) & 0xFF == ord('q'): # Press 'q' to exit
        break
cap.release()
cv2.destroyAllWindows()