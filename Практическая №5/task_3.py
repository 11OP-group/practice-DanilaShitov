USD_TO_RUB = 95.50

def convert_usd_to_rub(amount_usd):

    amount_rub = amount_usd * USD_TO_RUB

    return amount_rub

amount_usd = float(input("Введите сумму в долларах: "))
amount_rub = convert_usd_to_rub(amount_usd)

print(f"{amount_usd:.2f} USD = {amount_rub:.2f} RUB")



