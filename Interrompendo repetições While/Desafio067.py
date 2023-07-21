'''Faça um programa que mostre a TABUADA de VÁRIOS NÚMEROS, um de cada vez, para cada valor digitado pelo usuário.
O programa será INTERROMPIDO quando o número solicitado for NEGATIVO'''
quant = 1
tabuada = int(input('Digite para ver a tabuada: '))
while quant <= 10:
    if tabuada < 0:
        break
    print(f'{tabuada} x {quant} = {tabuada*quant}')
    quant += 1
   
print('Programa encerrado.')