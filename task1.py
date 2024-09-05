from datetime import datetime, date

def get_days_from_today(date_str):
    # Перетворюємо рядок у об'єкт datetime
    target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    # Отримуємо поточну дату
    today = date.today()
    # Обчислюємо різницю між датами
    delta = target_date - today
    # Повертаємо кількість днів
    return delta.days

# Приклад використання:
print(get_days_from_today("2021-10-09"))  # Якщо сьогодні 5 травня 2021 року, результат: 157
