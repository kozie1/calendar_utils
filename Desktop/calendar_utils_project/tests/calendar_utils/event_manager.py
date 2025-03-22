events = []

def add_event(title, date):
    events.append({"title": title, "date": date})
    return f"Wydarzenie '{title}' dodane na {date}"

def list_events_by_date(date):
    return [e for e in events if e['date'] == date]

def remove_event(title, date):
    global events
    events = [e for e in events if not (e["title"] == title and e["date"] == date)]
