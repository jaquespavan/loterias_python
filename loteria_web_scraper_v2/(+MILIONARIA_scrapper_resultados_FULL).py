import atualizar_criar_driver as nav
import busca_dados_concurso_atual as bdca
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

c_inicial = 0

url = 'https://loterias.caixa.gov.br/Paginas/Mais-Milionaria.aspx'

conc_atual = bdca.concurso_atual(url)
print(conc_atual[0])

string_concurso_atual = conc_atual[0]
n_concurso_atual = conc_atual[1]
d_concurso_atual = conc_atual[2]

print('##################################################')
print('### Concurso atual: {} ###'.format(string_concurso_atual))
print('##################################################')
print('')
print('Número concurso ATUAL: {}'.format(n_concurso_atual))
print('Data: {}'.format(d_concurso_atual))
print('')


# CAPTURAR OS NUMEROS, ALOCANDO EM LISTA

# XPath caixa pesquisa concurso: //*[@id="buscaConcurso"]
# XPath label concurso (número e data): //*[@id="wp_resultados"]/div[1]/div/h2/span
# XPath label dezena: //*[@id="wp_resultados"]/div[2]/div/div/div[1]/ul/li[1]



lista_conc_total = []

if c_inicial == 0:
    c_inicial = 1

for c in range(c_inicial, (int(n_concurso_atual)+1)): #+1
    #print(c)
    lista_conc = []
    xpath_busca_concurso = '//*[@id="buscaConcurso"]'
    nav.navegador.find_element(By.XPATH, xpath_busca_concurso).clear()
    nav.navegador.find_element(By.XPATH, xpath_busca_concurso).send_keys(c)
    ActionChains(nav.navegador).key_down(Keys.ENTER).perform()

    time.sleep(1)

    xpath_concurso = '//*[@id="wp_resultados"]/div[1]/div/h2/span'
    concurso = nav.navegador.find_element(By.XPATH, xpath_concurso).text

    n_concurso_aux = concurso[:-13]
    n_concurso = n_concurso_aux[9:]
    data_concurso = concurso[-11:-1]

    lista_conc.append(n_concurso.rjust(4, '0'))
    lista_conc.append(data_concurso)

    for i in range(1, 7):  # LOOP PARA FACILITAR A CAPTURA DAS DEZENAS 01 A 06, SEM PRECISAR UTILIZAR 6 LINHAS
        # XPath = //*[@id="ulDezenas"]/li[1]
        xpath_n = '//*[@id="ulDezenas"]/li[' + str(i) + ']'
        # print(xpath_n)
        n = nav.navegador.find_element(By.XPATH, xpath_n).text
        # print(n)
        lista_conc.append(n)

    for i in range(1, 3):  # LOOP PARA FACILITAR A CAPTURA DAS DEZENAS TREVO 01 A 02, SEM PRECISAR UTILIZAR 2 LINHAS
        # XPath = //*[@id="wp_resultados"]/div[2]/div/div/p[2]/img[1]
        xpath_t = '//*[@id="wp_resultados"]/div[2]/div/div/p[2]/img[' + str(i) + ']'
        # print(xpath_n)
        t = nav.navegador.find_element(By.XPATH, xpath_t).get_attribute("alt")
        # print(n)
        lista_conc.append(t[-1])

    lista_conc_total.append(lista_conc)

    print(lista_conc)

print('')

# GRAVAR EM ARQUIVO CSV

nome_arquivo = 'arquivos_CSV\+MILIONARIA_resultados_CSV.csv'

with open(nome_arquivo, 'w') as arquivo:
    arquivo.write(
        'Concurso;Data_concurso;Dezena_01;Dezena_02;Dezena_03;Dezena_04;Dezena_05;Dezena_06;Trevo_01;Trevo_02')
    arquivo.write('\n')

    for lista in lista_conc_total:
        # print(lista)
        for dados_conc in lista:
            # print(dados_conc, end=";")
            arquivo.write(str(dados_conc))
            arquivo.write(';')
        # print('')
        arquivo.write('\n')
arquivo.close

nav.navegador.close()