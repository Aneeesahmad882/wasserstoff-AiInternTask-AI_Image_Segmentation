import unittest
from text_extraction_model import extract_text

class TestTextExtraction(unittest.TestCase):
    def setUp(self):
        self.test_image_path = "segmented_objects/object_0.png"  # Replace with a valid test image path

    def test_text_extraction(self):
        extracted_text = extract_text(self.test_image_path)
        self.assertIsNotNone(extracted_text)
        self.assertIsInstance(extracted_text, str)  # Ensure extracted text is a string
        self.assertTrue(len(extracted_text) >= 0)  # Check that the length is not negative

if __name__ == "__main__":
    unittest.main()
