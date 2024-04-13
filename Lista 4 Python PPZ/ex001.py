import random
num = random.sample(range(100), 10)
print (num)

x = 0
y = 0
maior = 0
menor = 100

while x < 10 :
    if num [x] > maior:
        maior = num [x]
    else:
        maior = maior
    x = x + 1

while y < 10:
    if num[y] < menor:
        menor = num[y]
    else:
        menor = menor
    y = y + 1

print(f'Menor: {menor}.')
print(f'Maior: {maior}.')
