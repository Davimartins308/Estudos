import pandas as pd

dados_df = pd.read_excel("produtos_ficticios.xlsx")

#Liste os produtos fabricados na China acima de 50 unidades

produto_chi = dados_df.loc[(dados_df['País de origem']== "China") & (dados_df["Quantidade em estoque"] > 50),['Nome do produto','País de origem','Quantidade em estoque']]
print(produto_chi)