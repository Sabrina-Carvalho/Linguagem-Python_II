# Relatório de análise III
## Imóveis residenciais

dados = pd.read_csv('Base_dados/aluguel.csv', sep = ';')
dados.head(10)

list(dados['Tipo'].drop_duplicates())

residencial = ['Quitinete',
 'Casa',
 'Apartamento',
 'Casa de Condomínio',
 'Casa de Vila']
residencial

selecao = dados['Tipo'].isin(residencial)
selecao

dados_residencial = dados[selecao]
dados_residencial

list(dados_residencial['Tipo'].drop_duplicates())

dados_residencial.shape[0]

dados_residencial.shape[0]