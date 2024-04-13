#3-Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dias = int(input("Digite a quantidade de dias:"))
hrs = int(input("Digite a quantidade de horas:"))
min = int(input("Digite a quantidade de minutos:"))
seg = int(input("Digite a quantidade de segundos:"))

dias_seg = (dias * 24) * 60 ** 2
hrs_seg = hrs * 60 ** 2
min_seg = min * 60

seg_final = dias_seg + hrs_seg + min_seg + seg

print ("Esse tempo todo é equivalente a", seg_final, 'segundos')
