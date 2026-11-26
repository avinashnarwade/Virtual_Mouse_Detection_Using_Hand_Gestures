class SensitivityManager:
    def __init__(self, sensitivity=1.5):
        """Initialize with default sensitivity."""
        self.sensitivity = sensitivity

    def set_sensitivity(self, sensitivity):
        """Update sensitivity."""
        self.sensitivity = sensitivity

    def adjust_cursor_position(self, x, y, frame_width, frame_height):
        """Map hand coordinates to full screen."""
        screen_width, screen_height = 1920, 1080  # Screen resolution
        normalized_x = x / frame_width
        normalized_y = y / frame_height

        # Scale coordinates based on sensitivity
        adjusted_x = int(normalized_x * screen_width * self.sensitivity)
        adjusted_y = int(normalized_y * screen_height * self.sensitivity)

        return adjusted_x, adjusted_y
