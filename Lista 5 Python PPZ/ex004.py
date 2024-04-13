count = 0
for n in range(18644, 33088):
    n_str = str(n)
    if '2' in n_str and '7' not in n_str:
        count = count + 1
print(f'existem {count} números sortudos.')