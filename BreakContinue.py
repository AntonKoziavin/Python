print("Для выхода нажите Y")
while True:         #Вечный цикл
    data = input("Введите сумму, которую хотите обменять: ")
    if data.lower() == "y":
        break
    money = int(data)
    if money < 1:
        print("Сумма должна быть положительной!")
        continue    #Запуск цикла с начала
    cache = round(money / 56, 2)
    print("Ваша сумма:", cache, "долларов США")
print("Завершение работы")