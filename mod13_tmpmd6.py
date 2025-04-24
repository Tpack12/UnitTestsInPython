import unittest
from unittest.mock import patch
from utils import validate_date_range
from main import show_menu

class TestProject3Inputs(unittest.TestCase):
    # Date‐range validation (start/end date)
    def test_validate_date_range_valid(self):
        self.assertTrue(validate_date_range("2025-01-01", "2025-12-31"))

    def test_validate_date_range_invalid_format(self):
        # wrong format for start or end
        self.assertFalse(validate_date_range("01-01-2025", "2025-12-31"))
        self.assertFalse(validate_date_range("2025/01/01", "2025-12-31"))

    def test_validate_date_range_end_before_start(self):
        # end date earlier than start
        self.assertFalse(validate_date_range("2025-12-31", "2025-01-01"))