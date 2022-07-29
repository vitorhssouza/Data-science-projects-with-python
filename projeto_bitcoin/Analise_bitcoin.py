"""
 -> Nesse projeto iremos uma análise dos preços de fechamento do bitcoin durante o período de 5 anos
    In this project we will analyze the closing prices of bitcoin during the period of 5 years

->  A base de dados para análise foi retirada do site:
    The database for analysis was taken from the website:
https://br.financas.yahoo.com/quote/BTC-USD/history?period1=1501113600&period2=1658880000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true

"""

# importing libraries
import pandas as pd
from projeto_bitcoin.classes import BaseDados
from modulos.funcoes import *



# reading the file
#bitcoin_data = pd.read_csv('BTC-USD.csv')

# Passing Date column to datetime type
#bitcoin_data['Date'] = pd.to_datetime(bitcoin_data['Date'])

# Indexando a coluna date
#bitcoin_data.set_index('Date', inplace=True)


def main():
    menu()


if __name__ == '__main__':
    main()




