import json
import os

# Map object data and store it in JSON format
def map_object_data(object_id, description, text, summary, master_id, output_dir):
    data = {
        "object_id": object_id,
        "description": description,
        "text": text,
        "summary": summary,
        "master_id": master_id
    }
    output_path = os.path.join(output_dir, f"object_{object_id}.json")
    with open(output_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Generate a final data mapping for all objects in the image
def map_final_output(object_data_list, master_image_id, output_dir):
    output_path = os.path.join(output_dir, f"{master_image_id}_final_mapping.json")
    with open(output_path, 'w') as json_file:
        json.dump(object_data_list, json_file, indent=4)
