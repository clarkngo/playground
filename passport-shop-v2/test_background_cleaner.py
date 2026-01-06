from image_loader import ImageLoader
from face_detector import FaceDetector
from image_cropper import ImageCropper
from background_cleaner import BackgroundCleaner

# Load image
pil_image = ImageLoader.load_image("photo.jpg")
image_np = ImageLoader.to_numpy(pil_image)

# Detect face
face_box = FaceDetector.detect_face(image_np)

# Crop face
cropped_image = ImageCropper.crop_face(image_np, face_box, margin_ratio=0.3)

# Clean background
cleaned_image = BackgroundCleaner.clean_background(cropped_image)

# Show cleaned image
cleaned_image.show()
