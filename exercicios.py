# Exercício 22

nome = str(input('{}What is your full name ?{} '.format('\033[1;32m', '\033[m'))).strip()
print('Your name {}UPPER{} is {}{}{}.'.format('\033[4;36m', '\033[m', '\033[4;36m', nome.upper(), '\033[m'))
print('Your name {}lower{} is {}{}{}.'.format('\033[4;34m', '\033[m', '\033[4;34m', nome.lower(), '\033[m'))
print('Your name have {}{}{} characters.'.format('\033[1;31m', len(''.join(nome.split())), '\033[m'))
separado = nome.split()
print('Your first name is {}{}{} and have {}{}{} characters.'.format('\033[1;32m', separado[0], '\033[m', '\033[1;31m',
                                                                     len(separado[0]), '\033[m'))

# Exercício 23

numero = int(input('Digite um número de 0 a 9999: '))
print('{}Você digitou{} {}{}{}'.format('\033[1;36m', '\033[m', '\033[1;31m', numero, '\033[m'))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('{}Unidade:{} {}{}{}'.format('\033[4;32m', '\033[m', '\033[1;31m', u, '\033[m'))
print('{}Dezena:{} {}{}{}'.format('\033[4;32m', '\033[m', '\033[1;31m', d, '\033[m'))
print('{}Centena:{} {}{}{}'.format('\033[4;32m', '\033[m', '\033[1;31m', c, '\033[m'))
print('{}Milhar:{} {}{}{}'.format('\033[4;32m', '\33[m', '\033[1;31m', m, '\033[m'))

# Exercício 24

city = str(input('What is your town? ')).strip()
city = city.upper()
frstnm = city.split()
print('\033[1;34mYour towns name begins with\033[m \033[1;33m"Santo"\033[m \033[1;34m?\033[m')
if 'SANTO' in frstnm:
    print('\033[1;34mAnswer:\033[m \033[1;32mTrue\033[m')
else:
    print('\033[1;34mAnswer:\033[m \033[1;31mFalse\033[m')

# Exercício 25

name = str(input('\033[1;36mWhat is your name ?\033[m ')).strip()
upper = name.upper()
if 'SILVA' in upper:
    print('\033[1;36mYour name\033[m \033[1;32mhave\033[m \033[1;33m"Silva"\033[m')
else:
    print('\033[1;36mYour name\033[m \033[1;31mdont have\033[m "Silva"')

# Exercício 26

print('{}Type a text:{}'.format('\033[1;32m', '\033[m'))
text = str(input().strip().upper())
txt = text.split()
txt = ''.join(txt)
print('{}Times "a" appears{} -> {}{}{}'.format('\033[1;33m', '\033[m', '\033[1;31m', txt.count("A"), '\033[m'))
print('{}First time "a" appears{} -> {}{}{}'.format('\033[1;33m', '\033[m', '\033[1;31m', txt.find("A") + 1, '\033[m'))
print('{}Last time "a" appears{} -> {}{}{}'.format('\033[1;33m', '\033[m', '\033[1;31m', txt.rfind("A") + 1, '\033[m'))

# Exercício 27

name = str(input('\033[4;33mType your name here:\033[m ')).strip()
split = name.split()
print('{}First name:{} {}{}{}'.format('\033[1;34m', '\033[m', '\033[1;32m', split[0].capitalize(), '\033[m'))
print('{}Last name:{} {}{}{}'.format('\033[1;36m', '\033[m', '\033[1;32m', split[-1].capitalize(), '\033[m'))

# Exercício 28

import random

# num = [1, 2, 3, 4, 5]
# n = random.choice(num)
n = random.randint(0, 5)
print('\033[1;33m=-\033[m' * 18)
print('\033[1;35mEstou pensando em um número de 0-5!\033[m')
print('\033[1;33m=-\033[m' * 18)
chute = int(input('\033[1;33mTente adivinhar qual é :\033[m '))
if n == chute:
    print('\033[1;32mIsso aí! você acertou :).\033[m')
else:
    print('\033[1;31mQue pena! :(\033[m')
print('\033[1;33mEu estava pensando no número\033[m \033[1;31m{}\033[m'.format(n))

# Exercício 29

print('\033[1;33mVocê está em uma rodovia com o limite de velocidade de\033[m \033[7;33;41m80Km/h\033[m.')
velocidade = float(input('Qual a velocidade do seu carro ? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Você foi \033[1;31m multado!\033[m por passar a \033[4;31m{}Km\033[m em uma via de \033[4m80\033[m'.format(
        velocidade))
    print('Você terá que pagar uma \033[31m multa\033[m de \033[4;31m{}\033[m reais.'.format(multa))
else:
    print('\033[32mVocê chegou com sucesso em seu destino.\033[m')

# Exercício 30

num = float(input('\033[35mDigite um número inteiro:\033[m '))
par = num % 2
if par == 0:
    print('Esse número é \033[1;34mpar\033[m.')
else:
    print('Esse número é \033[1;36mimpar\033[m.')

# Exercício 31

dist = float(input('\033[1;31mQual a distância da viagem (em km) ?\033[m '))
pass_1 = 0.50
pass_2 = 0.45
if dist <= 200:
    cash = dist * pass_1
else:
    cash = dist * pass_2
print('\033[1;33mO preço da viagem será de\033[m \033[1;35m{}\033[m \033[1;33mreais.\033[m'.format(cash))

# Exercício 32

year = int(input('\033[1;34mDigite um ano:\033[m '))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('\033[1;35mEsse ano \033[4;32mé bissexto\033[m.')
else:
    print('\033[1;35mEsse ano \033[4;31mnão é bissexto\033[m.')

# Exercício 33

numb_1 = float(input('\033[1;35mDigite o 1º número: '))
numb_2 = float(input('2º número: '))
numb_3 = float(input('3º número:\033[m '))
maior = int(0)
menor = int(0)
if numb_1 > numb_2 and numb_1 > numb_3:
    maior = numb_1
else:
    if numb_2 > numb_3 and numb_2 > numb_1:
        maior = numb_2
    else:
        maior = numb_3
print('\033[1;34mO maior número é o\033[m \033[1;31m{}\033[m'.format(maior))
if numb_1 < numb_2 and numb_1 < numb_3:
    menor = numb_1
else:
    if numb_2 < numb_3 and numb_2 < numb_1:
        menor = numb_2
    else:
        menor = numb_3
print('\033[1;36mO menor número é o\033[m \033[1;31m{}\033[m'.format(menor))

# Exercício 34

cash = float(input('Qual é o seu salário ? '))
if cash > 1250.00:
    percentage = 10
    increase = (cash * 10) / 100
    cash_2 = cash + increase
else:
    percentage = 15
    increase = (cash * 15) / 100
    cash_2 = cash + increase
print('Você receberá um aumento de {}%, {:.2f} reais'.format(percentage, increase))
print('Seu novo salário é {:.2f} reais'.format(cash_2))

# Exercício 35

import time

print('\033[1;35;44m#\033[m' * 28)
print('\033[1;37;44m   Verificando Triãngulos   \033[m')
print('\033[1;35;44m#\033[m' * 28)

a = float(input('\033[1;35mPrimeiro lado: \033[m'))
b = float(input('\033[1;35mSegundo lado: \033[m'))
c = float(input('\033[1;35mTerceiro lado: \033[m'))
print('\033[4;34mProcessando...\033[m')
time.sleep(1)
print('')
if a < b + c and b < a + c and c < a + b:
    print('\033[1;32mForma um triângulo\033[m')
else:
    print('\033[1;31mNão forma um triângulo\033[m')

# Exercício 36

valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
parcelas = int(input('Em quantos anos quer financiar ? '))
parcelas = parcelas * 12
prestacao = valor / parcelas
condicion = (salario * 30) / 100
if prestacao > condicion:
    print('As prestações exedem a porcentagem permitida pelo seu salário')
    print('infelismente não podemos liberar o empréstimo.')
else:
    print('O empréstimo será liberado!')
    print('Você pagará {} parcelas mensais no valor de {:.2f} reais.'.format(parcelas, prestacao))

# Exercício 37

num = int(input('Digite um número: '))
print('Qual será a conversão ?')
txt = """Digite:
[ 1 ] para BINARIO
[ 2 ] para OCTAL
[ 3 ] para HEXADECIMAL
"""
print(txt)
options = int(input(''))
print('')
if options == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif options == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif options == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print("'-'")
print('terminado processo')

# Exercício 38

n1 = int(input('1º \033[34mnúmero\033[m: '))
n2 = int(input('2º \033[34mnúmero\033[m: '))

if n1 > n2:
    print('O \033[33mprimeiro valor\033[m é \033[1;34mmaior\033[m.')
elif n1 < n2:
    print('O \033[33msegundo valor\033[m é \033[1;34mmaior.')
elif n1 == n2:
    print('\033[33mNão existe\033[m valor maior, os dois são \033[1;34miguais\033[m.')

# Exercício 39

from datetime import datetime

now = datetime.now()
alist = (now.year - 18)
ano = int(input('Em que ano você nasceu ?'))
if ano > alist:
    falta = ano - alist
    print('Você ainda irá se alistar.')
    print('Faltam {} ano(s) para se alsitar'.format(falta))
elif ano == alist:
    print('está na hora de se alistar')
elif ano < alist:
    passou = alist - ano
    print('Já passou da hora de se alistar.')
    print('Deveria ter se alistado {} ano(s) atrás'.format(passou))

# Exercício 40

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
print('Sua média foi de {}'.format(m))
if m < 50:
    print('REPROVADO')
elif 50 <= m <= 69:
    print('RECUPERAÇÃO')
elif m >= 70:
    print('APROVADO')

# Exercício 41

from datetime import datetime

ano = int(input('Em que ano você nasceu ?'))
now = datetime.now()
age = now.year - ano
print('O atleta tem {} anos.'.format(age))
if age <= 9:
    categoria = 'Mirim'
elif 10 <= age <= 14:
    categoria = 'Infantil'
elif 15 <= age <= 19:
    categoria = 'Junior'
elif 20 <= age <= 25:
    categoria = 'Senior'
else:
    categoria = 'Master'

print('Sua categoria é: {}!'.format(categoria))

# Exercício 42

import time

print('\033[1;35;44m#\033[m' * 28)
print('\033[1;37;44m   Verificando Triãngulos   \033[m')
print('\033[1;35;44m#\033[m' * 28)

a = float(input('\033[1;35mPrimeiro lado: \033[m'))
b = float(input('\033[1;35mSegundo lado: \033[m'))
c = float(input('\033[1;35mTerceiro lado: \033[m'))
print('\033[4;34mProcessando...\033[m')
time.sleep(1)
print('')
if a < b + c and b < a + c and c < a + b:
    print('\033[1;32mForma um triângulo\033[m')
    if a == b == c:
        print('\033[1;35mEsse triângulo é equilátero!\033[m')
    elif a == b or a == c or b == c:
        print('\033[1;35mEsse triângulo é isóceles\033[m')
    elif a != b and a != c:
        print('\033[1;35mEsse triângulo é escaleno\033[m')

else:
    print('\033[1;31mNão forma um triângulo\033[m')

# Exercício 43

import time

print('\033[1;31;46m#\033[m' * 10)
print('\033[1;37;46m   I.M.C   \033[m')
print('\033[1;31;46m#\033[m' * 10)
print('')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print('Calculando seu I.M.C...')
time.sleep(2)
print('Seu I.M.C é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc <= 25:
    print('Você está no peso ideal.')
elif 25 <= imc <= 30:
    print('Você está sobrepeso.')
elif 30 <= imc <= 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade mórbida')

# Exercício 44

print('{:=^40}'.format(' LOJINHO DO TADEU '))

cash = float(input('Preço do produto: '))

txt = """FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque.
[ 2 ] À vista no cartão.
[ 3 ] Em até duas vezes no cartão.
[ 4 ] 3x ou mais."""
print(txt)
payment = float(input('Qual é a opção ? '))
if payment == 1:
    print('Selecionado: Preço à vista.')
    print('Compras à vista no dinheiro tem 10% de desconto.')
    x = int(10)
    desconto = (cash * x) / 100
    cash = cash - desconto
    print('O valor a ser pago é de {} reais'.format(cash))
elif payment == 2:
    print('Selecionado: Preço à vista.')
    print('Compras à vista no cartão tem 5% de desconto.')
    x = int(5)
    desconto = (cash * x) / 100
    cash = cash - desconto
    print('O valor a ser pago é de {} reais'.format(cash))
elif payment == 3:
    print('Selecionado: 2x sem juros no cartão.')
    parcela = cash / 2
    print('2 parcelas de {}'.format(parcela))
elif payment == 4:
    quantidade = int(input('Quantidade de parcelas: '))
    acressimo = (cash * 20) / 100
    cash = cash + acressimo
    parcelas = cash / quantidade
    print('Selecionado: {}x (juros de 20%)'.format(quantidade))
    print('{} parcelas de {} reais'.format(quantidade, parcelas))
else:
    cash = 0
    print('OPÇÃo INVÁLIDA de pagamento. Tente Novamente!')

# Exercício 45

import random

mao = random.randint(1, 3)
if mao == 1:
    jokempo = 'Pedra'
elif mao == 2:
    jokempo = 'Papel'
else:
    jokempo = 'Tesoura'

txt = '''
Jokempo !
1 --> Pedra.
2 --> Papel.
3 --> Tesoura.
'''
print(txt)
vc = int(input(''))

if mao == vc:
    print('O computador escolheu {} também !'.format(jokempo))
    print('O jogo empatou.')

print('O computador escolheu {}!'.format(jokempo))

if mao == 1 and vc == 2:
    print('Você escolheu PAPEL! Parabéns você ganhou !!!!')
elif mao == 2 and vc == 3:
    print('Você escolheu TESOURA! Parabéns você ganhou !!!!')
elif mao == 3 and vc == 1:
    print('Você escolheu PEDRA! Parabéns você ganhou !!!!')

if mao == 2 and vc == 1:
    print('Você escolheu PEDRA! o computador ganhou.')
elif mao == 3 and vc == 2:
    print('Você escolheu PAPEL! o computador ganhou.')
elif mao == 1 and vc == 3:
    print('Você escolheu TESOURA! o computador ganhou.')

# Exercício 46

import time

for x in range(10, -1, -1):
    print(x)
    time.sleep(0.5)
print('BOOOOOMMMMM !!!!')
print("seu cu é meu '-'")

# Exercício 47

for x in range(2, 51, 2):
    print(x)

# Exercício 48

c = 0
s = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
        c += 1
        s += x
print('A soma de todos os {} valores solicitados é {}'.format(c, s))

# Exercício 49

n = int(input('Digite um número: '))
print('Tabuada do {} -->'.format(n))
for x in range(1, 11):
    print('{} x {} = {}'.format(n, x, n * x))

# Exercício 50

s = 0
c = 0
for x in range(0, 6):
    n = int(input('Digite o {}º número: '.format(x + 1)))
    if n % 2 == 0:
        s += n
        c += 1
print('Você informou {} valores pares e soma deles é = {}'.format(c, s))

# Exercício 51

a1 = int(input('Digite o primeiro termo de uma P.A: '))
r = int(input('Digite a razão dessa P.A: '))
print('10 primeiros termos da P.A:')
for x in range(1, 11):
    x = a1 + (x - 1) * r
    print(x, end=' -> ')
    x = x + 1
print('ACABOU')

# Exercício 52

tot = 0
num = int(input('Digite um número: '))
for x in range(1, num + 1):
    if num % x == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(x), end=' ')
if tot == 2:
    print('\n\033[mEsse número é primo')
else:
    print('\n\033[mEsse número não é primo')
print('\033[mO número {} foi divisível {} vezes'.format(num, tot))

# Exercício 53

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for x in range(len(junto) - 1, -1, -1):
    inverso += junto[x]
print('{} ao contrário é {}, portanto'.format(junto, inverso), end=' ')
if inverso == junto:
    print('é um palíndromo')
else:
    print('não é um palíndromo')

# Exercício 54

from datetime import datetime

now = datetime.now()
maior = 0
menor = 0
print(now)
for x in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(x)))
    if now.year - ano >= 21:
        maior += 1
    elif now.year - ano <= 21:
        menor += 1
print('{} pessoas são maiores de idade'.format(maior))
print('{} pessoas são menores de idade'.format(menor))

# Exercício 55

maior = 0
menor = 0
for x in range(1, 6):
    peso = (float(input('Peso da {}ª pessoa: '.format(x))))
    if x == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {}kg'.format(maior))
print('O menor peso lido foi {}kg'.format(menor))

# Exercício 56

veio = 0
nome_do_veio = ''
mina = 0
soma_das_idades = 0
for x in range(1, 5):
    print('{:-^21}'.format(' {}ª PESSOA '.format(x)))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma_das_idades += idade
    if idade > veio and sexo == 'M':
        veio = idade
        nome_do_veio = nome
    if idade < 20 and sexo == 'F':
        mina += 1
print('A média de idade do grupo é de {} anos'.format(soma_das_idades / 5))
print('O homem mais velho tem {} anos e se chama {}'.format(veio, nome_do_veio))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mina))

# Exercício 57 "Validação de Dados"

n = 1
while n != 0:
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M' or sexo == 'F':
        n = 0
    else:
        print('Sintaxe errada digite "M" para masculino ou "F" para feminino')

# Exercício 58 "Jogo da advinhação 2.0"

import random
import emoji

acertou = bool(False)
n = random.randint(0, 100)
tentativas = 1
print('\033[1;33m=-\033[m' * 18)
print('\033[1;35mEstou pensando em um número de 0-10!\033[m')
print('\033[1;33m=-\033[m' * 18)
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

# Exercício 59 "Menu de opções"

import time

choice = 0
menu = '''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do programa
'''
choices = [1, 2, 3, 4, 5]
n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
print('')

while choice != 5:
    print(menu)
    choice = int(input('>>>>> Qual é sua opção? '))
    if choice == 1:
        print('')
        print('=-=' *10)
        print('{:^10}'.format('{} + {} = {}'.format(n1, n2, n1 + n2)))
        print('=-=' *10)
        time.sleep(2)
    elif choice == 2:
        print('')
        print('=-=' *10)
        print('\n{} x {} = {}'.format(n1, n2, n1 * n2))
        print('=-=' *10)
        time.sleep(2)
    elif choice == 3:
        if n1 > n2:
            print('')
            print('=-=' *10)
            print('O primeiro número é o maior.')
            print('=-=' *10)
            time.sleep(2)
        elif n2 > n1:
            print('')
            print('=-=' *10)
            print('O segundo número é o maior.')
            print('=-=' *10)
            time.sleep(2)
        else:
            print('')
            print('=-=' *10)
            print('Os dois números são iguais.')
            print('=-=' *10)
            time.sleep(2)
    elif choice == 4:
        n1 = int(input('1º número: '))
        n2 = int(input('2º número: '))
    elif choice == 5:
        print('Encerrando o programa. ', end='')
    else:
        print('')
        print('#' *32)
        print('Opção inválida! Tente novamente.')
        print('#' *32)
        print('')
        time.sleep(3)

time.sleep(1)
print('. ', end='')
time.sleep(1)
print('. ')
time.sleep(1)

# Exercício 60 "Cálculo Fatorial"
import time

print('Digite um número para')
n = int(input('calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
time.sleep(1)
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

# Exercício 61 "Progressão Aritimética"

a1 = int(input('Digite o primeiro termo de uma P.A: '))
r = int(input('Digite a razão dessa P.A: '))
x = 1
while x != 10:
    print(a1 + r, end=' -> ')
    a1 = a1 + r
    x += 1
print('ACABOU')

# Exercício 62 "Super Progressão Aritimética"

t = 10
a1 = int(input('Digite o primeiro termo de uma P.A: '))
r = int(input('Digite a razão dessa P.A: '))
while t != 0:
    x = 1
    while x != t:
        print(a1 + r, end=' -> ')
        a1 = a1 + r
        x += 1
    print('ACABOU')
    q = int(input('Mais termos? quantos: '))
    if q != 0:
        t += q
    else:
        t = 0

# Exercício 63 "Gerador de Fibonacci"

print('-'*30)
print('{:^30}'.format('Sequência de fibonacci'))
print('-'*30)
x = 0
y = int(input('Quantos números você quer mostrar? '))
a = 0
b = 1
print('~'*(y*6))
print('{} -> {}'.format(a,b), end=' -> ')
while x != (y-2):
    c = a + b
    a = b
    b = c
    print(c, end=' -> ')
    x += 1
print('FIM')
print('~'*(y*6))

# Exercício 64 "Tratando Vários Valore"

end = False
qnt = 1
soma = 0
while not end:
    n = int(input('Digite o {}º número [999 para parar]: '.format(qnt)))
    qnt += 1
    if n != 999:
        soma = soma + n
    else:
        end = True
print('Você digitou {} números, e a soma deles é: {}'.format(qnt-2, soma))

# Exercício 65 "Maior e Menor valores"

quer_continuar = True
qnt = 1
maior = 0
menor = 0
soma = 0
while quer_continuar:
    n = int(input('Digite o {}º número: '.format(qnt)))
    qnt += 1
    soma = soma + n
    quer = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if quer == 'N':
        quer_continuar = False
    elif quer == 'S':
        quer_continuar = True
    else:
        print('Vou interpretar isso como "sim"')
    if qnt == 2:
        maior = n
        menor = n
    else:
        if maior < n:
            maior = n
        if n < menor:
            menor = n
print('A média de todos os números foi: {}'.format(soma / (qnt - 1)))
print('O maior número digitado foi: {}'.format(maior))
print('O menor número digitado foi: {}'.format(menor))

# Exercício 66 "Vários números com Flag"

n = s = 0
c = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c += 1
    s += n
# print('A soma dos valores é: {}'.format(s))
print(f'Você digitou {c} números.')
print(f'A soma deles é: {s}')

# Exercício 67 "Tabuada"

while True:
    print('=-='*12)
    n = int(input('Quer ver a tabuada de qual valor ? '))
    print('=-='*12)
    if n < 0:
        break
    for x in range(1,11):
            print(f'{n} x {x} = {n*x}')
print('acabou')

# Exercício 68 "Par ou Ímpar ?"

import random
perdeu = False
win = 0
print('=-'*15)
print('{:^30}'.format('VAMOS JOGAR PAR OU ÍMPAR'))
print('=-'*15)
while not perdeu:
    n_pc = random.randint(0,10)
    par_ou_impar = str(input('Par ou impar? ')).strip().upper()[0]
    n = int(input('Seu número [0-10]: '))
    if n == n_pc:
        print(f'O computador escolheu {n_pc} também!')
    else:
        print(f'O computador escolheu {n_pc}')
    jogo = n + n_pc
    print(f'{n} + {n_pc} = {jogo}')
    if jogo % 2 == 0:
        print('Deu par!')
        if par_ou_impar == 'P':
            print('Parabéns, você venceu!')
            win += 1    
        else:
            print('Você perdeu.')
            perdeu = True
    else:
        print('Deu ímpar!')
        if par_ou_impar == 'I':
            print('Parabéns, você venceu!')
            win += 1    
        else:
            print('Você perdeu.')
            perdeu = True
print(f'Você teve {win} vitórias consecutivas')

# Exercício 69 "análize de dados de um grupo"

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

# Exercício 70 "Lojinho do Tadeu (quem comprou se fodeu) 2.0"

print('='*50)
print('{:-^50}'.format('Lojinho do Tadeu 2.0'))
print('='*50)
quer_continuar = True
mais_de_mil = 0
mais_barato = 'Pinto'
valor_barato = 0
contador = 0
total = 0
while quer_continuar:
    podrutu = str(input('Nome do produto: ')).strip().capitalize()
    preco = float(input('Preço R$'))
    total += preco
    contador += 1
    if contador == 1:
        valor_barato = preco
        mais_barato = podrutu
    if preco > 1000.00:
        mais_de_mil += 1
    if preco < valor_barato:
        valor_barato = preco
        mais_barato = podrutu
    while True:
        quer = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if quer == 'S':
            break
        elif quer == 'N':
            quer_continuar = False
            break
print('\n{:-^50}'.format('FIM DO PROGRAMA'))
print('O total gasto na compra foi de: R${:.2f}'.format(total))
print(f'{mais_de_mil} produtos custam mais de R$1000')
print('O produto mais barato foi o {} custando R${:.2f}'.format(mais_barato, valor_barato)) 
print('-'*50)

# Exercício 71 "Simulador de Caixa eletronico"

print('='*25)
print('{:^25}'.format('FuckBank'))
print('='*25)
valor = int(input('Que valor você quer sacar? R$'))
cinquenta = int(0)
vinte = int(0)
dez = int(0)
um = int(0)
while valor > 0:
    if valor > 50:
        cinquenta = valor // 50
        valor = valor - (cinquenta * 50)
    elif valor > 20:
        vinte = valor // 20
        valor = valor - (vinte * 20)
    elif valor > 10:
        dez = valor // 10
        valor = valor - (dez *10)
    elif valor < 10:
        um = valor
        valor = 0
if cinquenta > 0:
    print(f'Total de {cinquenta} notas de R$50')
if vinte > 0:
    print(f'Total de {vinte} notas de R$20')
if dez > 0:    
    print(f'Total de {dez} notas de R$10')
if um > 0:
    print(f'Total de {um} notas de R$1')
print('='*25)
print('Volte sempre ao FuckBanck! tenha um dia Foda!')



