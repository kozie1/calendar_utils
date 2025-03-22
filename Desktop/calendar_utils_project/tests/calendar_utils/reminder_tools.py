from datetime import datetime

reminders = []

def add_reminder(text, date_time):
    reminders.append({"text": text, "date_time": date_time})
    return f"Przypomnienie dodane na {date_time}"

def get_today_reminders():
    today = datetime.now().date()
    return [r for r in reminders if datetime.strptime(r["date_time"], "%Y-%m-%d %H:%M").date() == today]
