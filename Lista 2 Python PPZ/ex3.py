peso = float(input('Qual a pesagem de peixes de hoje?'))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f"Você excedeu kg {excesso:.2f}.")
    print (f'Sua multa é de {multa:.2f}')
elif peso <= 50:
    excesso = 0
    multa = 0
    print('Sua pesagem está dentro do permitido.')