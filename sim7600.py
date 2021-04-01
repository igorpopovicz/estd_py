import socket

quatro_g = False
wifi = True

confiaveis = ['www.google.com', 'www.twitch.tv', 'www.youtube.com']

def check_host():
    global confiaveis
    for host in confiaveis:
        a=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        a.settimeout(.5)
        try:
            b=a.connect_ex((host, 80))
            if b==0: #ok, conectado
                return True
        except:
            pass
        a.close()
    return False

# print(check_host() and "Conexão Ativa" or "Conexão Inativa")

if check_host() == True:
    print('Tudo ok meu patrão')
else:
    print('D: ta morto')
    quatro_g = True
    wifi = False

if quatro_g == True:
    