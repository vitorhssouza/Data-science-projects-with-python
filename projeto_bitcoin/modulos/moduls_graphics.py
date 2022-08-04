import plotly.express as px
from projeto_bitcoin.modulos.funcoes import *
from projeto_bitcoin.classes import *

dados = BaseDados('BTC-USD.csv')

def grafico_linha():
    """
       Nessa função foi realizado uma plotagem do fechamento do preço do bitcoin
       """
    grafico = px.line(dados.basedados, y='Close')
    return layout_linha(grafico)


def grafico_media_movel() -> None:
    grafico_linha_media = px.line(dados.media_movel)
    layout_linha(grafico_linha_media)


def grafico_tendencia() -> None:
    grafico_linha_tendencia = px.line(dados.tendencia)
    layout_linha(grafico_linha_tendencia)


def grafico() -> None:
    dados.basedados['Média Móvel'] = dados.media_movel
    dados.basedados['Tendência'] = dados.tendencia
    grafico = px.line(dados.basedados[['Close', 'Média Móvel', 'Tendência']])
    layout_linha(grafico)


def grafico_bar() -> None:
    grafico_barra = px.bar(dados.dados_fechamento)
    layout_bar(grafico_barra)


def grafico_histograma() -> None:
    grafico_hist = px.histogram(dados.basedados, x=dados.basedados['Close'])
    layout_histo(grafico_hist)


def grafico_box() -> None:
    graf_box = px.box(dados.dados_mes(), x=dados.basedados['Months'], y=dados.basedados['Close'])
    layout_box(graf_box)