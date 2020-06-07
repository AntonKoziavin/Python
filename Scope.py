name="Антон"            #Переменная глобальная (может использоваться где угодно)
def say_hello():
    print("Привет,", name)
def say_goodbye():
    print("Пока,", name)
say_hello()
say_goodbye()
print("")
print("Задача локальных переменных(внутри функции)")
def say_hello():
    name="Антон"
    surname="Козявин"
    print("Привет,", name, surname)
def say_goodbye():
    name="Толик"
    print("Пока,", name)
say_hello()
say_goodbye()
print()
print("Локально заданная переменная замещает собой глобальную!")
print()
print("Задание глобальной переменной внутри функции")
def say_hello():
    global name
    name="Антон"
    print("Привет,", name)
say_hello()