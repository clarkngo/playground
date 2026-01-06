"""
ImageLoader module for PassportShop

Responsibilities:
- Load image from file path
- Validate file existence and format
- Convert image to RGB
- Provide NumPy/OpenCV-compatible output
"""

import os
from PIL import Image
import numpy as np


class ImageLoader:
    SUPPORTED_EXTENSIONS = (".jpg", ".jpeg", ".png")

    @staticmethod
    def load_image(path: str) -> Image.Image:
        """
        Load an image from disk and return a PIL Image in RGB format.

        :param path: Path to the image file
        :return: PIL.Image.Image
        :raises FileNotFoundError, ValueError
        """
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Image file not found: {path}")

        if not path.lower().endswith(ImageLoader.SUPPORTED_EXTENSIONS):
            raise ValueError("Unsupported file format. Use JPG or PNG.")

        try:
            image = Image.open(path)
            image = image.convert("RGB")
            return image
        except Exception as e:
            raise ValueError(f"Unable to load image: {e}")

    @staticmethod
    def to_numpy(image: Image.Image) -> np.ndarray:
        """
        Convert a PIL Image to a NumPy array (RGB).

        :param image: PIL image
        :return: NumPy array (H, W, 3)
        """
        return np.array(image)

    @staticmethod
    def to_opencv(image: Image.Image) -> np.ndarray:
        """
        Convert a PIL Image to OpenCV format (BGR).

        :param image: PIL image
        :return: NumPy array (BGR)
        """
        rgb = np.array(image)
        return rgb[:, :, ::-1]
