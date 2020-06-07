class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(18, 99):
            self.__age = age
        else:
            print("Wrong age")

    def info(self):
        print(self.__name, self.__age)

    def __str__(self):                                                      # Строковое представление объекта
        return "Имя: {}   Возраст: {}".format(self.__name, self.__age)


anton = Person("Anton", 24)
print(anton)                                                                # Вывод объекта в строку

