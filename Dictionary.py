print("Примеры словарей:")
dictionary = {"Ключ1: Значение1, ключ2: Значение2, ..."}
users1 = {1: "Tom", 2: "Anton", 3: "Bill"}
elements = {"Au": "Золото", "Fe": "Железо", "H": "Водород"}
objects1 = {1: "Tom", "2": True, 3: 100.6}
objects2 = {}
users2 = dict()                 # Круглые скобки
print()
print("Для преборазования списка в словарь неоходимо,"
      " чтобы словарь включал в себя вложенный список, "
      "состоящий из 2 элементов")
users_list = [
    ["+375(33)-335-44-19", "Anton"],
    ["+375(29)-667-60-28", "Olga"],
    ["+375(33)-335-44-16", "Sergei"]
]
users_dict = dict(users_list)
print(users_dict)
print("Идентично преобразовываются и двухмерные кортежи")
print()
print("Получение и изменение элементов по ключам")
print(users_dict["+375(33)-335-44-19"])
users_dict["+375(29)-667-60-28"] = "Mama"       # Изменение элемента
print(users_dict["+375(29)-667-60-28"])
users_dict["123"] = "Sam"                       # Добавление элемента
print(users_dict["123"])
print("Для обхода исключений используем функцию in")
key = "123"
if key in users_dict:
    user = users_dict[key]
    print(user)
else:
    print("Пользователь не найден")
print()
print("Также можно использовать метод get")
user = users_dict.get("1")                      # Возвращает None, если не найден
print(user)
user = users_dict.get("1", "Unknown user")      # Возвращает выражение после запятой, если не найден
print(user)
print()
print("Удаление элементов по ключам")
del users_dict["123"]
print(users_dict)
print("Для избежания исключения также используем in")
users_dict["123"] = "Sam"                       # Добавим обратно перед удалением
key = "123"
if key in users_dict:
    user = users_dict[key]
    print("Пользователь", user, "удалён")
    del user
else:
    print("Пользователь не найден")
print()
print("Удаление через pop")
users_dict["123"] = "Sam"                       # Добавим обратно перед удалением
key = "123"
user = users_dict.pop(key)                      # Метод pop позволяет возвращать элемент, даже удалив его из словаря
print(user)
print(users_dict)
key = "1"
users_dict["123"] = "Sam"                       # Добавим обратно перед удалением
user = users_dict.pop(key, "Unknown user")      # Возвращает выражение после запятой, если не найден
print(user)
users_dict.clear()                              # Очистка словаря
print()
print("Копирование и объединение словарей")
users = {1: "Anton", 2: "Sam", 4: "Bill"}
users2 = users.copy()
print(users2)
users3 = {3: "Alex", 5: "Bob"}
users.update(users3)
print(users)
print("Изменения вносят в словарь users, чтобы он остался без изменений, можно создать новый словарь")
users4 = users2.copy()
print(users4)
users4.update(users3)
print(users4)
print()
print("Перебор словаря")
users = {
    "+375(33)-335-44-19": "Anton",
    "+375(29)-667-60-28": "Olga",
    "+375(33)-335-44-16": "Sergei"
}
for key in users:
    print(key, "-", users[key])
print()
print("Метод items")
for key, value in users.items():        # Он возвращает набор кортежей, а так же переменные key,value
    print(key, "-", value)
print()
print("keys, values")                   # Возврат ключей и значений по отдельности
for key in users.keys():
    print(key)
for value in users.values():
    print(value)
print()
print("Комплексные словари")
users = {
    "Anton": {
        "phone": "+375(33)-335-44-19",
        "email": "anton_koziavin@gmail.com"
    },
    "Bill": {
        "phone": "788763908",
        "email": "superbob@gmail.com"
    }
}
print(users)
old_email = users["Anton"]["email"]                 # Возврат по двум ключам
print(old_email)
users["Anton"]["email"] = "superanton@mail.ru"      # Замена по двум ключам
print(users)
print("Во избежание ошибки при поиске ключами:")
key = "skype"
if key in users["Anton"]:
    print(users["Anton"][key])
else:
    print("Ключ", key, "Не найден")
