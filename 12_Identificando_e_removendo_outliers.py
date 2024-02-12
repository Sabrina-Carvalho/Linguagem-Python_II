# Relatório de Análise VIII
## Identificando e removendo outliers

plt.rc('figure', figsize = (14,6))

dados = pd.read_csv('Base_dados/aluguel_residencial.csv', sep = ';')

dados.boxplot(['Valor'])

dados[dados['Valor'] >= 500000]

valor = dados['Valor']

Q1 = valor.quantile(.25)
Q3 = valor.quantile(.75)
IIQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ

selecao = (valor >= limite_inferior) & (valor <= limite_superior)
dados_new = dados[selecao]

dados_new.boxplot(['Valor'])

dados.hist(['Valor'])
dados_new.hist(['Valor'])

dados.boxplot(['Valor'], by = ['Tipo'])

grupo_tipo = dados.groupby('Tipo')['Valor']

type(grupo_tipo)

grupo_tipo.groups

Q1

Q3

IIQ

limite_inferior

limite_superior

limite_superior['Casa']

dados_new.boxplot(['Valor'], by = ['Tipo'])

dados_new.to_csv('Base_dados/aluguel_residencial_sem_outliers.csv', sep = ';', index = False)

area = plt.figure()

g1 = area.add_subplot(2, 2, 1)

g1 = area.add_subplot(2, 2, 1)
g2 = area.add_subplot(2, 2, 2)
g3 = area.add_subplot(2, 2, 3)
g4 = area.add_subplot(2, 2, 4)

g1.scatter(dados.Valor, dados.Area)
g1.set_title('Valor X Área')

g2.hist(dados.Valor)
g2.set_title('Histograma')

dados_g3 = dados.Valor.sample(100) 
dados_g3.index = range(dados_g3.shape[0])
g3.plot(dados_g3)
g3.set_title('Amostra (Valor)')

grupo = dados.groupby('Tipo')['Valor']
label = grupo.mean().index
valores = grupo.mean().values
g4.bar(label, valores)
g4.set_title('Valor Médio por Tipo')

area = ''

dados_g3 = dados.Valor.sample(100)
dados_g3