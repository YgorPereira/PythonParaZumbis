#5-Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar

preço = float(input('Qual o preço do produto?'))

desc = float(input('Qual foi o desconto dado (em porcentagem)?'))

valorDesc = (desc / 100) * preço

preçoFinal = (preço + valorDesc)

print (f'O valor do desconto é de R$ {valorDesc:2.f} e o preço a se pagar R${preçoFinal:.2f}')