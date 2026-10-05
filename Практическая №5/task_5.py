NOTE_5000 = 5000
NOTE_2000 = 2000
NOTE_1000 = 1000
NOTE_500 = 500
NOTE_200 = 200
NOTE_100 = 100


def calculate_banknotes(amount):
    count_5000 = amount // NOTE_5000
    remainder = amount % NOTE_5000

    count_2000 = remainder // NOTE_2000
    remainder = remainder % NOTE_2000

    count_1000 = remainder // NOTE_1000
    remainder = remainder % NOTE_1000

    count_500 = remainder // NOTE_500
    remainder = remainder % NOTE_500

    count_200 = remainder // NOTE_200
    remainder = remainder % NOTE_200

    count_100 = remainder // NOTE_100

    return count_5000, count_2000, count_1000, count_500, count_200, count_100


amount = int(input("Введите сумму для снятия (кратную 100): "))

count_5000, count_2000, count_1000, count_500, count_200, count_100 = calculate_banknotes(amount)

print("Банкомат выдаст:")
print(f"  5000 руб. x {count_5000}")
print(f"  2000 руб. x {count_2000}")
print(f"  1000 руб. x {count_1000}")
print(f"   500 руб. x {count_500}")
print(f"   200 руб. x {count_200}")
print(f"   100 руб. x {count_100}")
