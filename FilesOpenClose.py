print("Открытие файлов")
print("Первый параметр указывает путь к файлу, "
      "второй - режим открытия файла: \nr - для чтения,"
      "\nw - создание нового для записи или перезаписи существующего, "
      "\na - создание нового для записи или добавления к существующему,"
      "\nb - для работы с бинарными файлами")
new_file = open("Def.py", "r")
print("Для избегания исключений")
try:
    some_file = open("Files_Hello.txt", "w")
    try:
        some_file.write("Hello_world")
    except Exception as e:
        print(e)
    finally:
        some_file.close()
except Exception as ex:
    print(ex)
print("Для упрощения используется конструкция with")
with open("Files_Hello.txt", "a") as my_file:
    my_file.write("\nHello_world_again")
