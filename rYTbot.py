import requests
import time
import sys
import os

print('''
____________________$
___________________$$$
__________________$$$$$
_________________$$$$$$$
________________$$$$$$$$$
_______________$$$$$$$$$$$
______________$$$$$$$$$$$$$
_____________$$==RYTBOT==$$$
____________$$$$$$$$$$$$$$$$$
___________$$$$$$$$$$$$$$$$$$$
_________$$$$$$$$$$$$$$$$$$$$$$$
________$_______________________$
_______$_________________________$
_______$_________________________$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
_____$$$$$$__$$___________$$__$$$$$
____$$$$$___$$$$_________$$$$__$$$$_$_$_$_$_$_$
____$$$$$____$$___________$$____$$$_$$$$$$$$$$
_____$$$$_______________________$$$_$_$__$__$
_______$$$$____$$______$$______$$$__$_$_$__$
__________$$$____$$$$$$$_____$$______$_$$_$
____________$$$___________$$$________$$$$$
_____________$$$$$$$$$$$$$$$$$$______$$$$
___________$$$$$$$$$$$$$$$$$$$$$$$___$$$
__________$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
_________$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
________$$$$$$$$$$$$$$$$$$$$$$_$$__$$$
________$___$$$$$$$$$$$$$$$$$$___$$$$
________$$__$$$$$$$$$$$$$$$$$$____$$
_________$$$$$$$$$$$$$$$$$$$$$___$$
___________$$$$$$$$$$$$$$$$$$$___$$
___________$$$$$$$$$$$$$$$$$$$__$$
___________$$$$$$$$$$$$$$$$$$$__$$
___________$$$$$$$$$$$$$$$$$$$_$$
____________$$$___$$$$$___$$$__$$
_______________$$$_____$$$____$$
Ver: 2.6 beta
    ''')
print('''
===============BOT BY RAI==================
Mantenha o BOT atualizado para continuar funcionando.
Atenção! Copie o link do YouTube pelo navegador. (Veja o tutorial no github)
''')

youtube_url = input("Insira a URL do video: ")

try:
    with open(input("Nome do arquivo contendo as proxys: "), "r") as proxy_file:
        proxies = proxy_file.read().splitlines()
except FileNotFoundError:
    print("Arquivo não encontrado.")
    proxies = []

print("Verificando as proxies...")
valid_proxies = []
for proxy in proxies:
    print("Verificando a proxy: " + proxy)
    try:
        # Usa a proxy para entrar no video.
        response = requests.head(youtube_url, proxies={"http": "http://"+proxy, "https": "http://"+proxy}, headers={'User-Agent': 'Mozilla/5.0'},  timeout=5)
        # Se a proxy retornar o valor 200, a proxy será bem sucedida
        if response.status_code == 200:
            valid_proxies.append(proxy)
    except:
        pass

if len(valid_proxies) == 0:
    print("Nenhuma proxy valida encontrada.")
else:
    print(f"{len(valid_proxies)} proxy(s) validas(s) encontradas. Utilizando as proxys para visualizar o video...")
    salvar = input("Deseja salvar as proxys funcionais em um arquivo txt? (s/n)")
    if salvar == "s":
        with open("proxies_validas.txt", "w") as valid_proxy_file:
            for valid_proxy in valid_proxies:
                valid_proxy_file.write(valid_proxy + "\n")
                print(f"Usando a proxy: {valid_proxy}")
                try:
                    # Use the proxy to access the video
                    response = requests.get(youtube_url, proxies={"http": "http://"+valid_proxy, "https": "http://"+valid_proxy}, headers={'User-Agent': 'Mozilla/5.0'},  timeout=30)
                    if response.status_code == 200:
                        time.sleep(30)
                except requests.exceptions.RequestException:
                    print("Proxy " + valid_proxy + " inválida.")
   
    else:
        for valid_proxy in valid_proxies:
            print(f"Usando a proxy: {valid_proxy}")
            try:
                # Use the proxy to access the video
                response = requests.get(youtube_url, proxies={"http": "http://"+valid_proxy, "https": "http://"+valid_proxy}, headers={'User-Agent': 'Mozilla/5.0'},  timeout=30)
                if response.status_code == 200:
                    time.sleep(30)
            except requests.exceptions.RequestException:
                print("Proxy " + valid_proxy + " inválida.")
