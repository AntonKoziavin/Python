class Person:
    name = "Anton"

    def display_info(self):
        print("Привет, меня зовут", self.name)


person1 = Person()
person1.display_info()
person2 = Person()
person2.name = "Ann"
person2.display_info()


class Person:
    def __init__(self, imya):                           # Конструктор
        self.name = imya

    def display_info(self):
        print("Привет, меня зовут", self.name)


person1 = Person("Antoshka")
person1.display_info()
del person1                                             # Деструктор вне класса
try:
    person1.display_info()
except:
    print("Объект не найден")


class Person:
    def __init__(self, imya, age):                      # Конструктор
        self.name = imya
        self.age = age

    def __del__(self):                                  # Деструктор внутри класса
        print(self.name, "Удалён")

    def display_info(self):
        print("Привет, меня зовут", self.name + ".", "Мне", self.age)


person1 = Person("Antoshka", "24")
person1.display_info()
person1.age = "20"
person1.display_info()
person2 = Person("Anya", "24")
person2.display_info()
