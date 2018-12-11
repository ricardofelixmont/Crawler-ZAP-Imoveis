from selenium import webdriver   # Importa o webdriver
from selenium.webdriver.chrome.options import Options  # Options para utilizar o chrome driver em modo HeadLess(sem interface gráfica)
from bs4 import BeautifulSoup
import requests


url = 'https://www.zapimoveis.com.br/aluguel/imoveis/#{"pagina":"1","paginaOrigem":"Home","formato":"Lista"}'
req = requests.get(url,headers ={"User-Agent":"=Mozila/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}).text

print(req)
