"""
BackgroundCleaner module for PassportShop

Responsibilities:
- Remove background from cropped image
- Replace background with solid white
- Preserve face and shoulders
"""

from PIL import Image, ImageFilter, ImageDraw
import numpy as np


class BackgroundCleaner:
    @staticmethod
    def clean_background(pil_image: Image.Image) -> Image.Image:
        """
        Replace background with white using edge detection and flood fill.

        :param pil_image: PIL Image to process
        :return: PIL Image with white background
        """
        # Convert to RGB if needed
        if pil_image.mode != 'RGB':
            pil_image = pil_image.convert('RGB')
        
        # Get numpy array
        img_array = np.array(pil_image)
        
        # Create a simple mask by assuming the person is in the center
        # and the edges are background
        height, width = img_array.shape[:2]
        
        # Sample edge pixels (top, bottom, left, right edges)
        edge_samples = []
        edge_width = max(5, min(width, height) // 20)
        
        # Top edge
        edge_samples.extend(img_array[0:edge_width, :].reshape(-1, 3))
        # Bottom edge
        edge_samples.extend(img_array[-edge_width:, :].reshape(-1, 3))
        # Left edge
        edge_samples.extend(img_array[:, 0:edge_width].reshape(-1, 3))
        # Right edge
        edge_samples.extend(img_array[:, -edge_width:].reshape(-1, 3))
        
        # Calculate mean background color
        bg_color = np.median(edge_samples, axis=0).astype(int)
        
        # Create mask for pixels similar to background
        # Use a more generous tolerance
        tolerance = 60
        color_diff = np.sqrt(np.sum((img_array - bg_color) ** 2, axis=2))
        mask = color_diff < tolerance
        
        # Apply morphological operations to clean up the mask
        from scipy.ndimage import binary_erosion, binary_dilation
        
        # Erode to remove noise
        mask = binary_erosion(mask, iterations=2)
        # Dilate to restore edges
        mask = binary_dilation(mask, iterations=2)
        
        # Create output image
        result = img_array.copy()
        result[mask] = [255, 255, 255]
        
        return Image.fromarray(result)