# Ввод данных
name = input("Ваше имя: ")
surname = input("Фамилия: ")
age = input("Возраст: ")

# Реализация через format
print("\nРеализация через format:")
print("Ваше имя: {}, Фамилия: {}, Возраст: {} лет".format(name, surname, age))

# Реализация через f-string
print("\nРеализация через f-string:")
print(f"Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет")
