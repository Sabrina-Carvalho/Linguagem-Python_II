# Relatório de Análise VI
## Criando novas variáveis

dados = pd.read_csv('Base_dados/aluguel_residencial.csv', sep = ';')
dados.head(10)

dados['Valor Bruto'] = dados['Valor'] + dados['IPTU']
dados.head(10)

dados['Valor m2'] = dados['Valor'] / dados['Area']
dados.head(10)

dados['Valor m2'] = dados['Valor m2'].round(2)
dados.head(10)

dados['Valor Bruto m2'] = (dados['Valor Bruto'] / dados['Area']).round(2)
dados.head(10)

casa = ['Casa', 'Casa de Condomínio', 'Casa de Vila']

dados['Tipo Agregado'] = dados['Tipo'].apply(lambda x: 'Casa' if x in casa else 'Apartamento')
dados
