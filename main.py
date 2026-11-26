import cv2
import time
import pyautogui
from hand_tracking import HandTracker
from mouse_control import MouseControl
from sensitivity_manager import SensitivityManager

# Initialize Hand Tracker and Mouse Control
hand_tracker = HandTracker()
mouse_control = MouseControl()
sensitivity_manager = SensitivityManager(sensitivity=1.5)

# Capture video from webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1920)  # Set width
cap.set(4, 1080)  # Set height
cap.set(cv2.CAP_PROP_FPS, 90)

prev_time = 0  # To calculate FPS

while True:
    success, frame = cap.read()
    if not success:
        break

    # Flip the frame horizontally for natural movement
    frame = cv2.flip(frame, 1)

    # Convert BGR to RGB for Mediapipe
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hand_landmarks = hand_tracker.find_hand_landmarks(frame_rgb)

    h, w, _ = frame.shape  # Get height and width of the frame

    if hand_landmarks:
        for landmarks in hand_landmarks:
            # Get relevant landmarks for gestures (index, thumb, middle, pinky)
            index_tip = landmarks.landmark[8]    # Index tip (Landmark 8)
            thumb_tip = landmarks.landmark[4]     # Thumb tip (Landmark 4)
            middle_tip = landmarks.landmark[12]   # Middle tip (Landmark 12)
            pinky_tip = landmarks.landmark[20]    # Pinky tip (Landmark 20)

            # Draw hand landmarks on screen (for debugging/tracking)
            hand_tracker.mp_draw.draw_landmarks(frame, landmarks, hand_tracker.mp_hands.HAND_CONNECTIONS)

            # Perform actions based on gestures
            mouse_control.perform_click(thumb_tip, index_tip)
            mouse_control.perform_right_click(thumb_tip, middle_tip)
            mouse_control.perform_drag(index_tip, middle_tip)
            mouse_control.scroll_vertical(index_tip, pinky_tip)

            # Adjust cursor position using sensitivity
            x, y = int(index_tip.x * w), int(index_tip.y * h)
            adjusted_x, adjusted_y = sensitivity_manager.adjust_cursor_position(x, y, w, h)
            pyautogui.moveTo(adjusted_x, adjusted_y, duration=0.02)

    # Calculate and display FPS in top-right corner
    curr_time = time.time()  # Fixed the typo here (time_ -> time)
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time
    cv2.putText(frame, f'FPS: {int(fps)}', (w - 150, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the frame with hand landmarks and FPS
    cv2.imshow("Virtual Mouse", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
