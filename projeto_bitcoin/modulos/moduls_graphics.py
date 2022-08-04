import plotly.express as px
from projeto_bitcoin.modulos.funcoes import *
from projeto_bitcoin.classes import *

dados = BaseDados('BTC-USD.csv')

def grafico_linha():
    """Nessa função foi realizado uma plotagem do fechamento do preço do bitcoin
       foi utilizado a biblioteca plotly.express para as plotagem dos grafico"""

    grafico = px.line(dados.basedados, y='Close')
    return layout_linha(grafico)


def grafico_media_movel() -> None:
    """Foi realizo uma importação de um metodo get da classe BaseDados
       que retornará a média móvel após 12 dias para suavizar a
       visualização do gráfico de linha. """

    grafico_linha_media = px.line(dados.media_movel)
    layout_linha(grafico_linha_media)


def grafico_tendencia() -> None:
    """ Foi realizo uma importação de um metodo get da classe BaseDados
        que retornará uma tendência de 30 dias para suavizar e melhorá
        a visualização do gráfico de linha. """

    grafico_linha_tendencia = px.line(dados.tendencia)
    layout_linha(grafico_linha_tendencia)


def grafico() -> None:
    """ Nessa função foi criada duas colunas na base de dados com a média
        móvel e tendência e utilizando metodos get da classe basedados
        podemos imprimir um o gráfico de linha contendo os valores de
        fechamento, média móvel e sua tendência. """

    dados.basedados['Média Móvel'] = dados.media_movel
    dados.basedados['Tendência'] = dados.tendencia
    grafico = px.line(dados.basedados[['Close', 'Média Móvel', 'Tendência']])
    layout_linha(grafico)


def grafico_bar() -> None:
    """Foi realizo uma importação de um metodo get da classe BaseDados
       que retornará os dados da variação de fechamento mensal durante
       o período da análise. """

    grafico_barra = px.bar(dados.dados_fechamento)
    layout_bar(grafico_barra)


def grafico_histograma() -> None:
    """Foi realizo uma importação de um metodo get da classe BaseDados
       que retornará quantidade de vezes que o bitcoin atingiu certo
       valor. """

    grafico_hist = px.histogram(dados.basedados, x=dados.basedados['Close'])
    layout_histo(grafico_hist)


def grafico_box() -> None:
    """Foi realizo uma importação de um metodo get da classe BaseDados
       que retornará uma coluna months contendo o index da base de dados. """

    graf_box = px.box(dados.dados_mes(), x=dados.basedados['Months'], y=dados.basedados['Close'])
    layout_box(graf_box)
