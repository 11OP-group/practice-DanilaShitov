total = 1
while True:
    x = int(input("Введите число "))
    if x < 0:
        break
    else:
        total *= x
print(total)
