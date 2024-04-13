sal_hr = float(input('Quanto você ganha por hora?'))
hr_trab = float(input('Quantas horas você trabalha no mês?'))

sal_bruto = sal_hr * hr_trab

ir = sal_bruto * 0.11
inss = sal_bruto * 0.08
sindc = sal_bruto * 0.05
descont = ir + inss + sindc

sal_liquid = sal_bruto - descont

print (f'Foram descontados R$ {descont:.2f}. Seu salário líquido é de R$ {sal_liquid:.2f}')