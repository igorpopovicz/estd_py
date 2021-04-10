import random
print('-'*30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-'*30)
q = int(input('Quantos jogos? '))
for x in range(0,q):
    jogo = [[random.randint(1,60)],
        [random.randint(1,60)],
        [random.randint(1,60)],
        [random.randint(1,60)],
        [random.randint(1,60)],
        [random.randint(1,60)]]
    print(f'Jogo {x+1}:')
    print(jogo)
