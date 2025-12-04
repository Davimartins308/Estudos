import pandas as pd

dados_df = pd.read_excel("produtos_ficticios.xlsx")

dados_df['Valor em estoque'] = dados_df['Preço'] * dados_df['Quantidade em estoque'] # adicionar colunas a tabela desejada
dados_df['imposto'] = 0

dados_df.loc[2,'imposto']  = 4

#dados_df.to_excel("produtos_ficticios2.xlsx",index=False)

dados_df['imposto'] = dados_df['Valor em estoque'] * 0.03
dados_df['Valor final'] = dados_df['Valor em estoque']  *  dados_df['imposto']
dados_df['Status'] = dados_df.loc[:,'Status'] = 'Esgotado'
dados_df.loc[dados_df['Quantidade em estoque']> 0, 'Status'] = 'Disponível'


esgotado = dados_df.loc[dados_df["Status"] == 'Esgotado']

dados_df['Custo medio por unidade'] = dados_df.loc[:,'Custo medio por unidade'] = 'N/A'

dados_df.loc[dados_df['Quantidade em estoque'] == 0, 'Custo medio por unidade'] = 'N/A'
dados_df.loc[dados_df['Quantidade em estoque'] > 0, 'Custo medio por unidade'] = dados_df['Valor em estoque'] / dados_df['Quantidade em estoque']

dados_df['Frete'] = dados_df.loc[:,'Frete'] = 0

dados_df.loc[(dados_df['Categoria'] == "Roupas" , "Frete")] =  12.90
dados_df.loc[(dados_df['Categoria'] == "Eletrônicos" , "Frete")] =  25.00
dados_df.loc[(dados_df['Categoria'] == "Acessórios" , "Frete")] =  8.50
dados_df.loc[(dados_df['Categoria'] == "Calçados" , "Frete")] =  15.00

planilha = dados_df[['Nome do produto','Categoria','Código do produto','Preço','Valor em estoque','imposto','Valor final','Status','Custo medio por unidade','Frete']]

dados_df.to_excel("planilha_aula16.xlsx",index=False)
print(planilha)
