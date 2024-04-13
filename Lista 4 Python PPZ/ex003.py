from random import sample
vet1 = sample(range(100), 10)
vet2 = sample(range(100), 10)
vet3 = []
x = 0
for x in range(10):
    vet3.append(vet1[x])
    vet3.append(vet2[x])
print (f'Vetor 1: {vet1}')
print (f'Vetor 2: {vet2}')
print (f'Vetor 3: {vet3}')
