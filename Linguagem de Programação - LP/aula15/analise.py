import pandas as pd

dados_df = pd.read_excel("produtos_ficticios.xlsx")
#print(dados_df.to_string()) # todos
#print(dados_df.columns) # apenas as colunas
#print(dados_df.shape) # quantidade de colunas e linhas

#produto = dados_df[['Categoria','Código do produto']]  # Mostrar apenas determinada coluna
#print(produto)

#roupas = dados_df.loc[dados_df['Cor'] == "Preto",['Cor','Nome do produto','Preço'] ] # mostra determinado tipo de item de uma categoria
#print(roupas)

#produto_cor_df = dados_df.loc[(dados_df['Categoria']== "Roupas") & (dados_df["Cor"] == "Preto"),['Categoria','Cor','Preço']]  # condicional de colunas
#print(produto_cor_df)
print(dados_df.loc[5, 'Código do produto']) #procurar a linha e a coluna 
