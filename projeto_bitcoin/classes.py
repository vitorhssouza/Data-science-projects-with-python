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

    @property
    def descricao_base_dados(self: object) -> None:
        return self.__basedados.describe()

    @property
    def media_movel(self: object) -> None:
        return self.__basedados['Close'].rolling(12).mean()

    @property
    def tendencia(self: object) -> None:
        return self.__basedados['Close'].rolling(30).mean()

    @property
    def dados_fechamento(self: object) -> None:
        return self.__basedados['Close'].diff().groupby(self.__basedados.index.month).mean()

    def dados_mes(self: object) -> None:
        self.__basedados['Months'] = self.__basedados.index.month
        return self.__basedados['Months']





