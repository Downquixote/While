'''Crie um programa que leia a IDADE e o SEXO de VÁRIAS PESSOAS.
A cada pessoa cadastrada, o programa deverá se o USUÁRIO quer ou não continuar.
No final, mostre: 

[A] Quantas pessoas tem mais de 18 ANOS.
[B] Quantos HOMENS foram cadastrados.
[C] Quantas MULHERES tem menos de 20 ANOS.'''

quant = 0
maioridade = 0
homens = 0
mulheres = 0


while True:
    print('CADASTRAR UMA PESSOA.')
    print('-'*50)
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()
    if sexo != 'M' and sexo != 'F':
       while sexo != 'M' and sexo != 'F':
        print('O que você quis dizer...? tente novamente, respeitando as opções de gênero acima!')
        sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()
    quant += 1
    if idade >= 18:
       maioridade += 1
    if sexo == 'M':
       homens += 1
    if sexo == 'F':
       if idade <= 20:
          mulheres +=1

    continuar = str(input('Cadastre mais alguém ou saia [S/N]: ')).upper().strip()
    if continuar == 'S':
        print('-'*50)
        continue
    elif continuar == 'N':
        print('-'*50)
        print('Obrigador por utilizar nossos sistemas de cadastro.')
        break
    else:
        while continuar != 'S' and continuar != 'N':
            print('Não entendi, digite novamente.')
            continuar = str(input('Cadastre mais alguém ou saia [S/N]: ')).upper().strip()
            print('-'*50)
    
print(f'''
Total de pessoas cadastradas: {quant}
Total de pessoas maiores de 18 anos: {maioridade}
Total de homens que foram cadastrados: {homens}
Total de mulheres com 20 anos ou menos: {mulheres}''')

        