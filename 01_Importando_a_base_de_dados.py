# Relatório de Análise I
## Importando a Base de Dados

# Importando bibliotecas
import pandas as pd

# Importando base de dados
pd.read_csv('Base_dados/aluguel.csv', sep = ';')

dados = pd.read_csv('Base_dados/aluguel.csv', sep = ';')
dados

type(dados)

dados.info()

dados.head(10)

## Informações Gerais sobre a Base de Dados 

dados.dtypes

tipos_de_dados = pd.DataFrame(dados.dtypes, columns = ['Tipos de Dados'])

tipos_de_dados.columns.name = 'Variáveis'
tipos_de_dados

dados.shape
# 32960 linhas e 9 variáveis

dados.shape[0]

dados.shape[1]

print('A base de dados apresenta {} registros (imóveis) e {} variáveis.'.format(dados.shape[0], dados.shape[1]))