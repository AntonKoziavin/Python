print("Запись в файл двумя методами")
with open("Files_Hello.txt", "w") as hello:
    print("Hello_world", file=hello)
    hello.write("Bye_world")
print()
print("Чтение файла")
with open("Files_Hello.txt", "r") as hello:
    for line in hello:
        print(line, end="")
print("\n")
with open("Files_Hello.txt", "r") as hello:
    str1 = hello.readline()                     # Построчный метод считывания
    print(str1, end="")
    str2 = hello.readline()
    print(str2)
print()
with open("Files_Hello.txt", "r") as hello:
    data = hello.read()                         # Полное считывание файла
    print(data)
print()
with open("Files_Hello.txt", "r") as hello:
    content = hello.readlines()                 # Считывание всех строк и вывод по номеру
    str1 = content[0]
    str2 = content[1]
    print(str1, end="")
    print(str2)
print()
print("Если кодировка не совпадает с ASCII")
file = "Files_Hello.txt"
with open(file, encoding="utf8") as hello:
    text = hello.read
print()
print("Скрипт для закрепления")
filename = "Files_Test"
messages = list()
for i in range(4):
    message = input("Введите строку " + str(i+1) + ":")
    messages.append(message)
with open("Files_Test", "w") as test:
    for message in messages:
        test.write(message)
print("Считанные сообщения:")
with open("Files_Test", "r") as test:
    for message in messages:
        print(message)
