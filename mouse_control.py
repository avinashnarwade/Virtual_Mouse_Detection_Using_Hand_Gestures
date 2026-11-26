import pyautogui
import numpy as np

class MouseControl:
    def __init__(self):
        """Initialize Mouse Control."""
        self.click_threshold = 0.05  # Distance to trigger a click
        self.drag_threshold = 0.08  # Distance to trigger a drag

    def perform_click(self, thumb_tip, index_tip):
        """Perform left-click when thumb and index finger touch."""
        distance = np.linalg.norm([thumb_tip.x - index_tip.x, thumb_tip.y - index_tip.y])
        if distance < self.click_threshold:
            pyautogui.click()  # Trigger a left click

    def perform_right_click(self, thumb_tip, middle_tip):
        """Perform right-click when thumb and middle finger touch."""
        distance = np.linalg.norm([thumb_tip.x - middle_tip.x, thumb_tip.y - middle_tip.y])
        if distance < self.click_threshold:
            pyautogui.rightClick()  # Trigger a right click

    def perform_drag(self, index_tip, middle_tip):
        """Hold and drag when index and middle finger are close together."""
        distance = np.linalg.norm([index_tip.x - middle_tip.x, index_tip.y - middle_tip.y])
        if distance < self.drag_threshold:
            pyautogui.mouseDown()  # Start dragging
        else:
            pyautogui.mouseUp()  # End dragging

    def scroll_vertical(self, index_tip, pinky_tip):
        """Scroll based on vertical hand movement."""
        if index_tip.y > pinky_tip.y:
            pyautogui.scroll(-5)  # Scroll down
        else:
            pyautogui.scroll(5)   # Scroll up
