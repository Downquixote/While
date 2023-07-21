# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 TERMOS.
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
contador = 1
total = 0
add = 10

while add != 0:
    total += add
    while contador <= total:
        print('{} - '.format(termo), end='')
        termo += razao
        contador += 1
    print('Pausa...')
    add = int(input('\nDigite algum número para adicionar a quantidade de termos, caso queira sair, digite "0": '))
print('Total de termos mostrados na tela: {}'.format(total))
print('Fim.')