"""
Aqui encontramos as funções que iremos utilizar nas plotagem dos graficos

"""
from time import sleep
from projeto_bitcoin.classes import *
from projeto_bitcoin.Analise_bitcoin import *
import plotly.express as px

dados = BaseDados('BTC-USD.csv')

def menu():
    """
    Função menu
    :return: O que o usuario solicitou
    """
    print(40 * '-=-')
    print(('GRÁFICO DE ANÁLISE DE FECHAMENTO DO BITCOIN \n'
          'DURANTE O PERÍODO DE 27/07/2017 ATÉ 27/07/2022').center(40))
    print(40 * '-=-')
    print('1 - PLOTAGEM DO GRÁFICO DE LINHA\n'
          '2 - PLOTAGEM DO GRÁFICO DE LINHA COM MÉDIA MÓVEL DE 12 DIAS\n'
          '3 - PLOTAGEM DO GRÁFICO DE LINHA COM TENDÊNCIA DE 30 DIAS\n'
          '4 - PLOTAGEM GRÁFICO DE LINHA COM A MÉDIA MÓVEL E TENDÊNCIA\n'
          '5 - PLOTAGEM DO GRAFICO DE BARRA\n'
          '6 - PLOTAGEM DO GRAFICO HISTOGRAMA\n'
          '7 - PLOTAGEM DO GRÁFICO BOXPLOT\n'
          '8 - SAIR DO SISTEMA ')
    while True:
        opcao: int = int(input('Informe sua opção: '))
        if opcao == 1:
            grafico_linha()
            print('Plotando o gráfico de linha')
            sleep(0.5)
        elif opcao == 2:
            pass
        elif opcao == 3:
            pass
        elif opcao == 4:
            pass
        elif opcao == 5:
            pass
        elif opcao == 6:
            pass
        elif opcao == 7:
            pass
        elif opcao == 8:
            print('Saindo do sistema')
            sleep(0.5)
            break
        else:
            print('Opção inválida..')
            sleep(0.2)


def grafico_linha():
    """
       Nessa função foi realizado uma plotagem do fechamento do preço do bitcoin
       """
    grafico = px.line(dados.basedados, y='Close')
    return layout_linha(grafico)


def layout_linha(grafico):
    grafico.update_layout(
        dict(title='Ánalise de Fechamento Bitcoin', titlefont_size=25),
        xaxis=dict(title='Período Histórico', titlefont_size=18, tickfont_size=12),
        yaxis=dict(title='Preço Fechamento ($)', titlefont_size=18, tickfont_size=12))

    return grafico.show()


def layout_bar(grafico):
    grafico.update_layout(
                        dict(title='Análise mensal de fechamento do bitcoin'),
                        titlefont_size=25,
                        xaxis=dict(title='Período Mensal', titlefont_size=18, tickfont_size=12),
                        yaxis=dict(title='Variação da Média de Preço do Fechamento', titlefont_size=18, tickfont_size=12)
                    )
    return grafico.show()


def layout_bar_volume(grafico):
    grafico.update_layout(
                        dict(title='Análise Mensal de Volume do Bitcoin'), titlefont_size=25,
                        xaxis=dict(title='Período Mensal', titlefont_size=18, tickfont_size=12),
                        yaxis=dict(title='Variação da Média de Volume', titlefont_size=18, tickfont_size = 12)
                        )
    return grafico.show()


def layout_histo(grafico):
    grafico.update_layout(
                      dict(title='Ánalise de Frequência do Bitcoin', titlefont_size=25),
                      xaxis=dict(title='Preço Histórico $', titlefont_size=18, tickfont_size=12),
                      yaxis=dict(title='Quantidade', titlefont_size=18, tickfont_size=12))
    return grafico.show()
