import math

specified_number = float(input("Введите число X для вычисления выражения ⌊x⌋+⌈x⌉: "))

result = math.floor(specified_number) + math.ceil(specified_number)

print(f"Ваш ответ: {result}")