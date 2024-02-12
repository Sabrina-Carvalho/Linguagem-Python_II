## Excluindo Variáveis

dados_aux = pd.DataFrame(dados[['Tipo Agregado', 'Valor m2', 'Valor Bruto', 'Valor Bruto m2']])
dados_aux.head(10)

del dados_aux['Valor Bruto']
dados_aux.head(10)

dados_aux.pop('Valor Bruto m2')
dados_aux

## axis 1 significa 'coluna'
dados.drop(['Valor Bruto', 'Valor Bruto m2'], axis = 1, inplace = True)

dados.head(10)

dados.to_csv('Base_dados/aluguel_residencial.csv', sep = ';', index = False)

s = pd.Series(list('jkndkjfnkjdsnf'))
s

s.unique()

s.value_counts()

dados = pd.read_csv('Base_dados/aluguel.csv', sep = ';')

dados.Tipo.unique()

dados.Tipo.value_counts()