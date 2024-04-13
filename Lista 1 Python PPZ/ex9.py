#9-Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km = int(input("Quantos quilometros você percorreu com o carro alugado?"))
dias = int(input('Por quantos dias você ficou com o carro alugado?'))

p_dia = dias * 60
p_km = km * 0.15

p_final = p_dia + p_km

print (f'O preço total a ser pago é de R$ {p_final:.2f}.')