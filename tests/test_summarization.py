import unittest
from summarization_model import summarize_text

class TestSummarization(unittest.TestCase):
    def setUp(self):
        self.test_text = "This is a test text that should be summarized."  # Example text for summarization

    def test_summarization(self):
        summary = summarize_text(self.test_text)
        self.assertIsNotNone(summary)
        self.assertIsInstance(summary, str)  # Ensure summary is a string
        self.assertGreater(len(summary), 0)  # Check that the summary is not empty

if __name__ == "__main__":
    unittest.main()
