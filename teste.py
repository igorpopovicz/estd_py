'''
listafoda = []
c = 0
for x in range(0,4):
    valor = int(input('Digite um valor: '))
    if c == 0:
        listafoda.append(valor)
        print('Adicionado ao final da lista...')
        c = 1
    if valor < min(listafoda):
        listafoda.insert(0, valor)
        print('Adicionando na posição 0 da lista...')
    elif valor > max(listafoda):
        listafoda.append(valor)
        print('Adicionando ao final da lista...')
    elif len(listafoda) == 3:
        if valor >= listafoda[1]:
            listafoda.insert(2, valor)
            print('Adicionando valor na posição 2 da lista...')
        elif valor < listafoda[1]:
            listafoda.insert(1, valor)
            print('Adicionando valor na posição 1 da lista...')
    elif len(listafoda) == 4:
        if valor >= listafoda[1] or valor > listafoda[2]:
            listafoda.insert(2, valor)
            print('Adicionando valor na posição 2 da lista...')
        elif valor < listafoda[1]:
            listafoda.insert(1, valor)
            print('Adicionando valor na posição 1 da lista...')
        elif valor >= listafoda[2]:
            listafoda.insert(3, valor)
            print('Adicionando valor na posição 3 da lista...')
print(listafoda)
'''
listapika = []
continua = True
while continua:
    listapika.append(int(input('Digite um valor: ')))
