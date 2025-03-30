number = input("Введите число: ")

if number.lstrip('-').isdigit():
    num = int(number)
    if num > 0:
        if num % 2 == 0:
            print(f"Число {num} является четным")
        else:
            print(f"Число {num} не является четным")
    else:
        print("Ошибка: введите положительное число")
else:
    print("Ошибка: введено не число")
