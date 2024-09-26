import torch
from torchvision import models, transforms
from PIL import Image

# Load Mask R-CNN model for segmentation
def load_segmentation_model():
    model = models.detection.maskrcnn_resnet50_fpn(pretrained=True)
    model.eval()  # Set to evaluation mode
    return model

# Segment the input image
def segment_image(model, image_path):
    image = Image.open(image_path)
    transform = transforms.Compose([transforms.ToTensor()])
    img_tensor = transform(image).unsqueeze(0)
    
    # Get the segmentation predictions
    with torch.no_grad():
        predictions = model(img_tensor)
    
    return predictions
