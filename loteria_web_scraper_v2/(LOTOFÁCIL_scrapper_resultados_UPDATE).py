import atualizar_criar_driver as nav
import busca_dados_concurso_atual as bdca
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

url = 'https://loterias.caixa.gov.br/Paginas/Lotofacil.aspx'
patch_arquivo = 'arquivos_CSV\LOTOFÁCIL_resultados_CSV.csv'

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


# ABRIR O ARQUIVO CSV, VERIFICAR O ULTIMO CONCURSO, E CAPTURAR OS NUMEROS ALOCANDO EM LISTA

# XPath caixa pesquisa concurso: //*[@id="buscaConcurso"]
# XPath label concurso (número e data): //*[@id="wp_resultados"]/div[1]/div/h2/span
# XPath label dezena: //*[@id="ulDezenas"]/li[1]

nome_arquivo = patch_arquivo

with open(nome_arquivo, 'r') as arquivo:
    lista_atual_arq = arquivo.readlines()
arquivo.close

tamanho_lista_atual_arq = len(lista_atual_arq)-1
num_ultimo_concurso_atual_arq = int((lista_atual_arq[tamanho_lista_atual_arq][0:4]))

#print(tamanho_lista_atual_arq)
#print(num_ultimo_concurso_atual_arq)
#print((lista_atual_arq[tamanho_lista_atual_arq][0:4]))

# CAPTURAR OS NUMEROS, ALOCANDO EM LISTA

# XPath caixa pesquisa concurso: //*[@id="buscaConcurso"]
# XPath label concurso (número e data): //*[@id="wp_resultados"]/div[1]/div/h2/span
# XPath label dezena: //*[@id="ulDezenas"]/li[1]

#import time

c_inicial = int(num_ultimo_concurso_atual_arq+1)

lista_conc_total = []

for c in range(c_inicial, (int(n_concurso_atual)+1)):
    #print(c)
    lista_conc = []
    xpath_busca_concurso = '//*[@id="buscaConcurso"]'
    nav.navegador.find_element(By.XPATH, xpath_busca_concurso).clear()
    nav.navegador.find_element(By.XPATH, xpath_busca_concurso).send_keys(c)
    ActionChains(nav.navegador).key_down(Keys.ENTER).perform()

    time.sleep(2)

    xpath_concurso = '//*[@id="wp_resultados"]/div[1]/div/h2/span'
    concurso = nav.navegador.find_element(By.XPATH, xpath_concurso).text
    #print(concurso)

    #lista_conc = []

    n_concurso_aux = concurso[:-13]
    n_concurso = n_concurso_aux[9:]
    data_concurso = concurso[-11:-1]

    lista_conc.append(n_concurso.rjust(4, '0'))
    lista_conc.append(data_concurso)

    for i in range(1,16): # LOOP PARA FACILITAR A CAPTURA DAS DEZENAS 01 A 15, SEM PRECISAR UTILIZAR 15 LINHAS
        # XPath = //*[@id="ulDezenas"]/li[1]
        xpath_n = '//*[@id="wp_resultados"]/div[2]/div/div/div[1]/ul/li['+str(i)+']'
        #print(xpath_n)
        n = nav.navegador.find_element(By.XPATH, xpath_n).text
        #print(n)
        lista_conc.append(n)
    lista_conc_total.append(lista_conc)

print('Número último concurso no arquivo: {}'.format(num_ultimo_concurso_atual_arq))

print('')

# ABRIR ARQUIVO CSV E GRAVAR

nome_arquivo = patch_arquivo

with open(nome_arquivo, 'a') as arquivo:

    for lista in lista_conc_total:
            #print(lista)
            for dados_conc in lista:
                #print(dados_conc, end=";")
                arquivo.write(dados_conc)
                arquivo.write(';')
            #print('')
            arquivo.write('\n')
arquivo.close

nav.navegador.close()

print('Número concurso ATUAL.......................: {}'.format(n_concurso_atual))
print('Número último concurso no arquivo...........: {}'.format(num_ultimo_concurso_atual_arq))

with open(nome_arquivo, 'r') as arquivo:
    lista_atual_arq_atualizada = arquivo.readlines()
arquivo.close

tamanho_lista_atual_arq_atualizada = len(lista_atual_arq_atualizada)-1
num_ultimo_concurso_atual_arq_atualizado = int((lista_atual_arq_atualizada[tamanho_lista_atual_arq_atualizada][0:4]))

print('Número último concurso ATUALIZADO no arquivo: {}'.format(num_ultimo_concurso_atual_arq_atualizado))