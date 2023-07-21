# Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. No final da execução, mostre a MÉDIA ENTRE TODOS os valores e qual foi o MAIOR e o MENOR valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não CONTINUAR a digitar valores.
contador = maior = menor = soma = 0
escolha = 'S'

while escolha in 'S':
   n = int(input('Digite um número: '))
   escolha = str(input('Deseja continuar? [S/N]: ')).upper().strip()
   contador += 1 
   soma += n
   if contador == 1:
      maior = n 
      menor = n
   else:
      if n > maior:
        maior = n
      if n < menor:
        menor = n
m = soma / contador
print('Média dos {} números digitados: {}'.format(contador, m))
print('Maior número digitado: {}'.format(maior))
print('Menor número digitado: {}'.format(menor))