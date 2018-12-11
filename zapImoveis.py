import ast
from selenium import webdriver   # Importa o webdriver
from selenium.webdriver.chrome.options import Options  # Options para utilizar o chrome driver em modo HeadLess(sem interface gráfica)
from bs4 import BeautifulSoup

# Configurando o chromeDriver para o modo Headless
options = Options()
options.headless = True
driver = webdriver.Chrome(chrome_options=options)
page = '1'

url = 'https://www.zapimoveis.com.br/aluguel/imoveis/#{"pagina":"'+page+'","paginaOrigem":"Home","formato":"Lista"}'

driver.get(url)  # Faz o request

pageContent = driver.page_source

soup = BeautifulSoup(pageContent, 'html.parser') # Tranformando em objeto BeautifulSoup

listaDeAnuncios = soup.find_all('article', class_='minificha')  # Lista com os 22 anuncios da página

# Atualizado em:
atualizado = listaDeAnuncios[0].find(class_='atualizacao').get_text() # Find retorna um objeto BeautifulSoup, find_all retorna uma lista de objetos Bsoup

print(listaDeAnuncios[0].find(class_='preco').strip().get_text())


'''
desc = listaDeAnuncios[0]['data-clickstream']  # Desc é uma string com a mesma sintaxe que um dicionario
dic = eval(desc) # Eval transforma strings em objetos do python de acordo com sua sintaxe


#print(listaDeAnuncios[0])
print(dic['listingId'])
print(dic['unitTypes'])
print(dic['areas'])
print(dic['parkingSpaces'])
print(dic['bathrooms'])
print(dic['bedrooms'])
print(dic['suites'])
print(dic['salePrices'])
print(dic['rentalPrices'])
print(dic['condoFee'])
print(dic['iptuPrices'])
print(dic['address'])
print(dic['amenities'])
print(atualizado)
'''
