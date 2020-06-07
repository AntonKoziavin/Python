class Test:                                                             # Задача класса без инкапсуляции
    def __init__(self, name):
        self.name = name
        self.age = 18

    def display_info(self):
        print("Меня зовут:", self.name, "Мой возраст:", self.age)


class Person:                                                           # Инкапсуляция - закрытие изменения аттрибутов
    def __init__(self, name):
        self.__name = name                                              # Приватный атрибут __name
        self.__age = 24                                                 # Приватный атрибут __age

    def get_name(self):                                                 # Геттер - получение значения аттрибута
        return self.__name

    def set_age(self, age):                                             # Сеттер - установка значения аттрибута
        if age in range(1, 100):
            self.__age = age
        else:
            print("Неверное значение возраста")

    def get_age(self):                                                  # Геттер - получение значения аттрибута
        return self.__age

    def display_info(self):
        print("Меня зовут:", self.__name, "Мой возраст:", self.__age)


test = Test("Mary")
test.display_info()
test.name = "Bill"                                                     # Изменение атрибутов класса без инкапсуляции
test.age = -140
test.display_info()
print("Инкапсуляция включена")
anya = Person("Anya")
anya.__age = 43                                                         # Доступ закрыт, возраст не изменится
anya.display_info()
anya.set_age(53487)                                                     # Возраст не изменится
anya.display_info()
anya.set_age(30)                                                        # Возраст изменится
anya.display_info()

