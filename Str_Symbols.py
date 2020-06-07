string = "Hello World"
print(string[0])                        # Вывод первого символа
print(string[5])                        # Вывод пробела
print(string[-2])                       # Вывод второго с конца символа
try:
    print(string[20])                   # Вывод несуществующего символа
except Exception as e:
    print(e)
print()
try:
    string[1] = "E"                     # Нельзя изменять символы строки, только строки целиком
except Exception as e:
    print(e)
print()
print(string[:5])                       # Вывод символов от 0 до 5
print(string[1:-1])                     # Вывод символов от 1 до последнего
print(string[1:-1:2])                   # Вывод символов от 1 до последнего с шагом 2
print(len(string))                      # Длина строки
print(ord("A"))                         # Вывод числового значения для символа в кодировке Unicode
print()
print("Hello" in string)                # Существует ли подстрока "Hello" в строке
print("Anton" in string)
for symbol in string:                   # Перебор символов в строке
    print(symbol, end=" ")  
