from image_loader import ImageLoader

image = ImageLoader.load_image("photo.jpg")
opencv_image = ImageLoader.to_opencv(image)

print(image.size)          # (width, height)
print(opencv_image.shape)  # (height, width, 3)
