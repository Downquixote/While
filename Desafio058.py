# Melhore o jogo do DESAFIO 028, onde o computador vai 'pensar' em um NÚMERO ENTRE 0 E 10.
# Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint

pc = randint(0, 10)
tentativa = 0
user = 0

print('Bem-Vindo(a) ao Downquixote Prize Draw!')

while user != pc:
    user = int(input('Digite um número entre 0 e 10: '))
    tentativa += 1
    if user > 10:
        print('Excedeu o número permitido, tente novamente!')
    elif user == pc:
        print('Você acertou!')
        print('O número escolhido pelo PC foi: {}'.format(pc))
        print('Quantidade de tentativas: {}'.format(tentativa))