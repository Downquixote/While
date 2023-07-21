# Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a CONDIÇÃO DE PARADA. No final, mostre QUANTOS NÚMEROS foram digitados e qual foi a SOMA entre eles.
n = 0
contador = 0
soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma += n 
    contador += 1
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles é: {}'.format(n, soma))