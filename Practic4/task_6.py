import math

x = float(input("Введите угол в градусах: "))
r = math.radians(x)

sin_x = math.sin(r)
cos_x = math.cos(r)
tan_x = math.tan(r)

result = sin_x + cos_x + tan_x ** 2
print(result)