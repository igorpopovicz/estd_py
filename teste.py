quer_parar = False
maior = 0
homem = 0
mulher = 0
mulher_menos_vinte = 0
while not quer_parar:
    print('-'*30)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('-'*30)
    idade = int(input('Idade: '))
    if idade >= 18:
        maior += 1
    while True:
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if sexo == 'M':
            homem += 1
            break
        elif sexo == 'F':
            if idade < 20:
                mulher_menos_vinte += 1
            mulher += 1
            break
    while True:
        mais = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if mais == 'N':
            quer_parar = True
        elif mais == 'S':
            break
print(f'{maior} pessoas tem mais de 18 anos')
print(f'{homem} homens foram cadastrados.')
print(f'{mulher} mulheres foram cadastradas')
print(f'{mulher_menos_vinte} mulheres tem menos de 20 anos')
      