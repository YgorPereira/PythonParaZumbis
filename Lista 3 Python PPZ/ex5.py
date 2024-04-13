num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))

while num1 % num2 != 0:
    num1, num2 = num2, num1 % num2

print(f'O mdc é {num2:.2f}.')
