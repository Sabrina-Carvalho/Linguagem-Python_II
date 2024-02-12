# Relatótio de Análise VII
## Criando Agrupamentos

dados = pd.read_csv('Base_dados/aluguel_residencial.csv', sep = ';')
dados.head(10)

dados['Valor'].mean()

bairros = ['Barra da Tijuca', 'Copacabana', 'Ipanema', 'Leblon', 'Botafogo', 'Flamengo', 'Tijuca']
selecao = dados['Bairro'].isin(bairros)
dados = dados[selecao]

dados['Bairro'].drop_duplicates()

grupo_bairro = dados.groupby('Bairro')
type(grupo_bairro)

grupo_bairro.groups

for bairro, data  in grupo_bairro:
    print('{} -> {}'.format(bairro, data.Valor.mean()))

grupo_bairro[['Valor','Condominio']].mean().round(2)