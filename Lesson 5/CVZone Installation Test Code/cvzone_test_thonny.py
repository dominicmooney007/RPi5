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

print("CVZone installation test completed successfully!")