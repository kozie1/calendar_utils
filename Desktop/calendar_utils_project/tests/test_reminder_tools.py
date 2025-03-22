import unittest
from calendar_utils.reminder_tools import add_reminder, get_today_reminders
from datetime import datetime

class TestReminderTools(unittest.TestCase):
    def test_add_reminder(self):
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        add_reminder("Zadanie domowe", now)
        reminders = get_today_reminders()
        self.assertGreaterEqual(len(reminders), 1)
