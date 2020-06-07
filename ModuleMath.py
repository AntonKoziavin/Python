import math
print(math.pow(5, 2))                               # Возведение числа в степень
print(math.sqrt(10))                                # Квадратный корень
print(math.ceil(4.261209))                          # Округление до целого числа в большую сторону
print(math.floor(4.261209))                         # Округление до целого числа в меньшую сторону
print(math.factorial(4))                            # Факториал
print(math.degrees(3.14158))                        # Перевод из радиан в градусы
print(math.radians(180))                            # Перевод из градусов в радианы
print(round(math.cos(math.radians(60)), 5))         # Косинус в радианах (acos - арккосинус)
print(round(math.sin(math.radians(30)), 5))         # Синус в радианах (asin - арксинус)
print(round(math.tan(math.radians(30)), 5))         # Тангенс в радианах (atan - арктангенс)
print(math.log(2048, 2))                            # Логарифм числа по основанию
print(math.log10(1000))                             # Десятичный логарифм
print()
radius = 30
area = math.pi * math.pow(radius, 2)                # Применение константы Пи
print(round(area))
print(math.log(10, math.e))                         # Применение константы e .Натуральный логарифм числа 10
