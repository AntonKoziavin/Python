text = "Hello, {first_name}.".format(first_name="Anton")                    # Именованные параметры
print(text)
info = "Name: {name}\t\t Age: {age}".format(name="Anton", age=24)
print(info)
info = "Name: {0}\t\t Age: {1}".format("Anton", 24)                         # Параметры по позиции
print(info)
print()
welcome = "Hello {:s}"                                                      # Плейсхолдер для строк
name = "Anton"
formatted_welcome = welcome.format(name)
print(formatted_welcome)
print()
source = "{:d} символов"                                                    # Плейсхолдер для чисел
number = 5
target = source.format(number)
print(target)
print()
source = "{:,d} символов"                                                   # Разделение разрядов числа
print(source.format(5000))
print()
number = 23.854738                                                          # Плейсхолдер для дробных чисел
print("{:.2f}".format(number))                                              # 2 - количество знаков после запятой
print("{:.3f}".format(915.1932878))
print("{:10.4f}".format(2873.89127))                                        # 10 - задача минимального кол-ва символов
print()
print("{:%}".format(.1234))                                                 # Плейсхолдер процентов
print("{:.1%}".format(0.03846))
print()
print("{:e}".format(12345.6789))                                            # Плейсхолдер экспоненты
print("{:.1e}".format(127834.56789))
print()
info = "Имя: %s \t Возраст: %d" % ("Антон", 23)                             # Простое форматирование
print(info)
number = 23.8598374
print("%.2f - %e" % (number, number))
