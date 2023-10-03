def count_digits(number):
    return len(str(number))

user_input = input("Введіть число: ")

try:
    number = int(user_input)
    digit_count = count_digits(number)
    print(f"Кількість цифр у числі {number}: {digit_count}")
except ValueError:
    print("Введене значення не є числом.")
