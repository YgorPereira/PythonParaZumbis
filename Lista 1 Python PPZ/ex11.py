#11-Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão

import sys
sys.set_int_max_str_digits(1000000)
num = int(2 ** 1000000)
text = str(num)
numCaract = len(text)

print ('dois elevado a um milhão tem', numCaract, 'caracteres')
