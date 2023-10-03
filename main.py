def display_square(side_length, fill, filled=True):
    for i in range(side_length):
        if filled:
            row = fill * side_length
        else:
            if i == 0 or i == side_length - 1:
                row = fill * side_length
            else:
                row = fill + " " * (side_length - 2) + fill
        print(row)

print("Заповнений квадрат:")
display_square(5, "$", True)

print("Порожній квадрат:")
display_square(5, "$", False)
