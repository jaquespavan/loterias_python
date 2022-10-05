import requests
from bs4 import BeautifulSoup
import time
import random
from datetime import datetime
from datetime import date

#from dateutil.relativedelta import relativedelta

file = open('D:\\testep\[novo]\scrap_teste_USA_miniteste.txt','w', encoding='utf-8')

lista = [
'https://en.wikipedia.org/wiki/George_Washington',
'https://en.wikipedia.org/wiki/John_Adams',
'https://en.wikipedia.org/wiki/Thomas_Jefferson',
'https://en.wikipedia.org/wiki/James_Madison',
'https://en.wikipedia.org/wiki/James_Monroe',
'https://en.wikipedia.org/wiki/John_Quincy_Adams',
'https://en.wikipedia.org/wiki/Andrew_Jackson',
'https://en.wikipedia.org/wiki/Martin_Van_Buren',
'https://en.wikipedia.org/wiki/William_Henry_Harrison',
'https://en.wikipedia.org/wiki/John_Tyler',
'https://en.wikipedia.org/wiki/James_K._Polk',
'https://en.wikipedia.org/wiki/Zachary_Taylor',
'https://en.wikipedia.org/wiki/Millard_Fillmore',
'https://en.wikipedia.org/wiki/Franklin_Pierce',
'https://en.wikipedia.org/wiki/James_Buchanan',
'https://en.wikipedia.org/wiki/Abraham_Lincoln',
'https://en.wikipedia.org/wiki/Andrew_Johnson',
'https://en.wikipedia.org/wiki/Ulysses_S._Grant',
'https://en.wikipedia.org/wiki/Rutherford_B._Hayes',
'https://en.wikipedia.org/wiki/James_A._Garfield',
'https://en.wikipedia.org/wiki/Chester_A._Arthur',
'https://en.wikipedia.org/wiki/Grover_Cleveland',
'https://en.wikipedia.org/wiki/Benjamin_Harrison',
'https://en.wikipedia.org/wiki/Grover_Cleveland',
'https://en.wikipedia.org/wiki/William_McKinley',
'https://en.wikipedia.org/wiki/Theodore_Roosevelt',
'https://en.wikipedia.org/wiki/William_Howard_Taft',
'https://en.wikipedia.org/wiki/Woodrow_Wilson',
'https://en.wikipedia.org/wiki/Warren_G._Harding',
'https://en.wikipedia.org/wiki/Calvin_Coolidge',
'https://en.wikipedia.org/wiki/Herbert_Hoover',
'https://en.wikipedia.org/wiki/Franklin_D._Roosevelt',
'https://en.wikipedia.org/wiki/Harry_S._Truman',
'https://en.wikipedia.org/wiki/Dwight_D._Eisenhower',
'https://en.wikipedia.org/wiki/John_F._Kennedy',
'https://en.wikipedia.org/wiki/Lyndon_B._Johnson',
'https://en.wikipedia.org/wiki/Richard_Nixon',
'https://en.wikipedia.org/wiki/Gerald_Ford',
'https://en.wikipedia.org/wiki/Jimmy_Carter',
'https://en.wikipedia.org/wiki/Ronald_Reagan',
'https://en.wikipedia.org/wiki/George_H._W._Bush',
'https://en.wikipedia.org/wiki/Bill_Clinton',
'https://en.wikipedia.org/wiki/George_W._Bush',
'https://en.wikipedia.org/wiki/Barack_Obama',
'https://en.wikipedia.org/wiki/Donald_Trump',
]

classe = "infobox vcard"

#print('========================================')
#file.write('========================================' + '\n')

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

    table = soup.find('table',{'class':classe})

    tr = table.find_all('tr')

            
    '''
    data_nasc_aux = table.find('span',{'class':"bday"}).get_text()
    print(data_nasc_aux)

    data_hoje = datetime.today().strftime('%Y-%m-%d')
    print(data_hoje)

    d1 = datetime.strptime(data_nasc_aux, '%Y-%m-%d')
    d2 = datetime.strptime(data_hoje, '%Y-%m-%d')
    qtd_anos = abs((d2 - d1).days) / 365
    print(qtd_anos)
    '''

    nome = soup.find_all('th')[0].get_text()
    #print(nome)

    data_nasc_aux = table.find('span',{'class':"bday"}).get_text()
    #print(data_nasc_aux)

    data_hoje = datetime.today().strftime('%Y-%m-%d')
    #print(data_hoje)

    d1 = datetime.strptime(data_nasc_aux, '%Y-%m-%d')
    d2 = datetime.strptime(data_hoje, '%Y-%m-%d')
    qtd_anos = abs((d2 - d1).days) / 365
    #print(qtd_anos)

    controle = False
    while controle == False:

        for i in tr:
            

            dt_ini = ''
                      
            try:
                td = i.find('td').get_text()
                if td[0:9] == 'In office':
                    dt_ini = td
                    #print(dt_ini)
                    break
                else:
                    #controle = False
                    dt_ini = ''
                                            
            except:
                #controle = False
                dt_ini = ''

        controle = True
            
        linha_box_info = str(dt_ini)
        print(nome + ';' + data_nasc_aux + ';' + linha_box_info)
        file.write(nome + ';' + data_nasc_aux + ';' + linha_box_info + '\n')
            
#    print('========================================')
#    file.write('========================================' + '\n')

print('\n' + '===== FIM =====')
file.write('\n' + '===== FIM =====')

file.close()
