# Gerador de números, e coleta de resultados das loterias da Caixa Econômica Federal.
Este repositório contém um conjunto de scripts em Python, para fins de:

# Gerador de Números
O script "loterias.py" é um gerador de números aleatórios simples, que utiliza a biblioteca random.
Você pode personalizar a quantidade de jogos gerados, em um intervalo entre 1 a 20 jogos.

# Coleta dos resultados
Os scripts "scraper" (na pasta 'loteria_web_scraper') são exemplos de técnicas de web scraping, utilizando a biblioteca Selenium, para fazer a coleta dos resultados.
Cada script se conecta ao site da Caixa, e faz a raspagem dos dados, armazenando-as em arquivos CSV.
A versão "FULL" faz o scraping desde o concurso nº 1.
A versão "UPDATE" apenas atualiza o arquivo "CSV" já existente na pasta "loteria_web_scraper\arquivos_CSV".

# Como Utilizar
Para utilizar os scripts, basta executá-los.
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