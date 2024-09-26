import os
import cv2
import numpy as np

# Save segmented object images with unique IDs
def save_segmented_objects(predictions, image_path, save_dir):
    image = cv2.imread(image_path)
    os.makedirs(save_dir, exist_ok=True)
    
    for i, mask in enumerate(predictions[0]['masks']):
        # Create binary mask
        mask = mask[0].mul(255).byte().cpu().numpy()
        ret, thresh = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
        
        # Apply mask to image
        object_image = cv2.bitwise_and(image, image, mask=thresh)
        object_save_path = os.path.join(save_dir, f"object_{i}.png")
        cv2.imwrite(object_save_path, object_image)
