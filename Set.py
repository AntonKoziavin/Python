print("Множество содержит только уникальные значения")
print("Способы задания множества")
users = {"Anton", "Bill", "Tom", "Anton"}
print(users)                                        # "Anton" вывело только 1 раз
users_list = ["Anton", "Bill", "Tom", "Anton"]
users2 = set(users_list)                            # Задача множества из списка(кортежа)
print(users2)
users3 = set()                                      # Задача пустого множества
print(len(users2))                                  # Длина множества
users3.add("Sam")                                   # Добавление элемента
print(users3)
print()
print("Удаление элементов")
users = {"Anton", "Bill", "Tom", "Anton"}
user = "Bill"
if user in users:
    users.remove(user)
    print(users)
else:
    print("Пользователь не найден")
print("Более удобный метод удаления discard не генерирует исключения")
users.add("Bill")
print(users)
users.discard("Tom")
users.discard("Sam")                                # Удаляем невходящий во множество элемент
print(users)
users.clear()                                       # Очистка множества
print()
print("Перебор множества")
users = {"Anton", "Bill", "Tom", "Anton"}
for user in users:
    print(user)
print()
print("Операции с множествами")
users2 = users.copy()                               # Копирование
print(users2)
users3 = {"Bob", "Alex"}
users4 = users2.union(users3)                       # Объединение 2 множеств в новое
print(users4)
users = {"Anton", "Bill", "Tom", "Anton"}
users2 = {"Anton", "Bob", "Alex", "Bill"}
users3 = users.intersection(users2)                 # Возврат только пересекающихся в 2 множествах элементов
print(users3)
print(users & users2)                               # Логическое умножение как аналог intersection
users3 = users.difference(users2)                   # Вычитание: возврат элементов 1 множества, которых нет во втором
print(users3)
print(users - users2)                               # Аналог difference
users = {"Anton", "Bill", "Tom", "Anton"}
database = {"Anton", "Sam", "Caroline", "Bill",
            "George", "Mike", "Tom", "Anton"}
print(users.issubset(database))                     # Является ли users частью database?
print(database.issuperset(users))                   # Включает ли в себя database множество users?
print()
print("Задание неизменяющегося множества")
users = frozenset({"Anton", "Bill", "Tom", "Anton"})
print(users)
