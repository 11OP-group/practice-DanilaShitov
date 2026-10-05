def calculate_bmi(weight, height):

    result = weight / (height**2)

    return result

weight, height = map(float, input("Введите свой вес (в кг) и рост (в метрах) в одной строке через пробел: ").split())

result = calculate_bmi(weight, height)

print(f"Ваш ИМТ: {result:.1f}")
