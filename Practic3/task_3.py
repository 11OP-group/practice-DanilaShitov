# Задание 3
try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))

    otvet = num1 + num2
    print("Сумма:", otvet)

except ValueError:
    print("Ошибка: нужно ввести целые числа.")