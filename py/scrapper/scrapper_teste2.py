import requests
from bs4 import BeautifulSoup
import time
import random

#file = open('D:\\testep\[novo]\scrap_teste3.csv','w', encoding='utf-8')

lista = [
'https://en.wikipedia.org/wiki/George_Washington',
]

#url = 'https://www.mobygames.com/game/final-fight'

for i in lista:

    page = requests.get(i)

    #print(page.status_code)

    #status = page.status_code

    soup = BeautifulSoup(page.text, 'html.parser')

    conteudo = soup.prettify()

    titulo = soup.title.string
    #titulo_jogo = soup.find_all('th')[0].get_text()

    print(titulo)

    #print(soup.find_all('th'))


    #print(soup.find_all('th').get_text())
     


    '''
    for i in soup.find_all('td'):
        print(i.get('td'))
        print(i.get('th'))
    
        #file.write(conteudo)

#file.close()
'''