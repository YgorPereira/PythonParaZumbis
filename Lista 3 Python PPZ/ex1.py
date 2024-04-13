nota = float(input('digite a sua nota de 0 a 10: '))

while nota > 10 or nota < 0:
    print ('Essa não é uma nota valida.')
    nota = float(input('digite a sua nota de 0 a 10: '))
    
print (f'sua nota é {nota}')
