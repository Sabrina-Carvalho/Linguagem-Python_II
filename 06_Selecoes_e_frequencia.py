## Seleções e Frequências

dados = pd.read_csv('Base_dados/aluguel_residencial.csv', sep = ';')
dados.head(10)

# Selecione somente os imóveis classificados com tipo 'Apartamento'.
selecao = dados['Tipo'] == 'Apartamento'
n1 = dados[selecao].shape[0]
n1

# Selecione os imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'.
selecao = (dados['Tipo'] == 'Casa') | (dados['Tipo'] == 'Casa de Condomínio') | (dados['Tipo'] == 'Casa de Vila')
n2 = dados[selecao].shape[0]
n2

# Selecione os imóveis com área entre 60 e 100 metros quadrados, incluindo os limites.
# 60 <- Area <- 100
selecao = (dados['Area'] >= 60) & (dados['Area'] <= 100)
n3 = dados[selecao].shape[0]
n3

# Selecione os imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00.
selecao = (dados['Quartos'] >= 4) & (dados['Valor'] < 2000)
n4 = dados[selecao].shape[0]
n4

print("Nº de imóveis classificados com tipo 'Apartamento'. -> {}".format(n1))
print("Nº de imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'. -> {}".format(n2))
print("Nº de imóveis com área entre 60 e 100 metros quadrados, incluindo os limites. -> {}".format(n3))
print("Nº de imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00. -> {}".format(n4))

'l1 l2 l3 l4'.split()

data = [(1, 2, 3, 4),
        (5, 6, 7, 8),
        (8, 10, 11, 12),
        (13, 14, 15, 16)]
df = pd.DataFrame(data, 'l1 l2 l3 l4'.split(), 'c1 c2 c3 c4'.split())
df

df['c1']

type(df['c1'])

df[['c3','c1']]

type(df[['c3','c1']])

df[1:2]


df[1:][['c3','c1']]

df.loc['l3']

df.loc[['l3','l2']]

df.loc['l1','c2']

df.loc[['l3','l1'], ['c4','c1']]

df.iloc[[2,0], [3,0]]