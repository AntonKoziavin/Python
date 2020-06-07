from datetime import timedelta, datetime                # Класс для промежутка времени

print(timedelta(4, 20, 800, 20, 33, 12, 0))             # timedelta(days,seconds,microsecond,millisecond,min,hour,week)
print(timedelta(hours=3))
print(timedelta(days=2, minutes=10))
current_time = datetime.now()
print(current_time)
print(current_time - timedelta(2))                      # Вычет 2 дней из текущего времени
print(current_time - timedelta(hours=10, minutes=20))   # Вычет 10 часов и 20 минут
another_time = datetime(2020, 4, 7, 21, 33)
period = current_time - another_time                    # Разница между текущей данной и заданной
print("{} дней, {} секунд, {} микросекунд"              # Возврат дней, секунд и микросекунд в разнице
      .format(period.days, period.seconds,
              period.microseconds))
print("{} секунд".format(period.total_seconds()))       # Возврат разницы в секундах и микросекундах

deadline = datetime(2020, 4, 8)                         # Проверка разницы во времени
current_time = datetime.now()
period = deadline - current_time                        # Timedelta
if current_time.date() > deadline.date():               # Сравнение дат без времени
    print("Срок сдачи проекта прошел")
elif current_time.date() == deadline.date():
    print("Срок сдачи сегодня!")
else:
    print("Осталось {} дней ({} секунд)"
          .format(period.days, period.seconds))
