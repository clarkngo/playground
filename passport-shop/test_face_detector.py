from image_loader import ImageLoader
from face_detector import FaceDetector

# Load image
pil_image = ImageLoader.load_image("photo.jpg")
image_np = ImageLoader.to_numpy(pil_image)

# Detect face
top, right, bottom, left = FaceDetector.detect_face(image_np)
print(f"Face detected at: top={top}, right={right}, bottom={bottom}, left={left}")
