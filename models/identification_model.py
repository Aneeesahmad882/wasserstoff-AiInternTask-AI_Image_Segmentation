from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch


# Load CLIP model for object identification
def load_identification_model():
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
    return model, processor

# Identify objects in segmented images
def identify_object(model, processor, image_path):
    image = Image.open(image_path)
    inputs = processor(text=["object"], images=image, return_tensors="pt", padding=True)
    
    # Get object identification probabilities
    with torch.no_grad():
        outputs = model(**inputs)
    
    logits_per_image = outputs.logits_per_image
    probs = logits_per_image.softmax(dim=1)
    
    return probs
