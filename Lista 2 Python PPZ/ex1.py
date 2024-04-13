ladoA = int(input('Qual o tamanho do primeiro lado?'))
ladoB = int(input('Qual o tamanho do segundo lado?'))
ladoC = int(input('Qual o tamanho do terceiro lado?'))

if ladoA == ladoB == ladoC:
    print('Seu triângulo é equilatero.')
elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
    print('Seu triângulo é isósceles.')
else:
    print('Seu triângulo é escaleno.')

