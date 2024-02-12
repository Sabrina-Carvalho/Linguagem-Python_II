## Exportando a base de dados 

dados_residencial.to_csv('Base_dados/aluguel_residencial.csv', sep = ';', index = False)

dados_residencial_2 = pd.read_csv('Base_dados/aluguel_residencial.csv', sep = ';')
dados_residencial_2

data = [[1,2,3], 
        [4,5,6], 
        [7,8,9]]
data

list('321')

df = pd.DataFrame(data, list('321'), list('ZYX'))
df

df.sort_index(inplace = True)
df

df.sort_index(inplace = True, axis = 1)
df

df.sort_values(by = ['X', 'Y'], inplace = True)
df

df.sort_values(by = '3', axis = 1, inplace = True)
df