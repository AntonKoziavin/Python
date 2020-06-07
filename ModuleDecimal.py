from decimal import Decimal, ROUND_HALF_EVEN, ROUND_HALF_UP, ROUND_05UP, ROUND_CEILING, ROUND_HALF_DOWN, ROUND_FLOOR
number = 0.1 + 0.1 + 0.1
print(number)                                       # Неточный результат при работе с float
number = Decimal("0.1")                             # Использование конструктора Decimal для числа 0.1
number += number + number
print(number)                                       # Точный результат
print(Decimal(number) + 2)                          # Можно использовать целые числа
try:                                                # Но нельзя дробные
    print(Decimal(number) + 0.2)
except Exception:
    print("Нельзя использовать дробные числа вместе с Decimal")
number = Decimal("0.100")                           # Задача дополнительных знаков после запятой
print(number + number)
print("ROUND_HALF_EVEN ")                           # Округление в большую сторону нечетных цифр, если последнее число>4
number = Decimal("0.4444")
print(number.quantize(Decimal("1.00")))
number = Decimal("12.025")
print(number.quantize(Decimal("0.01"), ROUND_HALF_EVEN))            # Округление только нечетных цифр (тут 2)
number = Decimal("12.035")
print(number.quantize(Decimal("0.01"), ROUND_HALF_EVEN))            # Округление успешно
print("ROUND_HALF_UP ")                                         # Округляет в большую сторону, если последнее число >=5
number = Decimal("12.025")
print(number.quantize(Decimal("0.01"), ROUND_HALF_UP))
number = Decimal("12.024")
print(number.quantize(Decimal("0.01"), ROUND_HALF_UP))
print("ROUND_HALF_DOWN ")                                       # Округляет в большую сторону, если последнее число >5
number = Decimal("12.026")
print(number.quantize(Decimal("0.01"), ROUND_HALF_DOWN))
number = Decimal("12.025")
print(number.quantize(Decimal("0.01"), ROUND_HALF_DOWN))
print("ROUND_05UP ")                                            # Округляет только 0 до 1, если после него идет 5
number = Decimal("12.005")
print(number.quantize(Decimal("0.01"), ROUND_05UP))
number = Decimal("12.025")
print(number.quantize(Decimal("0.01"), ROUND_05UP))
print("ROUND_CEILING")                                          # Округляет в большую сторону при любой цифре
number = Decimal("12.001")
print(number.quantize(Decimal("0.01"), ROUND_CEILING))
number = Decimal("12.025")
print(number.quantize(Decimal("0.01"), ROUND_CEILING))
print("ROUND_FLOOR")                                            # Не округляет при любой цифре
number = Decimal("12.005")
print(number.quantize(Decimal("0.01"), ROUND_FLOOR))
number = Decimal("12.025")
print(number.quantize(Decimal("0.01"), ROUND_FLOOR))