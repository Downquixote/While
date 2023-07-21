'''Crie um programa que simule o funcionamento de um CAIXA ELETRÔNICO.
No início, pergunte ao usuário qual será o VALOR A SER SACADO (número inteiro) e o programa vai informar quantas CÉDULAS de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$1, R$10, R$20 e R$50'''

print('{:^30}'.format('BANCO DOWNQUIXOTE'))
print('=' * 30)


valor = int(input('Digite o valor para sacar: '))
total = valor
cedula = 50
totalCedula = 0

while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'Total de cédulas de {cedula}: {totalCedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0
        if total == 0:
            break
print('=' * 30)
print('Obrigado por utilizar nossos sistemas!')