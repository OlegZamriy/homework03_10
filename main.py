def display_even_numbers(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num)

start = int(input("Введіть початкове число: "))
end = int(input("Введіть кінцеве число: "))

display_even_numbers(start, end)
