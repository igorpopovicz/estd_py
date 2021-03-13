import random
import emoji

acertou = bool(False)
n = random.randint(0, 100)
tentativas = 1
print('\033[1;33m=-\033[m' * 18)
print('\033[1;35mEstou pensando em um número de 0-10!\033[m')
print('\033[1;33m=-\033[m' * 18)
print(n)
chute = int(input('\033[1;33mTente adivinhar qual é :\033[m '))
if chute == n:
    print('\033[1;32mParabéns! Você acertou de primeira\033[m', end=' ')
    print(emoji.emojize(':exploding_head:'))
while not acertou:
    if chute < n:
        print('\033[1;33mO número é \033[1;35mmaior\033[m', end=' ')
        print(emoji.emojize(':backhand_index_pointing_up:'))
    elif chute > n:
        print('\033[1;33mO número é \033[1;35mmenor\033[m', end=' ')
        print(emoji.emojize(':backhand_index_pointing_down:'))
    chute = int(input('\033[1;33mTente novamente: \033[m'))
    if chute == n:
        acertou = True
        print(emoji.emojize('\033[1;32mIsso aí :OK_hand: você acertou :partying_face:.\033[m'))
    tentativas += 1
print(emoji.emojize('\033[1;33mEu estava pensando :thinking_face: no número\033[m \033[1;31m{}\033[m'.format(n)))
print('\033[1;33mVocê acertou na \033[31m{}ª\033[m \033[1;33mtentativa.\033[m'.format(tentativas))


