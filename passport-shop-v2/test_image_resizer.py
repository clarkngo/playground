# test_image_resizer.py

from PIL import Image
from image_loader import ImageLoader
from face_detector import FaceDetector
from image_cropper import ImageCropper
from background_cleaner import BackgroundCleaner
from image_resizer import ImageResizer

# --- 1. Load the image ---
pil_image = ImageLoader.load_image("photo.jpg")
print("Loaded:", type(pil_image), pil_image.size)

# --- 2. Detect face ---
face_box = FaceDetector.detect_face(pil_image)
print("Face detected at:", face_box)

# --- 3. Crop the face ---
cropped_image = ImageCropper.crop_face(pil_image, face_box, margin_ratio=0.3)
print("Cropped:", type(cropped_image), cropped_image.size)

# --- 4. Clean the background (replace with white) ---
cleaned_image = BackgroundCleaner.clean_background(cropped_image)
print("Cleaned:", type(cleaned_image), cleaned_image.size)

# --- 5. Resize to 2x2 inches at 300 DPI ---
resized_image = ImageResizer.resize_for_passport(cleaned_image)
print("Resized:", type(resized_image), resized_image.size)

# --- 6. Show final passport photo ---
resized_image.show()

# --- 7. Save final image ---
resized_image.save("passport_photo.jpg", dpi=(300, 300))
print("Saved final passport photo as 'passport_photo.jpg'")
