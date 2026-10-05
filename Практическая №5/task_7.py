FUEL_PRICE_PER_LITER = 49.5

def calculate_fuel_cost(distance_km, consumption_per_100km):

    fuel_liters = distance_km * (consumption_per_100km / 100)
    total_cost = fuel_liters * FUEL_PRICE_PER_LITER
    return fuel_liters, total_cost

distance_km = float(input("Введите расстояние поездки (км): "))
consumption_per_100km = float(input("Введите расход топлива на 100 км (л): "))

fuel_liters, total_cost = calculate_fuel_cost(distance_km, consumption_per_100km)

print(f"Необходимо топлива: {fuel_liters:.2f} л")
print(f"Стоимость поездки: {total_cost:.2f} р")
