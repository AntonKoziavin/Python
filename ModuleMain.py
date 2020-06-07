import Module1          #Базовый импорт
rate=int(input("Введите процентную ставку: "))
money=int(input("Введите сумму:"))
period=int(input("Введите срок в месяцах:"))

result=Module1.calculate_income(rate, money, period)
print("Параметры счета:\nСумма:", money, "\nСтавка:", rate, "\n"
"Период:", period, "\nСумма на счету в конце периода:", result)
print()
print("Возможности импорта:")
import Module1 as Mod                       #Изменение имени портируемого модуля
from Module1 import calculate_income        #Импорт 1 функции из модуля

