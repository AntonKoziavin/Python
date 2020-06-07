import os
try:
    os.mkdir("Hello")                           # Создание папки в текущей директории
except Exception as e:
    print(e)                                    # Для удаления папок - rmdir
try:
    os.mkdir("c://some_dir")                    # Создание папки на диске С
except Exception as e:
    print(e)
try:
    os.mkdir("c://some_dir/hello")              # Создание подпапки
except Exception as e:
    print(e)
with open("C://some_dir/some_file.txt", "w") as file:
    file.write("Hey_world")
try:
    os.rename("C://some_dir/some_file.txt",     # Переименовывание созданного файла
              "C://some_dir/new_file.txt")
except Exception as e:
    print(e)
try:
    os.remove("C://some_dir/some_file.txt")     # Удаление первоначального файла
except Exception as e:
    print(e)
if os.path.exists("C://some_dir/new_file.txt"):          # Проверка наличия файла
    print("Файл существует")
else:
    print("Файл не существует")
