import random
num = random.sample(range(100), 20)
pares = []
impares = []
x = 0   

for x in num:
    if x % 2 == 0:
        pares.append(x)
    elif x % 2 >= 1:
        impares.append(x)

print (num)
print (pares)
print (impares)
