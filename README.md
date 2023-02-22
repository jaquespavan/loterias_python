# Gerador de Loteria e Coleta de Resultados
Este repositório contém um conjunto de scripts em Python, no formato do Jupyter Notebook, que podem ser utilizados para gerar números aleatórios para jogos das loterias da Caixa Econômica Federal, bem como para coletar resultados direto do site oficial. 

# Gerador de Números de Loteria
O script ((Loterias)).ipynb é um gerador de números de loteria simples, que utiliza a biblioteca random do Python para gerar números aleatórios. Você pode personalizar a quantidade de jogos gerados, em um intervalo entre 1 a 20 jogos.

# Resultados de Loteria utilizando Web Scraping com Selenium
Os scripts "scraper" são exemplos de técnicas de web scraping, utilizando a biblioteca Selenium, para coletar resultados de jogos da Loteria da Caixa Econômica Federal. Cada script se conecta ao site da loteria e extrai as informações dos resultados, armazenando-as em arquivos CSV.
A versão "FULL" faz o scraping desde o concurso nº 1.
A versão "UPDATE" apenas atualiza o arquivo "CSV" já existente na pasta.

# Como Utilizar
Para utilizar os scripts, basta executar os notebooks com o Jupyter Notebook.
Certifique-se de que você tem as bibliotecas necessárias instaladas.

# Melhorias
- o código principal do gerador será otimizado futuramente; é uma versão bem inicial, que mexi muito pouco depois de finalizado.
- está em desenvolvimento um script de análise, com trechos para verificar:
	CONTAGEM QTDE DE CADA DEZENA;
	ANÁLISE DE PALPITE NOS CONCURSOS ANTERIORES;
	entre outros;
	
# Contribuições
Contribuições são sempre bem-vindas!
Sinta-se à vontade para enviar sugestões de melhorias.