def calculate_product_in_range(lower, upper):
    if lower > upper:
        lower, upper = upper, lower

    product = 1
    for num in range(lower, upper + 1):
        product *= num
    return product


lower_limit = int(input("Введіть нижню межу діапазону: "))
upper_limit = int(input("Введіть верхню межу діапазону: "))

result = calculate_product_in_range(lower_limit, upper_limit)
print(f"Добуток чисел у діапазоні [{lower_limit}, {upper_limit}]: {result}")
