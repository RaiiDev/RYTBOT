import requests
import re
import time

# Recebe o nome do arquivo de proxies
file_name = input("Insira o nome do arquivo de proxies: ")

# Recebe o link do video
url = input("Insira o link do video: ")

# Verifica se o link é válido e pertence ao YouTube
youtube_regex = re.compile(r'^(https?\:\/\/)?(www\.)?(youtube\.com|youtu\.?be)\/.+$')
if not youtube_regex.match(url):
    print("O link não é válido ou não pertence ao YouTube.")
    exit()
else:
    try:
        response = requests.get(url)
        if "youtube" in response.text.lower():
            print("Link válido para vídeo do YouTube.")
        else:
            print("O link não é válido ou não pertence ao YouTube.")
            exit()
    except requests.exceptions.RequestException as e:
        print("Erro ao verificar link: " + e)
        exit()

# Abrir arquivo com proxy
with open(file_name) as f:
    proxies = f.read().splitlines()

# Adiciona o protocolo http ou https se ele não estiver presente na proxy
for i, proxy in enumerate(proxies):
    if not re.match(r'^https?:\/\/', proxy):
        proxies[i] = 'http://' + proxy

proxy_counter = 0
while proxy_counter < len(proxies):
    protocol = "http"
    while True:
        try:
            start_time = time.time()
            response = requests.get(url, proxies={protocol: proxies[proxy_counter]}, timeout=30)
            response.raise_for_status()
            end_time = time.time()
            total_time = end_time - start_time
            if total_time < 30:
                time.sleep(30 - total_time)
            print("Proxy bem-sucedida: " + proxies[proxy_counter] + " Protocolo: " + protocol + " Tempo de visualização: {} segundos".format(total_time))
            proxy_counter += 1
            break

        except requests.exceptions.RequestException as e:
            if protocol == "http":
                protocol = "https"
                continue
            elif protocol == "https":
                print("Erro ao utilizar proxy: " + proxies[proxy_counter])
                proxy_counter += 1
                break
else:
    print("Todas as proxys foram lidas.")
    exit()