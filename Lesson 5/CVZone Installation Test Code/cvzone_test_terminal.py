# test_cvzone.py
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import numpy as np

# Check versions (CVZone doesn't have __version__ attribute)
try:
    print("CVZone version:", cvzone.__version__)
except AttributeError:
    print("CVZone imported successfully (version not available)")

print("OpenCV version:", cv2.__version__)

# Test basic functionality
detector = HandDetector()
print("Hand detector initialized successfully!")

# Test camera (optional - comment out if no camera)
# cap = cv2.VideoCapture(0)
# success, img = cap.read()
# if success:
#     print("Camera test successful!")
#     hands, img = detector.findHands(img)
#     print(f"Detected {len(hands)} hands")
# cap.release()

print("CVZone installation test completed successfully!")