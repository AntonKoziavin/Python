import locale
locale.setlocale(locale.LC_ALL, "de")                   # Локализация всех переменных для Германии
number = 12345.6789                                     # Локализация чисел
print(number)                                           # Неотформатированное число в англосаксонской локализации
print(locale.format_string("%f", number))               # Локализация в число с плавающей запятой
print(locale.format_string("%.2f", number))             # Локализация в число с 2 символами после запятой
print(locale.format_string("%d", number))               # Локацизация в цепое число
print(locale.format_string("%e", number))               # Локализация в экспоненциональный вид числа
money = 234.567
print(locale.currency(money))                           # Локализация валют
print()
locale.setlocale(locale.LC_ALL, "")                     # Не задаем локализацию
print(locale.format_string("%.2f", number))
print(locale.getlocale())                               # Вывод используемой локализации

