'''Faça um programa que jogue PAR ou ÍMPAR com o computador.
O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. '''
from random import randint

print('Par ou ímpar')
print('~'*20)

quant = 0

while True:
    valor = int(input('Digite um valor: '))
    escolha = str(input('Par ou ímpar? [P/I]: ')).upper().strip()
    pc = randint(0, 10)
    print('~'*20)
    soma = pc + valor
    if escolha == 'P':
        if soma % 2 == 0:
            print('Você escolheu PAR!')
            print(f'PC escolheu: {pc}')
            print(f'Você escolheu: {valor}')
            print('-'*20)
            print(f'Total de {soma} - PAR!')
            print('Você ganhou!')
            print('~'*20) 
            quant += 1
        else:
            print('Você escolheu PAR!')
            print(f'PC escolheu: {pc}')
            print(f'Você escolheu: {valor}')
            print('-'*20)
            print(f'Total de {soma} - ÍMPAR!')
            print('Você perdeu!')
            break
    elif escolha == 'I':
        if soma % 2 == 0:
            print('Você escolheu ÍMPAR!')
            print(f'PC escolheu: {pc}')
            print(f'Você escolheu: {valor}')
            print('-'*20)
            print(f'Total de {soma} - PAR!')
            print('Você perdeu!')
            break
        else:
            print('Você escolheu ÍMPAR!')
            print(f'PC escolheu: {pc}')
            print(f'Você escolheu: {valor}')
            print('-'*20)
            print(f'Total de {soma} - ÍMPAR!')
            print('Você ganhou!')
            print('~'*20) 
            quant += 1
    if escolha != 'P' and escolha != 'I':
        print('Ops... parece que você digitou errado, tente novamente!')

print('~'*20)        
print(f'Você ganhou {quant} vezes consecutivas.')
    