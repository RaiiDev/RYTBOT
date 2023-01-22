import random
import requests
import time
import socks
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
Ver: 3.1 beta
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

# Lista de user-agents possíveis
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
]

print("Verificando as proxies...")
valid_proxies = []
for proxy in proxies:
    print("Verificando a proxy: " + proxy)
    try:
        # Usa a proxy para entrar no video.
        response = requests.head(youtube_url, proxies={"http": "socks5://"+proxy, "https": "socks5://"+proxy}, headers={'User-Agent': random.choice(user_agents)}, timeout=5)
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
                    response = requests.get(youtube_url, proxies={"http": "socks5://"+valid_proxy, "https": "socks5://"+valid_proxy}, headers={'User-Agent': random.choice(user_agents)}, timeout=20)
                    if response.status_code == 200:
                        time.sleep(30)
                except requests.exceptions.RequestException:
                    print("Proxy " + valid_proxy + " inválida.")
   
    else:
        for valid_proxy in valid_proxies:
            print(f"Usando a proxy: {valid_proxy}")
            try:
                # Use the proxy to access the video
                response = requests.get(youtube_url, proxies={"http": "socks5://"+valid_proxy, "https": "socks5://"+valid_proxy}, headers={'User-Agent': random.choice(user_agents)}, timeout=20)
                if response.status_code == 200:
                    time.sleep(30)
            except requests.exceptions.RequestException:
                print("Proxy " + valid_proxy + " inválida.")
