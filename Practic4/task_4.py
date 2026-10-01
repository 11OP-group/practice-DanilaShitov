schoolchildren = int(input("Количество школьников: "))
mandarins = int(input("Количество мандаринов: "))

share = mandarins // schoolchildren
remainder = mandarins % schoolchildren

print("Мандаринов каждому: ", share)
print("Остаток: ", remainder)