def find_minimum(a, b, c, d, e):
    return min(a, b, c, d, e)

num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))
num4 = float(input("Введіть четверте число: "))
num5 = float(input("Введіть п'яте число: "))

min_number = find_minimum(num1, num2, num3, num4, num5)
print(f"Мінімальне число: {min_number}")
