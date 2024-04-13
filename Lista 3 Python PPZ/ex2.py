user = str(input('Digite o usuário: '))
password = str(input('Digite a senha: '))

while user == password:
    print ('ATENÇÃO! O usuário e a senha estão iguais.')
    user = str(input('Digite o usuário: '))
    password = str(input('Digite a senha: '))

print ('Cadastro feito com sucesso!')
