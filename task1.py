from datetime import datetime, date
import sys


def get_days_from_today(date_str):
    # Перетворюємо рядок у об'єкт datetime
    try:
        target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except Exception as e:
        sys.exit(e)
    # Отримуємо поточну дату
    today = date.today()
    # Обчислюємо різницю між датами
    delta = target_date - today
    # Повертаємо кількість днів
    return delta.days


# Приклад використання:
# Якщо сьогодні 5 травня 2021 року, результат: 157
print(get_days_from_today("2021-10-09"))
