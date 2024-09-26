# AI Pipeline for Image Segmentation and Object Analysis

# Project Overview
This project is an AI-powered image processing pipeline designed to segment, identify, and analyze objects within an input image. It uses state-of-the-art deep learning models to perform the following tasks:

1. Image Segmentation: Segment objects from an input image.
2. Object Extraction: Extract each segmented object as a separate image.
3. Object Identification: Identify and describe real-world objects.
4. Text/Data Extraction: Extract text or data from each object.
5. Object Attribute Summarization: Summarize the attributes and nature of each object.
6. Data Mapping and Output: Map all data to the original image and output the results in both visual and tabular form.

The project also includes a Streamlit UI for easy interaction, where users can upload images, view segmented objects, and review extracted and summarized data for each object.

# Features

1. Pre-trained Models: The project uses models like Mask R-CNN (for segmentation), CLIP (for identification), EasyOCR (for text extraction), and DistilBART (for summarization).
2. Visualization: View segmented objects on the original image.
3. User-Friendly Interface: An interactive Streamlit UI for uploading images and visualizing results.
4. Extensible Architecture: The modular structure allows easy extension or swapping of models.

# Installation
To set up the project locally, follow these steps:

# Prerequisites
1. Python 3.8 or higher
2. Virtual environment (optional but recommended)
3. CUDA-enabled GPU (optional for faster execution)

# Steps
Clone the repository:
git clone 

code:
cd Project_Image_Segmentation
Create and activate a virtual environment:

code:
python -m venv venv

# Install dependencies:

code: https://github.com/Aneeesahmad882/wasserstoff-AiInternTask-AI_Image_Segmentation.git

pip install -r requirements.txt
Download pre-trained models (if required): Some models, like those from Hugging Face, need to be downloaded manually.

# Run the Streamlit app:

code :
streamlit run streamlit.app/app.py

# Usage
1. Open the Streamlit app in your browser after running the command.
2. Upload an image through the UI.
3. View segmented objects and extracted data such as object descriptions, texts, and attributes.
4. Download the results as a table and final output image.

# Contact
For any inquiries, please contact:

Your Name: aneesahmad882@gmail.com
