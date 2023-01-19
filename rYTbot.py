import requests
import time

print('''
____________________$
___________________$$$
__________________$$$$$
_________________$$$$$$$
________________$$$$$$$$$
_______________$$$$$$$$$$$
______________$$$$$$$$$$$$$
_____________$$$$$$$$$$$$$$$
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

Ver: 2.1 beta
===============BOT BY RAI==================
Mantenha o BOT atualizado para continuar funcionando.
Para atualizar basta clonar o repositorio do github novamente.
    ''')

youtube_url = input("Insira a URL do video: ")

try:
    with open(input("Nome do arquivo contendo as proxys: "), "r") as proxy_file:
        proxies = proxy_file.read().splitlines()
except FileNotFoundError:
    print("Arquivo não encontrado.")
    proxies = []

valid_proxy = None
for proxy in proxies:
    try:
        # Usa a proxy para entrar no video.
        response = requests.get(youtube_url, proxies={"http": "http://"+proxy, "https": "http://"+proxy}, timeout=35)
        # Se a proxy retornar o valor 200, a proxy será bem sucedida
        if response.status_code == 200:
            valid_proxy = proxy
            print("Proxy " + proxy + " bem sucedida.")
            time.sleep(30)
        else:
            # Verifica se a proxy foi bloqueada
            if "The proxy server is refusing connections" in response.text or "The proxy server received an invalid response from an upstream server" in response.text:
                print("Proxy " + proxy + " bloqueada pelo youtube")
            else:
                print("Proxy " + proxy + " invalida.")
    except:
        print("Proxy " + proxy + " invalida.")

if valid_proxy == None:
    print("Nenhuma proxy valida encontrada.")
