area = float(input('Qual a área em m² a ser pintada?'))

litros = area / 3
latas = int(litros / 18)
if litros % 18 > 0:
    latas = latas + 1

valor = float(latas * 80)

print (f'Você terá que comprar {latas} latas e isso custará R$ {valor:.2f}')
