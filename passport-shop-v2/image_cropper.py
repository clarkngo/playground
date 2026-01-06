"""
ImageCropper module for PassportShop

Responsibilities:
- Crop image based on detected face
- Adjust head position and margins according to U.S. passport rules
"""

from typing import Tuple
from PIL import Image


class ImageCropper:
    @staticmethod
    def crop_face(pil_image: Image.Image, face_box: Tuple[int, int, int, int], margin_ratio: float = 0.3) -> Image.Image:
        """
        Crop the image around the face with some margin.

        :param pil_image: PIL Image
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
        w, h = pil_image.size
        crop_top = max(0, top - margin_y)
        crop_bottom = min(h, bottom + margin_y)
        crop_left = max(0, left - margin_x)
        crop_right = min(w, right + margin_x)

        # PIL crop uses (left, top, right, bottom)
        cropped = pil_image.crop((crop_left, crop_top, crop_right, crop_bottom))
        return cropped
