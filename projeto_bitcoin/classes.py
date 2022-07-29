"""
Classes que ira receber a base de dados que iremos estudar.
"""
import pandas as pd


class BaseDados:

    def __init__(self, base_dados):
        # reading the file
        self.__basedados = pd.read_csv(base_dados)

        # Passing Date column to datetime type
        self.__basedados['Date'] = pd.to_datetime(self.__basedados['Date'])

        # Indexando a coluna date
        self.__basedados.set_index('Date', inplace=True)

    @property
    def basedados(self: object) -> None:
        return self.__basedados

    @property
    def imprimir_dados(self: object) -> None:
        return self.__basedados.head()



