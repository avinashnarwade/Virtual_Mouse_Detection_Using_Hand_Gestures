import mediapipe as mp

class HandTracker:
    def __init__(self, detection_confidence=0.8, tracking_confidence=0.8):
        """Initialize Mediapipe Hand Tracker."""
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence
        )
        self.mp_draw = mp.solutions.drawing_utils

    def find_hand_landmarks(self, frame_rgb):
        """Process frame and return detected hand landmarks."""
        result = self.hands.process(frame_rgb)
        return result.multi_hand_landmarks
