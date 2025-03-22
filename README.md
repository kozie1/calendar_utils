calendar_utils

Praktyczna biblioteka do zarządzania datami, wydarzeniami i przypomnieniami w Pythonie.

Moduły:
- `date_tools.py` – operacje na datach (dzień tygodnia, dni robocze)
- `event_manager.py` – dodawanie, usuwanie i lista wydarzeń
- `reminder_tools.py` – przypomnienia na konkretną godzinę

Instalacja:

pip install -e .


 Przykład użycia:
python
from calendar_utils.date_tools import get_day_of_week
print(get_day_of_week("2025-03-22"))


 Autor: Dawid
