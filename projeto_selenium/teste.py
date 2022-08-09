from projeto_selenium.classes import *

site = Automatizar('https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br')

print(site.pega_cotacao())