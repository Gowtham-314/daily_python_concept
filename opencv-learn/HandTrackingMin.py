import cv2
from mediapipe.python.solutions import hands as mpHands
import time

cap = cv2.VideoCapture(1)

hands = mpHands.Hands()


while True:
    success, img = cap.read()
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)