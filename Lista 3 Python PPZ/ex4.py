num = int(input('numero: '))
a, b = 1, 1
cont = 1

while cont <= num - 2:
    a, b = b, a + b
    cont = cont + 1

print (b)
