import math

PI = math.pi

def calculate_rectangle_area(width, height):

    area = width * height

    return area

def calculate_circle_area(radius):

    area = PI * radius ** 2

    return area

width, height = map(float, input("Введите ширину и высоту прямоугольника через пробел: ").split())
rect_area = calculate_rectangle_area(width, height)
print(f"Площадь прямоугольника: {rect_area:.2f}")

radius = float(input("Введите радиус круга: "))
circle_area = calculate_circle_area(radius)
print(f"Площадь круга: {circle_area:.2f}")
