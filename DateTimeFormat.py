from datetime import datetime
import locale                                                   # Импорт для локализации

date = datetime.now()
print(date.strftime("%A"))                                      # Название дня недели
print(date.strftime("%a"))                                      # Сокращенное название дня недели
print(date.strftime("%B"))                                      # Название месяца
print(date.strftime("%b"))                                      # Сокращенное название месяца
print(date.strftime("%d"))                                      # День месяца, дополненный нулем (05)
print(date.strftime("%m"))                                      # Номер месяца, дополненный нулем
print(date.strftime("%Y"))                                      # Год полностью
print(date.strftime("%y"))                                      # Последние 2 числа года
print(date.strftime("%H"))                                      # Часы в формате 24
print(date.strftime("%I"))                                      # Часы в формате 12
print(date.strftime("%M"))                                      # Минуты
print(date.strftime("%S"))                                      # Секунды
print(date.strftime("%f"))                                      # Микросекунды
print(date.strftime("%p"))                                      # Указатель AM\PM
print(date.strftime("%c"))                                      # Дата и время для текущей локали
print(date.strftime("%x"))                                      # Дата для текущей локали
print(date.strftime("%X"))                                      # Время для текущей локали
print(date.strftime("%d(%A)-%m(%B)-%Y %H:%M:%S"))
locale.setlocale(locale.LC_ALL, "")                             # Установка локали
print(date.strftime("%d(%A)-%m(%B)-%Y %H:%M:%S"))




