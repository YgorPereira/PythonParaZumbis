popA = 80000
popB = 200000

ano = 0

while popA < popB:
    crescA = popA * 0.03
    crescB = popB * 0.015

    popA = popA + crescA
    popB = popB + crescB
    
    ano = ano + 1

print (f'Será necessário {ano} anos para a população de A ultrapassar a de B.')
