try:
    number1 = int(input("Введите число 1: "))
    number2 = int(input("Введите число 2: "))
    print("Результат деления:", round(number1 / number2, 2))
except ValueError:                          #Ошибка значения
    print("Ошибка ввода")
except ZeroDivisionError:                   #Деление на 0
    print("Нельзя делить на 0")
except Exception:
    print("Общее исключение")
print("Завершение работы")
print()
print("Блок finally")
try:
    number=int(input("Введите число: "))
    print("Введенное число: ",number)
except ValueError as e:                     #Задание исключения как переменной
    print("Ошибка ввода: ", e)              #Вывод исключения
finally:                                    #В любом случае выполняется
    print("Блок завершил работу")
print("Конец программы")
print()
print("Генерация исключений raise")
try:
    number1 = int(input("Введите число 1: "))
    number2 = int(input("Введите число 2: "))
    if number2 == 0:
        raise Exception("Второе число не должно равняться 0")   #
    print("Результат деления:", round(number1 / number2, 2))
except ValueError:
    print("Ошибка ввода")
except Exception as e:
    print(e)
print("Завершение работы")