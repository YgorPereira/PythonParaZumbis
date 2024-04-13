#10-Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

cigDia = int(input('Quantos cigarros você fuma por dia?'))
fumaAnos = int(input('Faz quantos anos que você fuma?'))

cigAno = cigDia * 366
totalCig = fumaAnos * cigAno
totalTemp_min = totalCig * 10
totalTemp_horas = totalCig / 60
totalTemp_dias = totalTemp_horas / 24

print (f'Você perdeu {totalTemp_dias:.2f}de vida por causa do cigarro. Pare de fumar!')