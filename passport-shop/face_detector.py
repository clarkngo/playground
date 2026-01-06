"""
FaceDetector module for PassportShop using OpenCV

Responsibilities:
- Detect faces in an image
- Ensure exactly one face is present
- Return face bounding box coordinates
"""

import cv2
import numpy as np
from typing import Tuple


class FaceDetector:
    # Load the pre-trained Haar cascade classifier for frontal face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    @staticmethod
    def detect_face(image_rgb: np.ndarray) -> Tuple[int, int, int, int]:
        """
        Detect exactly one face in an RGB image.

        :param image_rgb: NumPy array (RGB)
        :return: Face bounding box (top, right, bottom, left)
        :raises ValueError: if no face or multiple faces detected
        """
        if image_rgb is None or not isinstance(image_rgb, np.ndarray):
            raise ValueError("Invalid image input")

        # Convert RGB to grayscale for Haar cascade
        gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

        # Detect faces with stricter requirements
        faces = FaceDetector.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=8,    # Increased from 5 to 8 (filters out weak detections)
            minSize=(100, 100) # Increased from 50 to 100 (since it's a headshot)
        )

        if len(faces) == 0:
            raise ValueError("No face detected in the image")
        if len(faces) > 1:
            raise ValueError("Multiple faces detected. Please use a photo with one face only.")

        # Haar returns (x, y, w, h)
        x, y, w, h = faces[0]
        top, left, bottom, right = y, x, y + h, x + w
        return top, right, bottom, left
