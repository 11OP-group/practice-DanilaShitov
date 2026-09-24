#6 задание
# Сбор данных от пользователя
name = input("Ваше имя: ")
age_str = input("Ваш возраст: ")
subjects_str = input("Любимые предметы (через запятую): ")

# Преобразование типов
age = int(age_str)

# Разбиваем строку с предметами по запятой и убираем лишние пробелы
subjects_list = [subject.strip() for subject in subjects_str.split(',')]

# Создание словаря
student = {
    "name": name,
    "age": age,
    "subjects": subjects_list
}

# Оформление
print("=" * 30)
print("АНКЕТА СТУДЕНТА")
print("=" * 30)

# Вывод данных из словаря
print(f"Имя: {student['name']}")
print(f"Возраст: {student['age']}")
print(f"Любимые предметы: {student['subjects']}")

print("=" * 30)
