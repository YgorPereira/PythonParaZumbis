num1 = float(input('Digite o primeiro valor:'))
num2 = float(input('Digite o segundo valor:'))
num3 = float(input('Digite o terceiro valor:'))

if num1 >= num2 >= num3:
    maior = num1
    menor = num3
    print(f'Esse é o maior número:{maior:.2f}')
    print(f'Esse é o menor número:{menor:.2f}')

if num1 >= num3 >= num2:
    maior = num1
    menor = num2
    print(f'Esse é o maior número:{maior:.2f}')
    print(f'Esse é o menor número:{menor:.2f}')

if num2 >= num1 >= num3:
    maior = num2
    menor = num3
    print(f'Esse é o maior número:{maior:.2f}')
    print(f'Esse é o menor número:{menor:.2f}')

if num2 >= num3 >= num1:
    maior = num2
    menor = num1
    print(f'Esse é o maior número:{maior:.2f}')
    print(f'Esse é o menor número:{menor:.2f}')

if num3 >= num1>= num2:
    maior = num1
    menor = num2
    print(f'Esse é o maior número:{maior:.2f}')
    print(f'Esse é o menor número:{menor:.2f}')

if num3 >= num2 >= num1:
    maior = num3
    menor = num1
    print(f'Esse é o maior número:{maior:.2f}')
    print(f'Esse é o menor número:{menor:.2f}')