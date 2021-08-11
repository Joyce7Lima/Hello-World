#importação das bibliotecas

from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd

s = HTMLSession()
procutslist = []
searchterm = 'iphone'
url = f'https://www.amazon.com.br/s?k={searchterm}&ref=nb_sb_noss'

#Função para extração dos dados

def getdata(url):
    r = s.get(url)
    r.html.render(sleep=1)
    soup = BeautifulSoup(r.html.html, 'html.parser')
    return soup

#Função tratamento de dados. Nome/Preço

def getproducts(soup):
    products = soup.find_all('div', {'data-component-type': 's-search-result'})
    for item in products:
        title = item.find('a', {'class': 'a-link-normal a-text-normal'}).text.strip()
        try:
            price = item.find('span', {'class': 'a-offscreen'}).text.replace('R$', '').strip()
        except:
            price = 0

        iphoneitem = {
            'title': title,
            'price': price
             }
        procutslist.append(iphoneitem)
        print(iphoneitem)
    return


#Chamado das funções

soup = getdata(url)
getproducts(soup)
print(url)
print(len(procutslist))


#Exportando os dados


df = pd.DataFrame(procutslist)
df['title'] = (df.title)
df['price'] = (df.price)
df.to_csv('simple.csv', index=False)
print(df)
print('')
print('Processo Finalizado.')