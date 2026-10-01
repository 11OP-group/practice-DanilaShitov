x = int(input("Введите число четырехзначное число X для нахождения его цифр: "))

thousandths = int(x // 1000)
hundredths = int((x % 1000) / 100)
tenths = int(((x % 1000) % 100) / 10)
units = int(((x % 1000) % 100) % 10)

print("Цифры разрядов от 1000 до 1: ", thousandths, hundredths, tenths, units)