from PIL import Image
import cv2

# Preprocess images before feeding into the models
def preprocess_image(image_path):
    image = Image.open(image_path).convert("RGB")
    return image

def load_image_cv2(image_path):
    image = cv2.imread(image_path)
    return image
