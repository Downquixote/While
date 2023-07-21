# Faça um programa que leia o SEXO de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    if sexo == 'M':
        print('Você é homem!')
    elif sexo == 'F':
        print('Você é mulher!')
    else:
        print('Ops... parece que você digitou errado, tente novamente!')