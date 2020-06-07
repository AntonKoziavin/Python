import pickle
filename = "Files_binary.dat"
name = "Anton"
age = 23
with open(filename, "wb") as file:         # wb вместо w для бинарных файлов
    pickle.dump(name, file)
    pickle.dump(age, file)
with open(filename, "rb") as file:
    name = pickle.load(file)               # Считывание первого записанного объекта
    age = pickle.load(file)                # Считыванеие второго записанного объекта
    print("Имя:", name, "\nВозраст:", age)
print()
filename = "Files_binaries.dat"
users = [
    ["Anton", 23, False],
    ["Bill", 30, True],
    ["Sam", 29, False]
]
with open(filename, "wb") as file:
    pickle.dump(users, file)                      # Всего 1 объект - вложенный список
with open(filename, "rb") as file:
    users_from_file = pickle.load(file)
    for user in users_from_file:
        print("Имя:", user[0], "Возраст:", user[1], "Женат:", user[2])
