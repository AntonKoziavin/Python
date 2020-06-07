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
        if age in range(18, 75):
            self.__age = age
        else:
            print("Wrong age")

    def info(self):
        print("Имя:", self.__name, "\tВозраст", self.__age)


class Employee(Person):
    def __init__(self, name, age, company):                     # Изменение конструктора с доп. атрибутом
        Person.__init__(self, name, age)                        # Включаем конструктор суперкласса
        self.company = company                                  # Добавляем новый атрибут

    def info(self):                                             # Изменение метода info
        Person.info(self)                                       # Включаем метод суперкласса
        print("Компания:", self.company)                        # Добавляем новую строку


class Student(Person):
    def __init__(self, name, age, university):
        Person.__init__(self, name, age)
        self.university = university

    def info(self):
        Person.info(self)
        print("Университет:", self.university)


people = [Person("Tom", 21), Employee("Anton", 24, "Itransition"), Student("Sam", 18, "Harvard")]
for human in people:
    human.info()
    print()

for person in people:                                       # Проверка типа объекта на принаждежность к каждому классу
    if isinstance(person, Student):                         # Если объект принадлежит к классу Student
        print(person.university)                            # Вывод его атрибута university
    elif isinstance(person, Employee):
        print(person.company)
    else:
        print(person.name)
