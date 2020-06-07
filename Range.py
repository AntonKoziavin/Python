for i in range(5):
    print(i, end=" ")       #end - удаление новой строки после print и добавление "_"
print("")
for i in range(1,5):
    print(i, end=" ")
print("")
for i in range(2,10,2):
    print(i, end=" ")
print("")
for i in range(5,0,-1):
    print(i, end=" ")
print("")
print("")
print("Создание таблицы умножения")
for i in range(1,10):
    for j in range(1,10):
        print(i * j, end="\t")
    print("\n")
