"""
Criando classes para utilização do selenium

"""

# Importando bibliotecas
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from time import sleep
import pandas as pd


class Automatizar:

    def __init__(self: object, site: str) -> None:
        self.__site = site


    @property
    def site(self: object) -> None:
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        driver.get(self.__site)
        driver = input('Nesse site encontramos codígos de ações que estão na bolsa de valores\n'
                       'Aperte ENTER para fechar o site.')
        self.__site = driver
        return self.__site

    def pega_cotacao(self) :
        options = Options()
        options.add_argument('--headless')

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

        driver.get('https://economia.uol.com.br/cotacoes/bolsas/')
        empresas = ['PETR3.SA', 'MGLU3.SA', 'VIVT3.SA']
        valores = list()
        data_hora = list()

        for empresa in empresas:
            input_busca = driver.find_element(By.ID, 'filled-normal')
            input_busca.send_keys(empresa)
            sleep(10)

            input_busca.send_keys(Keys.ENTER)
            sleep(5)

            span_val = driver.find_element(By.XPATH, '//span[@class="chart-info-val ng-binding"]')
            cotacao_valor = span_val.text

            valores.append(cotacao_valor)
            data_hora.append(datetime.now().strftime('%d/%m/%Y'))

            print(f'Valor da cotação da {empresa}: {cotacao_valor}')

        dados = {
            'Data-hora': data_hora,
            'Empresas': empresas,
            'Valor': valores
        }

        self.__site = pd.DataFrame(dados)

        self.__site.set_index('Data-hora', inplace=True)

        return self.__site

