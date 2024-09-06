import random


def get_numbers_ticket(min_val, max_val, quantity):
    # Перевіряємо обмеження параметрів
    if min_val < 1 or max_val > 1000 \
            or min_val > max_val or quantity < 1:
        return []

    # Генеруємо унікальний набір чисел
    random_numbers = random.sample(range(min_val, max_val + 1), quantity)

    # Повертаємо відсортований список
    return sorted(random_numbers)


# Приклад використання:
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
