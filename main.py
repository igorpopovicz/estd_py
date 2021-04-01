# Verificação de String


a = input('Digite algo: ')
print('Você Digitou', a)
print(a, 'é da classe', type(a))
print('São espaços ?', a.isspace())
print('É um número ?', a.isnumeric())
print('É alfabético ?', a.isalpha())
print('É alfanumérico ?', a.isalnum())
print('Está em maiúsculas ?', a.isupper())
print('É um "título"', a.istitle())
print('Está em minúsculas ?', a.islower())


# Sequência de operação


print('1 - ().')
print('2 - ** (potência).')
print('3 - *, /, // (divisão inteira), % (resto da divisão).')
print('4 - + e -.') 


# .format


# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite mais um: '))
# s = n1 + n2
# print('A soma desses dois números é: {}'.format(s))

# nome = input('Qual é o seu nome ? ')
# print('Prazer em te conhecer {:=^20}!'.format(nome))

# n1 = int(input('digite um número: '))
# n2 = int(input('Outro número: '))
# s = n1 + n2
# m = n1 * n2
# d = n1 / n2
# di = n1 // n2
# p = n1 ** n2
# print('A soma dos dois é {}, o produto é {}, a divisão é {}'.format(s, m, d))


# Bibliotecas (usando a math e random)


import math
an = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O seno de {}° é: {:.2f}'.format(an, sen))
print('O cosseno de {}° é: {:.2f}'.format(an, cos))
print('A tangente de {}° é: {:.2f}'.format(an, tan))


# Função choice (escolher)

import random

aln1 = str(input('Digite o nome do primeiro aluno: '))
aln2 = str(input('Segundo aluno: '))
aln3 = str(input('Terceiro aluno: '))
aln4 = str(input('Quarto aluno: '))

lista = [aln1, aln2, aln3, aln4]

escolha = random.choice(lista)

print('O aluno escolhido foi {}'.format(escolha))


# Função shuffle (embaralhar)


import random

aln1 = str(input('Primeiro aluno: '))
aln2 = str(input('Segundo aluno: '))
aln3 = str(input('Terceiro aluno: '))
aln4 = str(input('Quarto aluno: '))

lista = [aln1, aln2, aln3, aln4]

random.shuffle(lista)

print('A ordem será :')
print(lista)


# Biblioteca datetime (pegando a data do sistema)

from datetime import datetime
ano = datetime.today().strftime('%d-%m-%Y')
print(ano)


# Manipulando texto

frase = 'pega no meu pau'
print(frase[9:14])
print(len(frase))  # Retorna o comprimento (caracteres) da string.
frase.count('e')  # Conta quantas vezes o caracter 'e' aparece.
frase.count('e', 0, 13)  # Conta quantas vezes o caracter 'e' aparece no intervalo 0-12.
frase.find('meu')  # Encontra quantas vezes aparece a string 'meu'.
'pau' in frase  # Retorna, true, se houver 'pau' na string.
frase.replace('pau', 'pipi')  # Substitue 'pau' por 'pipi'.
frase.upper()  # Transforma a string inteira em maiúscula.
frase.lower()  # Transforma a string inteira em minúscula.
frase.capitalize()  # Transforma a string em "correta gramaticamente".
frase.title()  # Coloca todoas as palavras com a primeira letra maiúscula.
frase.strip()  # Remove tos os espaços inúteis de uma string
frase.rstrip()  # Remove todos os espaços inúteis a direita.
frase.lstrip()  # Remove todos os espaços inúteis a esquerda.
frase.split()  # Divide a string por palavras, transformando-as em novas strings (lista).
'-'.join(frase)  # Junta string separadas (listas) em uma única string separadas por '-'.
print('texto foda!', end='') # Não pula linha.


# Condicionais


tempo = int(input('Quantos anos tem o seu carro ? '))
if tempo <= 3:
    print('Tá novinho :)')
else:
    print('Vamo trocar esse meninão aí em ;)')



n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
print('Sua média foi de {}'.format(m))
if m >= 60.0:
    print('Parabéns! Sua média é azul.')
else:
    print('Está com média vermelha >:( estude mais!')


# Cores no Terminal

# \033[0;30;41m
# \033[4;33;44m
# \033[1;35;43m
# \033[0;30;42m
# \033[m
# \033[7;30m
# \033[4;36;45m esse é foda
# \033[4;33;45m topzera

# Condicionais aninhadas


nome = str(input('Qual o seu nome ? '))  
if nome == 'caralinhos':
    print('Opa tudo bom {}'.format(nome))
elif nome == 'igor':
    print('um dos caras mais fodas do brasil')
elif nome == 'João' or 'Joao' or 'Jão':
    print('Faaaala jão bão ?')
elif nome in 'Pedro Maria Thiago Marcos':
    print('Opa bom dia')
else: 
    print('Tenha um bom dia')


# Laço de repetição for


for x in range(0, 15): # imprimindo a string 15 vezes.
    print('cu')

for x in range(0, 4): # imprimindo a variable x criada pelo for 4 vezes.
    print(x)

caralho = 'pipi'
for x in range(0, 2): # imprimindo a variable caralho 2 vezes.
    print(caralho)

for a in range(4, 0, -1): # imprimindo " de traz pra frente ".
    print(a)

for b in range(0, 7, 2): # imprimindo de 0 até 6 pulando de 2 em 2.
    print(b)

n = int(input('Digite um número: '))
for c in range(0, n):
    print(c)

i = int(input('início: '))
f = int(input('fim: '))
p = int(input('passo: '))
for n in range (i, f+1, p):
    print(n)


# Laço de repetição while

c = 1
while c < 10:
    print(c)
    c += 1

n = 1
while n != 0:
    n = int(input('digite um valor: '))

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM')

par = impar = 0
n = 1
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} ímpares.'.format(par, impar))

# Interrompendo o while

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# print('A soma dos valores é: {}'.format(s))
print(f'A soma dos valores é: {s}')

# Variáveis compostas 

# Tuplas

lanche = ('hambúrger', 'suco', 'pizza', 'pudim')
print(lanche)
print(lanche[1])
print(lanche[1:3])
print(lanche[2:])
for comida in lanche:
    print(comida)
for x in range(0, len(lanche)):
    print(lanche[x])
for y, x in enumerate(lanche):
    print(f'Eu vou comer {y} na posição {x}')

print(sorted(lanche)) # Ordem alfabética

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # -> c = (2, 5, 4, 5, 8, 1, 2)
print(c.count(5)) # quantas vezes aparece o número 5
print(c.index(8)) # em qual posição está o 8
del (a) # deleta a tupla "a"

# Listas

lanche = ['Hamburger', 'Suco', 'Pizza', 'Pudim']
#substituindo
lanche[3] = 'Sorvete' # Lanche -> ['hamburger', 'suco', 'pizza', 'SORVETE']
#Adicionando
lanche.append('Cookie') # Lanche -> ['hamburger', 'suco', 'pizza', 'sorvete', 'COOKIE"]
lanche.insert(0,'Cachorro_quente') # ['CACHORRO_QUENTE', 'hamburger', 'suco', 'pizza', 'sorvete', 'cookie"]
#Removendo
del lanche[3] # -> ['cachorro_quente', 'hamburger', 'suco', 'sorvete', 'cookie"]
lanche.pop(3) # ^^^^^^
lanche.remove('pizza') # ^^^^^^
lanche.pop() # Remove o último elemento

if 'pizza' in lanche:
    lanche.remove('pizza')

valores = list(range(4,11)) # -> valores = [4, 5, 6, 7, 8, 9, 10]
valore = [8,2,5,4,9,3,0]
#Organizar: 
valores.sort() # -> valores = [0, 2, 3, 4, 5, 8, 9]
#Ordem inversa: 
valores.sort(reverse=True) # -> [9, 8, 5, 4, 3, 2, 1]
#Quantidade de valores em uma Lista
len(valores) # -> 7

# Valores dados por um usuário em uma tupla
valores = []
for x in range(0,3):
    valores.append(int(input('Digite um número: ')))
print('Você Digitou os valores: ', end='')

for x in valores:
    print(x , end='')
print('\n')

# Verificando tuplas
valoress = []
valoress.append(5)
valoress.append(9)
valoress.append(4)

for y, x in enumerate(valoress):
    print(f'Na posição {y} encontrei o valor {x}!')
print('Cheguei ao final da lista')

# "Ligando uma lista a outra"
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(a) # [2, 3, 8, 7]
print(b) # [2, 3, 8, 7]

# "Criando uma cópia"
a = [1, 2, 3, 4]
b = a[:]
b[2] = 8
print(a) # [1, 2, 3, 4]
print(b) # [1, 2, 8, 4]

