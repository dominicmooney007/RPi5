from cvzone.HandTrackingModule import HandDetector
import cv2
from gpiozero import LED
import cvzone

# Initialize LED on GPIO pin 17 (you can change this to any available GPIO pin)
led = LED(17)

# Initialize the webcam to capture video
# Use 0 for the default camera on Raspberry Pi
cap = cv2.VideoCapture(0)

# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

# LED status flag for display
led_status = False

try:
    # Continuously get frames from the webcam
    while True:
        # Capture each frame from the webcam
        success, img = cap.read()
        
        if not success:
            print("Failed to read from camera")
            break
        
        # Find hands in the current frame
        hands, img = detector.findHands(img, draw=True, flipType=True)
        
        # Check if any hands are detected
        if hands:
            # Information for the first hand detected
            hand1 = hands[0]
            
            # Count the number of fingers up for the first hand
            fingers1 = detector.fingersUp(hand1)
            finger_count = fingers1.count(1)
            
            # Control LED based on finger count
            if finger_count == 3:
                led.on()
                led_status = True
                led_color = (0, 255, 0)  # Green when LED is ON
            else:
                led.off()
                led_status = False
                led_color = (0, 0, 255)  # Red when LED is OFF
            
            # Display finger count on screen
            cvzone.putTextRect(img, f"Fingers: {finger_count}", (50, 50), 
                             scale=2, thickness=2, 
                             colorT=(255, 255, 255), colorR=(255, 0, 255))
            
            # Display LED status
            status_text = "LED: ON" if led_status else "LED: OFF"
            cvzone.putTextRect(img, status_text, (50, 100), 
                             scale=2, thickness=2,
                             colorT=(255, 255, 255), colorR=led_color)
            
            # Visual indicator circle
            cv2.circle(img, (300, 75), 20, led_color, cv2.FILLED)
            
            # Print to console
            print(f"Fingers: {finger_count} | LED: {'ON' if led_status else 'OFF'}")
            
            # Check if a second hand is detected
            if len(hands) == 2:
                hand2 = hands[1]
                fingers2 = detector.fingersUp(hand2)
                print(f"Hand 2: {fingers2.count(1)} fingers")
        else:
            # No hands detected - turn off LED
            led.off()
            led_status = False
            
            # Display status when no hands detected
            cvzone.putTextRect(img, "No hands detected", (50, 50),
                             scale=2, thickness=2,
                             colorT=(255, 255, 255), colorR=(128, 128, 128))
            cvzone.putTextRect(img, "LED: OFF", (50, 100),
                             scale=2, thickness=2,
                             colorT=(255, 255, 255), colorR=(0, 0, 255))
        
        # Display the image in a window
        cv2.imshow("Hand Tracking - LED Control", img)
        
        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting...")
            break

except KeyboardInterrupt:
    print("\nProgram interrupted by user")

finally:
    # Clean up
    led.off()
    led.close()
    cap.release()
    cv2.destroyAllWindows()
    print("Cleanup complete - LED turned off and resources released")