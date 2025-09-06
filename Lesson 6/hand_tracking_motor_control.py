from cvzone.HandTrackingModule import HandDetector
import cv2
from gpiozero import Motor, PWMOutputDevice
import cvzone
from time import sleep

# L298N Motor Driver GPIO Pin Configuration
# Motor A connections
MOTOR_ENA = 18  # Enable A (PWM pin for speed control)
MOTOR_IN1 = 23  # Input 1 for Motor A
MOTOR_IN2 = 24  # Input 2 for Motor A

# Initialize motor with L298N driver
# Using PWMOutputDevice for speed control on ENA pin
pwm = PWMOutputDevice(MOTOR_ENA)
motor = Motor(forward=MOTOR_IN1, backward=MOTOR_IN2)

# Speed mapping for finger counts
speed_map = {
    0: 0,     # No fingers - motor stopped
    1: 0.5,   # 1 finger - 50% speed
    2: 0.6,   # 2 fingers - 60% speed
    3: 0.7,   # 3 fingers - 70% speed
    4: 0.8,   # 4 fingers - 80% speed
    5: 1.0    # 5 fingers - 100% speed
}

# Initialize the webcam to capture video
cap = cv2.VideoCapture(0)

# Initialize the HandDetector class
detector = HandDetector(staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

# Motor state variables
current_speed = 0
motor_running = False

def set_motor_speed(finger_count):
    """Set motor speed based on finger count"""
    global current_speed, motor_running
    
    # Get speed from mapping
    target_speed = speed_map.get(finger_count, 0)
    
    if target_speed > 0:
        # Set PWM duty cycle for speed control
        pwm.value = target_speed
        # Start motor forward
        motor.forward()
        motor_running = True
    else:
        # Stop motor
        motor.stop()
        pwm.value = 0
        motor_running = False
    
    current_speed = target_speed
    return target_speed

def draw_motor_status(img, finger_count, speed):
    """Draw motor status and speed indicator on the image"""
    # Draw speed gauge background
    gauge_x, gauge_y = 450, 100
    gauge_width, gauge_height = 150, 30
    
    # Background rectangle
    cv2.rectangle(img, (gauge_x, gauge_y), (gauge_x + gauge_width, gauge_y + gauge_height), 
                  (200, 200, 200), -1)
    
    # Speed fill (colored based on speed)
    if speed > 0:
        fill_width = int(gauge_width * speed)
        # Color gradient from green to red based on speed
        if speed <= 0.6:
            color = (0, 255, 0)  # Green for low speed
        elif speed <= 0.8:
            color = (0, 165, 255)  # Orange for medium speed
        else:
            color = (0, 0, 255)  # Red for high speed
        
        cv2.rectangle(img, (gauge_x, gauge_y), 
                      (gauge_x + fill_width, gauge_y + gauge_height), 
                      color, -1)
    
    # Draw border
    cv2.rectangle(img, (gauge_x, gauge_y), (gauge_x + gauge_width, gauge_y + gauge_height), 
                  (0, 0, 0), 2)
    
    # Display finger count
    cvzone.putTextRect(img, f"Fingers: {finger_count}", (50, 50), 
                      scale=2, thickness=3,
                      colorT=(255, 255, 255), colorR=(255, 0, 255))
    
    # Display motor speed percentage
    speed_percent = int(speed * 100)
    speed_color = (0, 255, 0) if motor_running else (0, 0, 255)
    cvzone.putTextRect(img, f"Motor Speed: {speed_percent}%", (50, 100), 
                      scale=2, thickness=3,
                      colorT=(255, 255, 255), colorR=speed_color)
    
    # Display motor status
    status_text = "RUNNING" if motor_running else "STOPPED"
    status_color = (0, 255, 0) if motor_running else (0, 0, 255)
    cvzone.putTextRect(img, f"Status: {status_text}", (50, 150), 
                      scale=1.5, thickness=2,
                      colorT=(255, 255, 255), colorR=status_color)
    
    # Draw speed indicators for each finger count
    y_pos = 250
    for fingers in range(1, 6):
        speed_val = int(speed_map[fingers] * 100)
        indicator_color = (0, 255, 0) if finger_count == fingers else (150, 150, 150)
        cvzone.putTextRect(img, f"{fingers} finger(s): {speed_val}%", 
                          (50, y_pos + (fingers-1)*40), 
                          scale=1, thickness=1,
                          colorT=(255, 255, 255), colorR=indicator_color)
    
    # Safety warning
    if speed >= 0.8:
        cvzone.putTextRect(img, "HIGH SPEED!", (450, 50), 
                          scale=1.5, thickness=2,
                          colorT=(255, 255, 255), colorR=(0, 0, 255))

try:
    print("Hand Tracking Motor Control Started")
    print("Show fingers to control motor speed:")
    print("1 finger = 50% | 2 = 60% | 3 = 70% | 4 = 80% | 5 = 100%")
    print("Press 'q' to quit")
    
    # Initial motor stop
    motor.stop()
    pwm.value = 0
    
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
            
            # Count the number of fingers up
            fingers1 = detector.fingersUp(hand1)
            finger_count = fingers1.count(1)
            
            # Set motor speed based on finger count
            speed = set_motor_speed(finger_count)
            
            # Draw motor status and indicators
            draw_motor_status(img, finger_count, speed)
            
            # Print to console
            print(f"Fingers: {finger_count} | Speed: {int(speed*100)}% | Status: {'Running' if motor_running else 'Stopped'}")
            
            # Check if a second hand is detected
            if len(hands) == 2:
                hand2 = hands[1]
                fingers2 = detector.fingersUp(hand2)
                hand2_count = fingers2.count(1)
                
                # Display second hand info
                cvzone.putTextRect(img, f"Hand 2: {hand2_count} fingers (ignored)", (50, 200),
                                 scale=1, thickness=1,
                                 colorT=(255, 255, 255), colorR=(128, 128, 255))
        else:
            # No hands detected - stop motor
            set_motor_speed(0)
            
            # Display status when no hands detected
            draw_motor_status(img, 0, 0)
            cvzone.putTextRect(img, "No hands detected - Motor STOPPED", (50, 200),
                             scale=1.5, thickness=2,
                             colorT=(255, 255, 255), colorR=(128, 128, 128))
        
        # Display instructions
        cvzone.putTextRect(img, "L298N Motor Control | Press 'q' to quit", 
                          (50, 470), scale=1, thickness=1,
                          colorT=(255, 255, 255), colorR=(0, 0, 0))
        
        # Display the image in a window
        cv2.imshow("Hand Tracking - DC Motor Control", img)
        
        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("\nStopping motor and exiting...")
            break

except KeyboardInterrupt:
    print("\nProgram interrupted by user")

finally:
    # Clean up - stop motor and release resources
    print("Performing cleanup...")
    motor.stop()
    pwm.value = 0
    pwm.close()
    motor.close()
    cap.release()
    cv2.destroyAllWindows()
    print("Cleanup complete - Motor stopped and resources released")