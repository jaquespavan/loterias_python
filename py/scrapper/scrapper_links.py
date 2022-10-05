import requests
from bs4 import BeautifulSoup

file = open('D:\\testep\[novo]\scrapper_links.txt','w', encoding='utf-8')

url = 'https://en.wikipedia.org/wiki/List_of_Neo_Geo_games'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

conteudo = soup.prettify()

#links = []

for i in soup.find_all('a'):
    #texto = i.get('href')
    links = "'" + str(i.get('href')) + "'," + '\n'
    file.write(links)
    #if texto[0:6] == '/wiki/':
#    links.append(texto)

#print(links)
#print('Texto:', type(texto))
#print('Links:', type(links))

file.close()


