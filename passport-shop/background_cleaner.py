"""
BackgroundCleaner module for PassportShop

Responsibilities:
- Remove background from cropped image
- Replace background with solid white
- Preserve face and shoulders
"""

from PIL import Image
import numpy as np
import cv2

class BackgroundCleaner:
    @staticmethod
    def clean_background(pil_image: Image.Image) -> Image.Image:
        image_np = np.array(pil_image)
        gray = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
        
        # 1. Use Adaptive Thresholding to find edges
        # This is better for hair than simple GrabCut
        thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                     cv2.THRESH_BINARY_INV, 11, 2)

        # 2. Clean up noise with morphological operations
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
        thresh = cv2.dilate(thresh, kernel, iterations=1)

        # 3. Find the largest contour (the person)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        mask = np.zeros(image_np.shape[:2], np.uint8)
        if contours:
            largest_cnt = max(contours, key=cv2.contourArea)
            cv2.drawContours(mask, [largest_cnt], -1, 255, -1)

        # 4. Use this mask as a 'Definite' hint for a single GrabCut pass
        # This prevents the 'holes' inside the face
        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)
        
        # We tell GrabCut: everything inside our contour is PROBABLY foreground
        grab_mask = np.where(mask == 255, cv2.GC_PR_FGD, cv2.GC_BGD).astype('uint8')
        
        cv2.grabCut(image_np, grab_mask, None, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_MASK)

        # 5. Create soft edges
        final_mask = np.where((grab_mask == 2) | (grab_mask == 0), 0, 1).astype('float32')
        final_mask = cv2.GaussianBlur(final_mask, (7, 7), 0)

        # 6. Composite onto white
        white_bg = np.ones_like(image_np) * 255
        mask_3d = final_mask[:, :, np.newaxis]
        final_image = (image_np * mask_3d + white_bg * (1 - mask_3d)).astype(np.uint8)

        return Image.fromarray(final_image)