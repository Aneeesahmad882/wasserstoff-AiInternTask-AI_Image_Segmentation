import unittest
from identification_model import load_identification_model, identify_object

class TestIdentification(unittest.TestCase):
    def setUp(self):
        self.model, self.processor = load_identification_model()
        self.test_image_path = "segmented_objects/object_0.png"  # Replace with a valid test image path

    def test_identification(self):
        probabilities = identify_object(self.model, self.processor, self.test_image_path)
        self.assertIsNotNone(probabilities)
        self.assertGreater(probabilities.sum().item(), 0)  # Ensure there's some confidence

if __name__ == "__main__":
    unittest.main()
