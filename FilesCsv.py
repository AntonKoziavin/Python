import csv
filename = "Files_users.csv"
users = [
    ["Anton", 23],
    ["Anna", 24],
    ["Bob", 28]
]
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)                   # Получение объекта writer для дальнейшей записи
    writer.writerows(users)                     # Запись многомерного объекта - writerows
with open(filename, "a", newline="") as file:   # newline="" убирает лишний пропуск строки, заменяяюсь пробелом
    user = ["Sam", 30]
    writer = csv.writer(file)
    writer.writerow(user)                       # Дозапись одномерного объекта - writerow
with open(filename, "r") as file:
    reader = csv.reader(file)                   # Получение объекта reader для чтения
    for row in reader:
        print(row[0], " - ", row[1])            # row[] - элемент каждой строки
print()
filename = "Files_users2.csv"                   # Пример строк - словарей
users = [
    {"name": "Anton", "age": "23"},
    {"name": "Bill", "age": "28"},
    {"name": "Anna", "age": "24"}
]
with open(filename, "w", newline="") as file:
    columns = ["name", "age"]
    writer = csv.DictWriter(file, fieldnames=columns)       # DictWriter, DictReader = writer и reader для словарей
    writer.writeheader()                        # Запись названий столбцов
    writer.writerows(users)
