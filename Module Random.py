import random
number = random.random()                            # От 0.0 до 1.0
print(number)
print(random.random()*100)                          # От 0.0 до 100.0
print(random.randint(20, 35))                       # От 20 до 35 (целые числа, включая последнее число)
print(random.randrange(30))                         # От 0 до 30 (целые числа, не включая последнее)
print(random.randrange(10, 20))                     # От 10 до 20
print(random.randrange(10, 20, 2))                  # От 10 до 20 с шагом 2
print()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(numbers)                             # Перемешивание списка
print(numbers)
print(random.choice(numbers))                       # Рандомное число из списка
