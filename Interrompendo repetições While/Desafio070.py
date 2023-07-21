'''Crie um programa que leia o NOME e o PREÇO de VÁRIOS PRODUTOS.
O programa deverá perguntar se o USUÁRIO vai continuar.
No final, mostre:

[A] Qual é o TOTAL GASTO na compra.
[B] Quantos produtos custam MAIS de R$1.000,00.
[C] Qual é o NOME do produto mais BARATO.'''

quant = 0
total = 0
mais = 0
barato = 0

while True:
    print('LISTA DE COMPRAS.')
    print('-'*50)
    nome = str(input('Digite o nome do produto: ')).strip().upper()
    preco = float(input('Digite o preço do produto: R$ '))
    total += preco
    quant += 1

    if preco > 1000:
        mais += 1
    
    if quant == 1:
        barato = preco
    if preco < barato:
        barato = preco
        preco = str(nome)

    continuar = str(input('Continuar? [S/N]: ')).upper().strip()
    if continuar == 'S':
        print('-'*50)
        continue
    if continuar == 'N':
        break
    if continuar != 'S' and continuar != 'N':
        while continuar != 'S' and continuar != 'N':
            print('Digite a opção certa, por gentileza!')
            continuar = str(input('Continuar? [S/N]: ')).upper().strip()
            if continuar == 'S':
                print('-'*50)
                continue
            elif continuar == 'N':
                break
    else:
        break
print('-'*50)
print(f'''
Total gasto na compra: R$ {total:.2f}
Total de produtos que custam mais de R$ 1.000: {mais} itens
Nome do produto mais barato: {nome}''')