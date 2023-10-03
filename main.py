def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]

user_input = input("Введіть число: ")

try:
    number = int(user_input)
    result = is_palindrome(number)
    if result:
        print(f"Число {number} є паліндромом.")
    else:
        print(f"Число {number} не є паліндромом.")
except ValueError:
    print("Введене значення не є числом.")
