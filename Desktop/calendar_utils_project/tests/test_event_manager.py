import unittest
from calendar_utils.event_manager import add_event, list_events_by_date, remove_event

class TestEventManager(unittest.TestCase):
    def test_add_and_list_event(self):
        add_event("Spotkanie", "2025-03-22")
        events = list_events_by_date("2025-03-22")
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]["title"], "Spotkanie")

    def test_remove_event(self):
        remove_event("Spotkanie", "2025-03-22")
        events = list_events_by_date("2025-03-22")
        self.assertEqual(len(events), 0)
