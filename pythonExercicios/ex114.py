import requests
import urllib.request
try:
    site = 'https://www.cursoemvideo.com/'
    conect = requests.get(site)
    print("Consegui acessar o site 'Curso em Video' com sucesso!")
except:
    print("Falha! Site não está acessível no momento.")

try:
    site2 = urllib.request.urlopen('https://www.pudim.com.br/')
except urllib.error.URLError:
    print("Não consegui acessar o site 'pudim'")
else:
    print("OK")
