# Crie um programa que leia DOIS VALORES e mostre um MENU na tela.
'''
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] SAIR DO PROGRAMA'''

# Seu programa deverá realizar a operação solicitada em cada caso.

opcao = 0

while opcao != 4:
    print('Bem-vindo(a) ao Downquixote calculator!')

    print('''
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] SAIR DO PROGRAMA''')
    print()
    opcao = int(input('Escolha uma opção: '))
    
    if opcao == 1:
        user1 = int(input('Digite o 1º valor: '))
        user2 = int(input('Digite o 2º valor: '))
        soma = user1 + user2
        print('A soma entre os valores digitados é: {}'.format(soma))
        opcao = int(input('Digite "0" para novo calculo ou "4" para sair: '))
        print('-'*50)
        if opcao == 4:
            print('Obrigado por utilizar nossos sistemas!')
    elif opcao == 2:
        user1 = int(input('Digite o 1º valor: '))
        user2 = int(input('Digite o 2º valor: '))
        multi = user1 * user2
        print('A multiplicação dos valores digitados é: {}'.format(multi))
        opcao = int(input('Digite "0" para novo calculo ou "4" para sair: '))
        print('-'*50)   
        if opcao == 4:
            print('Obrigado por utilizar nossos sistemas!')
    elif opcao == 3:
        user1 = int(input('Digite o 1º valor: '))
        user2 = int(input('Digite o 2º valor: '))
        if user1 > user2:
            print('O maior valor digitado é: {}'.format(user1))
            opcao = int(input('Digite "0" para novo calculo ou "4" para sair: '))
            print('-*50')
            if opcao == 4:
                print('Obrigado por utilizar nossos sistemas!')
        else:
            print('O maior valor digitado é: {}'.format(user2))
            opcao = int(input('Digite "0" para novo calculo ou "4" para sair: '))
            print('-'*50)
            if opcao == 4:
                print('Obrigado por utilizar nossos sistemas!')
    elif opcao > 4:
        print('Opção inválida, tente novamente!')
        print('-'*50)
    else:
        print('-'*50)
        print('Obrigado por utilizar nossos sistemas!')