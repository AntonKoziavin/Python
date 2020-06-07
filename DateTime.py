from datetime import date                                       # Класс date
from datetime import time                                       # Класс time
from datetime import datetime                                   # Класс datetime


yesterday = date(2020, 3, 22)                                   # Класс date(year, month, day)
print(yesterday)
today = date.today()                                            # Метод today класса date
print(today)
print("{}-{}-{}".format(today.day, today.month, today.year))    # То же самое через format со свойствами day,month,year


current_time = time()                                           # Класс time(hour, minute, sec, microsecond)
print(current_time)
current_time = time(23, 27)
print(current_time)
current_time = time(23, 27, 55)
print(current_time)


my_time = datetime(2020, 3, 23, 23, 50)                         # Класс datetime(year,month,day,hour,minute,sec)
print(my_time)
now = datetime.now()                                            # Метод now - Вывод текущего момента времени
print(now)
print(now.date())                                               # Текущая дата метод date
print(now.time())                                               # Текущее время метод time
print("{}-{}-{} "
      "{}:{}:{}:{}".format(now.day, now.month, now.year,
                           now.hour, now.minute, now.second,
                           now.microsecond))

time = datetime.strptime("25.03.2020 22:23:45",                 # Преобразование строки в дату. d - день, m - месяц
                         "%d.%m.%Y %H:%M:%S")                   # Y - год в 4 цифрах, y - в 2, H,M,S - время
print(time)
