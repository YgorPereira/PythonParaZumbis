count = 0
for n in range(1067, 3628):
    if n % 2 == 0 and n % 7 == 0:
        count = count + 1
print(f'{count} são números pares e dívisiveis por 7.')
print('FIM')