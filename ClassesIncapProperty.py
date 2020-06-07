class Person:
    def __init__(self, name):
        self.__name = name                                              # Приватный атрибут __name
        self.__age = 24                                                 # Приватный атрибут __age

    @property                                                           # Аннотация
    def age(self):                                                      # Геттер - получение значения аттрибута
        return self.__age

    @age.setter
    def age(self, age):                                                 # Сеттер идет после геттера
        if age in range(1, 100):
            self.__age = age
        else:
            print("Неверное значение возраста")

    @property
    def name(self):                                                     # Геттер - получение значения аттрибута
        return self.__name

    def display_info(self):
        print("Меня зовут:", self.__name, "Мой возраст:", self.__age)


anton = Person("Anton")
anton.display_info()
print(anton.age)                                                        # Доступ к аттрибутам
anton.age = 43                                                          # Изменение аттрибута
anton.display_info()





