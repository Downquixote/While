# Escreva um programa que leia um NÚMERO N inteiro qualquer e mostre na tela os N primeiros elementos de uma SEQUÊNCIA DE FIBONACCI.
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
n = int(input('Digite um número: '))
t1 = 0
t2 = 1
contador = 3

print('{} - {}'.format(t1, t2), end='')
while contador <= n:
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    contador += 1
print(' - Fim.')