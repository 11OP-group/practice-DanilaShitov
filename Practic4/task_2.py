#2
import math

x1_coordinate, y1_coordinate = map(float, input("Введите координаты первой точки: ").split())
x2_coordinate, y2_coordinate = map(float, input("Введите координаты второй точки: ").split())

def calculate_distance(x1, y1, x2, y2):
    """Вычисление по формуле"""
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

result = calculate_distance(x1_coordinate, y1_coordinate, x2_coordinate, y2_coordinate)

print(f"Ваш результат: {result:.2f}")
