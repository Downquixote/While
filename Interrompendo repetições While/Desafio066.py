'''Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor "999", que é a CONDIÇÃO DE PARADA.
No final, mostre QUANTOS NÚMEROS foram digitados e qual foi a SOMA entre eles.
(DESCONSIDERANDO O FLAG)'''
quant = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    quant += 1
    soma += n
print(f'Quantidade de números digitados: {quant}')
print(f'Soma dos números digitados: {soma}')