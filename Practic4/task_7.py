#Константа
SEATS_PER_COMPARTMENT = 4

print("Это программа которая определяет номер купе, в котором находится место с заданным номером")
seat_number = int(input("Введите номер вашего места в вагоне: "))

compartment_number = (seat_number - 1) // SEATS_PER_COMPARTMENT + 1

print("Ваше место находится в купе под номером: ", compartment_number)
