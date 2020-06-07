number = int(input("Введите число: "))
factorial = 1
for i in range(1, number+1):                #последний символ не включается в range
    factorial *= i
print("Факториал числа", number, "равен:", factorial)