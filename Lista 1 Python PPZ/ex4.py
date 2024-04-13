#4-  Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e aporcentagem do aumento. Exiba o valor do aumento e do novo salário

salInicial = float(input('Qual o seu salário atual?'))

porcento = float (input('Qual é o aumento que você recebeu (em porcentagem)?'))

aumento = float (porcento / 100) * salInicial

print (f'O seu novo salário é R$ {salInicial + aumento:.2f}')