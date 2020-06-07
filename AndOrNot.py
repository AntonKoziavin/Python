age=24
weight=78
print(age> 21 and weight < 90)
print("Добавим в условие переменную, отдающую False")
is_married=False
print(age> 21 and weight < 90 and is_married)
print("Возвращаем True, если верно хотя бы одно утверждение")
print(age> 21 or weight < 90 or is_married)
print("Логическое отрицание")
print(not age > 21)
print(not is_married)
print("Вначале выполняется оператор not, затем оператор and, а в конце оператор or:")
print("age> 21 or is_married and not weight < 90", age> 21 or is_married and not weight < 90)
print("not weight < 90", not weight < 90)
print("is_married and not weight < 90", is_married and not weight < 90)
print(age> 21 or False)
print("Можно использовать скобки")
print((age> 21 or is_married) and not weight < 90)
