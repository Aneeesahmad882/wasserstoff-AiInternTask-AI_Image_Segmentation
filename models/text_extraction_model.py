import easyocr

# Extract text from object images using EasyOCR
def extract_text(image_path):
    reader = easyocr.Reader(['en'])
    text_results = reader.readtext(image_path)
    
    # Extract and return the detected text
    extracted_text = " ".join([text[1] for text in text_results])
    return extracted_text
