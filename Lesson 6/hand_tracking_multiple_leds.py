from cvzone.HandTrackingModule import HandDetector
import cv2
from gpiozero import LED
import cvzone

# Initialize LEDs on different GPIO pins
led1 = LED(17)  # LED for 1 finger - GPIO 17
led2 = LED(27)  # LED for 2 fingers - GPIO 27
led3 = LED(22)  # LED for 3 fingers - GPIO 22

# Initialize the webcam to capture video
# Use 0 for the default camera on Raspberry Pi
cap = cv2.VideoCapture(0)

# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

# LED status dictionary
led_status = {1: False, 2: False, 3: False}

def control_leds(finger_count):
    """Control LEDs based on finger count"""
    # Turn off all LEDs first
    led1.off()
    led2.off()
    led3.off()
    led_status[1] = False
    led_status[2] = False
    led_status[3] = False
    
    # Turn on appropriate LED based on finger count
    if finger_count == 1:
        led1.on()
        led_status[1] = True
    elif finger_count == 2:
        led2.on()
        led_status[2] = True
    elif finger_count == 3:
        led3.on()
        led_status[3] = True
    
    return led_status

def draw_led_indicators(img, led_status, finger_count):
    """Draw LED status indicators on the image"""
    # Base positions for LED indicators
    x_start = 50
    y_start = 50
    spacing = 120
    
    # LED 1 Indicator
    color1 = (0, 255, 0) if led_status[1] else (100, 100, 100)
    cvzone.putTextRect(img, "LED1", (x_start, y_start), 
                      scale=1.5, thickness=2,
                      colorT=(255, 255, 255), colorR=color1)
    cv2.circle(img, (x_start + 70, y_start - 10), 15, color1, cv2.FILLED)
    
    # LED 2 Indicator
    color2 = (0, 255, 0) if led_status[2] else (100, 100, 100)
    cvzone.putTextRect(img, "LED2", (x_start + spacing, y_start), 
                      scale=1.5, thickness=2,
                      colorT=(255, 255, 255), colorR=color2)
    cv2.circle(img, (x_start + spacing + 70, y_start - 10), 15, color2, cv2.FILLED)
    
    # LED 3 Indicator
    color3 = (0, 255, 0) if led_status[3] else (100, 100, 100)
    cvzone.putTextRect(img, "LED3", (x_start + spacing*2, y_start), 
                      scale=1.5, thickness=2,
                      colorT=(255, 255, 255), colorR=color3)
    cv2.circle(img, (x_start + spacing*2 + 70, y_start - 10), 15, color3, cv2.FILLED)
    
    # Display finger count
    cvzone.putTextRect(img, f"Fingers: {finger_count}", (50, 120), 
                      scale=2, thickness=3,
                      colorT=(255, 255, 255), colorR=(255, 0, 255))
    
    # Display instructions
    cvzone.putTextRect(img, "1 finger = LED1 | 2 fingers = LED2 | 3 fingers = LED3", 
                      (50, 450), scale=1, thickness=1,
                      colorT=(255, 255, 255), colorR=(0, 0, 0))

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
            
            # Control LEDs based on finger count
            led_status = control_leds(finger_count)
            
            # Draw LED indicators
            draw_led_indicators(img, led_status, finger_count)
            
            # Print to console
            status_str = f"Fingers: {finger_count} | "
            status_str += f"LED1: {'ON' if led_status[1] else 'OFF'} | "
            status_str += f"LED2: {'ON' if led_status[2] else 'OFF'} | "
            status_str += f"LED3: {'ON' if led_status[3] else 'OFF'}"
            print(status_str)
            
            # Check if a second hand is detected
            if len(hands) == 2:
                hand2 = hands[1]
                fingers2 = detector.fingersUp(hand2)
                hand2_count = fingers2.count(1)
                
                # Display second hand info
                cvzone.putTextRect(img, f"Hand 2: {hand2_count} fingers", (50, 160),
                                 scale=1.5, thickness=2,
                                 colorT=(255, 255, 255), colorR=(128, 128, 255))
        else:
            # No hands detected - turn off all LEDs
            led1.off()
            led2.off()
            led3.off()
            led_status = {1: False, 2: False, 3: False}
            
            # Display status when no hands detected
            draw_led_indicators(img, led_status, 0)
            cvzone.putTextRect(img, "No hands detected - All LEDs OFF", (50, 200),
                             scale=1.5, thickness=2,
                             colorT=(255, 255, 255), colorR=(128, 128, 128))
        
        # Display the image in a window
        cv2.imshow("Hand Tracking - Multiple LED Control", img)
        
        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("\nExiting...")
            break

except KeyboardInterrupt:
    print("\nProgram interrupted by user")

finally:
    # Clean up - turn off all LEDs
    led1.off()
    led2.off()
    led3.off()
    led1.close()
    led2.close()
    led3.close()
    cap.release()
    cv2.destroyAllWindows()
    print("Cleanup complete - All LEDs turned off and resources released")