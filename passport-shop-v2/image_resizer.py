"""
ImageResizer module for PassportShop

Responsibilities:
- Resize image to U.S. passport size (2x2 inches)
- Set correct DPI (300 DPI)
"""

from PIL import Image

class ImageResizer:
    PASSPORT_SIZE_INCHES = (2, 2)
    DPI = 300

    @staticmethod
    def resize_for_passport(pil_image: Image.Image) -> Image.Image:
        width_px = int(ImageResizer.PASSPORT_SIZE_INCHES[0] * ImageResizer.DPI)
        height_px = int(ImageResizer.PASSPORT_SIZE_INCHES[1] * ImageResizer.DPI)

        # resize returns a new image
        resized_image = pil_image.resize((width_px, height_px), Image.LANCZOS)
        resized_image.info['dpi'] = (ImageResizer.DPI, ImageResizer.DPI)
        return resized_image  # <-- MUST return the new image
