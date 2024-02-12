## Tratamento de dados faltantes

dados = pd.read_csv('Base_dados/aluguel_residencial.csv', sep = ';')
dados.head(10)

dados.isnull()

dados.notnull()

dados.info()

dados[dados['Valor'].isnull()]

A = dados.shape[0]
dados.dropna(subset = ['Valor'], inplace = True)
B = dados.shape[0]
A - B

data = [0.5, None, None, 0.52, 0.54, None, None, 0.59, 0.6, None, 0.7]
s = pd.Series(data)
s

s.fillna(0)

s.fillna(method = 'ffill')

s.fillna(method = 'bfill')

s.fillna(s.mean())

s.fillna(method = 'ffill', limit = 1)

s1 = s.fillna(method = 'ffill', limit = 1)

s1.fillna(method = 'bfill', limit = 1)