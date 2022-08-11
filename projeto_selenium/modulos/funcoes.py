"""
Criando funções
"""
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from time import sleep
from projeto_selenium.classes import Automatizar

site = Automatizar('https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br')


def linha(tamanho: int = 90) -> int:
    print(tamanho * '=')


def menu() -> int:
    linha()
    print('PROJETO SELENIUM'.center(90))
    print('RASPAGEM DA BOLSA DE VALORES DO SITE UOL'.center(90))
    linha()
    print('1  - CÓDIGOS DE AÇÕES\n'
          '2  - INFORME O CÓDIGO DAS AÇÕES QUE DESEJA VERIFICAR SEU VALOR\n'
          '3  - SAIR DO SISTEMA')

    opcao: int = int(input('Informe sua opção: '))
    escolha_opcao(opcao)


def escolha_opcao(opcao: int) -> None:
    if opcao == 1:
        linha()
        print('Abrindo o site da B3 para visualizar códigos das ações ')
        sleep(3)
        print(site.site)
        print('Retornando ao menu')
        sleep(2)
        menu()
    elif opcao == 2:
        nome_empresa()
        #site.pega_cotacao()
        linha()
        print('Retornando ao menu')
        sleep(3)
        menu()
    elif opcao == 3:
        print('Saindo do sistema')
        sleep(2)
        exit()
    else:
        print('Opção inválida. Tente novamente.')
        sleep(2)
        menu()


def nome_empresa() -> None:
    empresas = list()
    while True:
        empresas.append(str(input('Informe o nome das empresas: ')))
        while True:
            opcao = int(input('Deseja informa mais alguma empresa? 1-Sim ou 2-Não '))
            if opcao < 1 or opcao > 2:
                print('Informe apenas 1-Sim ou 2-Não ')
            elif opcao == 1:
                break
            elif opcao == 2:
                break
        if opcao == 2:
            linha()
            print('Imprimindo as cotações das empresas ')
            site.pega_cotacao(empresas)
            break


