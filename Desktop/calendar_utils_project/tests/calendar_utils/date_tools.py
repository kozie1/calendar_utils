from datetime import datetime, timedelta

def get_day_of_week(date_str):
    """Zwraca dzień tygodnia dla podanej daty (format: YYYY-MM-DD)."""
    date = datetime.strptime(date_str, "%Y-%m-%d")
    return date.strftime("%A")

def add_workdays(start_date_str, days):
    """Dodaje określoną liczbę dni roboczych do daty."""
    date = datetime.strptime(start_date_str, "%Y-%m-%d")
    while days > 0:
        date += timedelta(days=1)
        if date.weekday() < 5:
            days -= 1
    return date.strftime("%Y-%m-%d")
