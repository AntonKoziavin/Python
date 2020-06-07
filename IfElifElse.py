age = 18
if age > 21:
    print("Доступ разрешен")
elif age >=18:
    print("Доступ частично разрешен")
else:
    print("Завершение работы")
print("Так же конструкция If сама может содержать в себе конструкцию If:")
age = 18
if age >=18:
    print("Больше или равно 18")
    if age > 21:
        print("Больше 21")
    else:
        print("От 18 до 21")
else:
    print("Меньше 18")
print("")
print("Тест-программа на закрепление")
usd = 57
euro = 60
money = int(input("Введите сумму, которую вы хотите обменять: "))
currency = int(input("Укажите вод валюты (доллары-400, евро-401): "))
if currency == 400:
    cash = round(money / usd, 2)
    print("Валюта: доллары США")
elif currency == 401:
    cash = round(money / euro, 2)
    print("Валюта: Евро")
else:
    cash=0
    print("Неизвестная валюта")
print("К получению: ", cash)