# BAIXAR WEBDRIVER ATUAL E CRIAR O NAVEGADOR (CHROME)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

navegador = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))