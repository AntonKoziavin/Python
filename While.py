choice = "y"
while choice.lower() == "y":
    print("Привет")
    choice = input("Для продолжения введите Y, а для выхода любую другую клавишу: ")
print("Завершение программы")
print("")
print("Вычислим факториал:")
number = int(input("Введите число: "))
i = 1
factorial = 1
while i<=number:
    factorial *= i
    i += 1
print("Факториал числа", number, "равен", factorial)
