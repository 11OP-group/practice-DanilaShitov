
# Константы нормы
TEMP_MIN_NORM, TEMP_MAX_NORM = 36, 37
PRESSURE_MIN_NORM, PRESSURE_MAX_NORM = 110, 130
PULSE_MIN_NORM, PULSE_MAX_NORM = 60, 100

# Константы лёгкого недомогания (края диапазонов)
TEMP_LOW_MILD, TEMP_HIGH_MILD = 35, 38
PRESSURE_LOW_MILD, PRESSURE_HIGH_MILD = 105, 140
PULSE_LOW_MILD, PULSE_HIGH_MILD = 55, 110

print("Вас приветствует программа, которая на основе параметров предполагает состояние здоровья!")
print("Введите входные данные по порядку:")

try:
    temperature = int(input("1. Температура (°C) = "))
    systolic_blood_pressure = int(input("2. Давление (верхнее) = "))
    pulse = int(input("3. Пульс (уд/мин) = "))
except ValueError:
    print("Вводите целые числа!!!")
    exit()

# Проверка на "норма"
if (TEMP_MIN_NORM <= temperature <= TEMP_MAX_NORM and
        PRESSURE_MIN_NORM <= systolic_blood_pressure <= PRESSURE_MAX_NORM and
        PULSE_MIN_NORM <= pulse <= PULSE_MAX_NORM):
    status = "Нормальное состояние"

# Проверка на "лёгкое недомогание". Если значения будут на краях диапазона, то сработает 1 блок (состояние нормальное)
elif (TEMP_LOW_MILD <= temperature < TEMP_MIN_NORM or TEMP_MAX_NORM < temperature <= TEMP_HIGH_MILD) and \
     (PRESSURE_LOW_MILD <= systolic_blood_pressure < PRESSURE_MIN_NORM or
      PRESSURE_MAX_NORM < systolic_blood_pressure <= PRESSURE_HIGH_MILD) and \
     (PULSE_LOW_MILD <= pulse < PULSE_MIN_NORM or PULSE_MAX_NORM < pulse <= PULSE_HIGH_MILD):
    status = "Лёгкое недомогание"

# Проверка на "требуется врач"
elif (temperature < TEMP_LOW_MILD or temperature > TEMP_HIGH_MILD or
      systolic_blood_pressure < PRESSURE_LOW_MILD or systolic_blood_pressure > PRESSURE_HIGH_MILD or
      pulse < PULSE_LOW_MILD or pulse > PULSE_HIGH_MILD):
    status = "Требуется врач!"
# если заданные значения вышли за рамки
else:
    status = "Показатели вне диапазонов."

# вывод
print(f"Температура: {temperature}°C | Давление: {systolic_blood_pressure} | Пульс: {pulse} уд/мин")
print(f"Состояние здоровья: {status}")