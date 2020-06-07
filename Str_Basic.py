name = "Anton"
surname = "Koziavin"
print(name, surname)
print("Объединение строк")
fullname= name + " " + surname        #первая строка + пробел + вторая строка
print(fullname)
print("Приведение числа к строке")
age = 23
info = "Имя:" + name + "    Возраст:" + str(age)
print(info)
print("")
print("А сейчас мы начнем кое что интересное,\nа именно перенос строки. А еще я могу\nТак! \t И так! \t И так!")
print('')
print("Слеш помогает \"Отобразить кавычки\"")
print("Сравнение строк")
print("Цифры всегда меньше букв, заглавные меньше строчных")
str1="1a"
str2="aa"
str3="Aa"
print(str1,">",str2,"?", str1>str2)
print(str2,">",str3,"?", str2>str3)
print("")
print("Функция lower() приводит строку к нижнему регистру\nФункция upper() к верхнему")
str1="Антон"
str2="антон"
print(str1==str2)
print(str1.lower()==str2.lower())

