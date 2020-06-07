numbers1 = [1, 2, 3, 4, 5]
numbers2 = list(numbers1)
print(numbers1)
print(numbers2)
print()
print("Вывод конкретных элементов списка")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[0])       # Первый
print(numbers[2])       # Третий
print(numbers[-1])      # Последний
numbers[0] = 125        # Изменение первого элемента списка
print(numbers[0])
print()
print("Задача списка одинаковых элементов")
numbers = [5]*6
print(numbers)
print()
print("Задача списка с помощью range")
numbers1 = list(range(10))
numbers2 = list(range(2, 8))
numbers3 = list(range(8, 2, -2))
print(numbers1)
print(numbers2)
print(numbers3)
print()
print("Перебор элементов")
companies=["Microsoft", "Google", "Oracle", "Apple"]
for item in companies:
    print(item)
print()
print("Перебор с помощью while")
i=0
while i<len(companies):             #len()-количество элементов списка
    print(companies[i])
    i +=1
print()
print("Сравнение списков")
numbers1=[1,2,3,4,5]
numbers2=list(range(1,6))
print(numbers1,"=",numbers2,"?")
if numbers1==numbers2:
    print("Списки равны")
else:
    print("Списки не равны")
print()
print("Методы и функции для работы со списками")
users = ["Tom", "Bob"]
print(users)
users.append("Alice")       #Добавление в конец списка
users.insert(1, "Bill")     #Добавление по индексу(второй номер)
print(users)
i=users.index("Tom")        #Получение номера для элемента
print("Порядковый номер \"Tom\"=", i)
removedItem=users.pop(i)    #Удаление элемента по полученному номеру
print(users)
users.remove(users[-1])     #Удаление последнего элемента
print(users)
users.clear()               #Очистка списка
print(users)
print()
print("Если элемент не найден во избежание исключений при работе с remove и index используется in")
companies=["Microsoft", "Google", "Oracle", "Apple"]
item="Oracle"
print(companies)
if item in companies:
    companies.remove(item)
print(companies)
print()
print("Подсчет вхождений")
users=["Tom", "Bob", "Alice", "Tom", "Bill","Tom"]
print(users)
print("Количество \"Tom\"", users.count("Tom"))
print()
print("Сортировка")
users.sort()
print(users)
print("Обратная сортировка")
users.reverse()
print(users)
print("Сортировка по регистру")
users=["Tom", "bob", "alice", "tom", "Bill", "Tom"]
users.sort(key=str.lower)
print(users)
users=["Tom", "bob", "alice", "tom", "Bill", "Tom"]
usersSorted=sorted(users, key=str.lower)        #Сортировка без изменения оригинала
print(usersSorted)
print(users)
print()
print("Минимум и максимум")
numbers=[1,4,90,74,15]
print(numbers)
print("Минимум:", min(numbers))
print("Максимум:",max(numbers))
print()
print("Копирование списков")
users1=["Tom", "Alice", "Bob"]
users2=users1
users2.append("Sam")        #Изменения при копировании вносятся сразу в оба списка
print(users1)
print(users2)
print("Копирование без замены оригинала")
import copy
users1=["Tom", "Alice", "Bob"]
users2= copy.deepcopy(users1)
users2.append("Sam")
print(users1)
print(users2)
print()
print("Копирование части списка")
users=["Tom", "bob", "alice", "tom", "Bill", "Tom"]
print(users)            #Каждую часть можно вынести как переменную
print(users[:3])        #с 0 по 3
print(users[1:3])       #с 1 по 3
print(users[1:5:2])     #с 1 по 5 с шагом 2
print()
print("Соединение списков")
users1=["Tom", "Alice", "Bob"]
users2=["Bill", "Sam", "Anton"]
print(users1+users2)
print()
print("Списки списков")
users=[
    ["Tom", 29],        #2 элемента в первом элементе основного списка
    ["Anton", 23],
    ["Bill", 33]
]
print(users[0])         #Первый элемент списка
print(users[0][0])      #Первый элемент первого списка
print(users[0][1])
print()
print("Операции с вложенными списками протекают так же, как и с одинарными")
users=[
    ["Tom", 29],
    ["Anton", 23],
    ["Bill", 33]
]
print(users)
user=list()                 #Добавление вложенного списка
user.append("Bob")
user.append(19)
users.append(user)
print(users[-1])
users[-1].append("+375(33)-335-44-19")
print(users)
users[-1].pop()             #Удаление последнего элемента списка
print(users)
users.pop(-1)               #Удаление последнего вложенного списка
print(users)
users[0]=["Sam", 25]        #Изменение первого элемента списка
print(users)
print()
print("Перебор вложенных списков")
users=[
    ["Tom", 29],
    ["Anton", 23],
    ["Bill", 33]
]
for user in users:
    for item in user:
        print(item, end="|")



