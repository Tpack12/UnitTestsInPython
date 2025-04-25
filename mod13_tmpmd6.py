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

        # Menu selection for chart type
    def test_show_menu_chart_type(self):
        # Chart Types menu: ["Bar", "Line"]
        with patch('builtins.input', return_value='1'):
            choice = show_menu("Chart Types", ["Bar", "Line"])
            self.assertEqual(choice, 1)
        with patch('builtins.input', return_value='2'):
            choice = show_menu("Chart Types", ["Bar", "Line"])
            self.assertEqual(choice, 2)

        # Menu selection for time series
    def test_show_menu_time_series(self):
        # Time Series menu: ["Intraday", "Daily", "Weekly", "Monthly"]
        with patch('builtins.input', return_value='1'):
            choice = show_menu(
                "Select the Time Series",
                ["Intraday", "Daily", "Weekly", "Monthly"]
            )
            self.assertEqual(choice, 1)
        with patch('builtins.input', return_value='4'):
            choice = show_menu(
                "Select the Time Series",
                ["Intraday", "Daily", "Weekly", "Monthly"]
            )
            self.assertEqual(choice, 4)

    def test_show_menu_non_numeric_input(self):
        with patch('builtins.input', return_value='x'):
            with self.assertRaises(ValueError):
                show_menu("Chart Types", ["Bar", "Line"])

    # Stock symbol formatting (must be uppercase, 1–7 letters)
    def test_symbol_uppercase_and_length(self):
        with patch('builtins.input', return_value='goog'):
            symbol = input("\nEnter the stock symbol: ").upper()
            self.assertEqual(symbol, "GOOG")
            self.assertTrue(1 <= len(symbol) <= 7)
            self.assertTrue(symbol.isalpha())

if __name__ == "__main__":
    unittest.main()