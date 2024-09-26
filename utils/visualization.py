import matplotlib.pyplot as plt
import cv2

# Visualize segmented objects on the original image
def visualize_segmented_objects(image_path, predictions):
    image = cv2.imread(image_path)
    
    for i, (box, mask) in enumerate(zip(predictions[0]['boxes'], predictions[0]['masks'])):
        box = box.cpu().numpy().astype(int)
        mask = mask[0].mul(255).byte().cpu().numpy()
        
        # Draw bounding box and mask
        cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), (255, 0, 0), 2)
        plt.imshow(mask, alpha=0.5, cmap='gray')
    
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.show()

# Save final output image
def save_final_output(image_path, output_path, predictions):
    image = cv2.imread(image_path)
    
    for i, box in enumerate(predictions[0]['boxes']):
        box = box.cpu().numpy().astype(int)
        cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
    
    cv2.imwrite(output_path, image)
