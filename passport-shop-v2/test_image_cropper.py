from image_loader import ImageLoader
from face_detector import FaceDetector
from image_cropper import ImageCropper

# Load image
pil_image = ImageLoader.load_image("photo.jpg")
image_np = ImageLoader.to_numpy(pil_image)

# Detect face
face_box = FaceDetector.detect_face(image_np)

# Crop face with margin
cropped_image = ImageCropper.crop_face(image_np, face_box, margin_ratio=0.3)

# Show cropped image
cropped_image.show()
