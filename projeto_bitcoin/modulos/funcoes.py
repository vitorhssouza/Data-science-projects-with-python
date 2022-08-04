"""
Aqui encontramos as funções que iremos utilizar nas plotagem dos graficos

"""

from time import sleep
from projeto_bitcoin.Analise_bitcoin import *
from projeto_bitcoin.modulos.moduls_graphics import *


<<<<<<< HEAD

def linha(tamanho: int = 60) -> int:
=======
def linha(tamanho: int = 90) -> int:
>>>>>>> developer
    print(tamanho * '=')


def menu() -> None:
    linha()
<<<<<<< HEAD
    print('GRÁFICO DE ANÁLISE DE FECHAMENTO DO BITCOIN \n'
           'DURANTE O PERÍODO DE 27/07/2017 ATÉ 27/07/2022'.center(60))
=======
    print('GRÁFICO DE ANÁLISE DE FECHAMENTO DO BITCOIN'.center(90))
    print('DURANTE O PERÍODO DE 27/07/2017 ATÉ 27/07/2022'.center(90))
>>>>>>> developer
    linha()
    print('1  - TABELA\n'
          '2  - DESCRIÇÃO DA BASE DE DADOS\n'
          '3  - PLOTAGEM DO GRÁFICO DE LINHA\n'
          '4  - PLOTAGEM DO GRÁFICO DE LINHA COM MÉDIA MÓVEL DE 12 DIAS\n'
          '5  - PLOTAGEM DO GRÁFICO DE LINHA COM TENDÊNCIA DE 30 DIAS\n'
          '6  - PLOTAGEM GRÁFICO DE LINHA COM A MÉDIA MÓVEL E TENDÊNCIA\n'
          '7  - PLOTAGEM DO GRAFICO DE BARRA\n'
          '8  - PLOTAGEM DO GRAFICO HISTOGRAMA\n'
          '9  - PLOTAGEM DO GRÁFICO BOXPLOT\n'
          '10 - SAIR DO SISTEMA ')

    opcao: int = int(input('Informe sua opção: '))
    escolha_opcao(opcao)


def escolha_opcao(opcao: int) -> None:
    """
    Função escolha
    :return: O que o usuario solicitou
    """
<<<<<<< HEAD
    #while True:

=======
>>>>>>> developer
    if opcao == 1:
        linha()
        print('Imprimindo a tabela ')
        sleep(0.5)
        print(dados.basedados)
        sleep(4)
        print('Retornando ao menu inicial')
        sleep(0.5)
        menu()
    elif opcao == 2:
        linha()
        print('Imprimindo descrição da base de dados')
        sleep(4)
        print(dados.descricao_base_dados)
        print('Retornando ao menu inicial')
        sleep(0.5)
        menu()
    elif opcao == 3:
        print('Plotando o gráfico de linha')
        grafico_linha()
        sleep(4)
        print('Retornando ao menu inicial')
        sleep(0.5)
        menu()
    elif opcao == 4:
        print('Plotando o gráfico de média móvel de 12 dias.')
        grafico_media_movel()
        sleep(4)
        print('Retornando ao menu inicial')
        sleep(0.5)
        menu()
    elif opcao == 5:
        print('Plotando o gráfico de têndencia de 30 dias.')
        grafico_tendencia()
        sleep(4)
        print('Retornando ao menu inicial')
        sleep(0.5)
        menu()
    elif opcao == 6:
        print('Plotando o gráfico de têndencia de 30 dias.')
        grafico()
        sleep(4)
        print('Retornando ao menu inicial')
        sleep(0.5)
        menu()
    elif opcao == 7:
        print('Plotando o gráfico de barra.')
        grafico_bar()
        sleep(4)
        print('Retornando ao menu inicial')
        sleep(0.5)
        menu()
    elif opcao == 8:
        print('Plotando o gráfico de barra.')
        grafico_histograma()
        sleep(4)
        print('Retornando ao menu inicial')
        sleep(0.5)
        menu()
    elif opcao == 9:
<<<<<<< HEAD
        print('Plotando o gráfico de barra.')
=======
        print('Plotando o gráfico Boxplot.')
>>>>>>> developer
        grafico_box()
        sleep(4)
        print('Retornando ao menu inicial')
        sleep(0.5)
        menu()
    elif opcao == 10:
        print('Saindo do sistema')
        sleep(0.5)
        exit()
    else:
        print('Opção inválida..')
        sleep(0.2)
<<<<<<< HEAD


def grafico_linha():
    """
       Nessa função foi realizado uma plotagem do fechamento do preço do bitcoin
       """
    grafico = px.line(dados.basedados, y='Close')
    return layout_linha(grafico)
=======
>>>>>>> developer


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

    px.box(dados.basedados, x=dados.dados_mes(), y='Close')


def layout_linha(grafico):
    """Função para alterar o layout do gráfico de linha.
       Essa função da um nome de título ao gráfico,
       nome aos eixos x e y do gráfico e
       altera o tamanho da fonte"""

    grafico.update_layout(
        dict(title='Ánalise de Fechamento Bitcoin', titlefont_size=25),
        xaxis=dict(title='Período Histórico', titlefont_size=18, tickfont_size=12),
        yaxis=dict(title='Preço Fechamento ($)', titlefont_size=18, tickfont_size=12),
        )

    return grafico.show()


def layout_bar(grafico):
    """ Função para alterar o layout do gráfico de barra.
        Essa função da um nome de título ao gráfico,
        nome aos eixos x e y do gráfico e
        altera o tamanho da fonte"""

    grafico.update_layout(
                        dict(title='Análise mensal de fechamento do bitcoin'),
                        titlefont_size=25,
                        xaxis=dict(title='Período Mensal', titlefont_size=18, tickfont_size=12),
                        yaxis=dict(title='Variação da Média de Preço do Fechamento', titlefont_size=18, tickfont_size=12)
                    )
    return grafico.show()


def layout_histo(grafico):
    """ Função para alterar o layout do histograma.
        Essa função da um nome de título ao gráfico,
        nome aos eixos x e y do gráfico e
        altera o tamanho da fonte"""

    grafico.update_layout(
                      dict(title='Ánalise de Frequência do Bitcoin', titlefont_size=25),
                      xaxis=dict(title='Preço Histórico $', titlefont_size=18, tickfont_size=12),
                      yaxis=dict(title='Quantidade', titlefont_size=18, tickfont_size=12))
    return grafico.show()


def layout_box(grafico):
    """ Função para alterar o layout do gráfico boxplot.
        Essa função da um nome de título ao gráfico,
        nome aos eixos x e y do gráfico e
        altera o tamanho da fonte"""

    grafico.update_layout(
        dict(title='Ánalise de variação de preço de fechamento do Bitcoin', titlefont_size=25),
        xaxis=dict(title='Meses', titlefont_size=18, tickfont_size=12),
        yaxis=dict(title='Valores $', titlefont_size=18, tickfont_size=12))

    return grafico.show()
