import atualizar_criar_driver as nav
import importacoes as imp
import time

def concurso_atual(url):
    nav.navegador.get(url)

    time.sleep(2)

    xpath_concurso = '//*[@id="wp_resultados"]/div[1]/div/h2/span'
    concurso_atual = nav.navegador.find_element(imp.By.XPATH, xpath_concurso).text

    n_concurso_aux = concurso_atual[:-13]
    n_concurso_atual = n_concurso_aux[9:]
    data_concurso_atual = concurso_atual[-11:-1]
    return concurso_atual, n_concurso_atual, data_concurso_atual