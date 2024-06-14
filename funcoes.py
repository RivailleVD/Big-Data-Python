import pandas as pd #carregamento das bibliotecas
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display


#from Bibliotecas import *

#leitura do arquivo CSV
df = pd.read_csv("C:/Users/Levyto/Desktop/big_data/Sindrome_gripais-2024.csv", sep=";")
df


  
'''cores = {
    "amarelo": "\33[33;1m",
    "verde": "\33[32;1m",
    "vermelho": "\33[31;1m",
    "roxo": "\33[35;1m",
    "ciano": "\33[36;1m"'''


#FUNÇÃO PARA EXIBIR O NOME DAS COLUNAS SELECIONADAS DO ARQUIVO CSV

def mostrar_colunas():
    # Definir os nomes das colunas
    colunas = ["municipio", "sintomas", "idade", "profissionalSaude", "dataInicioSintomas", "dataColetaTeste1", "sexo"]
    
    # Criar uma string com os nomes das colunas e quebras de linha entre elas
    nomes_colunas = '\n'.join(colunas)
    
    return nomes_colunas

#FUNÇÃO PARA EXIBIR A QUANTIDADE E O NOME DOS MUNICÍPIOS

def mostrar_municipios():
    
    df = pd.read_csv("C:/Users/Levyto/Desktop/big_data/Sindrome_gripais-2024.csv", sep=";")
    print(f"\33[43;1m{df['municipio'].nunique():>30} \33[43;1mmunicipios atendidos\33[m                                  \n\n")
    print(f'\33[m                           \33[43;1mLISTA DE TODOS OS MUNICIPIOS\33[m\n\n                            ')
    print(f'\33[m{df["municipio"].unique()}')
    return

#FUNÇÃO PARA EXIBIR O GRAFICO DA QUANTIDADE DE HOMENS E MULHERES USANDO A BIBLIOTECA DISPLAY

def graficos_genero():
    sns.countplot(x = "sexo" , data = df)
    plt.title("Total de Pacientes por Sexo")
    return display(plt.show())  # Exibe o gráfico no Visual Studio Code

#FUNÇÃO PARA PESQUISAR O NOME DA CIDADE E OBTER INFORÇÕES

def pesquisar_cidade(cidade_pesquisada):
    """
    Função para filtrar dados por cidade específica.

    Argumentos:
        cidade_pesquisada (str): Nome da cidade a ser pesquisada.

    Retorna:
        DataFrame: Subconjunto do dataframe contendo dados da cidade especificada.
    """

    df = pd.read_csv("C:/Users/Levyto/Desktop/big_data/Sindrome_gripais-2024.csv", sep=";", dtype={ 'municipio': 'object',
                                                                                                    'sintomas': 'object',
                                                                                                    'idade': 'float64',
                                                                                                    'profissionalSaude': 'object',
                                                                                                    'dataInicioSintomas': 'object',
                                                                                                    'dataColetaTeste1': 'object',
                                                                                                    'evolucaoCaso': 'object',
                                                                                                    'sexo': 'object'})

                                                                                            #É PRECISO DETERMINAR O TIPO DE INFORMAÇÕES ALOCADAS EM
                                                                                            #CADA COLUNA OU HAVERÁ ERROS NA LEITURA DO DATASET



    #TRATAMENTO DE ERROS
    
    # Validação de entrada (opcional)
    if cidade_pesquisada not in df["municipio"].unique():
        raise ValueError(f"Cidade '{cidade_pesquisada}' não encontrada no dataframe.")

    subset = df[df["municipio"] == cidade_pesquisada]
    subset = subset[["municipio", "sintomas",  "idade", 
                     "profissionalSaude", 
                     "dataInicioSintomas",  
                     "dataColetaTeste1" , "sexo"]]
    
    

    return subset 



# Função para exibir o menu
def exibir_menu():
    print('\33[36;1m_____________________________________________________________________________\33[m\n')
    print('\33[32;1m                       GESTOR DE INDICES GRIPAIS')
    print('\33[36;1m_____________________________________________________________________________\33[m\n\n')
    print('\33[32;1m                 UTILIZE O PROGRAMA PARA CONSULTAR A PREVALÊNCIA \n                       DA SINDROME VIRAL NO ESTADO DO CEARÁ\n\n')
    print('\33[36;1m_____________________________________________________________________________\33[m\n')
    print('                                \33[42;1m MENU \33[m \n\n\33[32;1m1.Indice \n\n2.Exibir Municípios \n\n3.Gráfico de casos por gênero \n\n4.Pesquisar município (\33[43;1mCONSIDERE LETRAS MAIÚSCULAS E ACENTOS!\33[m\33[32;1m)\n\n')
    print('\33[36;1m_____________________________________________________________________________\33[m\n')

# Função para mostrar o menu e obter a opção do usuário
def obter_opcao():
    while True:
        try:
            opcao = int(input("\33[42;1mEscolha uma opção:\33[m  "))
            return opcao
        except ValueError:
            print("\n\n\33[41;1mPor favor, digite um número válido!\33[m\n\n")

# Main

