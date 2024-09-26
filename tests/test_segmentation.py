import unittest
from segmentation_model import load_segmentation_model, segment_image

class TestSegmentation(unittest.TestCase):
    def test_segmentation(self):
        model = load_segmentation_model()
        predictions = segment_image(model, "input_images/sample.jpg")
        self.assertIsNotNone(predictions)

if __name__ == "__main__":
    unittest.main()
