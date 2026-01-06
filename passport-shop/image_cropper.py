"""
ImageCropper module for PassportShop

Responsibilities:
- Crop image based on detected face
- Adjust head position and margins according to U.S. passport rules
"""

from typing import Tuple
from PIL import Image
import numpy as np

class ImageCropper:
    @staticmethod
    def crop_face(image: np.ndarray, face_box: Tuple[int, int, int, int], margin_ratio: float = 0.3) -> Image.Image:
        """
        Crop the image around the face with some margin.

        :param image: NumPy array (RGB)
        :param face_box: (top, right, bottom, left)
        :param margin_ratio: Extra margin around face as fraction of face height
        :return: PIL Image of cropped face
        """
        top, right, bottom, left = face_box
        face_height = bottom - top
        face_width = right - left

        # Add margin around face
        margin_y = int(face_height * margin_ratio)
        margin_x = int(face_width * margin_ratio)

        # Calculate crop coordinates, ensuring they stay within image bounds
        crop_top = max(0, top - margin_y)
        crop_bottom = min(image.shape[0], bottom + margin_y)
        crop_left = max(0, left - margin_x)
        crop_right = min(image.shape[1], right + margin_x)

        cropped = image[crop_top:crop_bottom, crop_left:crop_right]

        # Convert to PIL Image
        return Image.fromarray(cropped)
