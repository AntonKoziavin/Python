import shelve
filename = "Files_states"
with shelve.open(filename) as states:
    states["London"] = "Great Britain"
    states["Paris"] = "France"
    states["Berlin"] = "Germany"
    states["Madrid"] = "Spain"
with shelve.open(filename) as states:
    print(states["London"])
    print(states["Madrid"])
    key = "Brussels"                                    # Обход исключения при отсутствии ключа
    if key in states:
        print(states[key])
    print()
    print(states.get("Brussels", "Не найден ключ"))     # Обход через get, второй параметр выводится при исключении
    print()
    for key in states:                                  # Перебор данных
        print(key, "-", states[key])
    print()
    for city in states.keys():                          # Перебор ключей
        print(city, end=" ")
    print()
    for country in states.values():                     # Перебор значений
        print(country, end=" ")
    print()
    print()
    for state in states.items():                        # Возврат кортежей
        print(state)
    print()
    states["London"] = "United Kingdom"
    states["Brussels"] = "Belgium"                      # Будет присутствовать со след. запуска, если не обнулить
    for key in states:
        print(key, "-", states[key])
    print()
    state = states.pop("London", "Not Found")           # Удаление по ключу или вывод Not Found при исключении
    print(state)                                        # Вывод значения по удаленному ключу
    print()
    del states["Madrid"]                                # Простое удаление
    for key in states:
        print(key, "-", states[key])
    states.clear()                                      # Очистка
