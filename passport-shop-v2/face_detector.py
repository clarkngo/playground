"""
FaceDetector module for PassportShop using MediaPipe

Responsibilities:
- Detect faces in an image
- Ensure exactly one face is present
- Return face bounding box coordinates
"""

import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np
from typing import Tuple
from PIL import Image


class FaceDetector:
    
    @staticmethod
    def detect_face(pil_image: Image.Image) -> Tuple[int, int, int, int]:
        """
        Detect exactly one face in a PIL image.

        :param pil_image: PIL Image (RGB)
        :return: Face bounding box (top, right, bottom, left)
        :raises ValueError: if no face or multiple faces detected
        """
        if pil_image is None or not isinstance(pil_image, Image.Image):
            raise ValueError("Invalid image input")

        # Convert PIL to MediaPipe Image
        image_np = np.array(pil_image)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_np)
        
        # Create FaceDetector
        base_options = python.BaseOptions(model_asset_path='detector.tflite')
        options = vision.FaceDetectorOptions(
            base_options=base_options,
            min_detection_confidence=0.5
        )
        
        with vision.FaceDetector.create_from_options(options) as detector:
            detection_result = detector.detect(mp_image)
            
            if not detection_result.detections:
                raise ValueError("No face detected in the image")
            if len(detection_result.detections) > 1:
                raise ValueError("Multiple faces detected. Please use a photo with one face only.")
            
            # Get bounding box from first detection
            detection = detection_result.detections[0]
            bbox = detection.bounding_box
            
            # Convert to absolute coordinates
            left = bbox.origin_x
            top = bbox.origin_y
            width = bbox.width
            height = bbox.height
            right = left + width
            bottom = top + height
            
            return top, right, bottom, left
