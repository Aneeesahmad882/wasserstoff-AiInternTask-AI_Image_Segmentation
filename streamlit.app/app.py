import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.visualization import visualize_segmented_objects
from utils.postprocessing import save_segmented_objects


from models.segmentation_model import load_segmentation_model, segment_image
from models.identification_model import load_identification_model, identify_object
from models.text_extraction_model import extract_text
from models.summarization_model import summarize_text



import streamlit as st
from PIL import Image
import numpy as np
# Streamlit UI
st.title("AI Pipeline for Image Segmentation and Object Analysis")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    image_path = f"input_images/{uploaded_file.name}"
    with open(image_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())
    
    # Load models
    seg_model = load_segmentation_model()
    id_model, id_processor = load_identification_model()

    # Perform segmentation
    predictions = segment_image(seg_model, image_path)
    st.image(image_path, caption="Uploaded Image", use_column_width=True)

    # Visualize segmented objects
    st.write("Segmented Objects:")
    visualize_segmented_objects(image_path, predictions)

    # Save segmented objects
    object_dir = f"segmented_objects/{os.path.basename(image_path)}"
    save_segmented_objects(predictions, image_path, object_dir)
    
    # Identify objects, extract text, and summarize attributes
    for object_file in os.listdir(object_dir):
        object_path = os.path.join(object_dir, object_file)
        st.write(f"Object: {object_file}")
        st.image(object_path, use_column_width=True)

        description = identify_object(id_model, id_processor, object_path)
        text = extract_text(object_path)
        summary = summarize_text(text)
        
        st.write(f"Description: {description}")
        st.write(f"Extracted Text: {text}")
        st.write(f"Summary: {summary}")
