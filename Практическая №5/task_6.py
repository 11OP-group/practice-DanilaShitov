import math

def calculate_distance(x1, y1, x2, y2):

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return distance

def calculate_triangle_area(a, b, c):

    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))

    return area

x1, y1 = map(float, input("Введите координаты точки A (x y): ").split())
x2, y2 = map(float, input("Введите координаты точки B (x y): ").split())
x3, y3 = map(float, input("Введите координаты точки C (x y): ").split())

side_a = calculate_distance(x2, y2, x3, y3)
side_b = calculate_distance(x1, y1, x3, y3)
side_c = calculate_distance(x1, y1, x2, y2)

area = calculate_triangle_area(side_a, side_b, side_c)

print(f"Площадь треугольника: {area:.2f}")
