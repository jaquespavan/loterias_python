import requests
from bs4 import BeautifulSoup
import time
import random

file = open('D:\\testep\[novo]\scrap_teste_USA.txt','w', encoding='utf-8')

lista = [
#'https://en.wikipedia.org/wiki/George_W._Bush',
'https://en.wikipedia.org/wiki/Barack_Obama',
#'https://en.wikipedia.org/wiki/Donald_Trump',
]

classe = "infobox vcard"

print('========================================')
file.write('========================================' + '\n')

for i in lista:

    page = requests.get(i)

    #print(page.status_code)

    #status = page.status_code

    soup = BeautifulSoup(page.text, 'html.parser')

    conteudo = soup.prettify()

    titulo = soup.title.string
    

    #print(soup.find('tr'))

    
    #print(soup.table('class="infobox hproduct"'))

    #print(soup.find("table",{"class":"infobox hproduct"}))

    try:        

        table = soup.find('table',{'class':classe})

        #data_nasc = table.find('span',{'class':"bday"}).get_text()
        #print(data_nasc)
                
        #print(table)

        tr = table.find_all('tr')

        for i in tr:

            separador = ': '

            try:
                th = i.find('th').get_text()
            except:
                th = ''
                separador = ''

            try:
                td = i.find('td').get_text()
                if th == '':
                    td = td + '\n'
            except:
                td = '' + '\n'
                separador = ''
                #th = '\n' + th
        
            linha_box_info = str(th) + separador + str(td)
            print(linha_box_info)
            file.write(linha_box_info + '\n')
                        
    except:
        print('\n')
        print('\n')
        print('ERROR ========================================')
        print(titulo)
        print('Classe ' + classe + ' não encontrada')
        print('ERROR ========================================')
        print('\n')
        print('\n')

        file.write('\n' + '\n' + 'ERROR ========================================' + '\n' + titulo + '\n' + 'Classe ' + classe + ' não encontrada' + '\n' + 'ERROR ========================================' + '\n' + '\n')

    print('========================================')
    file.write('========================================' + '\n')

print('\n' + '===== FIM =====')
file.write('\n' + '===== FIM =====')

file.close()
