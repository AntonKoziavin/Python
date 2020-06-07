print("tuple = кортеж (неизменяемый список list)")
print()
print("Способы задачи tuple")
user = ("Tom", 23)
print(user)
user = "Anton", 23
print(user)
user = "Anton",
print(user)
print()
print("Задача tuple из list")
user_list = ["Tom", "Bob", "Kate", "Anton", "Daniel"]
user_tuple = tuple(user_list)
print(user_tuple)
print()
print("Обращение к элементам в tuple аналогично обращению в list")
print(user_tuple[0])
print(user_tuple[2])
print(user_tuple[1:4])
print()
print("Возможность разложить кортеж на отдельные переменные")
user = "Anton", 23, False
name, age, is_married = user
print(name)
print(age)
print(is_married)
print(len(user))  # Длина кортежа
print()
print("При возвращении нескольких значений из функции "
      "они фактически возвращаются в виде кортежа")
def get_user():
    name = "Anton"
    age = 23
    is_married = False
    return name, age, is_married
user = get_user()
print(user)
print(user[0])
print()
print("Перебор кортежей аналогичен перебору списков")
user = ("Tom", 22, False)
for item in user:
    print(item)
user = ("Tom", 22, False)
i = 0
while i < len(user):
    print(user[i])
    i += 1
print()
print("Как и для списков наличие значения в кортеже "
      "можно проверить через in")
user = ("Tom", 22, False)
name = "Tom"
if name in user:
    print("Пользователя зовут Tom")
else:
    print("Пользователь имеет другое имя")
countries = (
    ("Germany", 80.2, (("Berlin", 3.326), ("Hamburg", 1.718))),
    ("France", 66, (("Paris", 2.2), ("Marsel", 1.6)))
)
for country in countries:
    countryName, countryPopulation, cities = country
    print("\nCountry: {}  population: {}".format(countryName, countryPopulation))
    for city in cities:
        cityName, cityPopulation = city
        print("City: {}  population: {}".format(cityName, cityPopulation))
