class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(18, 75):
            self.__age = age
        else:
            print("Wrong age")

    @property
    def name(self):
        return self.__name

    def info(self):
        print(self.__name, self.__age)


person1 = Person("Anton", 24)
person1.info()


class Employee(Person):                                 # Наследование
    def details(self, company):                         # Новый метод подкласса
        print(self.name, company)


employee1 = Employee("Anton", 24)                       # Параметры суперкласса Person
employee1.details("ITransition")                        # Метод подкласса
employee1.age = 20                                      # Сеттер суперкласса работает и для объектов подкласса
employee1.info()                                        # Метод суперкласса
