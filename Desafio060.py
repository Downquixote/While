# Faça um programa qur leia um NÚMERO qualquer e mostre o seu FATORIAL.
# EX: 5! = 5x4x3x2x1 = 120

num = int(input('Digite um valor para saber o seu fatorial: '))
print('Calculando {}! = '.format(num), end='')
conta = num
fato = 1

while conta > 0:
    print('{} '.format(conta), end='')
    print('x ' if conta > 1 else '= ', end='')
    fato = fato * conta
    conta -= 1
print(fato)