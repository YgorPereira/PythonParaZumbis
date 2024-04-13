km = int(input("Quantos quilometros você percorreu com o carro alugado?"))
dias = int(input('Por quantos dias você ficou com o carro alugado?'))

p_dia = dias * 60
p_km = km * 0.15

p_final = p_dia + p_km

print (f'O preço total a ser pago é de R$ {p_final:.2f}.')