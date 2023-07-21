# Refaça o DESAFIO 051, lendo o PRIMEIRO TERMO e a RAZÃO de uma PA.
# Mostrando os 10 PRIMEIROS TERMOS da progressão usando a estrutura WHILE.
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
contador = 1

while contador <= 10:
    print('{} - '.format(termo), end='')
    termo += razao
    contador += 1
print('Fim.')