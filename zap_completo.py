from bs4 import BeautifulSoup
import requests

def request(url):

    pageContent = requests.get(url,headers ={"User-Agent":"=Mozila/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"})
    #print(pageContent.text)

    # Para passar um objeto request para BeautifulSoup precisamos passar pageContent.content
    soup = BeautifulSoup(pageContent.content, 'html.parser') # Tranformando em objeto BeautifulSoup


    listaDeAnuncios = soup.find_all('article', class_='minificha')  # Lista com os 22 anuncios da página
    # Encontrar o numero de paginas:
    # nPaginas = soup.find(class_='pull-right num-of').get_text()[-6:]
    return listaDeAnuncios



if __name__=='__main__':
    # Passando de Pagina
    page = 1
    for c in range(0, 5):
        url = 'https://www.zapimoveis.com.br/aluguel/imoveis/#{"pagina":"' + str(page) + '","paginaOrigem":"Home","formato":"Lista"}'
        print(url+'\n')
        listaDeAnuncio = request(url)
        # Encontrando elemento final
        for anuncio in listaDeAnuncio:
            #d Atualizado em:
            atualizado = anuncio.find(class_='atualizacao').get_text() # Find retorna um objeto BeautifulSoup, find_all retorna uma lista de objetos Bsoup
            desc = anuncio['data-clickstream']  # Desc é uma string com a mesma sintaxe que um dicionario

            # Dic é de onde vou pegar todas as informações de cada anuncio
            dic = eval(desc) # Eval transforma strings em objetos do python de acordo com sua sintaxe
            dic['update'] = atualizado
            print(dic)
            print(atualizado)
        page += 1
'''
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
