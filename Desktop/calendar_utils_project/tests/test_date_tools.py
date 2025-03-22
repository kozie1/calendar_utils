import unittest
from calendar_utils.date_tools import get_day_of_week, add_workdays

class TestDateTools(unittest.TestCase):
    def test_get_day_of_week(self):
        self.assertEqual(get_day_of_week("2025-03-22"), "Saturday")

    def test_add_workdays(self):
        self.assertEqual(add_workdays("2025-03-21", 1), "2025-03-24")
