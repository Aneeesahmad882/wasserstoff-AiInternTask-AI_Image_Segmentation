from transformers import pipeline

# Summarize the attributes of objects using transformers pipeline
def summarize_text(text):
   
    # Get the length of the input
    input_length = len(text.split())

    # Dynamically adjust max_length based on input length
    max_length = min(50, input_length + 10)  # Set max_length no more than 10 tokens longer than input
    
     # Explicitly specify the model name and revision
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", revision="a4f8f3e")

    
    summary = summarizer(text, max_length=50, min_length=10, do_sample=False)
    
    return summary[0]['summary_text']

