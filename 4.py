while True:
    num_input = input("Введите число: → ")
    
    if num_input.lower() == 'exit':
        print("Выход из программы...")
        break
    
    if num_input.lstrip('-').isdigit():
        num_length = len(num_input.lstrip('-'))
        print(f"В этом числе {num_length} цифры.")
    else:
        print("Ошибка: данные не являются числом.")
